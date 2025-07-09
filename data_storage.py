# data_storage.py

import sqlite3
from datetime import datetime

DB_NAME = "voxciv_reports.db"

def init_db():
    """Create reports table if it doesn't exist"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            message TEXT,
            lat REAL,
            lon REAL,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_report(location, message, lat, lon):
    """Insert a new report into the database"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO reports (location, message, lat, lon, created_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (location, message, lat, lon, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def fetch_reports():
    """Fetch all reports from the database"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT location, message, lat, lon, created_at FROM reports ORDER BY created_at DESC')
    results = c.fetchall()
    conn.close()

    # Convert to list of dicts
    return [
        {
            "location": row[0],
            "message": row[1],
            "lat": row[2],
            "lon": row[3],
            "created_at": row[4]
        }
        for row in results
    ]
