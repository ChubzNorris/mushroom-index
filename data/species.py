# -*- coding: utf-8 -*-
"""
Seed dataset for the Spore Drop Index.

Each entry is a dict with a consistent schema. The backend derives filter
facets (cap colors, edibility, habitat, etc.) dynamically from this list, so
adding a species is just appending a dict here -- no code changes needed.

EDIBILITY vocabulary (conservative, educational):
    deadly   - can be fatal; do NOT eat
    poisonous- causes illness/hallucination; do NOT eat
    inedible - too tough/tasteless or unknown risk; not worth eating
    unknown  - edibility not well established; treat as not-for-eating
    edible   - generally considered safe when correctly identified & prepared
    choice   - excellent, sought-after edible

IMPORTANT: This is an educational reference only. Never eat a wild mushroom
based on an app. Many deadly species closely resemble edible ones.
"""

SPECIES = [
    {
        "id": "amanita-muscaria",
        "name": "Fly Agaric",
        "scientific_name": "Amanita muscaria",
        "aliases": ["fly amanita", "toadstool", "red cap"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "flat"], "colors": ["red", "orange"], "diameter_cm": [8, 20]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white"], "ring": True, "volva": True},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn", "winter"],
        "distribution": "Northern Hemisphere, widespread",
        "description": ("Iconic red cap flecked with white warts (universal veil remnants). "
                        "Contains ibotenic acid and muscimol; psychoactive and toxic, historically "
                        "used ritually. Not deadly in typical doses but causes severe poisoning."),
        "lookalikes": [
            {"name": "Amanita caesarea (Caesar's mushroom)", "distinguish": "Edible Amanita with an orange cap and orange stem; lacks the white-flecked red look."},
            {"name": "Amanita flavoconia", "distinguish": "Smaller yellow-orange cousin with yellow warts."}
        ],
        "fun_fact": "The model for most 'mushroom' illustrations and Super Mario's power-ups."
    },
    {
        "id": "amanita-phalloides",
        "name": "Death Cap",
        "scientific_name": "Amanita phalloides",
        "aliases": ["death cup"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "flat"], "colors": ["green", "olive", "tan", "brown"], "diameter_cm": [5, 15]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white"]},
        "stem": {"colors": ["white", "pale"], "ring": True, "volva": True},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere; introduced with oak/chestnut worldwide",
        "description": ("Responsible for the majority of fatal mushroom poisonings worldwide. "
                        "Contains amatoxins that cause irreversible liver and kidney failure, often "
                        "with a deceptive symptom-free delay. Caps are greenish to tan and easily "
                        "mistaken for edible mushrooms."),
        "lookalikes": [
            {"name": "Agaricus species (field/button mushrooms)", "distinguish": "Have pink-then-brown gills and a brown spore print; NEVER a white volva cup."},
            {"name": "Amanita caesarea / edible Amanitas", "distinguish": "Some edible Amanitas look similar -- white gills + volva is the danger signal for this group."},
            {"name": "Macrolepiota procera (parasol)", "distinguish": "Has a shaggy brown-scaled cap and a movable ring; no volva."}
        ],
        "fun_fact": "A single cap can contain enough amatoxin to kill an adult."
    },
    {
        "id": "amanita-bisporigera",
        "name": "Destroying Angel",
        "scientific_name": "Amanita bisporigera",
        "aliases": ["death angel"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "bell"], "colors": ["white"], "diameter_cm": [5, 12]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white"]},
        "stem": {"colors": ["white"], "ring": True, "volva": True},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Eastern North America",
        "description": ("A pure white, beautiful mushroom that is among the deadliest on Earth. "
                        "Same amatoxin family as the death cap. The white volva at the stem base "
                        "and white gills are key identifiers -- but so do several edible whites, "
                        "which is precisely why it kills."),
        "lookalikes": [
            {"name": "Agaricus campestris (field mushroom)", "distinguish": "Pink-then-brown gills, no volva, brown spores."},
            {"name": "Young Armillaria / Clitocybe", "distinguish": "Lack a volva cup and have attached (not free) gills."}
        ],
        "fun_fact": "Its name refers to its angelic appearance, not its intent."
    },
    {
        "id": "amanita-caesarea",
        "name": "Caesar's Mushroom",
        "scientific_name": "Amanita caesarea",
        "aliases": ["Caesar's agaric", "orange amanita"],
        "edibility": "choice",
        "cap": {"shape": ["convex", "flat"], "colors": ["orange", "red"], "diameter_cm": [5, 18]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["yellow", "gold"]},
        "stem": {"colors": ["yellow", "orange"], "ring": True, "volva": True},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Southern Europe, North Africa, parts of North America",
        "description": ("A prized Mediterranean delicacy with a vivid orange cap and golden stem, "
                        "eaten since Roman times (reserved for emperors). Safe only because its "
                        "features are distinctive -- a good lesson in learning ONE mushroom well."),
        "lookalikes": [
            {"name": "Amanita muscaria (fly agaric)", "distinguish": "Fly agaric has white warts on red and white gills/stem, not golden."},
            {"name": "Amanita phalloides", "distinguish": "Death cap is greenish-tan with white gills -- never golden."}
        ]
    },
    {
        "id": "agaricus-bisporus",
        "name": "Button / Portobello",
        "scientific_name": "Agaricus bisporus",
        "aliases": ["cultivated mushroom", "champignon"],
        "edibility": "choice",
        "cap": {"shape": ["convex", "flat"], "colors": ["white", "brown", "tan"], "diameter_cm": [3, 15]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["pink", "brown"]},
        "stem": {"colors": ["white"], "ring": True, "volva": False},
        "spore_print": "brown",
        "habitat": "cultivated",
        "substrate": "compost",
        "ecology": "saprotrophic",
        "season": ["year-round"],
        "distribution": "Grown globally in cultivation",
        "description": ("The supermarket mushroom in its white (button) and brown (cremini/portobello) "
                        "forms. Young gills are pink, maturing to chocolate brown -- a reliable field "
                        "mark for the whole Agaricus genus."),
        "lookalikes": [
            {"name": "Agaricus xanthodermus (yellow stainer)", "distinguish": "Bruises bright yellow and smells of phenol/ink; avoid."},
            {"name": "Amanita species", "distinguish": "Amanitas have white gills and a volva; Agaricus never does."}
        ]
    },
    {
        "id": "agaricus-campestris",
        "name": "Field Mushroom",
        "scientific_name": "Agaricus campestris",
        "aliases": ["meadow mushroom"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["white", "cream", "tan"], "diameter_cm": [4, 10]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["pink", "brown"]},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Worldwide in pastures and lawns",
        "description": ("The classic wild relative of the button mushroom, found in rings in pastures. "
                        "Pink-to-brown gills and a brown spore print. A good beginner edible -- but "
                        "only after ruling out the yellow stainer and any white-gilled lookalikes."),
        "lookalikes": [
            {"name": "Agaricus xanthodermus", "distinguish": "Yellow staining + chemical smell."},
            {"name": "Amanita species", "distinguish": "White gills + volva = danger."}
        ]
    },
    {
        "id": "agaricus-xanthodermus",
        "name": "Yellow Stainer",
        "scientific_name": "Agaricus xanthodermus",
        "aliases": ["yellowing mushroom"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "flat"], "colors": ["white", "cream"], "diameter_cm": [5, 12]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["pink", "brown"]},
        "stem": {"colors": ["white"], "ring": True, "volva": False},
        "spore_print": "brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Widespread in lawns and gardens",
        "description": ("Looks like an edible field mushroom but bruises bright yellow and emits a "
                        "sharp phenol/ink smell. Causes gastrointestinal upset. The yellow staining "
                        "at the base is the giveaway -- always check before eating any Agaricus."),
        "lookalikes": [
            {"name": "Agaricus campestris / bisporus", "distinguish": "These do NOT stain yellow and lack the chemical odor."}
        ]
    },
    {
        "id": "boletus-edulis",
        "name": "King Bolete",
        "scientific_name": "Boletus edulis",
        "aliases": ["porcini", "cep", "penny bun"],
        "edibility": "choice",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "tan", "chestnut"], "diameter_cm": [7, 25]},
        "gills": {"attachment": "pores", "spacing": "n/a", "colors": ["white", "olive", "yellow"]},
        "stem": {"colors": ["white", "tan"], "ring": False, "volva": False},
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere; widespread",
        "description": ("The king of edibles: a bun-shaped brown cap over a spongy pore layer (no "
                        "gills) and a fat, finely netted stem. Boletes are some of the safest edible "
                        "groups because the deadly Amanita types have gills, not pores."),
        "lookalikes": [
            {"name": "Boletus satanas (devil's bolete)", "distinguish": "Has a red-tinged stem and stains blue; poisonous."},
            {"name": "Tylopilus felleus (bitter bolete)", "distinguish": "Intensely bitter; pinkish pore mouths."}
        ],
        "fun_fact": "Dried porcini are more aromatic than fresh -- umami bombs."
    },
    {
        "id": "boletus-satanas",
        "name": "Devil's Bolete",
        "scientific_name": "Boletus satanas",
        "aliases": ["Satan's mushroom"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex"], "colors": ["white", "gray", "olive"], "diameter_cm": [8, 25]},
        "gills": {"attachment": "pores", "spacing": "n/a", "colors": ["red", "orange"]},
        "stem": {"colors": ["red", "yellow"], "ring": False, "volva": False},
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Europe, rarer in North America",
        "description": ("A pale capped bolete with a bulbous red/yellow stem and red pores. Causes "
                        "severe GI poisoning. The red pores and bulbous red stem separate it from "
                        "the choice king bolete."),
        "lookalikes": [
            {"name": "Boletus edulis", "distinguish": "King bolete has whitish pores and a pale, netted stem -- no red."}
        ]
    },
    {
        "id": "cantharellus-cibarius",
        "name": "Golden Chanterelle",
        "scientific_name": "Cantharellus cibarius",
        "aliases": ["chanterelle", "egg mushroom"],
        "edibility": "choice",
        "cap": {"shape": ["funnel", "depressed"], "colors": ["yellow", "orange"], "diameter_cm": [3, 10]},
        "gills": {"attachment": "decurrent", "spacing": "false-gills", "colors": ["yellow", "orange"]},
        "stem": {"colors": ["yellow", "orange"], "ring": False, "volva": False},
        "spore_print": "yellow",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Egg-yellow, fruity-smelling, with blunt false-gills (ridges, not sharp blades) "
                        "running down the stem. A top edible. Its apricot aroma is a good ID clue."),
        "lookalikes": [
            {"name": "Omphalotus olearius (jack-o'-lantern)", "distinguish": "Has TRUE sharp gills and glows in the dark; poisonous."},
            {"name": "Hygrophoropsis aurantiaca (false chanterelle)", "distinguish": "Has true forked gills; less choice."}
        ]
    },
    {
        "id": "omphalotus-olearius",
        "name": "Jack-o'-Lantern",
        "scientific_name": "Omphalotus olearius",
        "aliases": ["jack o lantern mushroom"],
        "edibility": "poisonous",
        "cap": {"shape": ["funnel", "convex"], "colors": ["orange"], "diameter_cm": [5, 15]},
        "gills": {"attachment": "decurrent", "spacing": "crowded", "colors": ["orange"]},
        "stem": {"colors": ["orange"], "ring": False, "volva": False},
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["autumn"],
        "distribution": "Eastern North America, Europe",
        "description": ("Brilliant orange with true, sharp, decurrent gills. Causes severe vomiting/"
                        "diarrhea. Famous for bioluminescence -- its gills glow faintly green at night. "
                        "Grows in clusters on wood, unlike chanterelles."),
        "lookalikes": [
            {"name": "Cantharellus (chanterelle)", "distinguish": "Chanterelles have blunt false-gills, grow on ground, don't glow, don't cluster on wood."}
        ],
        "fun_fact": "In the dark, a cluster can be bright enough to read by."
    },
    {
        "id": "morchella-esculenta",
        "name": "Common Morel",
        "scientific_name": "Morchella esculenta",
        "aliases": ["morel", "sponge mushroom"],
        "edibility": "choice",
        "cap": {"shape": [" conical", "pitted"], "colors": ["tan", "brown", "gray"], "diameter_cm": [3, 8]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white", "cream"], "ring": False, "volva": False},
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["spring"],
        "distribution": "Northern Hemisphere",
        "description": ("Honeycomb-capped, hollow spring delicacy. MUST be cooked -- raw morels are "
                        "toxic. Prized by chefs. Found in disturbed ground, old orchards, and burns."),
        "lookalikes": [
            {"name": "Gyromitra esculenta (false morel)", "distinguish": "Lobed/brain-like, NOT honeycombed; solid/ stuffed cap; deadly when raw."},
            {"name": "Verpa species", "distinguish": "Thimble-on-a-stick; cap not fully attached at sides."}
        ]
    },
    {
        "id": "gyromitra-esculenta",
        "name": "False Morel",
        "scientific_name": "Gyromitra esculenta",
        "aliases": ["brain mushroom", "turban fungus"],
        "edibility": "deadly",
        "cap": {"shape": ["lobed", "brain-like"], "colors": ["brown", "red-brown"], "diameter_cm": [3, 10]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white", "cream"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["spring"],
        "distribution": "Northern Hemisphere, conifer regions",
        "description": ("Resembles a morel but the cap is a lobed, brain-like mass that is NOT a "
                        "regular honeycomb and is attached only at the top. Contains gyromitrin, a "
                        "carcinogenic toxin converted to monomethylhydrazine. Deadly if eaten raw/"
                        "improperly prepared; some regions ban its sale."),
        "lookalikes": [
            {"name": "Morchella (true morel)", "distinguish": "True morels have a pitted honeycomb cap attached to the stem along its full length; false morels are irregularly lobed and hang free."}
        ]
    },
    {
        "id": "lactarius-deliciosus",
        "name": "Saffron Milkcap",
        "scientific_name": "Lactarius deliciosus",
        "aliases": ["delicious milkcap", "red pine mushroom"],
        "edibility": "edible",
        "cap": {"shape": ["funnel", "depressed"], "colors": ["orange", "red-orange"], "diameter_cm": [4, 12]},
        "gills": {"attachment": "decurrent", "spacing": "crowded", "colors": ["orange"]},
        "stem": {"colors": ["orange"], "ring": False, "volva": False},
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere pine forests",
        "description": ("When cut or bruised it weeps carrot-orange latex (milk). Cap has concentric "
                        "zones. Mild and good when cooked, with a piney note. A mycorrhizal partner "
                        "of pines."),
        "lookalikes": [
            {"name": "Lactarius deterrimus", "distinguish": "Very similar; stains greenish; also edible."},
            {"name": "Lactarius torminosus (woolly milkcap)", "distinguish": "Shaggy/inrolled cap edge, acrid; poisonous."}
        ]
    },
    {
        "id": "pleurotus-ostreatus",
        "name": "Oyster Mushroom",
        "scientific_name": "Pleurotus ostreatus",
        "aliases": ["oyster fungus", "tree oyster"],
        "edibility": "choice",
        "cap": {"shape": ["shell", "fan"], "colors": ["gray", "white", "tan", "blue"], "diameter_cm": [5, 20]},
        "gills": {"attachment": "decurrent", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "lilac-gray",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["autumn", "winter", "spring"],
        "distribution": "Worldwide",
        "description": ("Shelf-like, fan-shaped caps in overlapping clusters on dead hardwood. Oyster-"
                        "shaped, with decurrent gills and a lilac-gray spore print. Easy to cultivate "
                        "and a reliable edible."),
        "lookalikes": [
            {"name": "Pleurocybella porrigens (angel wings)", "distinguish": "Thinner, pure white; avoid for those with kidney issues."},
            {"name": "Omphalotus (jack-o'-lantern)", "distinguish": "Grows on wood too but is orange and poisonous."}
        ]
    },
    {
        "id": "lentinula-edodes",
        "name": "Shiitake",
        "scientific_name": "Lentinula edodes",
        "aliases": ["black forest mushroom", "oak mushroom"],
        "edibility": "choice",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "tan"], "diameter_cm": [5, 12]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white", "brown"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["spring", "summer", "autumn"],
        "distribution": "East Asia; cultivated worldwide",
        "description": ("Cultivated on oak logs; dark brown cap with white cracks when mature, tough "
                        "stem best removed. Rich, savory umami flavor. One of the most eaten mushrooms "
                        "globally."),
        "lookalikes": [
            {"name": "Various brown saprotrophic species", "distinguish": "Cultivated origin and cracked cap are distinctive; confirm spore print is white."}
        ]
    },
    {
        "id": "coprinus-comatus",
        "name": "Shaggy Mane",
        "scientific_name": "Coprinus comatus",
        "aliases": ["lawyer's wig", "shaggy ink cap"],
        "edibility": "edible",
        "cap": {"shape": ["bell", "cylindrical"], "colors": ["white"], "diameter_cm": [3, 7]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white", "black"]},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "black",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["spring", "autumn"],
        "distribution": "Worldwide, lawns and disturbed ground",
        "description": ("Tall white cylindrical cap covered in shaggy scales that auto-digests (deliquesces) "
                        "into black ink from the bottom up. Edible when young and fresh; do NOT combine "
                        "with alcohol (coprine causes a disulfiram-like reaction)."),
        "lookalikes": [
            {"name": "Coprinopsis atramentaria (common ink cap)", "distinguish": "Gray, smooth, no shaggy scales; also alcohol-reactive."},
            {"name": "Young Amanita", "distinguish": "Amanitas have a volva and do not deliquesce."}
        ]
    },
    {
        "id": "macrolepiota-procera",
        "name": "Parasol Mushroom",
        "scientific_name": "Macrolepiota procera",
        "aliases": ["parasol", "shaggy parasol"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "umbonate"], "colors": ["brown", "tan"], "diameter_cm": [10, 30]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white"]},
        "stem": {"colors": ["white", "brown"], "ring": True, "volva": False},
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Worldwide, grassy open areas",
        "description": ("Large, with a shaggy brown-scaled cap, a movable snake-skin-patterned ring, and "
                        "a stem that swells like a bulb at the base. Excellent edible -- but must be "
                        "distinguished from the green-spored parasol."),
        "lookalikes": [
            {"name": "Chlorophyllum molybdites (green-spored parasol)", "distinguish": "POISONOUS; green spore print and green-tinged gills when mature."},
            {"name": "Amanita species", "distinguish": "Amanitas have a volva cup; parasols do not."}
        ]
    },
    {
        "id": "chlorophyllum-molybdites",
        "name": "Green-Spored Parasol",
        "scientific_name": "Chlorophyllum molybdites",
        "aliases": ["false parasol", "green gill"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "umbonate"], "colors": ["brown", "tan"], "diameter_cm": [8, 30]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white", "green"]},
        "stem": {"colors": ["white", "brown"], "ring": True, "volva": False},
        "spore_print": "green",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "North America, warm regions worldwide",
        "description": ("The most common cause of mushroom poisoning in North America. Looks like an "
                        "edible parasol but the gills turn greenish with age and the spore print is "
                        "distinctly green. Causes violent GI illness."),
        "lookalikes": [
            {"name": "Macrolepiota procera (parasol)", "distinguish": "True parasol has a WHITE spore print; always print green-spored parasol before eating."}
        ]
    },
    {
        "id": "armillaria-mellea",
        "name": "Honey Fungus",
        "scientific_name": "Armillaria mellea",
        "aliases": ["honey mushroom"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["honey", "yellow-brown", "brown"], "diameter_cm": [3, 15]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["brown", "yellow"], "ring": True, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": ["autumn"],
        "distribution": "Worldwide",
        "description": ("Honey-colored caps in clusters at the base of trees, with a ring and black "
                        "rhizomorphs ('shoelaces') under the bark. Edible when young and thoroughly "
                        "cooked; some people are sensitive. A notorious plant pathogen."),
        "lookalikes": [
            {"name": "Galerina marginata (deadly galerina)", "distinguish": "Grows on wood too but is smaller, brown-spored, and DEADLY. Always check spore print."}
        ]
    },
    {
        "id": "galerina-marginata",
        "name": "Deadly Galerina",
        "scientific_name": "Galerina marginata",
        "aliases": ["funeral bell"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "bell"], "colors": ["brown", "tan", "rusty"], "diameter_cm": [2, 5]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["rusty", "brown"]},
        "stem": {"colors": ["brown"], "ring": False, "volva": False},
        "spore_print": "rusty-brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Small brown mushroom on wood containing amatoxins -- same family as the death "
                        "cap. Looks alarmingly like an edible honey fungus or a magic mushroom. The "
                        "rusty-brown spore print and wood habitat are clues."),
        "lookalikes": [
            {"name": "Armillaria mellea", "distinguish": "Honey fungus is larger, yellow-brown, ringed, white-spored."},
            {"name": "Psilocybe species", "distinguish": "Magic mushrooms grow on wood/dung; galerina is deadly -- never guess."}
        ]
    },
    {
        "id": "hericium-erinaceus",
        "name": "Lion's Mane",
        "scientific_name": "Hericium erinaceus",
        "aliases": ["bearded tooth", "pom pom mushroom", "yamabushitake"],
        "edibility": "choice",
        "cap": {"shape": ["spherical", "tooth"], "colors": ["white", "cream"], "diameter_cm": [5, 15]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["late summer", "autumn"],
        "distribution": "Northern Hemisphere hardwoods",
        "description": ("A white, cascading mass of icicle-like teeth rather than gills or pores. No "
                        "poisonous lookalikes resemble it. Tastes like seafood (lobster/crab) when "
                        "cooked. Studied for potential nerve-regenerative effects."),
        "lookalikes": [
            {"name": "Hericium coralloides / americanum", "distinguish": "Branched, coral-like forms; also edible."}
        ]
    },
    {
        "id": "sparassis-crispa",
        "name": "Cauliflower Fungus",
        "scientific_name": "Sparassis crispa",
        "aliases": ["cauliflower mushroom", "brain fungus"],
        "edibility": "edible",
        "cap": {"shape": ["lobed", "cauliflower"], "colors": ["cream", "tan"], "diameter_cm": [10, 40]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["cream"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["late summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("A large, ruffled mass resembling a head of cauliflower growing at the base of "
                        "conifers. Mild, crunchy, and good eating. Unmistakable once seen."),
        "lookalikes": [
            {"name": "Gyromitra esculenta (false morel)", "distinguish": "Brain-lobed and on the ground (not at a wood base); contains gyromitrin and is POISONOUS. Sparassis is a ruffled mass on wood."},
            {"name": "Hericium species (tooth fungi)", "distinguish": "Also cauliflower-like but covered in spiky teeth rather than smooth ruffled lobes; edible."}
        ]
    },
    {
        "id": "trametes-versicolor",
        "name": "Turkey Tail",
        "scientific_name": "Trametes versicolor",
        "aliases": ["Coriolus", "kawaratake"],
        "edibility": "inedible",
        "cap": {"shape": ["shell", "fan"], "colors": ["brown", "gray", "blue", "white", "tan"], "diameter_cm": [2, 8]},
        "gills": {"attachment": "pores", "spacing": "n/a", "colors": ["white"]},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["year-round"],
        "distribution": "Worldwide",
        "description": ("Thin, tough, concentric-zoned bracket fungus in overlapping colorful bands. "
                        "Too leathery to eat but valued in traditional medicine (PSP/beta-glucans). "
                        "A benchmark 'polypore' for ID practice."),
        "lookalikes": [
            {"name": "Stereum ostrea (false turkey tail)", "distinguish": "Smooth underside, no pores."}
        ]
    },
    {
        "id": "fomes-fomentarius",
        "name": "Hoof Fungus",
        "scientific_name": "Fomes fomentarius",
        "aliases": ["tinder fungus", "horse hoof fungus"],
        "edibility": "inedible",
        "cap": {"shape": ["hoof", "bracket"], "colors": ["gray", "black", "brown"], "diameter_cm": [5, 25]},
        "gills": {"attachment": "pores", "spacing": "n/a", "colors": ["brown"]},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["year-round"],
        "distribution": "Northern Hemisphere, on birch",
        "description": ("Hard, hoof-shaped bracket with concentric rings and a pore surface underneath. "
                        "Used historically as tinder (Ötzi the Iceman carried it) and for amadou. "
                        "Inedible but culturally fascinating."),
        "lookalikes": [
            {"name": "Phellinus igniarius (false tinder fungus)", "distinguish": "Near-identical hoof bracket; also inedible with darker context flesh."},
            {"name": "Ganoderma species (reishi)", "distinguish": "Lacquered reddish shelf with a lateral stem and rusty-brown spores; not hoof-shaped."}
        ]
    },
    {
        "id": "calvatia-gigantea",
        "name": "Giant Puffball",
        "scientific_name": "Calvatia gigantea",
        "aliases": ["puffball", "calf's lung"],
        "edibility": "edible",
        "cap": {"shape": ["spherical", "ball"], "colors": ["white", "tan"], "diameter_cm": [10, 50]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "olive-brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["late summer", "autumn"],
        "distribution": "Worldwide in pastures",
        "description": ("A soccer-ball-sized white sphere with no stem, gills, or cap. Edible ONLY while "
                        "pure white inside; once it yellows or turns into spores, discard. Cut one open "
                        "to confirm -- never eat anything that isn't uniformly white throughout."),
        "lookalikes": [
            {"name": "Amanita 'egg' (young death cap/destroying angel)", "distinguish": "Young Amanitas underground look like small puffballs but have a stem/volva inside when cut -- DEADLY."},
            {"name": "Scleroderma (earthball)", "distinguish": "Has a dark, powdery interior even when young; poisonous."}
        ]
    },
    {
        "id": "scleroderma-citrinum",
        "name": "Common Earthball",
        "scientific_name": "Scleroderma citrinum",
        "aliases": ["earthball", "poison puffball"],
        "edibility": "poisonous",
        "cap": {"shape": ["spherical", "ball"], "colors": ["yellow", "brown", "tan"], "diameter_cm": [3, 10]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "purple-black",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Looks like a puffball but the interior is dark purple-black and powdery even "
                        "when young, and the skin is thick and yellow-cracked. Causes GI upset. The "
                        "dark interior is the key difference from edible puffballs."),
        "lookalikes": [
            {"name": "Calvatia (puffball)", "distinguish": "Puffballs are white inside at edible stage."}
        ]
    },
    {
        "id": "lycoperdon-perlatum",
        "name": "Common Puffball",
        "scientific_name": "Lycoperdon perlatum",
        "aliases": ["gemmed puffball", "warted puffball"],
        "edibility": "edible",
        "cap": {"shape": ["pear", "ball"], "colors": ["white", "tan"], "diameter_cm": [2, 6]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Worldwide",
        "description": ("Pear-shaped, covered in small warts, with a stem-like base. Edible when young "
                        "and solid white inside. A safe, common beginner foraging find."),
        "lookalikes": [
            {"name": "Young Amanita", "distinguish": "Cut open: Amanita has a miniature cap/stem inside."}
        ]
    },
    {
        "id": "suillus-luteus",
        "name": "Slippery Jack",
        "scientific_name": "Suillus luteus",
        "aliases": ["pine bolete"],
        "edibility": "edible",
        "cap": {"shape": ["convex"], "colors": ["brown", "chestnut"], "diameter_cm": [5, 12]},
        "gills": {"attachment": "pores", "spacing": "n/a", "colors": ["yellow"]},
        "stem": {"colors": ["yellow", "cream"], "ring": True, "volva": False},
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere pine plantations",
        "description": ("A bolete (pores, no gills) with a slimy brown cap and a slimy ring on the stem. "
                        "Peel the slimy cap skin before eating. Common under pines, easy and safe once "
                        "you recognize the pore surface."),
        "lookalikes": [
            {"name": "Suillus granulatus", "distinguish": "Nearly identical but lacks the slimy ring on the stem; edible."},
            {"name": "Boletus edulis (porcini)", "distinguish": "Larger with a dry, non-slimy cap and no ring; a choice edible, so confusion is harmless."}
        ]
    },
    {
        "id": "tricholoma-matsutake",
        "name": "Matsutake",
        "scientific_name": "Tricholoma matsutake",
        "aliases": ["pine mushroom", "matsutake"],
        "edibility": "choice",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "tan", "white"], "diameter_cm": [6, 20]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["white"]},
        "stem": {"colors": ["white", "brown"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["autumn"],
        "distribution": "Asia, North America, Europe (declining)",
        "description": ("Highly prized in Japan for its spicy, cinnamon-pine aroma. White flesh that "
                        "stays white when cut, with a partial veil that often leaves a ring zone. "
                        "Forms mycorrhizae with specific pines/oaks."),
        "lookalikes": [
            {"name": "Amanita species", "distinguish": "Matsutake has white spores and no volva; some toxic Amanitas smell similar."},
            {"name": "Tricholoma pardinum (tiger trich)", "distinguish": "POISONOUS; similar size and white gills but a scaly/felted cap and an abruptly bulbous stem base causing violent GI poisoning. Check the cap surface and base."}
        ]
    },
    {
        "id": "russula-emetica",
        "name": "The Sickener",
        "scientific_name": "Russula emetica",
        "aliases": ["emetic russula"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "flat"], "colors": ["red", "pink"], "diameter_cm": [4, 10]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["white"]},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("A red-capped Russula with very brittle white gills and stem (characteristic of "
                        "the genus -- they snap like chalk). Acrid and emetic; causes vomiting. Many "
                        "Russulas are edible, so species-level ID matters."),
        "lookalikes": [
            {"name": "Edible Russulas (e.g. R. cyanoxantha)", "distinguish": "Those lack the hot, peppery taste and are not bright red."}
        ]
    },
    {
        "id": "russula-cyanoxantha",
        "name": "Charcoal Burner",
        "scientific_name": "Russula cyanoxantha",
        "aliases": ["blue-yellow russula"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["purple", "green", "brown", "red"], "diameter_cm": [5, 15]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("A variable-colored Russula with flexible, greasy gills (unusual -- most Russula "
                        "gills are brittle) and a mild, non-peppery taste. A reliable edible once you "
                        "learn the genus."),
        "lookalikes": [
            {"name": "Russula emetica", "distinguish": "Sickener is bright red and acrid-tasting."}
        ]
    },
    {
        "id": "hypholoma-fasciculare",
        "name": "Sulfur Tuft",
        "scientific_name": "Hypholoma fasciculare",
        "aliases": ["sulphur tuft"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "flat"], "colors": ["yellow", "orange", "olive"], "diameter_cm": [2, 6]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["green", "olive", "brown"]},
        "stem": {"colors": ["yellow"], "ring": False, "volva": False},
        "spore_print": "purple-brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["spring", "autumn"],
        "distribution": "Worldwide",
        "description": ("Dense clusters of sulfur-yellow caps with greenish-yellow gills on rotting wood. "
                        "Bitter and poisonous (contains fasciculol). The clustered growth on wood and "
                        "yellow coloring are distinctive."),
        "lookalikes": [
            {"name": "Armillaria mellea", "distinguish": "Honey fungus is larger, honey-colored, white-gilled."},
            {"name": "Edible clustered species", "distinguish": "None share the exact sulfur-yellow + green-gill combo on wood."}
        ]
    },
    {
        "id": "cortinarius-rubellus",
        "name": "Deadly Webcap",
        "scientific_name": "Cortinarius rubellus",
        "aliases": ["deadly cortinarius", "orange webcap"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "bell"], "colors": ["orange", "brown", "rusty"], "diameter_cm": [3, 8]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["rusty", "orange"]},
        "stem": {"colors": ["orange", "rusty"], "ring": True, "volva": False},
        "spore_print": "rusty-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["autumn"],
        "distribution": "Northern Europe and North America",
        "description": ("Contains orellanine, which causes delayed (days to weeks) but often fatal kidney "
                        "failure. Rusty-orange with a cobweb (cortina) veil when young. Part of a large, "
                        "difficult genus best avoided by amateurs."),
        "lookalikes": [
            {"name": "Many Cortinarius species", "distinguish": "The whole genus is risky; rusty spore print is a unifying trait."}
        ]
    },
    {
        "id": "clitocybe-dealbata",
        "name": "Ivory Funnel",
        "scientific_name": "Clitocybe dealbata",
        "aliases": ["poisonous funnel"],
        "edibility": "deadly",
        "cap": {"shape": ["funnel", "depressed"], "colors": ["white", "cream", "pale"], "diameter_cm": [2, 5]},
        "gills": {"attachment": "decurrent", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere lawns and pastures",
        "description": ("Small, pale, funnel-shaped and easily confused with edible field mushrooms or "
                        "oyster mushrooms. Contains muscarine, which can be fatal, especially dangerous "
                        "because it looks so innocuous and grows in grazed areas."),
        "lookalikes": [
            {"name": "Edible white fungi", "distinguish": "Small size, funnel shape, and white spore print on lawns are red flags."}
        ]
    },
    {
        "id": "psilocybe-cubensis",
        "name": "Magic Mushroom",
        "scientific_name": "Psilocybe cubensis",
        "aliases": ["golden teacher", "cubes"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "bell"], "colors": ["brown", "gold", "tan"], "diameter_cm": [2, 8]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["purple", "brown", "gray"]},
        "stem": {"colors": ["white", "blue"], "ring": True, "volva": False},
        "spore_print": "purple-brown",
        "habitat": "grassland",
        "substrate": "dung",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Subtropical/tropical worldwide",
        "description": ("Contains psilocybin and is a controlled hallucinogen in most jurisdictions. "
                        "Bruises blue, grows on dung, has a purple-brown spore print. Listed here for "
                        "education and harm reduction -- not recommended or legal in many places."),
        "lookalikes": [
            {"name": "Galerina marginata", "distinguish": "DEADLY; similar habitat/size but no blue bruising and rusty-brown spores."},
            {"name": "Panaeolus species", "distinguish": "Also dung-loving; some are psychoactive, some not."}
        ]
    },
    {
        "id": "flammulina-velutipes",
        "name": "Enoki",
        "scientific_name": "Flammulina velutipes",
        "aliases": ["velvet foot", "winter mushroom", "enokitake"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["white", "tan", "brown"], "diameter_cm": [2, 8]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["brown", "tan"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["autumn", "winter", "spring"],
        "distribution": "Worldwide on hardwood",
        "description": ("In the wild: small brown caps on a dark, velvety stem in clusters on dead trees. "
                        "Cultivated forms are the long, white, noodle-like enoki. Edible and mild."),
        "lookalikes": [
            {"name": "Galerina marginata", "distinguish": "Deadly; grows on wood too -- confirm white spores and velvety stem base."}
        ]
    },
    {
        "id": "auricularia-auricula-judae",
        "name": "Wood Ear",
        "scientific_name": "Auricularia auricula-judae",
        "aliases": ["jelly ear", "black fungus", "mu er"],
        "edibility": "edible",
        "cap": {"shape": ["ear", "shelf"], "colors": ["brown", "red-brown", "black"], "diameter_cm": [3, 10]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["year-round"],
        "distribution": "Worldwide on elder and other hardwoods",
        "description": ("A rubbery, ear-shaped jelly fungus, brown when moist and brittle when dry. "
                        "Flavorless but prized for crunch in Asian cooking. No dangerous lookalikes."),
        "lookalikes": [
            {"name": "Auricularia polytricha (cloud ear)", "distinguish": "Closely related, darker and hairier on top; equally edible."},
            {"name": "Tremella species (white/yellow jellies)", "distinguish": "Lobed or branched jellies, not ear-shaped; also edible."}
        ]
    },
    {
        "id": "tremella-fuciformis",
        "name": "Snow Fungus",
        "scientific_name": "Tremella fuciformis",
        "aliases": ["silver ear", "white jelly mushroom", "yin er"],
        "edibility": "edible",
        "cap": {"shape": ["lobed", "jelly"], "colors": ["white", "cream"], "diameter_cm": [3, 12]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": ["summer", "autumn"],
        "distribution": "Tropical/subtropical Asia; cultivated",
        "description": ("A translucent, ruffled white jelly fungus used in Chinese desserts and soups for "
                        "its texture and supposed health benefits. Requires a host fungus to fruit."),
        "lookalikes": [
            {"name": "Tremella mesenterica (yellow brain)", "distinguish": "Bright yellow lobed jelly; edible but insubstantial."},
            {"name": "Auricularia (wood ear)", "distinguish": "Ear-shaped brown/black jelly rather than white-lobed; both edible."}
        ]
    },
    {
        "id": "schizophyllum-commune",
        "name": "Split Gill",
        "scientific_name": "Schizophyllum commune",
        "aliases": ["split-gill fungus"],
        "edibility": "inedible",
        "cap": {"shape": ["shell", "fan"], "colors": ["white", "gray", "tan"], "diameter_cm": [1, 4]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["white", "gray"]},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["year-round"],
        "distribution": "Cosmopolitan",
        "description": ("Tiny fuzzy shells with gills that split lengthwise when dry and close when wet -- "
                        "a unique feature. Too tough and thin to eat; primarily of interest for its "
                        "unusual biology (it has over 20,000 sexes)."),
        "lookalikes": [
            {"name": "Small bracket fungi", "distinguish": "The split gills are unique."}
        ]
    },
    {
        "id": "phallus-impudicus",
        "name": "Common Stinkhorn",
        "scientific_name": "Phallus impudicus",
        "aliases": ["stinkhorn"],
        "edibility": "edible",
        "cap": {"shape": ["bell", "netted"], "colors": ["olive", "green", "white"], "diameter_cm": [3, 5]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white"], "ring": False, "volva": True},
        "spore_print": "olive",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Europe, North America",
        "description": ("Emerges as a white 'egg' (edible at this stage, like a truffle-ish delicacy in "
                        "some cuisines), then rapidly expands into a stinky, olive-spored phallus that "
                        "attracts flies to spread spores. The young egg is the edible part."),
        "lookalikes": [
            {"name": "Amanita 'egg'", "distinguish": "Both start as eggs; stinkhorn egg has a softer, more gelatinous texture and lacks a volva cup."}
        ]
    },
    {
        "id": "ramaria-formosa",
        "name": "Beautiful Coral",
        "scientific_name": "Ramaria formosa",
        "aliases": ["coral fungus"],
        "edibility": "poisonous",
        "cap": {"shape": ["branched", "coral"], "colors": ["pink", "salmon", "tan"], "diameter_cm": [8, 20]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white", "tan"], "ring": False, "volva": False},
        "spore_print": "ochre",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("A pink, branching coral-shaped fungus. Causes GI upset in many people. Coral "
                        "fungi are a mixed bag -- some edible, some not -- so species ID is essential "
                        "and beginners should avoid them."),
        "lookalikes": [
            {"name": "Ramaria botrytis (edible coral)", "distinguish": "Different color/branch tips; coral ID is expert-level."}
        ]
    },
    {
        "id": "clavulina-cristata",
        "name": "Crested Coral",
        "scientific_name": "Clavulina cristata",
        "aliases": ["white coral", "cock's comb"],
        "edibility": "edible",
        "cap": {"shape": ["branched", "coral"], "colors": ["white"], "diameter_cm": [3, 8]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("White, intricately branched coral with toothed tips. Generally considered edible "
                        "and mild, though not choice. A good example of the coral growth form."),
        "lookalikes": [
            {"name": "Ramaria formosa", "distinguish": "That one is pink and poisonous."}
        ]
    },
    {
        "id": "leccinum-scrobum",
        "name": "Birch Bolete",
        "scientific_name": "Leccinum scabrum",
        "aliases": ["rough-stemmed bolete"],
        "edibility": "edible",
        "cap": {"shape": ["convex"], "colors": ["brown", "tan", "gray"], "diameter_cm": [5, 15]},
        "gills": {"attachment": "pores", "spacing": "n/a", "colors": ["white", "gray"]},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere under birch",
        "description": ("A bolete (pores) with a gray-brown cap and a stem covered in dark scabrous "
                        "dots. Common under birch. Edible and easy to ID within the safe bolete group."),
        "lookalikes": [
            {"name": "Leccinum aurantiacum (red-capped bolete)", "distinguish": "Orange-red cap, also under hardwoods; edible."},
            {"name": "Boletus edulis (porcini)", "distinguish": "No scabrous stem dots and a smooth stem; a choice edible."}
        ]
    },
    {
        "id": "verpa-bohemica",
        "name": "Early Morel",
        "scientific_name": "Verpa bohemica",
        "aliases": ["false morel", "thimble morel"],
        "edibility": "edible",
        "cap": {"shape": ["thimble", "wrinkled"], "colors": ["tan", "brown"], "diameter_cm": [2, 5]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white", "cream"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["spring"],
        "distribution": "Northern Hemisphere",
        "description": ("A morel-lookalike with a cap attached only at the top like a thimble on a stem, "
                        "and a hollow stem. Edible when cooked but easily confused with the deadly "
                        "false morel (Gyromitra) -- learn the difference before foraging."),
        "lookalikes": [
            {"name": "Gyromitra esculenta", "distinguish": "Gyromitra cap is lobed and hangs free at the edge; Verpa cap attaches at the apex only."},
            {"name": "Morchella", "distinguish": "True morel cap is fully attached to the stem."}
        ]
    },
    {
        "id": "laetiporus-sulphureus",
        "name": "Chicken of the Woods",
        "scientific_name": "Laetiporus sulphureus",
        "aliases": ["sulfur shelf", "chicken mushroom"],
        "edibility": "edible",
        "cap": {"shape": ["shelf", "bracket"], "colors": ["orange", "yellow", "red"], "diameter_cm": [10, 40]},
        "gills": {"attachment": "pores", "spacing": "n/a", "colors": ["yellow", "white"]},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Worldwide on hardwoods (and conifers in some regions)",
        "description": ("Bright orange and yellow shelf clusters on tree trunks with a texture and taste "
                        "likened to chicken (when young). A favorite edible -- but some react to the "
                        "conifer form, so try a small amount first."),
        "lookalikes": [
            {"name": "Omphalotus (jack-o'-lantern)", "distinguish": "Also orange clusters on wood but has true gills, not pores, and is poisonous."}
        ]
    },
    {
        "id": "amerenia-smithiana",
        "name": "Deadly Parachute",
        "scientific_name": "Amanita smithiana",
        "aliases": ["Smith's amanita"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "flat"], "colors": ["white", "cream", "tan"], "diameter_cm": [4, 10]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white"]},
        "stem": {"colors": ["white"], "ring": True, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Pacific Northwest of North America; also reported in Europe",
        "description": ("A pale, innocuous-looking Amanita whose toxins (aminohexadienoic acid) cause irreversible kidney failure. It lacks the classic volva of death-cap types, which makes it dangerously easy to mistake for a harmless white mushroom."),
        "lookalikes": [
            {"name": "Amanita velosa (veiled amanita)", "distinguish": "An edible West Coast Amanita with a tan cap and similar size; positive ID requires microscopy."},
            {"name": "Agaricus species (field mushrooms)", "distinguish": "Have pink-then-brown gills and a ring but no volva/ring combination like Amanita."}
        ],
        "fun_fact": "One of several 'little brown' amanitas whose look is no clue to its lethality."
    },
    {
        "id": "amanita-ocreata",
        "name": "Death Angel",
        "scientific_name": "Amanita ocreata",
        "aliases": ["coccora", "European death cap (relative)"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "bell"], "colors": ["white", "cream", "pale-tan"], "diameter_cm": [4, 12]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white"]},
        "stem": {"colors": ["white"], "ring": True, "volva": True},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["winter", "spring"],
        "distribution": "Western North America (California to Baja)",
        "description": ("A pure white, ringed amanita with a cup (volva) at the base. Contains amatoxins and is responsible for fatal poisonings, often in spring when foragers confuse it with edible mushrooms."),
        "lookalikes": [
            {"name": "Amanita velosa", "distinguish": "Edible, but the margin of the cap is distinctly fuzzy/striate; still risky without expertise."},
            {"name": "Young Agaricus", "distinguish": "Have pink/brown gills even when young, never a true volva cup."}
        ],
        "fun_fact": "Its toxicity is unrelated to cooking — amatoxins survive heat intact."
    },
    {
        "id": "entoloma-sinuatum",
        "name": "Livid Entoloma",
        "scientific_name": "Entoloma sinuatum",
        "aliases": ["leaden entoloma", "sinuate entoloma"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "flat"], "colors": ["gray", "tan", "buff"], "diameter_cm": [6, 20]},
        "gills": {"attachment": "sinuate", "spacing": "crowded", "colors": ["pink"]},
        "stem": {"colors": ["white", "gray"], "ring": False, "volva": False},
        "spore_print": "pink",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Europe and North America",
        "description": ("A large gray-cap mushroom with the giveaway pink gills and spores of the Entoloma family. Causes severe gastrointestinal poisoning; responsible for many European poisonings because it vaguely resembles an edible field mushroom."),
        "lookalikes": [
            {"name": "Agaricus campestris (field mushroom)", "distinguish": "Has chocolate-brown spores and browner gills; Entoloma keeps pink gills from the start."},
            {"name": "Tricholoma species", "distinguish": "White-spored lookalikes; check spore print color."}
        ],
        "fun_fact": "The pink spore print is the family trademark and the key to telling it from white-spored toxic amanitas."
    },
    {
        "id": "sarcosphaera-crassa",
        "name": "Violet Crown Cup",
        "scientific_name": "Sarcosphaera coronaria",
        "aliases": ["crown cup", "violet fairy cap"],
        "edibility": "poisonous",
        "cap": {"shape": ["cup", "split"], "colors": ["lilac", "violet", "cream"], "diameter_cm": [5, 15]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["spring", "summer"],
        "distribution": "Europe, North America (west)",
        "description": ("A striking cup fungus that splits into star-like segments, revealing violet to lilac inner flesh. Contains gyromitrin-like compounds and is considered poisonous, especially when consumed with alcohol."),
        "lookalikes": [
            {"name": "Peziza species (cup fungi)", "distinguish": "Similar cups but lack the violet pigment and star-like splitting; many are edible but verify."},
            {"name": "Sarcoscypha (scarlet cup)", "distinguish": "Smaller brilliant-red cup with no violet tone or crown split; edible."}
        ],
        "fun_fact": "Its color fades to cream as it ages and dries in the sun."
    },
    {
        "id": "mutinus-caninus",
        "name": "Dog Stinkhorn",
        "scientific_name": "Mutinus caninus",
        "aliases": ["dog phallus"],
        "edibility": "inedible",
        "cap": {"shape": ["phallus", "cylindrical"], "colors": ["orange", "red", "pink"], "diameter_cm": [2, 10]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["orange", "pink"], "ring": False, "volva": False},
        "spore_print": "n/a",
        "habitat": "forest",
        "substrate": "litter",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Europe, North America",
        "description": ("A small, orange-tipped, phallus-shaped fungus covered in olive spore slime (gleba) at the tip that attracts flies for spore dispersal. Not poisonous but inedible and foul-smelling; related to the larger stinkhorns."),
        "lookalikes": [
            {"name": "Phallus impudicus (common stinkhorn)", "distinguish": "Much larger with a lacy skirt (indusium) and a more prominent smelly gleba."}
        ],
        "fun_fact": "Flies do the pollination job — they eat the slime and spread spores on their feet."
    },
    {
        "id": "battarrea-phalloides",
        "name": "Sand Warrior",
        "scientific_name": "Battarrea phalloides",
        "aliases": ["desert shaggy mane", "stalked puffball"],
        "edibility": "inedible",
        "cap": {"shape": ["puffball", "umbel"], "colors": ["brown", "tan"], "diameter_cm": [3, 8]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["tan", "brown"], "ring": False, "volva": False},
        "spore_print": "brown",
        "habitat": "grassland",
        "substrate": "sand",
        "ecology": "saprotrophic",
        "season": ["autumn", "winter"],
        "distribution": "Arid and semi-arid regions worldwide",
        "description": ("A desert puffball on a tall, shaggy stem with a ragged skirt-like veil. Spores release from a powdery cap at the top. Too tough and insubstantial to eat; admired for its odd, sculptural form."),
        "lookalikes": [
            {"name": "Young puffballs (Calvatia)", "distinguish": "Lack the long stem and the torn skirt; Battarrea is all stalk."}
        ],
        "fun_fact": "It can push up through gravel and even asphalt thanks to its force-generating stem."
    },
    {
        "id": "xerocomellus-chrysenteron",
        "name": "Red-cracked Bolete",
        "scientific_name": "Xerocomellus chrysenteron",
        "aliases": ["boletus chrysenteron"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "olive", "tan"], "diameter_cm": [3, 10]},
        "gills": {"attachment": "pores", "spacing": "n/a", "colors": ["yellow", "olive"]},
        "stem": {"colors": ["yellow", "brown"], "ring": False, "volva": False},
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Europe, North America",
        "description": ("A common bolete whose brown cap cracks to reveal reddish flesh beneath. Mild and edible, though not as prized as porcini. A good beginner bolete to learn the pore-under-cap structure."),
        "lookalikes": [
            {"name": "Boletus edulis (porcini)", "distinguish": "Larger, paler, with a fine net pattern on the stem; both edible."},
            {"name": "Boletus satanas", "distinguish": "Poisonous; has a red-tinged stem and stains blue."}
        ],
        "fun_fact": "The red 'cracks' are how it got the name chrysenteron — 'golden inside'."
    },
    {
        "id": "stropharia-rugosoannulata",
        "name": "Wine Cap",
        "scientific_name": "Stropharia rugosoannulata",
        "aliases": ["king stropharia", "garden giant"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["maroon", "red-brown", "brown"], "diameter_cm": [8, 30]},
        "gills": {"attachment": "adnate", "spacing": "crowded", "colors": ["purple-gray", "brown"]},
        "stem": {"colors": ["white", "gray"], "ring": True, "volva": False},
        "spore_print": "purple-brown",
        "habitat": "garden",
        "substrate": "woodchip",
        "ecology": "saprotrophic",
        "season": ["spring", "summer", "autumn"],
        "distribution": "Europe, North America; widely cultivated",
        "description": ("A large, wine-red capped mushroom that fruits on wood chips and mulched garden beds. Easy to cultivate and a reliable edible with a meaty texture. A favorite for permaculture gardens."),
        "lookalikes": [
            {"name": "Chlorophyllum molybdites", "distinguish": "Poisonous; has green spores and a scaly tan cap, not wine-red."},
            {"name": "Agaricus species", "distinguish": "Have pink-then-brown gills and a ring but a different cap color."}
        ],
        "fun_fact": "It's one of the few gourmet mushrooms you can grow in a backyard mulch bed."
    },
    {
        "id": "pleurotus-pulmonarius",
        "name": "Phoenix Oyster",
        "scientific_name": "Pleurotus pulmonarius",
        "aliases": ["lung oyster", "pale oyster"],
        "edibility": "edible",
        "cap": {"shape": ["fan", "shelf"], "colors": ["cream", "tan", "gray"], "diameter_cm": [4, 15]},
        "gills": {"attachment": "decurrent", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white"], "ring": False, "volva": False},
        "spore_print": "lilac-gray",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["spring", "summer", "autumn"],
        "distribution": "Worldwide",
        "description": ("A pale, fan-shaped oyster mushroom that fruits on dead hardwoods, often in warm weather (unlike the cooler-loving pearl oyster). Excellent edible, mild and tender; nearly identical in use to the pearl oyster."),
        "lookalikes": [
            {"name": "Pleurotus ostreatus (pearl oyster)", "distinguish": "Very similar; distinguished mainly by season and spore print shade."},
            {"name": "Ivory funnel (Clitocybe dealbata)", "distinguish": "Poisonous; smaller, centrally stemmed, and grows on the ground."}
        ],
        "fun_fact": "Its lilac-gray spore print helps separate it from the white-spored poisonous lookalikes."
    },
    {
        "id": "grifola-frondosa",
        "name": "Hen of the Woods",
        "scientific_name": "Grifola frondosa",
        "aliases": ["maitake", "sheep's head"],
        "edibility": "choice",
        "cap": {"shape": ["rosette", "shelf"], "colors": ["gray", "brown", "tan"], "diameter_cm": [10, 60]},
        "gills": {"attachment": "decurrent", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white", "gray"], "ring": False, "volva": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["autumn"],
        "distribution": "Asia, Europe, North America",
        "description": ("A large, clustered 'rosette' of grayish fan caps at the base of oaks and other hardwoods. Prized edible (maitake) with a rich, earthy flavor and a celebrated status in Asian cuisine and medicine."),
        "lookalikes": [
            {"name": "Clustered Polyporus (Meripilus)", "distinguish": "Has pores rather than gills and blackens when bruised."},
            {"name": "Berkeley's polypore", "distinguish": "Pored, not gilled; both grow at tree bases."}
        ],
        "fun_fact": "A single clump can weigh several kilos — hence 'hen of the woods'."
    },
    {
        "id": "tuber-melanosporum",
        "name": "Black Truffle",
        "scientific_name": "Tuber melanosporum",
        "aliases": ["Périgord truffle", "black diamond"],
        "edibility": "choice",
        "cap": {"shape": ["tuber", "subterranean"], "colors": ["black", "brown"], "diameter_cm": [2, 9]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": [], "ring": False, "volva": False},
        "spore_print": "n/a",
        "habitat": "forest",
        "substrate": "roots",
        "ecology": "mycorrhizal",
        "season": ["winter", "spring"],
        "distribution": "Mediterranean Europe, cultivated worldwide",
        "description": ("A subterranean, knobbly black fungus forming with oak and hazel roots. Among the most prized edibles in the world for its intense aroma. Found by trained dogs or pigs; never visible above ground."),
        "lookalikes": [
            {"name": "Tuber aestivum (summer truffle)", "distinguish": "Lighter, milder, and found in warmer months; similar but less aromatic."},
            {"name": "Deer truffle (Elaphomyces)", "distinguish": "Inedible false truffle with a different internal marbling; ID needs expertise."}
        ],
        "fun_fact": "Truffle hunters once used pigs, but dogs are preferred now — pigs tend to eat the prize."
    },
    {
        "id": "morchella-conica",
        "name": "Conical Morel",
        "scientific_name": "Morchella conica",
        "aliases": ["black morel", "pointed morel"],
        "edibility": "edible",
        "cap": {"shape": ["cone", "honeycomb"], "colors": ["gray", "brown", "black"], "diameter_cm": [3, 10]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white", "cream"], "ring": False, "volva": False},
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["spring"],
        "distribution": "Northern Hemisphere",
        "description": ("A classic morel with a tall, conical, deeply pitted cap. A top-tier edible with a nutty, smoky flavor — but MUST be cooked; raw morels are toxic. Found in spring, often after disturbance or burns."),
        "lookalikes": [
            {"name": "Gyromitra esculenta (false morel)", "distinguish": "Brain-like wrinkled cap, not honeycomb pits; contains gyromitrin and is poisonous."},
            {"name": "Verpa bohemica", "distinguish": "Cap hangs like a thimble on a separate stem; less choice."}
        ],
        "fun_fact": "Morels and trees sometimes fruit in the same burned area the year after a fire."
    },
    {
        "id": "amanita-virosa",
        "name": "Death Angel (European)",
        "scientific_name": "Amanita virosa",
        "aliases": ["destroying angel", "white death cap"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "flat"], "colors": ["white", "cream"], "diameter_cm": [5, 12]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white"]},
        "stem": {"colors": ["white"], "ring": True, "volva": True},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Europe, introduced N. America",
        "description": ("Pallid all-white destroying angel in the same lethal group as A. bisporigera and A. ocreata. Contains amatoxins; the white volva cup at the base is the tell-tale death sign."),
        "lookalikes": [
            {"name": "Amanita bisporigera", "distinguish": "Near-identical NA destroying angel; both deadly -- volva + white gills are the danger signal."},
            {"name": "Amanita caesarea (Caesar's mushroom)", "distinguish": "Edible Amanita has an orange cap/stem, never the stark white volva look."},
            {"name": "Calvatia (puffball)", "distinguish": "Young puffballs are solid white inside; destroying angels have gills + a stem."}
        ],
        "fun_fact": "Amatoxins resist cooking, freezing, and drying -- no preparation makes it safe."
    },
    {
        "id": "amanita-rubescens",
        "name": "The Blusher",
        "scientific_name": "Amanita rubescens",
        "aliases": ["blushing amanita"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "tan"], "diameter_cm": [5, 15]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white", "pinkish"], "ring": True, "volva": True},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("One of the few edible Amanitas -- but only for the experienced. Flesh and stem bruise pink/red, and it keeps a skirt-like ring + volva remnants. A key teaching species: most Amanitas kill, this one is eaten."),
        "lookalikes": [
            {"name": "Amanita muscaria (fly agaric)", "distinguish": "Fly agaric is red-capped and poisonous; the Blusher is brown and reddens where bruised."},
            {"name": "Amanita phalloides (death cap)", "distinguish": "Death cap stays green/tan and does NOT redden; if in doubt, never eat an Amanita."}
        ],
        "fun_fact": "Its scientific name means 'reddening' -- the bruise colour is the ID clue."
    },
    {
        "id": "cortinarius-orellanus",
        "name": "Deadly Webcap",
        "scientific_name": "Cortinarius orellanus",
        "aliases": ["orange webcap"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "flat"], "colors": ["orange", "brown", "rust"], "diameter_cm": [3, 8]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["rust", "orange"]},
        "stem": {"colors": ["orange", "rust"], "ring": False, "volva": False},
        "spore_print": "rust",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["autumn"],
        "distribution": "Europe, N. America",
        "description": ("Ounce-for-ounce one of the most dangerous mushrooms: contains orellanine, which causes irreversible kidney failure with a delay of days to weeks. Rusty spores and an orange-brown cap."),
        "lookalikes": [
            {"name": "Many Cortinarius species", "distinguish": "Most webcaps are unsafe to eat; the genus is best avoided entirely."},
            {"name": "Cantharellus (chanterelle)", "distinguish": "Chanterelles are yellow with blunt false gills and a yellow spore print, not rusty."}
        ],
        "fun_fact": "Symptoms can appear up to 3 weeks later -- by then kidney damage is often permanent."
    },
    {
        "id": "lepiota-brunneoincarnata",
        "name": "Deadly Parasol",
        "scientific_name": "Lepiota brunneoincarnata",
        "aliases": ["browned parasol"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "umbonate"], "colors": ["brown", "tan"], "diameter_cm": [2, 6]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white", "brown"], "ring": True, "volva": False},
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["late summer", "autumn"],
        "distribution": "Europe, N. America",
        "description": ("Small, deadly Lepiota containing amatoxins, easily mistaken for an edible parasol or button mushroom. Brown scaly cap, a ring on the stem, and a bulbous base."),
        "lookalikes": [
            {"name": "Macrolepiota procera (parasol)", "distinguish": "True parasol is much larger (cap 10-25cm) with a shaggy brown-scaled cap and movable ring."},
            {"name": "Agaricus species (field/button mushrooms)", "distinguish": "Field mushrooms have pink-then-brown gills and a brown spore print; Lepiotas have white spores."}
        ],
        "fun_fact": "Several small Lepiota species are lethally poisonous despite looking like harmless fairy-ring mushrooms."
    },
    {
        "id": "galerina-autumnalis",
        "name": "Autumn Galerina",
        "scientific_name": "Galerina autumnalis",
        "aliases": ["deadly galerina"],
        "edibility": "deadly",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "tan", "yellow-brown"], "diameter_cm": [2, 5]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["rust", "brown"]},
        "stem": {"colors": ["brown", "yellowish"], "ring": True, "volva": False},
        "spore_print": "rust",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Amatoxin-containing little brown mushroom that grows on wood and is a classic fatal confusion with edible oysters and honey fungus. Rusty-brown spores and a ring on the stem."),
        "lookalikes": [
            {"name": "Pleurotus ostreatus (oyster mushroom)", "distinguish": "Oysters grow on wood too but have white decurrent gills and a white spore print, no ring."},
            {"name": "Armillaria mellea (honey fungus)", "distinguish": "Honey fungus has yellow-brown caps and a ring but whitish spore print and grows from a shared base."},
            {"name": "Kuehneromyces mutabilis", "distinguish": "Similar wood-loving brown mushroom with a ring; also best avoided by non-experts."}
        ],
        "fun_fact": "Its amatoxin load is so reliable that foragers use Galerina to test for amatoxins in new areas."
    },
    {
        "id": "kuehneromyces-mutabilis",
        "name": "Sheathed Woodtuft",
        "scientific_name": "Kuehneromyces mutabilis",
        "aliases": ["changing pholiota"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "tan", "yellow-brown"], "diameter_cm": [2, 6]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["tan", "rust"]},
        "stem": {"colors": ["brown"], "ring": True, "volva": False},
        "spore_print": "rust",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["spring", "summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Wood-growing brown mushroom with a ring, once eaten in parts of Europe but now widely considered toxic and a dangerous Galerina lookalike. Colour shifts from damp dark-brown to pale when dry."),
        "lookalikes": [
            {"name": "Galerina marginata (deadly galerina)", "distinguish": "Near-identical and amatoxin-deadly; the two are separated only by microscopy. Do not eat either without expert ID."},
            {"name": "Armillaria mellea (honey fungus)", "distinguish": "Honey fungus has a whitish spore print and lacks the strong ring of Kuehneromyces."}
        ],
        "fun_fact": "So similar to deadly Galerina that many guides simply say: if it grows on wood with a ring and rusty spores, leave it."
    },
    {
        "id": "entoloma-rhodopolium",
        "name": "Pinkgill",
        "scientific_name": "Entoloma rhodopolium",
        "aliases": ["wood pinkgill"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "flat"], "colors": ["grey", "brown", "tan"], "diameter_cm": [3, 9]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["pink", "salmon"]},
        "stem": {"colors": ["white", "grey"]},
        "spore_print": "pink",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("A grey-brown mushroom with pink gills and a pink spore print -- the hallmark of the Entoloma genus, many of which are poisonous. Causes severe gastrointestinal illness."),
        "lookalikes": [
            {"name": "Tricholoma species", "distinguish": "Some Tricholomas are edible but have white spores, not pink."},
            {"name": "Agaricus species", "distinguish": "Field mushrooms have brown spores and free gills, never pink."}
        ],
        "fun_fact": "The pink spore print is the single fastest way to rule a mushroom out of the 'safe edibles' group."
    },
    {
        "id": "hebeloma-crustuliniforme",
        "name": "Poison Pie",
        "scientific_name": "Hebeloma crustuliniforme",
        "aliases": ["snapping-turtle mushroom"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex"], "colors": ["cream", "tan", "brown"], "diameter_cm": [3, 9]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["cream", "tan"]},
        "stem": {"colors": ["white", "cream"]},
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["late summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Common mycorrhizal mushroom with a sticky pale cap and a mealy, radish-like smell. Poisonous, causing vomiting and diarrhea; a frequent accidental pickup by new foragers."),
        "lookalikes": [
            {"name": "Agaricus species (field/button mushrooms)", "distinguish": "Edible Agaricus have pink-then-brown gills and a brown spore print; Hebeloma gills stay pale and it smells of radish."},
            {"name": "Edible white fungi", "distinguish": "Many white gilled mushrooms are dangerous; the mealy odour is a Hebeloma clue."}
        ],
        "fun_fact": "Its Latin name means 'crust-like', a nod to the smooth, bun-like cap."
    },
    {
        "id": "tricholoma-equestre",
        "name": "Man-on-Horseback",
        "scientific_name": "Tricholoma equestre",
        "aliases": ["yellow tricholoma"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "flat"], "colors": ["yellow", "olive", "brown"], "diameter_cm": [4, 10]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["yellow", "cream"]},
        "stem": {"colors": ["white", "yellowish"]},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Once considered a good edible, now linked to rhabdomyolysis (muscle breakdown) and at least one death when eaten repeatedly. Yellowish cap and yellow gills, growing under conifers."),
        "lookalikes": [
            {"name": "Cantharellus (chanterelle)", "distinguish": "Chanterelles are yellow but have blunt false gills and grow in moss/leaf litter, not with the white spores of Tricholoma."},
            {"name": "Tricholoma matsutake", "distinguish": "Matsutake is prizzed and edible but smells of cinnamon/spice; equestre smells faintly of flour."}
        ],
        "fun_fact": "A reminder that 'edible' can be conditional -- this one fails only after repeated meals."
    },
    {
        "id": "marasmius-oreades",
        "name": "Fairy Ring Mushroom",
        "scientific_name": "Marasmius oreades",
        "aliases": ["scotch bonnet"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat", "umbilicate"], "colors": ["tan", "brown", "cream"], "diameter_cm": [2, 5]},
        "gills": {"attachment": "attached", "spacing": "distant", "colors": ["cream", "tan"]},
        "stem": {"colors": ["tan", "brown"]},
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["spring", "summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Small, tough, fragrant mushroom that grows in rings on lawns and pastures -- the classic 'fairy ring'. A good edible with a nutty flavour, best dried. Must be well cooked."),
        "lookalikes": [
            {"name": "Clitocybe dealbata (ivory funnel)", "distinguish": "Deadly ivory funnel also forms rings in grass but has a mealy smell and is muscarine-poisonous."},
            {"name": "Agaricus campestris (field mushroom)", "distinguish": "Edible and also lawn-growing, but has pink-then-brown gills and a ring; no fairy-ring confusion risk since it is safe too."}
        ],
        "fun_fact": "The rings it forms can grow outward for decades -- some are centuries old."
    },
    {
        "id": "agaricus-arvensis",
        "name": "Horse Mushroom",
        "scientific_name": "Agaricus arvensis",
        "aliases": ["princess mushroom"],
        "edibility": "choice",
        "cap": {"shape": ["convex", "flat"], "colors": ["white", "cream", "tan"], "diameter_cm": [8, 20]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["pink", "brown"]},
        "stem": {"colors": ["white"], "ring": True, "volva": False},
        "spore_print": "brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("A large, choice meadow Agaricus with a pleasant anise scent, closely related to the button mushroom. Flesh may yellow slightly when bruised. One of the best wild edibles."),
        "lookalikes": [
            {"name": "Agaricus xanthodermus (yellow stainer)", "distinguish": "Poisonous stainer also yellows but smells of phenol/ink; arvensis smells sweetly of anise."},
            {"name": "Amanita species", "distinguish": "Death caps can sit in grass too; Agaricus have brown spores and pink-then-brown gills, never a volva."}
        ],
        "fun_fact": "Its anise odour is the quick field test that separates it from the poisonous yellow stainer."
    },
    {
        "id": "pleurotus-eryngii",
        "name": "King Oyster",
        "scientific_name": "Pleurotus eryngii",
        "aliases": ["king trumpet", "eryngii"],
        "edibility": "choice",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "tan", "grey"], "diameter_cm": [4, 12]},
        "gills": {"attachment": "decurrent", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white", "tan"]},
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["autumn", "winter"],
        "distribution": "Mediterranean, Europe, Asia",
        "description": ("Meaty, thick-stemmed oyster relative that grows on the roots of spiny shrubs (eryngo). Prized for its firm texture and umami flavour; widely cultivated."),
        "lookalikes": [
            {"name": "Pleurotus ostreatus (oyster mushroom)", "distinguish": "True oyster has a fan cap and the same edible status; eryngii is chunkier with a solid stem."},
            {"name": "Omphalotus (jack-o'-lantern)", "distinguish": "Jack-o'-lantern is poisonous and glows faintly in the dark; oysters do not."}
        ],
        "fun_fact": "The thick stem is the edible part most people throw away -- it is the best bit."
    },
    {
        "id": "craterellus-cornucopioides",
        "name": "Black Trumpet",
        "scientific_name": "Craterellus cornucopioides",
        "aliases": ["horn of plenty", "trumpet of death"],
        "edibility": "choice",
        "cap": {"shape": ["funnel", "irregular"], "colors": ["black", "dark grey", "brown"], "diameter_cm": [2, 7]},
        "gills": {"attachment": "decurrent", "spacing": "distant", "colors": ["grey", "black"]},
        "stem": {"colors": ["black", "grey"]},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Fragrant, all-black funnel mushroom that hides in leaf litter and is easy to miss. Intensely flavoured, highly prizzed edible. No dangerous lookalikes share its combo of black colour and hollow funnel shape."),
        "lookalikes": [
            {"name": "Cantharellus (chanterelle)", "distinguish": "Chanterelles are yellow/orange; black trumpets are dark and have a smokier taste."},
            {"name": "Craterellus fallax (false black trumpet)", "distinguish": "Near-identical and also edible; the two are treated as interchangeable in the kitchen."}
        ],
        "fun_fact": "It is one of the few choice fungi with essentially no poisonous confusion -- a safe one to learn first."
    },
    {
        "id": "boletus-bicolor",
        "name": "Two-colored Bolete",
        "scientific_name": "Boletus bicolor",
        "aliases": ["red-cracked bolete"],
        "edibility": "edible",
        "cap": {"shape": ["convex"], "colors": ["red", "brown", "pink"], "diameter_cm": [5, 15]},
        "gills": {"attachment": "pores", "spacing": "crowded", "colors": ["yellow", "red"]},
        "stem": {"colors": ["yellow", "red"]},
        "spore_print": "olive",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "E. North America",
        "description": ("Red-capped bolete with yellow pores that bruise blue. Edible and good when young, but the blue bruising must be told apart from the poisonous red-capped boletes."),
        "lookalikes": [
            {"name": "Boletus sensibilis", "distinguish": "Very similar and also blue-bruising but can cause illness; the two are hard to separate -- caution advised."},
            {"name": "Boletus satanas (devil's bolete)", "distinguish": "Devil's bolete is poisonous with a bulbous base and red pores on a fat stem; avoid all red-pored boletes when unsure."}
        ],
        "fun_fact": "The rule for boletes: red pores + blue bruising = be very careful; many are edible, some are not."
    },
    {
        "id": "suillus-americanus",
        "name": "American Slippery Jack",
        "scientific_name": "Suillus americanus",
        "aliases": ["chicken fat mushroom"],
        "edibility": "edible",
        "cap": {"shape": ["convex"], "colors": ["yellow", "brown", "tan"], "diameter_cm": [4, 10]},
        "gills": {"attachment": "pores", "spacing": "crowded", "colors": ["yellow"]},
        "stem": {"colors": ["yellow"], "ring": True},
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "N. America (pine)",
        "description": ("Slimy-capped, dotted-stemmed bolete under pines. Edible after the slimy cuticle and pore layer are removed; mild flavour. A safe, common beginner bolete."),
        "lookalikes": [
            {"name": "Suillus luteus (slippery jack)", "distinguish": "Nearly identical and also edible; americanus has dotted (not ring-only) stems and grows with eastern pines."},
            {"name": "Suillus spraguei (painted suillus)", "distinguish": "Red-scaled cap, also eastern pine + edible; the dotted stem on americanus separates them."}
        ],
        "fun_fact": "The slimy cap is the 'slippery' part -- peel it and the mushroom underneath is the meal."
    },
    {
        "id": "russula-brevipes",
        "name": "Short-stemmed Russula",
        "scientific_name": "Russula brevipes",
        "aliases": ["bread mushroom"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["white", "cream", "tan"], "diameter_cm": [5, 20]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white"]},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "N. America",
        "description": ("Large, squat white Russula with a peppery taste raw (mild when cooked). Edible and common; the peppery bite is typical of many Russulas, most of which are at worst unpalatable, not deadly."),
        "lookalikes": [
            {"name": "Russula emetica (the sickener)", "distinguish": "The sickener is also white but intensely peppery and poisonous; brevipes is mild-to-moderate and edible cooked."},
            {"name": "Edible white fungi", "distinguish": "Its brittle flesh (snaps like chalk) is the Russula family trait -- useful but not enough alone to declare safe."}
        ],
        "fun_fact": "Underneath, this mushroom is sometimes parasitised into a 'lobster mushroom' by another fungus."
    },
    {
        "id": "armillaria-tabescens",
        "name": "Ringless Honey Fungus",
        "scientific_name": "Armillaria tabescens",
        "aliases": ["ringless honey mushroom"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "tan", "honey"], "diameter_cm": [3, 10]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["brown", "tan"], "ring": False},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": ["autumn"],
        "distribution": "N. America, Europe, Asia",
        "description": ("Honey-coloured clustered mushroom like Honey Fungus but lacking the ring. Edible when cooked (the cause of many poisoning cases is eating it undercooked). Grows at the base of trees in big clumps."),
        "lookalikes": [
            {"name": "Armillaria mellea (honey fungus)", "distinguish": "The ringed cousin; both edible cooked, both confused with deadly Galerina on wood."},
            {"name": "Galerina marginata (deadly galerina)", "distinguish": "Rusty-spored and amatoxin-deadly; honey mushrooms have a white spore print -- check spores before eating."}
        ],
        "fun_fact": "Armillaria is the largest living organism on Earth -- a single clone in Oregon covers ~10 km2."
    },
    {
        "id": "psilocybe-semilanceata",
        "name": "Liberty Cap",
        "scientific_name": "Psilocybe semilanceata",
        "aliases": ["magic mushroom", "liberty cap"],
        "edibility": "poisonous",
        "cap": {"shape": ["conical", "bell"], "colors": ["brown", "tan", "cream"], "diameter_cm": [1, 2]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["purple-brown", "brown"]},
        "stem": {"colors": ["white", "cream"]},
        "spore_print": "purple-brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Small conical grassland mushroom containing psilocybin (a psychedelic). Legally restricted in many places and not food -- included here for education, not use. Bruises blue and has a distinct nipple on the cap."),
        "lookalikes": [
            {"name": "Panaeolus species", "distinguish": "Some Panaeolus are also psychoactive; many grassland little brown mushrooms are not -- microscopy is needed."},
            {"name": "Galerina marginata (deadly galerina)", "distinguish": "Rusty-spored and amatoxin-deadly; the danger of confusing the two is why ID here is expert-only."}
        ],
        "fun_fact": "One of the most widespread naturally occurring psychedelic mushrooms on the planet."
    },
    {
        "id": "ganoderma-lucidum",
        "name": "Reishi",
        "scientific_name": "Ganoderma lucidum",
        "aliases": ["lingzhi", "varnished conk"],
        "edibility": "inedible",
        "cap": {"shape": ["kidney", "shelf"], "colors": ["red", "orange", "brown"], "diameter_cm": [5, 25]},
        "gills": {"attachment": "pores", "spacing": "crowded", "colors": ["white", "tan"]},
        "stem": {"colors": ["red", "brown"]},
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": ["summer", "autumn"],
        "distribution": "Worldwide (temperate/tropical)",
        "description": ("Glossy red-brown shelf fungus used in traditional medicine (usually as a tea/extract, not eaten). Too woody to eat but prizzed. Kidney-shaped cap with a lacquered sheen."),
        "lookalikes": [
            {"name": "Ganoderma tsugae", "distinguish": "Near-identical hemlock reishi, also medicinal; the two are used interchangeably."},
            {"name": "Trametes versicolor (turkey tail)", "distinguish": "Turkey tail is thinner, multicoloured, and inedible too; reishi is thicker with a shiny red coat."}
        ],
        "fun_fact": "Its Chinese name lingzhi means 'mushroom of immortality' -- valued for millennia as medicine."
    },
    {
        "id": "fistulina-hepatica",
        "name": "Beefsteak Fungus",
        "scientific_name": "Fistulina hepatica",
        "aliases": ["beefsteak mushroom", "ox tongue"],
        "edibility": "edible",
        "cap": {"shape": ["shelf", "tongue"], "colors": ["red", "brown", "pink"], "diameter_cm": [5, 25]},
        "gills": {"attachment": "pores", "spacing": "crowded", "colors": ["pink", "red"]},
        "stem": {"colors": ["red", "pink"]},
        "spore_print": "pink",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": ["late summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Red, tongue-shaped bracket that bleeds a blood-red juice when cut and tastes faintly of beef. Edible and tangy; often grows on old oaks. Individual tubes (not a fused pore surface) are the giveaway."),
        "lookalikes": [
            {"name": "Ganoderma lucidum (reishi)", "distinguish": "Lacquered red-brown shelf, inedible/medicinal and never bleeds red juice when cut."},
            {"name": "Laetiporus sulphureus (chicken of the woods)", "distinguish": "Chicken of the woods is yellow and also edible; beefsteak is red and tongue-shaped."}
        ],
        "fun_fact": "Cut it and the juice really does look like blood -- hence 'beefsteak'."
    },
    {
        "id": "calocybe-gambosa",
        "name": "St George's Mushroom",
        "scientific_name": "Calocybe gambosa",
        "aliases": ["st george mushroom"],
        "edibility": "choice",
        "cap": {"shape": ["convex", "flat"], "colors": ["white", "cream", "tan"], "diameter_cm": [4, 12]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white"]},
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["spring"],
        "distribution": "Europe, N. America",
        "description": ("Meaty, fragrant spring mushroom that appears around St George's Day (23 Apr). Choice edible with a strong floury smell. Grows in rings in grassy places."),
        "lookalikes": [
            {"name": "Clitocybe dealbata (ivory funnel)", "distinguish": "Deadly ivory funnel also rings in grass; St George's has a strong mealy/flour smell and white (not dangerously muscarine) profile -- but expert ID is essential."},
            {"name": "Marasmius oreades (fairy ring)", "distinguish": "Fairy ring is smaller, tougher, and less mealy; both can form rings."}
        ],
        "fun_fact": "Timed to St George's Day so reliably that foragers use the calendar as an ID clue."
    },
    {
        "id": "lactarius-piperatus",
        "name": "Peppery Milkcap",
        "scientific_name": "Lactarius piperatus",
        "aliases": ["pepper milkcap"],
        "edibility": "inedible",
        "cap": {"shape": ["convex", "flat", "umbilicate"], "colors": ["white", "cream"], "diameter_cm": [5, 15]},
        "gills": {"attachment": "decurrent", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["white"]},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Pure white milkcap that exudes white latex and is ferociously peppery raw. Too acrid to eat for most, though some cultures salt-cure it. A classic 'beware' mushroom of the milkcap group."),
        "lookalikes": [
            {"name": "Lactarius deliciosus (saffron milkcap)", "distinguish": "Saffron milkcap is edible with orange milk and carrot-coloured stains; piperatus is white and searingly hot."},
            {"name": "Lactarius torminosus (woolly milkcap)", "distinguish": "Woolly milkcap is also inedible with a fuzzy cap edge; both are white and peppery."}
        ],
        "fun_fact": "The peppery burn is a defence chemical -- insects and mammals learn to leave milkcaps alone."
    },
    {
        "id": "chlorophyllum-brunneum",
        "name": "Shaggy Parasol",
        "scientific_name": "Chlorophyllum brunneum",
        "aliases": ["brown shaggy parasol"],
        "edibility": "poisonous",
        "cap": {"shape": ["convex", "umbonate"], "colors": ["brown", "tan"], "diameter_cm": [8, 25]},
        "gills": {"attachment": "free", "spacing": "crowded", "colors": ["white", "cream"]},
        "stem": {"colors": ["brown", "white"], "ring": True, "volva": False},
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["summer", "autumn"],
        "distribution": "N. America",
        "description": ("Large parasol with a brown scaly cap, a movable ring, and a fat, often bulbous stem that bruises orange-yellow. Poisonous, causing severe GI upset -- easily confused with the edible true parasol."),
        "lookalikes": [
            {"name": "Macrolepiota procera (parasol)", "distinguish": "True parasol is edible with a slender, snake-skin stem; brunneum has a swollen stem that stains yellow."},
            {"name": "Chlorophyllum molybdites (green-spored parasol)", "distinguish": "Another poisonous parasol whose spores are green -- the key danger sign."}
        ],
        "fun_fact": "The bulbous, yellow-bruising stem is the trap: it looks like an edible parasol but is not."
    },
    {
        "id": "morchella-angusticeps",
        "name": "Black Morel",
        "scientific_name": "Morchella angusticeps",
        "aliases": ["eastern black morel"],
        "edibility": "choice",
        "cap": {"shape": ["conical", "pitted"], "colors": ["black", "dark brown", "grey"], "diameter_cm": [3, 10]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["cream", "white"]},
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": ["spring"],
        "distribution": "E. North America",
        "description": ("Prized black-capped morel of eastern North American springs. Top-tier edible with a deep, smoky flavour -- but MUST be cooked; raw morels are toxic. Honeycomb pits on a dark conical cap."),
        "lookalikes": [
            {"name": "Gyromitra esculenta (false morel)", "distinguish": "False morel has a lobed, brain-like cap, not honeycomb pits, and is deadly."},
            {"name": "Verpa bohemica (early morel)", "distinguish": "Verpa's cap hangs free like a thimble; true morels have a continuous pitted cap."}
        ],
        "fun_fact": "Morel hunters guard their spring spots like state secrets -- the best ones are never shared."
    },
    {
        "id": "tuber-aestivum",
        "name": "Summer Truffle",
        "scientific_name": "Tuber aestivum",
        "aliases": ["burgundy truffle"],
        "edibility": "choice",
        "cap": {"shape": ["round", "lumpy"], "colors": ["black", "brown"], "diameter_cm": [2, 7]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["black", "brown"]},
        "spore_print": "n/a",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": ["summer", "autumn"],
        "distribution": "Europe, N. Africa, Middle East",
        "description": ("Subterranean, aromatic truffle with a black warty skin and a pale marbled interior. Highly prizzed edible, hunted with trained dogs or pigs. Found by smell, not sight, under hardwoods."),
        "lookalikes": [
            {"name": "Tuber melanosporum (black truffle)", "distinguish": "The prizzed Perigord truffle, near-identical and also choice; aestivum is milder and ripens in summer."},
            {"name": "Deer truffle (Elaphomyces)", "distinguish": "A common false truffle that is inedible and lacks the aromatic interior."}
        ],
        "fun_fact": "Truffles have no cap, gills, or stem -- they are the underground fruit of a fungus, more like a potato than a mushroom."
    },
    {
        "id": "hericium-coralloides",
        "name": "Coral Tooth Fungus",
        "scientific_name": "Hericium coralloides",
        "aliases": ["comb tooth", "coral hericium"],
        "edibility": "choice",
        "cap": {"shape": ["coral", "toothed"], "colors": ["white", "cream"], "diameter_cm": [5, 30]},
        "gills": {"attachment": "n/a", "spacing": "n/a", "colors": []},
        "stem": {"colors": ["white"]},
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["late summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Cascading white mass of fine hanging teeth, like a frozen waterfall. Choice edible with a seafood-like flavour, closely related to Lion's Mane. Grows on dead hardwoods."),
        "lookalikes": [
            {"name": "Hericium erinaceus (lion's mane)", "distinguish": "Lion's mane has longer, shaggier single clusters; both are choice and nearly interchangeable in the kitchen."},
            {"name": "Artomyces pyxidatus (crown-tipped coral)", "distinguish": "Branched coral with little crown-tipped ends; edible but less choice than Hericium. Confusion is harmless."}
        ],
        "fun_fact": "All three Hericium species are edible -- a rare group where every member is a good meal."
    },
    {
        "id": "agrocybe-aegerita",
        "name": "Poplar Mushroom",
        "scientific_name": "Agrocybe aegerita",
        "aliases": ["agrocybe cylindracea", "black poplar mushroom"],
        "edibility": "edible",
        "cap": {"shape": ["convex", "flat"], "colors": ["brown", "tan"], "diameter_cm": [4, 12]},
        "gills": {"attachment": "attached", "spacing": "crowded", "colors": ["clay", "brown"]},
        "stem": {"colors": ["white", "tan"], "ring": True},
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": ["spring", "summer", "autumn"],
        "distribution": "Northern Hemisphere",
        "description": ("Brown capped mushroom in clusters on poplar and other hardwoods. Edible with a mild, pleasant flavour; widely cultivated in Asia (where it is called yanagi-matsutake)."),
        "lookalikes": [
            {"name": "Kuehneromyces mutabilis", "distinguish": "Also wood-clustered and ringed but rusty-spored and best avoided; Agrocybe has a brown spore print."},
            {"name": "Galerina marginata (deadly galerina)", "distinguish": "Amatoxin-deadly and wood-loving; check the spore print (brown, not rusty) before any ID."}
        ],
        "fun_fact": "It is one of the few wild mushrooms successfully farmed at scale outside the usual button/oyster/shiitake trio."
    },
]
