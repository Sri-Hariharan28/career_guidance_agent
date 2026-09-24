from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS
from tools.ddgs import search
from tools.cutoff_cal import cutoff_cali

mcp = FastMCP("Career-Guidance-MCP-Server")

# TOOLS

@mcp.tool()
def cutoff_calu(mat: float, phy: float, che: float) -> float:
    """Calculate the engineering cutoff mark for college admissions."""
    return cutoff_cali(mat,phy,che)


@mcp.tool()
def search(query: str) -> str:
    """Search the web via DDGS for live internet information, college details, or general queries."""

    return search(query)


if __name__ == "__main__":
    mcp.run(transport="stdio")