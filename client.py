#!/usr/bin/env python3
"""
CLI client to test the MCP server
"""

import asyncio
import subprocess
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    """Run the MCP client to test server tools."""
    
    # Start the server as a subprocess
    print("🚀 Starting MCP server...\n")
    
    # Define server parameters
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["server.py"],
        env=None
    )
    
    try:
        # Connect to the server using stdio_client context manager
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                # Get available tools
                tools_response = await session.list_tools()
                print(f"📋 Available Tools: {len(tools_response.tools)}")
                for tool in tools_response.tools:
                    print(f"  ✓ {tool.name}")
                
                # Test each tool
                print("\n" + "="*60)
                print("🧪 Testing Tools")
                print("="*60)
                
                # Test 1: get_current_time
                print("\n1️⃣  Testing get_current_time...")
                result = await session.call_tool("get_current_time", {"timezone": "UTC"})
                print(f"   ✅ {result.content[0].text}")
                
                # Test 2: calculate
                print("\n2️⃣  Testing calculate...")
                result = await session.call_tool("calculate", {"expression": "10 + 5 * 2"})
                print(f"   ✅ {result.content[0].text}")
                
                # Test 3: word_count
                print("\n3️⃣  Testing word_count...")
                test_text = "Hello world! This is a test. How are you?"
                result = await session.call_tool("word_count", {"text": test_text})
                print(f"   ✅ Result:\n{result.content[0].text}")
                
                # Test 4: get_random_fact
                print("\n4️⃣  Testing get_random_fact...")
                try:
                    result = await session.call_tool("get_random_fact", {})
                    print(f"   ✅ {result.content[0].text}")
                except Exception as e:
                    print(f"   ⚠️  Could not fetch fact: {e}")
                
                print("\n" + "="*60)
                print("✅ All tests completed successfully!")
                print("="*60)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
