#!/usr/bin/env python3
"""
Database Connection Helper

This script helps verify that the DATABASE_URL is properly shared
between your PostgreSQL service and web service on Railway.

Steps:
1. Add PostgreSQL service to your Railway project
2. Share DATABASE_URL variable from PostgreSQL → web service
3. Run this script to test the connection
"""

import os
import sys

def check_environment():
    """Check if DATABASE_URL is available in the environment"""
    database_url = os.environ.get("DATABASE_URL")
    
    if database_url:
        print("✅ DATABASE_URL found in environment!")
        # Mask password for security
        if "password" in database_url:
            parts = database_url.split(":")
            if len(parts) >= 3:
                parts[2] = "***"
                masked_url = ":".join(parts)
                print(f"   Database: {masked_url}")
        else:
            print(f"   Database: {database_url}")
        return True
    else:
        print("❌ DATABASE_URL not found in environment")
        print("\nTo fix this:")
        print("1. Go to your Railway dashboard")
        print("2. Find your PostgreSQL service")
        print("3. Click 'Variables' tab")
        print("4. Find DATABASE_URL and click 'Share Variable'")
        print("5. Select your web service to share with")
        print("6. Wait 1-2 minutes for propagation")
        return False

def main():
    print("🔍 Checking Database Connection Setup...\n")
    
    # Check if we're running in Railway environment
    railway_env = os.environ.get("RAILWAY_ENVIRONMENT")
    if railway_env:
        print(f"✅ Running in Railway environment: {railway_env}")
    else:
        print("ℹ️  Running locally - make sure to set DATABASE_URL in .env file")
    
    print("\n" + "="*50)
    
    # Check database connection
    has_db_url = check_environment()
    
    print("\n" + "="*50)
    
    if has_db_url:
        print("\n🎉 Next steps:")
        print("1. Run: python database/init.py")
        print("2. Run: python scripts/migrate_to_postgres.py")
        print("3. Your data will be migrated to PostgreSQL!")
    else:
        print("\n📋 Please complete the variable sharing steps above first.")

if __name__ == "__main__":
    main()