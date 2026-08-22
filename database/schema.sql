-- Spore Drop Index PostgreSQL Schema
-- Educational catalog only. Constraints match live species.py values.

DROP TABLE IF EXISTS species_fun_facts CASCADE;
DROP TABLE IF EXISTS species_lookalikes CASCADE;
DROP TABLE IF EXISTS species_stem CASCADE;
DROP TABLE IF EXISTS species_gills CASCADE;
DROP TABLE IF EXISTS species_cap CASCADE;
DROP TABLE IF EXISTS species_host_trees CASCADE;
DROP TABLE IF EXISTS species_regions CASCADE;
DROP TABLE IF EXISTS species_seasons CASCADE;
DROP TABLE IF EXISTS species_aliases CASCADE;
DROP TABLE IF EXISTS species CASCADE;

CREATE TABLE species (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    scientific_name TEXT NOT NULL,
    edibility TEXT CHECK (edibility IN ('deadly', 'poisonous', 'inedible', 'unknown', 'edible', 'choice')),
    habitat TEXT,
    substrate TEXT,
    ecology TEXT,
    spore_print TEXT,
    potency TEXT CHECK (potency IS NULL OR potency IN ('none', 'low', 'moderate', 'high')),
    bioluminescent BOOLEAN DEFAULT FALSE,
    description TEXT,
    distribution TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE species_aliases (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    alias TEXT NOT NULL,
    PRIMARY KEY (species_id, alias)
);

CREATE TABLE species_seasons (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    season TEXT NOT NULL,
    PRIMARY KEY (species_id, season)
);

CREATE TABLE species_regions (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    region TEXT NOT NULL,
    PRIMARY KEY (species_id, region)
);

CREATE TABLE species_host_trees (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    tree TEXT NOT NULL,
    PRIMARY KEY (species_id, tree)
);

CREATE TABLE species_cap (
    species_id TEXT PRIMARY KEY REFERENCES species(id) ON DELETE CASCADE,
    shape TEXT[],
    colors TEXT[],
    diameter_cm NUMERIC[]
);

CREATE TABLE species_gills (
    species_id TEXT PRIMARY KEY REFERENCES species(id) ON DELETE CASCADE,
    attachment TEXT,
    spacing TEXT,
    colors TEXT[]
);

CREATE TABLE species_stem (
    species_id TEXT PRIMARY KEY REFERENCES species(id) ON DELETE CASCADE,
    colors TEXT[],
    ring BOOLEAN DEFAULT FALSE,
    volva BOOLEAN DEFAULT FALSE
);

CREATE TABLE species_lookalikes (
    id SERIAL PRIMARY KEY,
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    distinguish TEXT NOT NULL,
    link TEXT
);

CREATE TABLE species_fun_facts (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    fact TEXT NOT NULL,
    PRIMARY KEY (species_id, fact)
);

CREATE INDEX idx_species_edibility ON species(edibility);
CREATE INDEX idx_species_habitat ON species(habitat);
CREATE INDEX idx_species_ecology ON species(ecology);
CREATE INDEX idx_species_potency ON species(potency);
CREATE INDEX idx_species_bioluminescent ON species(bioluminescent);
CREATE INDEX idx_host_trees_tree ON species_host_trees(tree);
CREATE INDEX idx_regions_region ON species_regions(region);
CREATE INDEX idx_seasons_season ON species_seasons(season);
CREATE INDEX idx_species_name_trgm ON species (lower(name));
CREATE INDEX idx_species_scientific_trgm ON species (lower(scientific_name));
