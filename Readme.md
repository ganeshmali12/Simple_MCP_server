

# Simple MCP Server 🚀

A lightweight MCP server with 4 tools for Claude AI: calculator, time checker, random facts, and text analyzer.

```
✨ Features

🧮 Calculator: Safe math evaluation

🕰️ Time checker: Current time in any timezone

📚 Random facts: From public API

📊 Text analyzer: Word/character counts

⚡ Async performance

🔒 Safe execution

🚀 Quick Start
```

## 1. Install
```
bash
git clone https://github.com/yourusername/simple-mcp-server
cd simple-mcp-server
pip install "mcp[cli]" httpx
```
## 2. Run
```
python server.py
```

## 3. Configure Claude Desktop
```
Create config file:

macOS: ~/Library/Application Support/Claude/claude_desktop_config.json

Windows: %APPDATA%\Claude\claude_desktop_config.json

Linux: ~/.config/Claude/claude_desktop_config.json

Than create a config file to understand the claude which file have to run and give the proper file path of server file.
```
Add this config:
```
json
{
  "mcpServers": {
    "my-tools": {
      "command": "python",
      "args": ["/FULL/PATH/TO/server.py"]
    }
  }
}
```
## 4. Restart Claude Desktop and use!
```
🛠️ Usage Examples
Ask Claude:

"Calculate 25 * 4"

"What time is it in Tokyo?"

"Tell me a random fact"

"Count words in this text: Hello world"

```
## Project Structure
```
text
server.py              # Main MCP server
requirements.txt       # Dependencies
README.md             # This file
.gitignore           # Git ignore
```
##  Dependencies
```
txt
mcp[cli]>=1.0.0
httpx>=0.25.0
```
##  Troubleshooting
```
Tools not showing? Restart Claude Desktop

Python not found? Use full path like /usr/bin/python3

Module errors? Run pip install "mcp[cli]" httpx
```

## Contributing
```
Feel free to fork and submit PRs to add more tools!
``` 
## Note:-
If dont want to use the claude desktop you can also use the client CLI for test the MCP server which i inculde in the repo 
