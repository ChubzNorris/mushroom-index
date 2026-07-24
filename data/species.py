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
            {"name": "Gyromitra / other brain fungi", "distinguish": "Those are rounded, on the ground, and some are deadly."}
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
            {"name": "Phellinus species", "distinguish": "Similar brackets; context color differs."}
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
            {"name": "Other Suillus", "distinguish": "Most are edible; the slimy cap + ring is characteristic."}
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
            {"name": "Amanita species", "distinguish": "Matsutake has white spores and no volva; some toxic Amanitas smell similar."}
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
            {"name": "Other jelly fungi", "distinguish": "Most are harmless; wood ear is thin and ear-shaped."}
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
            {"name": "Other white jelly fungi", "distinguish": "Generally all harmless."}
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
            {"name": "Other Leccinum", "distinguish": "Most are edible; scabrous stem dots are distinctive."}
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
            {"name": "Other cup fungi (Peziza)", "distinguish": "Most lack the violet pigment and the crown-like splitting; still not recommended eating."}
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
]
