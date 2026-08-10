# 🍄 Spore Drop Index  ·  v1 — live

**Live:** [sporedropindex.com](https://sporedropindex.com) · [www](https://www.sporedropindex.com)  
**Fallback:** [sporedropindex.up.railway.app](https://sporedropindex.up.railway.app)

> **Status: v1 — public, usable, and evolving.** Trait filters, full-text search,
> **177 species** with real photos, edibility colour-coding, dangerous look-alike
> browsing, region/season quick filters, per-species permalinks with OG previews,
> and photo identify (Gemini when `GEMINI_API_KEY` is set; local visual fallback
> otherwise) are all in. Species set grew 58 → 177; look-alike coverage is fully
> named (no generic "other genus" placeholders).

> ⚠️ **Educational use only.** Many mushrooms are deadly and closely resemble
> edible ones. Never eat a wild mushroom based on an app. Always confirm with an
> expert and a spore print before consumption.

A small, fast, dependency-free web app for **searching and identifying mushrooms
by their traits** — cap color, gills vs. pores, habitat, ecology, spore print,
season, region, and edibility. It's an educational reference, not a foraging guide.

## Features

- **Trait filters** generated dynamically from the dataset (edibility, habitat,
  substrate, ecology, spore print, cap color, gill type, season, regions, potency).
- **Full-text search** across common name, scientific name, aliases, and description.
- **Detail view** for each species: traits table, description, look-alikes with
  how to tell them apart, and a fun fact. Deep links at `/species/<id>`.
- **Edibility badges** with a conservative vocabulary (choice → deadly).
- **Dangerous look-alikes mode** — browse confusable pairs where edibility differs.
- **Photo identify** — upload a photo; when `GEMINI_API_KEY` is set on the host,
  matches are constrained to this catalog (with confidence + short reasoning).
  Otherwise falls back to a local colour/texture similarity ranker. Educational
  only — never asserts a field ID and never invents species outside the index.
- **Zero runtime dependencies** — pure Python standard library backend + vanilla
  HTML/CSS/JS frontend. Runs anywhere `python` does.

## Run it

```bash
cd mushroom-index
python app.py
# open http://127.0.0.1:8000
```

Options:

```bash
python app.py --host 0.0.0.0 --port 8080
```

Requires Python 3.7+. No `pip install` needed.

## How it works

```
mushroom-index/
├── app.py            # stdlib HTTP server + JSON search API + static files
├── data/
│   └── species.py    # the dataset (a list of dicts -- add species here)
├── index.html        # app shell
├── styles.css        # theming
├── app.js            # frontend logic (fetch facets + species, render UI)
└── favicon.svg
```

### API

| Endpoint                | Description                                              |
|-------------------------|----------------------------------------------------------|
| `GET /api/species`      | List/search. Query params below (combined with AND).     |
| `GET /api/species/<id>` | Full record for one species.                             |
| `GET /api/facets`       | Available filter values (used to build the UI).          |

Query params for `/api/species` (all optional):

| Param             | Example values                                              |
|------------------|-------------------------------------------------------------|
| `q`              | `amanita`, `porcini` (searches name + sci name + aliases)   |
| `edibility`      | `deadly` `poisonous` `inedible` `unknown` `edible` `choice` |
| `habitat`        | `forest` `grassland` `cultivated`                           |
| `substrate`      | `ground` `deadwood` `dung` `compost`                       |
| `ecology`        | `mycorrhizal` `saprotrophic` `parasitic`                   |
| `spore_print`    | `white` `brown` `green` …                                  |
| `cap_color`      | `red` `brown` …                                            |
| `gill_attachment`| `free` `attached` `decurrent` `pores` `n/a`                |
| `season`         | `spring` `summer` `autumn` `winter`                        |
| `sort`           | `name` (default) `edibility` `random`                      |

```bash
curl "http://127.0.0.1:8000/api/species?edibility=deadly&habitat=forest"
```

## Adding species

Edit `data/species.py` and append a dict to `SPECIES`. Facets and filters build
themselves — no code changes needed. Schema:

```python
{
    "id": "unique-slug",
    "name": "Common Name",
    "scientific_name": "Genus species",
    "aliases": ["alt name"],
    "edibility": "choice",          # choice|edible|unknown|inedible|poisonous|deadly
    "cap": {"shape": ["convex"], "colors": ["brown"], "diameter_cm": [5, 15]},
    "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white"]},
    "stem": {"colors": ["white"], "ring": True, "volva": False},
    "spore_print": "brown",
    "habitat": "forest",
    "substrate": "ground",
    "ecology": "mycorrhizal",
    "season": ["summer", "autumn"],
    "distribution": "…",
    "description": "…",
    "lookalikes": [{"name": "…", "distinguish": "…"}],
    "fun_fact": "…"
}
```

For gill-bearing species use `"attachment": "free" | "attached" | "decurrent"`.
For boletes/polypores use `"attachment": "pores"`. For tooth/jelly/coral species
with no gills or pores use `"attachment": "n/a"`.

## Notes & limitations

- The dataset is curated but **not exhaustive** and should not be relied on for
  identification. Verify against a field guide and expert.
- The backend is single-process and intended for local/learning use. For public
  deployment, put it behind a proper WSGI/ASGI server and add rate limiting.

## Deploy it (so friends can use it)

The app already binds to `$PORT` and `0.0.0.0` (Railway/Render/Heroku convention),
and ships `requirements.txt` + `Procfile`, so hosting is near-zero-config.
The `images/` folder (~16 MB of CC photos across 177 species) is part of the
repo, so photos work on deploy.

### Option A — Railway (easiest) — **this is how production is hosted**
1. Put this folder in a GitHub repo.
2. Go to [railway.app](https://railway.app) → "New Project" → "Deploy from GitHub repo".
3. It auto-detects Python, installs nothing, and runs `python app.py` (see `Procfile`).
4. Generate a Railway domain, then attach a custom domain if you want.
5. **Production today:** custom domain on Cloudflare → Railway service
   (`cgwf6h27.up.railway.app`), public site at **https://sporedropindex.com**
   (and `www`). Optional env var: `GEMINI_API_KEY` for AI photo identify.

### Option B — Render
1. GitHub repo → [render.com](https://render.com) → "New" → "Web Service".
2. Build command: *(none)* · Start command: `python app.py`.
3. Free instance; you get a `*.onrender.com` URL.

### Option C — PythonAnywhere (no git needed)
1. Sign up (free), open the "Files" tab, upload this folder.
2. "Web" tab → "Add a new web app" → Manual / Python → set the WSGI file to import and
   run `app.py` (or use the "Run" console: `python app.py`).

### Option D — Share your local server (no deploy)
Keep it running here and expose a public URL with a tunnel:
```bash
pip install localtunnel
lt --port 8000        # prints a public https URL
```
Works only while this machine/session is up — good for a quick test, not permanent.

> For a permanent public deployment, front the stdlib server with `gunicorn`
> (`pip install gunicorn`, start `gunicorn app:app` — note you'd wrap `app.py` in a
> WSGI app) and add basic rate limiting. The stdlib server is fine for light friend traffic.

