Career Guidance Agent (MCP)

A simple MCP (Model Context Protocol) server that exposes two tools — a web search tool and a cutoff calculator — for use by any MCP-compatible AI agent (e.g. Claude Desktop, custom ADK agents).

Built by Sri Hariharan R.

What it does

This project wraps two basic tools behind a standard MCP server, so any MCP client can connect and use them without custom integration:

search — performs a web search using DDGS (DuckDuckGo Search).
cutoff_calculator — calculates engineering cutoff marks from subject scores (Maths + Physics/2 + Chemistry/2).
Tech Stack
Python 3.13.3
Visual Studio Code
google-adk
mcp[cli]
ddgs
starlette
uvicorn
Claude (Sonnet 5) — used as an AI pair-programmer while building this
Setup
1. Create a virtual environment
bash
python -m venv .venv
2. Activate it
powershell
.\.venv\Scripts\Activate.ps1
3. Install dependencies
bash
pip install google-adk ddgs "mcp[cli]" starlette uvicorn python-dotenv
Project Structure
career_guidance_agent/
│
├── tools/
│   ├── ddgs.py          # search tool
│   └── cutoff_calculator.py
│
├── server.py            # MCP server entry point
└── README.md
How it's built

Each tool lives in its own file inside tools/. server.py imports each tool function and registers it with FastMCP using the @mcp.tool() decorator:

python
from mcp.server.fastmcp import FastMCP
from tools.ddgs import search
from tools.cutoff_calculator import calculate_cutoff

mcp = FastMCP("career_guidance_agent")

@mcp.tool()
def search_tool(query: str):
    return search(query)

@mcp.tool()
def cutoff_tool(maths: float, physics: float, chemistry: float):
    return calculate_cutoff(maths, physics, chemistry)

if __name__ == "__main__":
    mcp.run(transport="stdio")
Running the server
bash
python server.py

To connect it to Claude Desktop, add it to your MCP config (claude_desktop_config.json, accessible via Settings → Connectors → Edit Config):

json
{
  "mcpServers": {
    "career-guidance-server": {
      "command": "D:\\90 DAYs commitment\\carrer guidance prj\\.omcpenv\\Scripts\\python.exe",
      "args": [
        "D:\\90 DAYs commitment\\carrer guidance prj\\server.py"
      ]
    }
  }
}

Tip: point command directly at the python.exe inside your project's virtual environment (as above), rather than just "python". This guarantees Claude Desktop runs the server using the exact environment where your dependencies (mcp, ddgs, etc.) are installed, instead of whatever python resolves to on your system PATH.

Restart Claude Desktop — the tools will appear under the 🔌 icon.

Example

Input: "My Maths mark is 100, Physics is 98, Chemistry is 99. What's my cutoff?"

Output:

Your engineering cutoff mark is 198.5 / 200.
(Maths 100 + Physics/2 = 49 + Chemistry/2 = 49.5)
What I learned building this
How MCP servers work and how tools are registered/exposed.
How to wrap existing Python functions as MCP tools using FastMCP.
How any MCP-compatible client (not just my own agent) can connect to and use a server I built myself.
