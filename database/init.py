# database/init.py
"""
Database initialization script.
Creates the schema and sets up the database structure.
"""

import os
import sys
from pathlib import Path

try:
    import psycopg2
    from dotenv import load_dotenv
except ImportError:
    print("Installing required packages...")
    os.system("python -m pip install psycopg2-binary python-dotenv")
    import psycopg2
    from dotenv import load_dotenv

def init_database():
    """Initialize the database with the schema"""
    load_dotenv()
    database_url = os.environ.get("DATABASE_URL")
    
    if not database_url:
        raise ValueError("DATABASE_URL environment variable not set")
    
    # Read schema file
    schema_file = Path(__file__).parent / "schema.sql"
    schema_sql = schema_file.read_text(encoding="utf-8")
    
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()
    
    try:
        # Execute schema creation
        cur.execute(schema_sql)
        conn.commit()
        print("Database schema created successfully!")
        
        # Verify tables were created
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name
        """)
        tables = [row[0] for row in cur.fetchall()]
        print(f"Created tables: {', '.join(tables)}")
        
    except Exception as e:
        conn.rollback()
        print(f"Schema creation failed: {e}")
        raise
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    init_database()