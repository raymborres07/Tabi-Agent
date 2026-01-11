import sqlite3
import json

def init_db():
    # Connect to the database (it will be created if it doesn't exist)
    conn = sqlite3.connect("travel.db")
    cursor = conn.cursor()

    # 1. Create Hotels Table
    # Schema matches your portfolio plan: ID, Name, Lat, Lon, Price, Rating, Amenities
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hotels (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        latitude REAL,
        longitude REAL,
        base_price INTEGER,
        star_rating REAL,
        amenities_json TEXT
    )
    """)

    # 2. Insert Mock Data (Rakuten Travel style data)
    hotels = [
        (1, "Rakuten STAY Kyoto Station", 34.985, 135.758, 15000, 4.5, json.dumps(["wifi", "kitchen", "washing_machine"])),
        (2, "Hakone Kowakien Tenyu", 35.237, 139.043, 55000, 5.0, json.dumps(["onsen", "kaiseki", "mountain_view"])),
        (3, "Business Hotel Namba", 34.665, 135.501, 8000, 3.0, json.dumps(["wifi", "breakfast_buffet"])),
    ]

    cursor.executemany("""
    INSERT OR IGNORE INTO hotels (id, name, latitude, longitude, base_price, star_rating, amenities_json)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, hotels)

    conn.commit()
    conn.close()
    print("Database 'travel.db' initialized and seeded with mock data.")

if __name__ == "__main__":
    init_db()