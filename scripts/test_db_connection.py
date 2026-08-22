#!/usr/bin/env python3
"""
Test database connection script.
Run this after adding PostgreSQL to Railway to verify the connection works.
"""

import os
import sys
from dotenv import load_dotenv

try:
    import psycopg2
except ImportError:
    print("Installing psycopg2-binary...")
    os.system("python -m pip install psycopg2-binary")
    import psycopg2

def test_connection():
    """Test the database connection"""
    load_dotenv()
    database_url = os.environ.get("DATABASE_URL")
    
    if not database_url:
        print("❌ DATABASE_URL environment variable not set")
        print("Please add PostgreSQL to your Railway project first")
        return False
    
    try:
        # Mask password for security in output
        masked_url = database_url
        if "password" in database_url:
            parts = database_url.split(":")
            if len(parts) >= 3:
                parts[2] = "***"
                masked_url = ":".join(parts)
        
        print(f"✅ DATABASE_URL found: {masked_url}")
        
        # Test connection
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        
        # Test simple query
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        
        cur.close()
        conn.close()
        
        print(f"✅ Connected to PostgreSQL: {version.split(',')[0]}")
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)