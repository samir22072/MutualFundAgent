import sqlite3
import datetime
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mutual_funds.db')

def setup_db():
    # Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Drop table if exists to ensure clean slate for our dummy data seeding
    cursor.execute("DROP TABLE IF EXISTS mutual_funds")

    # Create table
    cursor.execute("""
    CREATE TABLE mutual_funds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fund_name TEXT NOT NULL,
        fund_risk_profile TEXT NOT NULL,
        cagr_1_year REAL,
        cagr_3_year REAL,
        cagr_5_year REAL,
        created_by TEXT,
        modified_by TEXT,
        created_at TIMESTAMP,
        modified_at TIMESTAMP,
        is_deleted BOOLEAN
    )
    """)

    # Dummy data
    now = datetime.datetime.now().isoformat()
    dummy_funds = [
        ("Nippon India Liquid Fund", "low", 6.5, 6.2, 5.8),
        ("SBI Magnum Gilt Fund", "low", 7.1, 6.8, 6.5),
        ("HDFC Corporate Bond Fund", "low", 7.4, 7.0, 6.9),
        ("ICICI Prudential Savings Fund", "low", 6.8, 6.4, 6.1),
        ("Kotak Banking and PSU Debt Fund", "low", 7.2, 7.3, 7.0),
        ("Axis Short Term Fund", "low", 7.0, 6.9, 6.5),

        ("Parag Parikh Flexi Cap Fund", "medium", 22.5, 18.4, 20.1),
        ("SBI Equity Hybrid Fund", "medium", 15.2, 14.1, 13.5),
        ("HDFC Balanced Advantage Fund", "medium", 14.8, 13.9, 12.8),
        ("Mirae Asset Large Cap Fund", "medium", 18.5, 16.2, 15.4),
        ("ICICI Prudential Equity & Debt Fund", "medium", 17.1, 15.5, 14.2),
        ("Kotak Equity Opportunities Fund", "medium", 20.4, 18.8, 17.5),
        ("Axis Bluechip Fund", "medium", 16.5, 15.0, 14.8),

        ("Quant Small Cap Fund", "high", 55.4, 38.2, 32.5),
        ("Nippon India Small Cap Fund", "high", 48.2, 35.1, 28.4),
        ("HDFC Small Cap Fund", "high", 42.1, 31.5, 25.8),
        ("SBI Small Cap Fund", "high", 39.5, 29.8, 26.2),
        ("Tata Digital India Fund", "high", 35.2, 25.4, 28.1),
        ("ICICI Prudential Technology Fund", "high", 38.7, 28.9, 29.5),
        ("Aditya Birla Sun Life Frontline Equity", "high", 25.4, 21.2, 18.5)
    ]

    records_to_insert = []
    for fund in dummy_funds:
        records_to_insert.append((
            fund[0], fund[1], fund[2], fund[3], fund[4],
            "system", "system", now, now, False
        ))

    # Insert records
    cursor.executemany("""
    INSERT INTO mutual_funds (
        fund_name, fund_risk_profile, cagr_1_year, cagr_3_year, cagr_5_year,
        created_by, modified_by, created_at, modified_at, is_deleted
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, records_to_insert)

    conn.commit()
    conn.close()
    print(f"Database initialized and seeded at {DB_PATH}")

if __name__ == "__main__":
    setup_db()
