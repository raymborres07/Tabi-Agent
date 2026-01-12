from mcp.server.fastmcp import FastMCP
from tools import search_hotels # Import the logic we just moved

mcp = FastMCP("Rakuten TravelClone")

# We just wrap the imported function!
mcp.tool()(search_hotels)

if __name__ == "__main__":
    mcp.run()