# database/query_examples.py
"""
Example queries for the new PostgreSQL database.
"""

import os
import json
from dotenv import load_dotenv
import psycopg2

def get_db_connection():
    """Get database connection"""
    load_dotenv()
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

def example_queries():
    """Run example queries to demonstrate the new schema"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    print("=== Example Queries ===")
    
    # 1. Count species by edibility
    cur.execute("""
        SELECT edibility, COUNT(*) 
        FROM species 
        GROUP BY edibility 
        ORDER BY COUNT(*) DESC
    """)
    print("\n1. Species by edibility:")
    for row in cur.fetchall():
        print(f"  {row[0] or 'unknown'}: {row[1]}")
    
    # 2. Find all species associated with oak
    cur.execute("""
        SELECT s.name, s.scientific_name
        FROM species s
        JOIN species_host_trees ht ON s.id = ht.species_id
        WHERE ht.tree = 'oak'
        ORDER BY s.name
    """)
    print("\n2. Species associated with oak:")
    for row in cur.fetchall():
        print(f"  {row[0]} ({row[1]})")
    
    # 3. Get species with lookalikes
    cur.execute("""
        SELECT s.name, COUNT(l.id) as lookalike_count
        FROM species s
        LEFT JOIN species_lookalikes l ON s.id = l.species_id
        GROUP BY s.id, s.name
        HAVING COUNT(l.id) > 0
        ORDER BY lookalike_count DESC
        LIMIT 5
    """)
    print("\n3. Species with most lookalikes:")
    for row in cur.fetchall():
        print(f"  {row[0]}: {row[1]} lookalikes")
    
    # 4. Complex search example
    cur.execute("""
        SELECT s.name, s.scientific_name, s.edibility
        FROM species s
        JOIN species_seasons ss ON s.id = ss.species_id
        JOIN species_host_trees ht ON s.id = ht.species_id
        WHERE ss.season = 'autumn'
        AND ht.tree = 'pine'
        AND s.edibility = 'edible'
        ORDER BY s.name
    """)
    print("\n4. Edible pine-associated species fruiting in autumn:")
    for row in cur.fetchall():
        print(f"  {row[0]} ({row[1]})")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    example_queries()