# README-database-migration.md
# Phase 1: PostgreSQL Database Migration

## Overview
This phase moves the Spore Drop Index from in-memory JSON storage to a proper PostgreSQL database for better performance, scalability, and maintainability.

## Files Created

### 1. Database Schema
- `database/schema.sql` - Complete PostgreSQL schema with proper relationships
- `database/init.py` - Script to initialize the database schema

### 2. Migration Script
- `scripts/migrate_to_postgres.py` - Migrates data from `data/species.py` to PostgreSQL

### 3. Configuration
- `railway.toml` - Railway configuration with PostgreSQL dependencies
- `.env.example` - Environment variables template
- `database/query_examples.py` - Example queries demonstrating the new schema

## Migration Steps

### Step 1: Provision PostgreSQL on Railway
1. Go to your Railway dashboard
2. Add a PostgreSQL service to your project
3. Railway will automatically set the `DATABASE_URL` environment variable

### Step 2: Initialize Database
```bash
# Install dependencies
python -m pip install psycopg2-binary python-dotenv

# Initialize database schema
python database/init.py
```

### Step 3: Migrate Data
```bash
# Run migration
python scripts/migrate_to_postgres.py
```

### Step 4: Verify Migration
```bash
# Test some queries
python database/query_examples.py
```

## Schema Design

The new schema normalizes the data into proper relational tables:

- `species` - Main species information
- `species_aliases` - Multiple aliases per species
- `species_seasons` - Fruiting seasons
- `species_regions` - Geographic distribution
- `species_host_trees` - Mycorrhizal associations
- `species_cap` - Cap characteristics
- `species_gills` - Gill/pore characteristics
- `species_stem` - Stem characteristics
- `species_lookalikes` - Safety lookalike information
- `species_fun_facts` - Interesting facts

## Benefits

1. **Performance**: Database queries are much faster than filtering 250+ JSON objects
2. **Scalability**: Easy to add more species and complex queries
3. **Maintainability**: Proper schema with constraints and relationships
4. **Caching**: Database results can be aggressively cached
5. **Backups**: Built-in database backup capabilities

## Next Steps

After successful migration, Phase 2 will update `app.py` to use database queries instead of in-memory filtering.

## Troubleshooting

- Ensure `DATABASE_URL` is set in your environment
- Check that all required packages are installed
- Verify the database schema was created successfully before migrating data