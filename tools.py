import sqlite3

# This is the pure logic, separated from the server code.
def search_hotels(location: str = "", max_price: int = 50000):
    """
    Search for hotels in a specific location (e.g., 'Kyoto', 'Osaka') 
    that are below a certain price per night.
    """
    conn = sqlite3.connect("travel.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    query = "SELECT name, base_price, star_rating, amenities_json FROM hotels WHERE base_price <= ?"
    params = [max_price]

    if location:
        query += " AND name LIKE ?"
        params.append(f"%{location}%")

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No hotels found matching your criteria."
    
    results = []
    for r in rows:
        info = f"- {r['name']} (¥{r['base_price']}/night, {r['star_rating']} stars)"
        results.append(info)
    
    return "\n".join(results)