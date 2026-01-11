from mcp.server.fastmcp import FastMCP
import sqlite3

# Initialize the MCP Server
# "Rakuten TravelClone" is the name the AI will see
mcp = FastMCP("Rakuten TravelClone")

# Helper function to connect to your database
def get_db():
    conn = sqlite3.connect("travel.db")
    conn.row_factory = sqlite3.Row
    return conn

# Define the "Tool"
# This function becomes a tool the AI can choose to use
@mcp.tool()
def search_hotels(location: str, max_price: int) -> str:
    """
    Search for hotels in a specific location (e.g., 'Kyoto', 'Osaka') 
    that are below a certain price per night.
    """
    conn = get_db()
    cursor = conn.cursor()
    
    # 1. Build the SQL query securely
    query = "SELECT name, base_price, star_rating, amenities_json FROM hotels WHERE base_price <= ?"
    params = [max_price]

    if location:
        # Fuzzy match the location (e.g., "Kyoto" finds "Rakuten STAY Kyoto")
        query += " AND name LIKE ?"
        params.append(f"%{location}%")

    # 2. Execute the search
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    # 3. Format the results for the AI
    if not rows:
        return "No hotels found matching your criteria."
    
    results = []
    for r in rows:
        info = f"- {r['name']} (¥{r['base_price']}/night, {r['star_rating']} stars)"
        results.append(info)
    
    return "\n".join(results)

if __name__ == "__main__":
    mcp.run()