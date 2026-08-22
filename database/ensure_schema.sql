-- Idempotent schema for Spore Drop Index (no DROP).
-- Used by automatic catalog sync on boot/deploy.

CREATE TABLE IF NOT EXISTS species (
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

CREATE TABLE IF NOT EXISTS species_aliases (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    alias TEXT NOT NULL,
    PRIMARY KEY (species_id, alias)
);

CREATE TABLE IF NOT EXISTS species_seasons (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    season TEXT NOT NULL,
    PRIMARY KEY (species_id, season)
);

CREATE TABLE IF NOT EXISTS species_regions (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    region TEXT NOT NULL,
    PRIMARY KEY (species_id, region)
);

CREATE TABLE IF NOT EXISTS species_host_trees (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    tree TEXT NOT NULL,
    PRIMARY KEY (species_id, tree)
);

CREATE TABLE IF NOT EXISTS species_cap (
    species_id TEXT PRIMARY KEY REFERENCES species(id) ON DELETE CASCADE,
    shape TEXT[],
    colors TEXT[],
    diameter_cm NUMERIC[]
);

CREATE TABLE IF NOT EXISTS species_gills (
    species_id TEXT PRIMARY KEY REFERENCES species(id) ON DELETE CASCADE,
    attachment TEXT,
    spacing TEXT,
    colors TEXT[]
);

CREATE TABLE IF NOT EXISTS species_stem (
    species_id TEXT PRIMARY KEY REFERENCES species(id) ON DELETE CASCADE,
    colors TEXT[],
    ring BOOLEAN DEFAULT FALSE,
    volva BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS species_lookalikes (
    id SERIAL PRIMARY KEY,
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    distinguish TEXT NOT NULL,
    link TEXT
);

CREATE TABLE IF NOT EXISTS species_fun_facts (
    species_id TEXT REFERENCES species(id) ON DELETE CASCADE,
    fact TEXT NOT NULL,
    PRIMARY KEY (species_id, fact)
);

-- Tracks which species.py revision is currently loaded into Postgres.
CREATE TABLE IF NOT EXISTS catalog_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_species_edibility ON species(edibility);
CREATE INDEX IF NOT EXISTS idx_species_habitat ON species(habitat);
CREATE INDEX IF NOT EXISTS idx_species_ecology ON species(ecology);
CREATE INDEX IF NOT EXISTS idx_species_potency ON species(potency);
CREATE INDEX IF NOT EXISTS idx_species_bioluminescent ON species(bioluminescent);
CREATE INDEX IF NOT EXISTS idx_host_trees_tree ON species_host_trees(tree);
CREATE INDEX IF NOT EXISTS idx_regions_region ON species_regions(region);
CREATE INDEX IF NOT EXISTS idx_seasons_season ON species_seasons(season);
CREATE INDEX IF NOT EXISTS idx_species_name_lower ON species (lower(name));
CREATE INDEX IF NOT EXISTS idx_species_scientific_lower ON species (lower(scientific_name));
