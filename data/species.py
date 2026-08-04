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
        "aliases": [
            "fly amanita",
            "toadstool",
            "red cap"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "red",
                "orange"
            ],
            "diameter_cm": [
                8,
                20
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": True
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn",
            "winter"
        ],
        "distribution": "Northern Hemisphere, widespread",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Iconic red cap flecked with white warts (universal veil remnants). Contains ibotenic acid and muscimol; psychoactive and toxic, historically used ritually. Not deadly in typical doses but causes severe poisoning.",
        "lookalikes": [
            {
                "name": "Amanita caesarea (Caesar's mushroom)",
                "distinguish": "Edible Amanita with an orange cap and orange stem; lacks the white-flecked red look."
            },
            {
                "name": "Amanita flavoconia",
                "distinguish": "Smaller yellow-orange cousin with yellow warts."
            }
        ],
        "fun_fact": "The model for most 'mushroom' illustrations and Super Mario's power-ups."
    },
    {
        "id": "amanita-phalloides",
        "name": "Death Cap",
        "scientific_name": "Amanita phalloides",
        "aliases": [
            "death cup"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "green",
                "olive",
                "tan",
                "brown"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "pale"
            ],
            "ring": True,
            "volva": True
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere; introduced with oak/chestnut worldwide",
        "regions": [
            "asia",
            "europe",
            "global",
            "north-america"
        ],
        "description": "Responsible for the majority of fatal mushroom poisonings worldwide. Contains amatoxins that cause irreversible liver and kidney failure, often with a deceptive symptom-free delay. Caps are greenish to tan and easily mistaken for edible mushrooms.",
        "lookalikes": [
            {
                "name": "Agaricus species (field/button mushrooms)",
                "distinguish": "Have pink-then-brown gills and a brown spore print; NEVER a white volva cup."
            },
            {
                "name": "Amanita caesarea / edible Amanitas",
                "distinguish": "Some edible Amanitas look similar -- white gills + volva is the danger signal for this group."
            },
            {
                "name": "Macrolepiota procera (parasol)",
                "distinguish": "Has a shaggy brown-scaled cap and a movable ring; no volva."
            }
        ],
        "fun_fact": "A single cap can contain enough amatoxin to kill an adult."
    },
    {
        "id": "amanita-bisporigera",
        "name": "Destroying Angel",
        "scientific_name": "Amanita bisporigera",
        "aliases": [
            "death angel"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "bell"
            ],
            "colors": [
                "white"
            ],
            "diameter_cm": [
                5,
                12
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": True
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Eastern North America",
        "regions": [
            "north-america"
        ],
        "description": "A pure white, beautiful mushroom that is among the deadliest on Earth. Same amatoxin family as the death cap. The white volva at the stem base and white gills are key identifiers -- but so do several edible whites, which is precisely why it kills.",
        "lookalikes": [
            {
                "name": "Agaricus campestris (field mushroom)",
                "distinguish": "Pink-then-brown gills, no volva, brown spores."
            },
            {
                "name": "Young Armillaria / Clitocybe",
                "distinguish": "Lack a volva cup and have attached (not free) gills."
            }
        ],
        "fun_fact": "Its name refers to its angelic appearance, not its intent."
    },
    {
        "id": "amanita-caesarea",
        "name": "Caesar's Mushroom",
        "scientific_name": "Amanita caesarea",
        "aliases": [
            "Caesar's agaric",
            "orange amanita"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "orange",
                "red"
            ],
            "diameter_cm": [
                5,
                18
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "yellow",
                "gold"
            ]
        },
        "stem": {
            "colors": [
                "yellow",
                "orange"
            ],
            "ring": True,
            "volva": True
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Southern Europe, North Africa, parts of North America",
        "regions": [
            "africa",
            "europe",
            "north-america"
        ],
        "description": "A prized Mediterranean delicacy with a vivid orange cap and golden stem, eaten since Roman times (reserved for emperors). Safe only because its features are distinctive -- a good lesson in learning ONE mushroom well.",
        "lookalikes": [
            {
                "name": "Amanita muscaria (fly agaric)",
                "distinguish": "Fly agaric has white warts on red and white gills/stem, not golden."
            },
            {
                "name": "Amanita phalloides",
                "distinguish": "Death cap is greenish-tan with white gills -- never golden."
            }
        ],
        "fun_fact": "Roman emperors reserved this mushroom for themselves — hence 'Caesar's mushroom.' Deadly Amanita muscaria grows right beside it, so the ego boost isn't worth a mispick."
    },
    {
        "id": "agaricus-bisporus",
        "name": "Button / Portobello",
        "scientific_name": "Agaricus bisporus",
        "aliases": [
            "cultivated mushroom",
            "champignon"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "brown",
                "tan"
            ],
            "diameter_cm": [
                3,
                15
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "pink",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "cultivated",
        "substrate": "compost",
        "ecology": "saprotrophic",
        "season": [
            "year-round"
        ],
        "distribution": "Grown globally in cultivation",
        "regions": [
            "global"
        ],
        "description": "The supermarket mushroom in its white (button) and brown (cremini/portobello) forms. Young gills are pink, maturing to chocolate brown -- a reliable field mark for the whole Agaricus genus.",
        "lookalikes": [
            {
                "name": "Agaricus xanthodermus (yellow stainer)",
                "distinguish": "Bruises bright yellow and smells of phenol/ink; avoid."
            },
            {
                "name": "Amanita species",
                "distinguish": "Amanitas have white gills and a volva; Agaricus never does."
            }
        ],
        "fun_fact": "The most-eaten mushroom on Earth: the same species is sold as white button, cremini, and portobello at three different ages. Same fungus, three price points."
    },
    {
        "id": "agaricus-campestris",
        "name": "Field Mushroom",
        "scientific_name": "Agaricus campestris",
        "aliases": [
            "meadow mushroom"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "cream",
                "tan"
            ],
            "diameter_cm": [
                4,
                10
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "pink",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide in pastures and lawns",
        "regions": [
            "global"
        ],
        "description": "The classic wild relative of the button mushroom, found in rings in pastures. Pink-to-brown gills and a brown spore print. A good beginner edible -- but only after ruling out the yellow stainer and any white-gilled lookalikes.",
        "lookalikes": [
            {
                "name": "Agaricus xanthodermus",
                "distinguish": "Yellow staining + chemical smell."
            },
            {
                "name": "Amanita species",
                "distinguish": "White gills + volva = danger."
            }
        ],
        "fun_fact": "The wild original that supermarket buttons were bred from. A fresh cap smells of anise or almonds — a handy tell that separates it from the toxic yellow-stainer."
    },
    {
        "id": "agaricus-xanthodermus",
        "name": "Yellow Stainer",
        "scientific_name": "Agaricus xanthodermus",
        "aliases": [
            "yellowing mushroom"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "cream"
            ],
            "diameter_cm": [
                5,
                12
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "pink",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Widespread in lawns and gardens",
        "regions": [
            "global"
        ],
        "description": "Looks like an edible field mushroom but bruises bright yellow and emits a sharp phenol/ink smell. Causes gastrointestinal upset. The yellow staining at the base is the giveaway -- always check before eating any Agaricus.",
        "lookalikes": [
            {
                "name": "Agaricus campestris / bisporus",
                "distinguish": "These do NOT stain yellow and lack the chemical odor."
            }
        ],
        "fun_fact": "Bruise it and it turns bright yellow and reeks of phenol (ink/iodine). That chemical smell is the mushroom basically warning you not to eat it."
    },
    {
        "id": "boletus-edulis",
        "name": "King Bolete",
        "scientific_name": "Boletus edulis",
        "aliases": [
            "porcini",
            "cep",
            "penny bun"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan",
                "chestnut"
            ],
            "diameter_cm": [
                7,
                25
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "n/a",
            "colors": [
                "white",
                "olive",
                "yellow"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "tan"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere; widespread",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "The king of edibles: a bun-shaped brown cap over a spongy pore layer (no gills) and a fat, finely netted stem. Boletes are some of the safest edible groups because the deadly Amanita types have gills, not pores.",
        "lookalikes": [
            {
                "name": "Boletus satanas (devil's bolete)",
                "distinguish": "Has a red-tinged stem and stains blue; poisonous."
            },
            {
                "name": "Tylopilus felleus (bitter bolete)",
                "distinguish": "Intensely bitter; pinkish pore mouths."
            }
        ],
        "fun_fact": "Dried porcini are more aromatic than fresh -- umami bombs."
    },
    {
        "id": "boletus-satanas",
        "name": "Devil's Bolete",
        "scientific_name": "Boletus satanas",
        "aliases": [
            "Satan's mushroom"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex"
            ],
            "colors": [
                "white",
                "gray",
                "olive"
            ],
            "diameter_cm": [
                8,
                25
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "n/a",
            "colors": [
                "red",
                "orange"
            ]
        },
        "stem": {
            "colors": [
                "red",
                "yellow"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, rarer in North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A pale capped bolete with a bulbous red/yellow stem and red pores. Causes severe GI poisoning. The red pores and bulbous red stem separate it from the choice king bolete.",
        "lookalikes": [
            {
                "name": "Boletus edulis",
                "distinguish": "King bolete has whitish pores and a pale, netted stem -- no red."
            }
        ],
        "fun_fact": "Named for the devil for a reason — a bloated red-stemmed bolete that causes violent gut turmoil. Looks meaty and tempting; tastes like regret."
    },
    {
        "id": "cantharellus-cibarius",
        "name": "Golden Chanterelle",
        "scientific_name": "Cantharellus cibarius",
        "aliases": [
            "chanterelle",
            "egg mushroom"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "funnel",
                "depressed"
            ],
            "colors": [
                "yellow",
                "orange"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "False-gills",
            "colors": [
                "yellow",
                "orange"
            ]
        },
        "stem": {
            "colors": [
                "yellow",
                "orange"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "yellow",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Egg-yellow, fruity-smelling, with blunt False-gills (ridges, not sharp blades) running down the stem. A top edible. Its apricot aroma is a good ID clue.",
        "lookalikes": [
            {
                "name": "Omphalotus olearius (jack-o'-lantern)",
                "distinguish": "Has TRUE sharp gills and glows in the dark; poisonous."
            },
            {
                "name": "Hygrophoropsis aurantiaca (False chanterelle)",
                "distinguish": "Has True forked gills; less choice."
            }
        ],
        "fun_fact": "Its 'gills' are actually blunt folds that run down the stem — that's the key mark separating real chanterelles from the poisonous jack-o'-lantern impostor."
    },
    {
        "id": "omphalotus-olearius",
        "name": "Jack-o'-Lantern",
        "scientific_name": "Omphalotus olearius",
        "aliases": [
            "jack o lantern mushroom"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "funnel",
                "convex"
            ],
            "colors": [
                "orange"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "orange"
            ]
        },
        "stem": {
            "colors": [
                "orange"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn"
        ],
        "distribution": "Eastern North America, Europe",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "Brilliant orange with True, sharp, decurrent gills. Causes severe vomiting/diarrhea. Famous for bioluminescence -- its gills glow faintly green at night. Grows in clusters on wood, unlike chanterelles.",
        "lookalikes": [
            {
                "name": "Cantharellus (chanterelle)",
                "distinguish": "Chanterelles have blunt False-gills, grow on ground, don't glow, don't cluster on wood."
            }
        ],
        "fun_fact": "In the dark, a cluster can be bright enough to read by."
    },
    {
        "id": "morchella-esculenta",
        "name": "Common Morel",
        "scientific_name": "Morchella esculenta",
        "aliases": [
            "morel",
            "sponge mushroom"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                " conical",
                "pitted"
            ],
            "colors": [
                "tan",
                "brown",
                "gray"
            ],
            "diameter_cm": [
                3,
                8
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "spring"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Honeycomb-capped, hollow spring delicacy. MUST be cooked -- raw morels are toxic. Prized by chefs. Found in disturbed ground, old orchards, and burns.",
        "lookalikes": [
            {
                "name": "Gyromitra esculenta (False morel)",
                "distinguish": "Lobed/brain-like, NOT honeycombed; solid/ stuffed cap; deadly when raw."
            },
            {
                "name": "Verpa species",
                "distinguish": "Thimble-on-a-stick; cap not fully attached at sides."
            }
        ],
        "fun_fact": "One of the few wild mushrooms worth real money: morels can't be reliably cultivated, so foragers still cash in on the spring bounty."
    },
    {
        "id": "gyromitra-esculenta",
        "name": "False Morel",
        "scientific_name": "Gyromitra esculenta",
        "aliases": [
            "brain mushroom",
            "turban fungus"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "lobed",
                "brain-like"
            ],
            "colors": [
                "brown",
                "red-brown"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "spring"
        ],
        "distribution": "Northern Hemisphere, conifer regions",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Resembles a morel but the cap is a lobed, brain-like mass that is NOT a regular honeycomb and is attached only at the top. Contains gyromitrin, a carcinogenic toxin converted to monomethylhydrazine. Deadly if eaten raw/improperly prepared; some regions ban its sale.",
        "lookalikes": [
            {
                "name": "Morchella (True morel)",
                "distinguish": "True morels have a pitted honeycomb cap attached to the stem along its full length; False morels are irregularly lobed and hang free."
            }
        ],
        "fun_fact": "Contains gyromitrin, which your body turns into a rocket-fuel precursor (monomethylhydrazine). Some parboil it 'safe,' but the margin is thin and the risk is real."
    },
    {
        "id": "lactarius-deliciosus",
        "name": "Saffron Milkcap",
        "scientific_name": "Lactarius deliciosus",
        "aliases": [
            "delicious milkcap",
            "red pine mushroom"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "funnel",
                "depressed"
            ],
            "colors": [
                "orange",
                "red-orange"
            ],
            "diameter_cm": [
                4,
                12
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "orange"
            ]
        },
        "stem": {
            "colors": [
                "orange"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere pine forests",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "When cut or bruised it weeps carrot-orange latex (milk). Cap has concentric zones. Mild and good when cooked, with a piney note. A mycorrhizal partner of pines.",
        "lookalikes": [
            {
                "name": "Lactarius deterrimus",
                "distinguish": "Very similar; stains greenish; also edible."
            },
            {
                "name": "Lactarius torminosus (woolly milkcap)",
                "distinguish": "Shaggy/inrolled cap edge, acrid; poisonous."
            }
        ],
        "fun_fact": "Bleeds carrot-orange latex that stains your fingers — and the mushroom — blue-green with age. The color shift is part of the ID, not a defect."
    },
    {
        "id": "pleurotus-ostreatus",
        "name": "Oyster Mushroom",
        "scientific_name": "Pleurotus ostreatus",
        "aliases": [
            "oyster fungus",
            "tree oyster"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "shell",
                "fan"
            ],
            "colors": [
                "gray",
                "white",
                "tan",
                "blue"
            ],
            "diameter_cm": [
                5,
                20
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "lilac-gray",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn",
            "winter",
            "spring"
        ],
        "distribution": "Worldwide",
        "regions": [
            "global"
        ],
        "description": "Shelf-like, fan-shaped caps in overlapping clusters on dead hardwood. Oyster-shaped, with decurrent gills and a lilac-gray spore print. Easy to cultivate and a reliable edible.",
        "lookalikes": [
            {
                "name": "Pleurocybella porrigens (angel wings)",
                "distinguish": "Thinner, pure white; avoid for those with kidney issues."
            },
            {
                "name": "Omphalotus (jack-o'-lantern)",
                "distinguish": "Grows on wood too but is orange and poisonous."
            }
        ],
        "fun_fact": "Grows in shelf-like clusters and literally digests nematodes for nitrogen when food is scarce. A carnivorous mushroom that's also dinner."
    },
    {
        "id": "lentinula-edodes",
        "name": "Shiitake",
        "scientific_name": "Lentinula edodes",
        "aliases": [
            "black forest mushroom",
            "oak mushroom"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                5,
                12
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn"
        ],
        "distribution": "East Asia; cultivated worldwide",
        "regions": [
            "asia",
            "global"
        ],
        "description": "Cultivated on oak logs; dark brown cap with white cracks when mature, tough stem best removed. Rich, savory umami flavor. One of the most eaten mushrooms globally.",
        "lookalikes": [
            {
                "name": "Various brown saprotrophic species",
                "distinguish": "Cultivated origin and cracked cap are distinctive; confirm spore print is white."
            }
        ],
        "fun_fact": "The second most-cultivated mushroom on the planet. Its signature smoky flavor comes from a compound it makes in response to UV light and damage."
    },
    {
        "id": "coprinus-comatus",
        "name": "Shaggy Mane",
        "scientific_name": "Coprinus comatus",
        "aliases": [
            "lawyer's wig",
            "shaggy ink cap"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "bell",
                "cylindrical"
            ],
            "colors": [
                "white"
            ],
            "diameter_cm": [
                3,
                7
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "black"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "black",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "autumn"
        ],
        "distribution": "Worldwide, lawns and disturbed ground",
        "regions": [
            "global"
        ],
        "description": "Tall white cylindrical cap covered in shaggy scales that auto-digests (deliquesces) into black ink from the bottom up. Edible when young and fresh; do NOT combine with alcohol (coprine causes a disulfiram-like reaction).",
        "lookalikes": [
            {
                "name": "Coprinopsis atramentaria (common ink cap)",
                "distinguish": "Gray, smooth, no shaggy scales; also alcohol-reactive."
            },
            {
                "name": "Young Amanita",
                "distinguish": "Amanitas have a volva and do not deliquesce."
            }
        ],
        "fun_fact": "Self-digests into black ink from the bottom up — you've got hours to cook it after picking. Old English used the juice as actual writing ink."
    },
    {
        "id": "macrolepiota-procera",
        "name": "Parasol Mushroom",
        "scientific_name": "Macrolepiota procera",
        "aliases": [
            "parasol",
            "shaggy parasol"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "umbonate"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                10,
                30
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "brown"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide, grassy open areas",
        "regions": [
            "global"
        ],
        "description": "Large, with a shaggy brown-scaled cap, a movable snake-skin-patterned ring, and a stem that swells like a bulb at the base. Excellent edible -- but must be distinguished from the green-spored parasol.",
        "lookalikes": [
            {
                "name": "Chlorophyllum molybdites (green-spored parasol)",
                "distinguish": "POISONOUS; green spore print and green-tinged gills when mature."
            },
            {
                "name": "Amanita species",
                "distinguish": "Amanitas have a volva cup; parasols do not."
            }
        ],
        "fun_fact": "The stem scales form a snake-skin pattern and the whole cap slides up and down the stem like a telescope. A giant, edible, unmistakable meadow mushroom."
    },
    {
        "id": "chlorophyllum-molybdites",
        "name": "Green-Spored Parasol",
        "scientific_name": "Chlorophyllum molybdites",
        "aliases": [
            "False parasol",
            "green gill"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "umbonate"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                8,
                30
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "green"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "brown"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "green",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "North America, warm regions worldwide",
        "regions": [
            "global",
            "north-america"
        ],
        "description": "The most common cause of mushroom poisoning in North America. Looks like an edible parasol but the gills turn greenish with age and the spore print is distinctly green. Causes violent GI illness.",
        "lookalikes": [
            {
                "name": "Macrolepiota procera (parasol)",
                "distinguish": "True parasol has a WHITE spore print; always print green-spored parasol before eating."
            }
        ],
        "fun_fact": "The most commonly eaten poisonous mushroom in North America — it looks like a harmless parasol until you check the green spore print. The green drop is the warning."
    },
    {
        "id": "armillaria-mellea",
        "name": "Honey Fungus",
        "scientific_name": "Armillaria mellea",
        "aliases": [
            "honey mushroom"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "honey",
                "yellow-brown",
                "brown"
            ],
            "diameter_cm": [
                3,
                15
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "yellow"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": [
            "autumn"
        ],
        "distribution": "Worldwide",
        "regions": [
            "global"
        ],
        "description": "Honey-colored caps in clusters at the base of trees, with a ring and black rhizomorphs ('shoelaces') under the bark. Edible when young and thoroughly cooked; some people are sensitive. A notorious plant pathogen.",
        "lookalikes": [
            {
                "name": "Galerina marginata (deadly galerina)",
                "distinguish": "Grows on wood too but is smaller, brown-spored, and DEADLY. Always check spore print."
            }
        ],
        "fun_fact": "Forms one of the largest living organisms on Earth: a single clone in Oregon covers over 9 square kilometers. Also a tree-killing parasite you can eat if you cook it."
    },
    {
        "id": "galerina-marginata",
        "name": "Deadly Galerina",
        "scientific_name": "Galerina marginata",
        "aliases": [
            "funeral bell"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "bell"
            ],
            "colors": [
                "brown",
                "tan",
                "rusty"
            ],
            "diameter_cm": [
                2,
                5
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "rusty",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "rusty-brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Small brown mushroom on wood containing amatoxins -- same family as the death cap. Looks alarmingly like an edible honey fungus or a magic mushroom. The rusty-brown spore print and wood habitat are clues.",
        "lookalikes": [
            {
                "name": "Armillaria mellea",
                "distinguish": "Honey fungus is larger, yellow-brown, ringed, white-spored."
            },
            {
                "name": "Psilocybe species",
                "distinguish": "Magic mushrooms grow on wood/dung; galerina is deadly -- never guess."
            }
        ],
        "fun_fact": "Small brown mushroom, outsized danger — the same amatoxins as the death cap. A single cap can kill, which is why 'LBM' is mycologist shorthand for 'don't.'"
    },
    {
        "id": "hericium-erinaceus",
        "name": "Lion's Mane",
        "scientific_name": "Hericium erinaceus",
        "aliases": [
            "bearded tooth",
            "pom pom mushroom",
            "yamabushitake"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "spherical",
                "tooth"
            ],
            "colors": [
                "white",
                "cream"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere hardwoods",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A white, cascading mass of icicle-like teeth rather than gills or pores. No poisonous lookalikes resemble it. Tastes like seafood (lobster/crab) when cooked. Studied for potential nerve-regenerative effects.",
        "lookalikes": [
            {
                "name": "Hericium coralloides / americanum",
                "distinguish": "Branched, coral-like forms; also edible."
            }
        ],
        "fun_fact": "Looks like a pom-pom of white icicles and is studied for nerve-growth compounds. The only mushroom that doubles as a seafood substitute and a nootropic."
    },
    {
        "id": "sparassis-crispa",
        "name": "Cauliflower Fungus",
        "scientific_name": "Sparassis crispa",
        "aliases": [
            "cauliflower mushroom",
            "brain fungus"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "lobed",
                "cauliflower"
            ],
            "colors": [
                "cream",
                "tan"
            ],
            "diameter_cm": [
                10,
                40
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "cream"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A large, ruffled mass resembling a head of cauliflower growing at the base of conifers. Mild, crunchy, and good eating. Unmistakable once seen.",
        "lookalikes": [
            {
                "name": "Gyromitra esculenta (False morel)",
                "distinguish": "Brain-lobed and on the ground (not at a wood base); contains gyromitrin and is POISONOUS. Sparassis is a ruffled mass on wood."
            },
            {
                "name": "Hericium species (tooth fungi)",
                "distinguish": "Also cauliflower-like but covered in spiky teeth rather than smooth ruffled lobes; edible."
            }
        ],
        "fun_fact": "A giant brain-like mass of ruffled shelves that smells faintly of peppery almonds. Tastes surprisingly like crab or lobster when sautéed."
    },
    {
        "id": "trametes-versicolor",
        "name": "Turkey Tail",
        "scientific_name": "Trametes versicolor",
        "aliases": [
            "Coriolus",
            "kawaratake"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "shell",
                "fan"
            ],
            "colors": [
                "brown",
                "gray",
                "blue",
                "white",
                "tan"
            ],
            "diameter_cm": [
                2,
                8
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "n/a",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "year-round"
        ],
        "distribution": "Worldwide",
        "regions": [
            "global"
        ],
        "description": "Thin, tough, concentric-zoned bracket fungus in overlapping colorful bands. Too leathery to eat but valued in traditional medicine (PSP/beta-glucans). A benchmark 'polypore' for ID practice.",
        "lookalikes": [
            {
                "name": "Stereum ostrea (False turkey tail)",
                "distinguish": "Smooth underside, no pores."
            }
        ],
        "fun_fact": "Wears concentric rings like a turkey's tail and is among the most-studied medicinal mushrooms (PSK/PSP) in oncology, especially in Asia. Too tough to eat, but brewed for centuries."
    },
    {
        "id": "fomes-fomentarius",
        "name": "Hoof Fungus",
        "scientific_name": "Fomes fomentarius",
        "aliases": [
            "tinder fungus",
            "horse hoof fungus"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "hoof",
                "bracket"
            ],
            "colors": [
                "gray",
                "black",
                "brown"
            ],
            "diameter_cm": [
                5,
                25
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "n/a",
            "colors": [
                "brown"
            ]
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "year-round"
        ],
        "distribution": "Northern Hemisphere, on birch",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Hard, hoof-shaped bracket with concentric rings and a pore surface underneath. Used historically as tinder (Ötzi the Iceman carried it) and for amadou. Inedible but culturally fascinating.",
        "lookalikes": [
            {
                "name": "Phellinus igniarius (False tinder fungus)",
                "distinguish": "Near-identical hoof bracket; also inedible with darker context flesh."
            },
            {
                "name": "Ganoderma species (reishi)",
                "distinguish": "Lacquered reddish shelf with a lateral stem and rusty-brown spores; not hoof-shaped."
            }
        ],
        "fun_fact": "Ötzi the Iceman carried this fungus 5,000 years ago — it makes excellent tinder (amadou) and was likely his fire-starter and medicine kit in one."
    },
    {
        "id": "calvatia-gigantea",
        "name": "Giant Puffball",
        "scientific_name": "Calvatia gigantea",
        "aliases": [
            "puffball",
            "calf's lung"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "spherical",
                "ball"
            ],
            "colors": [
                "white",
                "tan"
            ],
            "diameter_cm": [
                10,
                50
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "olive-brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Worldwide in pastures",
        "regions": [
            "global"
        ],
        "description": "A soccer-ball-sized white sphere with no stem, gills, or cap. Edible ONLY while pure white inside; once it yellows or turns into spores, discard. Cut one open to confirm -- never eat anything that isn't uniformly white throughout.",
        "lookalikes": [
            {
                "name": "Amanita 'egg' (young death cap/destroying angel)",
                "distinguish": "Young Amanitas underground look like small puffballs but have a stem/volva inside when cut -- DEADLY."
            },
            {
                "name": "Scleroderma (earthball)",
                "distinguish": "Has a dark, powdery interior even when young; poisonous."
            }
        ],
        "fun_fact": "Can grow bigger than a basketball and feed a family. The dried inner flesh was used as a styptic (wound-clotting) field dressing in wartime."
    },
    {
        "id": "scleroderma-citrinum",
        "name": "Common Earthball",
        "scientific_name": "Scleroderma citrinum",
        "aliases": [
            "earthball",
            "poison puffball"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "spherical",
                "ball"
            ],
            "colors": [
                "yellow",
                "brown",
                "tan"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "purple-black",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Looks like a puffball but the interior is dark purple-black and powdery even when young, and the skin is thick and yellow-cracked. Causes GI upset. The dark interior is the key difference from edible puffballs.",
        "lookalikes": [
            {
                "name": "Calvatia (puffball)",
                "distinguish": "Puffballs are white inside at edible stage."
            }
        ],
        "fun_fact": "Looks like a puffball from outside but is poisonous inside — the giveaway is the dark, powdery interior and the lack of any stem. Cut before you commit."
    },
    {
        "id": "lycoperdon-perlatum",
        "name": "Common Puffball",
        "scientific_name": "Lycoperdon perlatum",
        "aliases": [
            "gemmed puffball",
            "warted puffball"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "pear",
                "ball"
            ],
            "colors": [
                "white",
                "tan"
            ],
            "diameter_cm": [
                2,
                6
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide",
        "regions": [
            "global"
        ],
        "description": "Pear-shaped, covered in small warts, with a stem-like base. Edible when young and solid white inside. A safe, common beginner foraging find.",
        "lookalikes": [
            {
                "name": "Young Amanita",
                "distinguish": "Cut open: Amanita has a miniature cap/stem inside."
            }
        ],
        "fun_fact": "Covered in tiny warts and releases a puff of spores when mature — the original 'puff' ball. Edible only while pure white and firm inside."
    },
    {
        "id": "suillus-luteus",
        "name": "Slippery Jack",
        "scientific_name": "Suillus luteus",
        "aliases": [
            "pine bolete"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex"
            ],
            "colors": [
                "brown",
                "chestnut"
            ],
            "diameter_cm": [
                5,
                12
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "n/a",
            "colors": [
                "yellow"
            ]
        },
        "stem": {
            "colors": [
                "yellow",
                "cream"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere pine plantations",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A bolete (pores, no gills) with a slimy brown cap and a slimy ring on the stem. Peel the slimy cap skin before eating. Common under pines, easy and safe once you recognize the pore surface.",
        "lookalikes": [
            {
                "name": "Suillus granulatus",
                "distinguish": "Nearly identical but lacks the slimy ring on the stem; edible."
            },
            {
                "name": "Boletus edulis (porcini)",
                "distinguish": "Larger with a dry, non-slimy cap and no ring; a choice edible, so confusion is harmless."
            }
        ],
        "fun_fact": "Named for the slimy, peelable cap cuticle that slips off like a jacket. The slimy layer is best removed before cooking or it gets gloopy."
    },
    {
        "id": "tricholoma-matsutake",
        "name": "Matsutake",
        "scientific_name": "Tricholoma matsutake",
        "aliases": [
            "pine mushroom",
            "matsutake"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan",
                "white"
            ],
            "diameter_cm": [
                6,
                20
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "autumn"
        ],
        "distribution": "Asia, North America, Europe (declining)",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Highly prized in Japan for its spicy, cinnamon-pine aroma. White flesh that stays white when cut, with a partial veil that often leaves a ring zone. Forms mycorrhizae with specific pines/oaks.",
        "lookalikes": [
            {
                "name": "Amanita species",
                "distinguish": "Matsutake has white spores and no volva; some toxic Amanitas smell similar."
            },
            {
                "name": "Tricholoma pardinum (tiger trich)",
                "distinguish": "POISONOUS; similar size and white gills but a scaly/felted cap and an abruptly bulbous stem base causing violent GI poisoning. Check the cap surface and base."
            }
        ],
        "fun_fact": "Prized in Japan for a smell described as spicy-cinnamon-dirty-socks; a single prime specimen can outprice a steak. Near-impossible to cultivate, so wild harvests fetch absurd money."
    },
    {
        "id": "russula-emetica",
        "name": "The Sickener",
        "scientific_name": "Russula emetica",
        "aliases": [
            "emetic russula"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "red",
                "pink"
            ],
            "diameter_cm": [
                4,
                10
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A red-capped Russula with very brittle white gills and stem (characteristic of the genus -- they snap like chalk). Acrid and emetic; causes vomiting. Many Russulas are edible, so species-level ID matters.",
        "lookalikes": [
            {
                "name": "Edible Russulas (e.g. R. cyanoxantha)",
                "distinguish": "Those lack the hot, peppery taste and are not bright red."
            }
        ],
        "fun_fact": "Named for exactly what it does — emetic (vomit-inducing). The bright red cap with white gills is a classic 'looks great, feels terrible' mushroom."
    },
    {
        "id": "russula-cyanoxantha",
        "name": "Charcoal Burner",
        "scientific_name": "Russula cyanoxantha",
        "aliases": [
            "blue-yellow russula"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "purple",
                "green",
                "brown",
                "red"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A variable-colored Russula with flexible, greasy gills (unusual -- most Russula gills are brittle) and a mild, non-peppery taste. A reliable edible once you learn the genus.",
        "lookalikes": [
            {
                "name": "Russula emetica",
                "distinguish": "Sickener is bright red and acrid-tasting."
            }
        ],
        "fun_fact": "One of the few Russulas safe to eat raw — its stem doesn't crumble like chalk, the 'crunch test' that separates edible Russulas from nasty ones."
    },
    {
        "id": "hypholoma-fasciculare",
        "name": "Sulfur Tuft",
        "scientific_name": "Hypholoma fasciculare",
        "aliases": [
            "sulphur tuft"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "yellow",
                "orange",
                "olive"
            ],
            "diameter_cm": [
                2,
                6
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "green",
                "olive",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "yellow"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "autumn"
        ],
        "distribution": "Worldwide",
        "regions": [
            "global"
        ],
        "description": "Dense clusters of sulfur-yellow caps with greenish-yellow gills on rotting wood. Bitter and poisonous (contains fasciculol). The clustered growth on wood and yellow coloring are distinctive.",
        "lookalikes": [
            {
                "name": "Armillaria mellea",
                "distinguish": "Honey fungus is larger, honey-colored, white-gilled."
            },
            {
                "name": "Edible clustered species",
                "distinguish": "None share the exact sulfur-yellow + green-gill combo on wood."
            }
        ],
        "fun_fact": "Clumps on wood with vivid yellow gills — beautiful and deadly. The immediate bitterness is a warning most people heed too late."
    },
    {
        "id": "cortinarius-rubellus",
        "name": "Deadly Webcap",
        "scientific_name": "Cortinarius rubellus",
        "aliases": [
            "deadly cortinarius",
            "orange webcap"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "bell"
            ],
            "colors": [
                "orange",
                "brown",
                "rusty"
            ],
            "diameter_cm": [
                3,
                8
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "rusty",
                "orange"
            ]
        },
        "stem": {
            "colors": [
                "orange",
                "rusty"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "rusty-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "autumn"
        ],
        "distribution": "Northern Europe and North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "Contains orellanine, which causes delayed (days to weeks) but often fatal kidney failure. Rusty-orange with a cobweb (cortina) veil when young. Part of a large, difficult genus best avoided by amateurs.",
        "lookalikes": [
            {
                "name": "Many Cortinarius species",
                "distinguish": "The whole genus is risky; rusty spore print is a unifying trait."
            }
        ],
        "fun_fact": "Contains orellanine, which destroys your kidneys over days to weeks — often too late by the time symptoms show. That cobweb (cortina) veil is the genus giveaway."
    },
    {
        "id": "clitocybe-dealbata",
        "name": "Ivory Funnel",
        "scientific_name": "Clitocybe dealbata",
        "aliases": [
            "poisonous funnel"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "funnel",
                "depressed"
            ],
            "colors": [
                "white",
                "cream",
                "pale"
            ],
            "diameter_cm": [
                2,
                5
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere lawns and pastures",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Small, pale, funnel-shaped and easily confused with edible field mushrooms or oyster mushrooms. Contains muscarine, which can be fatal, especially dangerous because it looks so innocuous and grows in grazed areas.",
        "lookalikes": [
            {
                "name": "Edible white fungi",
                "distinguish": "Small size, funnel shape, and white spore print on lawns are red flags."
            }
        ],
        "fun_fact": "Tiny, white, and deadly — loaded with muscarine that overloads your nervous system. A scattered cluster has killed foragers who mistook it for an edible mousse."
    },
    {
        "id": "psilocybe-cubensis",
        "name": "Magic Mushroom",
        "scientific_name": "Psilocybe cubensis",
        "aliases": [
            "golden teacher",
            "cubes"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "bell"
            ],
            "colors": [
                "brown",
                "gold",
                "tan"
            ],
            "diameter_cm": [
                2,
                8
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "purple",
                "brown",
                "gray"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "blue"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "grassland",
        "substrate": "dung",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Subtropical/tropical worldwide",
        "regions": [
            "global"
        ],
        "potency": "moderate",
        "description": "Contains psilocybin and is a controlled hallucinogen in most jurisdictions. Bruises blue, grows on dung, has a purple-brown spore print. Listed here for education and harm reduction -- not recommended or legal in many places.",
        "lookalikes": [
            {
                "name": "Galerina marginata",
                "distinguish": "DEADLY; similar habitat/size but no blue bruising and rusty-brown spores."
            },
            {
                "name": "Panaeolus species",
                "distinguish": "Also dung-loving; some are psychoactive, some not."
            }
        ],
        "fun_fact": "The species that launched a thousand studies: contains psilocybin, now in FDA 'breakthrough therapy' trials for depression. Legal status varies wildly by place — know your local law."
    },
    {
        "id": "flammulina-velutipes",
        "name": "Enoki",
        "scientific_name": "Flammulina velutipes",
        "aliases": [
            "velvet foot",
            "winter mushroom",
            "enokitake"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "tan",
                "brown"
            ],
            "diameter_cm": [
                2,
                8
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "tan"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn",
            "winter",
            "spring"
        ],
        "distribution": "Worldwide on hardwood",
        "regions": [
            "global"
        ],
        "description": "In the wild: small brown caps on a dark, velvety stem in clusters on dead trees. Cultivated forms are the long, white, noodle-like enoki. Edible and mild.",
        "lookalikes": [
            {
                "name": "Galerina marginata",
                "distinguish": "Deadly; grows on wood too -- confirm white spores and velvety stem base."
            }
        ],
        "fun_fact": "The long, spindly white 'enoki' in stores is grown in the dark so it stretches tall and pale. In the wild it's a short, brown, velvet-stemmed mushroom on stumps."
    },
    {
        "id": "auricularia-auricula-judae",
        "name": "Wood Ear",
        "scientific_name": "Auricularia auricula-judae",
        "aliases": [
            "jelly ear",
            "black fungus",
            "mu er"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "ear",
                "shelf"
            ],
            "colors": [
                "brown",
                "red-brown",
                "black"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "year-round"
        ],
        "distribution": "Worldwide on elder and other hardwoods",
        "regions": [
            "global"
        ],
        "description": "A rubbery, ear-shaped jelly fungus, brown when moist and brittle when dry. Flavorless but prized for crunch in Asian cooking. No dangerous lookalikes.",
        "lookalikes": [
            {
                "name": "Auricularia polytricha (cloud ear)",
                "distinguish": "Closely related, darker and hairier on top; equally edible."
            },
            {
                "name": "Tremella species (white/yellow jellies)",
                "distinguish": "Lobed or branched jellies, not ear-shaped; also edible."
            }
        ],
        "fun_fact": "Ear-shaped jelly that stays crunchy after cooking — the texture, not the flavor, is the point in Asian soups. Also called Judas's ear, from the legend of Judas hanging on an elder tree."
    },
    {
        "id": "tremella-fuciformis",
        "name": "Snow Fungus",
        "scientific_name": "Tremella fuciformis",
        "aliases": [
            "silver ear",
            "white jelly mushroom",
            "yin er"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "lobed",
                "jelly"
            ],
            "colors": [
                "white",
                "cream"
            ],
            "diameter_cm": [
                3,
                12
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Tropical/subtropical Asia; cultivated",
        "regions": [
            "asia"
        ],
        "description": "A translucent, ruffled white jelly fungus used in Chinese desserts and soups for its texture and supposed health benefits. Requires a host fungus to fruit.",
        "lookalikes": [
            {
                "name": "Tremella mesenterica (yellow brain)",
                "distinguish": "Bright yellow lobed jelly; edible but insubstantial."
            },
            {
                "name": "Auricularia (wood ear)",
                "distinguish": "Ear-shaped brown/black jelly rather than white-lobed; both edible."
            }
        ],
        "fun_fact": "The 'beauty mushroom' of Chinese desserts — prized for skin and supposed anti-aging properties. Translucent and slippery, valued for mouthfeel over taste."
    },
    {
        "id": "schizophyllum-commune",
        "name": "Split Gill",
        "scientific_name": "Schizophyllum commune",
        "aliases": [
            "split-gill fungus"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "shell",
                "fan"
            ],
            "colors": [
                "white",
                "gray",
                "tan"
            ],
            "diameter_cm": [
                1,
                4
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "white",
                "gray"
            ]
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "year-round"
        ],
        "distribution": "Cosmopolitan",
        "regions": [
            "global"
        ],
        "description": "Tiny fuzzy shells with gills that split lengthwise when dry and close when wet -- a unique feature. Too tough and thin to eat; primarily of interest for its unusual biology (it has over 20,000 sexes).",
        "lookalikes": [
            {
                "name": "Small bracket fungi",
                "distinguish": "The split gills are unique."
            }
        ],
        "fun_fact": "One of the most widespread mushrooms on Earth, on every continent but Antarctica. Has over 20,000 documented mating types — a genetics record-holder."
    },
    {
        "id": "phallus-impudicus",
        "name": "Common Stinkhorn",
        "scientific_name": "Phallus impudicus",
        "aliases": [
            "stinkhorn"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "bell",
                "netted"
            ],
            "colors": [
                "olive",
                "green",
                "white"
            ],
            "diameter_cm": [
                3,
                5
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": True
        },
        "spore_print": "olive",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "Emerges as a white 'egg' (edible at this stage, like a truffle-ish delicacy in some cuisines), then rapidly expands into a stinky, olive-spored phallus that attracts flies to spread spores. The young egg is the edible part.",
        "lookalikes": [
            {
                "name": "Amanita 'egg'",
                "distinguish": "Both start as eggs; stinkhorn egg has a softer, more gelatinous texture and lacks a volva cup."
            }
        ],
        "fun_fact": "Erupts from a white 'egg' and smells like rotting meat to lure flies that spread its spores. The young egg is edible and considered a delicacy in some countries."
    },
    {
        "id": "ramaria-formosa",
        "name": "Beautiful Coral",
        "scientific_name": "Ramaria formosa",
        "aliases": [
            "coral fungus"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "branched",
                "coral"
            ],
            "colors": [
                "pink",
                "salmon",
                "tan"
            ],
            "diameter_cm": [
                8,
                20
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white",
                "tan"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "ochre",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A pink, branching coral-shaped fungus. Causes GI upset in many people. Coral fungi are a mixed bag -- some edible, some not -- so species ID is essential and beginners should avoid them.",
        "lookalikes": [
            {
                "name": "Ramaria botrytis (edible coral)",
                "distinguish": "Different color/branch tips; coral ID is expert-level."
            }
        ],
        "fun_fact": "A pink coral pretty enough to pick and poisonous enough to regret it — causes violent vomiting. With coral fungi, the edible species are the exception, not the rule."
    },
    {
        "id": "clavulina-cristata",
        "name": "Crested Coral",
        "scientific_name": "Clavulina cristata",
        "aliases": [
            "white coral",
            "cock's comb"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "branched",
                "coral"
            ],
            "colors": [
                "white"
            ],
            "diameter_cm": [
                3,
                8
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "White, intricately branched coral with toothed tips. Generally considered edible and mild, though not choice. A good example of the coral growth form.",
        "lookalikes": [
            {
                "name": "Ramaria formosa",
                "distinguish": "That one is pink and poisonous."
            }
        ],
        "fun_fact": "White branching coral with toothed tips — sometimes turning brown or gray from a water mold that parasitizes it. Still edible, just uglier."
    },
    {
        "id": "leccinum-scrobum",
        "name": "Birch Bolete",
        "scientific_name": "Leccinum scabrum",
        "aliases": [
            "rough-stemmed bolete"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex"
            ],
            "colors": [
                "brown",
                "tan",
                "gray"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "n/a",
            "colors": [
                "white",
                "gray"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere under birch",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A bolete (pores) with a gray-brown cap and a stem covered in dark scabrous dots. Common under birch. Edible and easy to ID within the safe bolete group.",
        "lookalikes": [
            {
                "name": "Leccinum aurantiacum (red-capped bolete)",
                "distinguish": "Orange-red cap, also under hardwoods; edible."
            },
            {
                "name": "Boletus edulis (porcini)",
                "distinguish": "No scabrous stem dots and a smooth stem; a choice edible."
            }
        ],
        "fun_fact": "Always found under birch, with a stem covered in dark scabrous scales like a woolly jumper. The birch partnership is so tight it rarely shows up anywhere else."
    },
    {
        "id": "verpa-bohemica",
        "name": "Early Morel",
        "scientific_name": "Verpa bohemica",
        "aliases": [
            "False morel",
            "thimble morel"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "thimble",
                "wrinkled"
            ],
            "colors": [
                "tan",
                "brown"
            ],
            "diameter_cm": [
                2,
                5
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "spring"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A morel-lookalike with a cap attached only at the top like a thimble on a stem, and a hollow stem. Edible when cooked but easily confused with the deadly False morel (Gyromitra) -- learn the difference before foraging.",
        "lookalikes": [
            {
                "name": "Gyromitra esculenta",
                "distinguish": "Gyromitra cap is lobed and hangs free at the edge; Verpa cap attaches at the apex only."
            },
            {
                "name": "Morchella",
                "distinguish": "True morel cap is fully attached to the stem."
            }
        ],
        "fun_fact": "A 'half-free' morel that fruits weeks before True morels — the cap hangs from the stem like a thimble. Easy to confuse with the deadly False morel if you're not paying attention."
    },
    {
        "id": "laetiporus-sulphureus",
        "name": "Chicken of the Woods",
        "scientific_name": "Laetiporus sulphureus",
        "aliases": [
            "sulfur shelf",
            "chicken mushroom"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "shelf",
                "bracket"
            ],
            "colors": [
                "orange",
                "yellow",
                "red"
            ],
            "diameter_cm": [
                10,
                40
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "n/a",
            "colors": [
                "yellow",
                "white"
            ]
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide on hardwoods (and conifers in some regions)",
        "regions": [
            "global"
        ],
        "description": "Bright orange and yellow shelf clusters on tree trunks with a texture and taste likened to chicken (when young). A favorite edible -- but some react to the conifer form, so try a small amount first.",
        "lookalikes": [
            {
                "name": "Omphalotus (jack-o'-lantern)",
                "distinguish": "Also orange clusters on wood but has True gills, not pores, and is poisonous."
            }
        ],
        "fun_fact": "Tastes and shreds like chicken (seriously) when young — a famous meat substitute. But some people get gut upset, and it must not be confused with the lookalike sulfur tuft."
    },
    {
        "id": "amerenia-smithiana",
        "name": "Deadly Parachute",
        "scientific_name": "Amanita smithiana",
        "aliases": [
            "Smith's amanita"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "cream",
                "tan"
            ],
            "diameter_cm": [
                4,
                10
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Pacific Northwest of North America; also reported in Europe",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A pale, innocuous-looking Amanita whose toxins (aminohexadienoic acid) cause irreversible kidney failure. It lacks the classic volva of death-cap types, which makes it dangerously easy to mistake for a harmless white mushroom.",
        "lookalikes": [
            {
                "name": "Amanita velosa (veiled amanita)",
                "distinguish": "An edible West Coast Amanita with a tan cap and similar size; positive ID requires microscopy."
            },
            {
                "name": "Agaricus species (field mushrooms)",
                "distinguish": "Have pink-then-brown gills and a ring but no volva/ring combination like Amanita."
            }
        ],
        "fun_fact": "One of several 'little brown' amanitas whose look is no clue to its lethality."
    },
    {
        "id": "amanita-ocreata",
        "name": "Death Angel",
        "scientific_name": "Amanita ocreata",
        "aliases": [
            "coccora",
            "European death cap (relative)"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "bell"
            ],
            "colors": [
                "white",
                "cream",
                "pale-tan"
            ],
            "diameter_cm": [
                4,
                12
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": True
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "winter",
            "spring"
        ],
        "distribution": "Western North America (California to Baja)",
        "regions": [
            "north-america"
        ],
        "description": "A pure white, ringed amanita with a cup (volva) at the base. Contains amatoxins and is responsible for fatal poisonings, often in spring when foragers confuse it with edible mushrooms.",
        "lookalikes": [
            {
                "name": "Amanita velosa",
                "distinguish": "Edible, but the margin of the cap is distinctly fuzzy/striate; still risky without expertise."
            },
            {
                "name": "Young Agaricus",
                "distinguish": "Have pink/brown gills even when young, never a True volva cup."
            }
        ],
        "fun_fact": "Its toxicity is unrelated to cooking — amatoxins survive heat intact."
    },
    {
        "id": "entoloma-sinuatum",
        "name": "Livid Entoloma",
        "scientific_name": "Entoloma sinuatum",
        "aliases": [
            "leaden entoloma",
            "sinuate entoloma"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "gray",
                "tan",
                "buff"
            ],
            "diameter_cm": [
                6,
                20
            ]
        },
        "gills": {
            "attachment": "sinuate",
            "spacing": "crowded",
            "colors": [
                "pink"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "gray"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "pink",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe and North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A large gray-cap mushroom with the giveaway pink gills and spores of the Entoloma family. Causes severe gastrointestinal poisoning; responsible for many European poisonings because it vaguely resembles an edible field mushroom.",
        "lookalikes": [
            {
                "name": "Agaricus campestris (field mushroom)",
                "distinguish": "Has chocolate-brown spores and browner gills; Entoloma keeps pink gills from the start."
            },
            {
                "name": "Tricholoma species",
                "distinguish": "White-spored lookalikes; check spore print color."
            }
        ],
        "fun_fact": "The pink spore print is the family trademark and the key to telling it from white-spored toxic amanitas."
    },
    {
        "id": "sarcosphaera-crassa",
        "name": "Violet Crown Cup",
        "scientific_name": "Sarcosphaera coronaria",
        "aliases": [
            "crown cup",
            "violet fairy cap"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "cup",
                "split"
            ],
            "colors": [
                "lilac",
                "violet",
                "cream"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "spring",
            "summer"
        ],
        "distribution": "Europe, North America (west)",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A striking cup fungus that splits into star-like segments, revealing violet to lilac inner flesh. Contains gyromitrin-like compounds and is considered poisonous, especially when consumed with alcohol.",
        "lookalikes": [
            {
                "name": "Peziza species (cup fungi)",
                "distinguish": "Similar cups but lack the violet pigment and star-like splitting; many are edible but verify."
            },
            {
                "name": "Sarcoscypha (scarlet cup)",
                "distinguish": "Smaller brilliant-red cup with no violet tone or crown split; edible."
            }
        ],
        "fun_fact": "Its color fades to cream as it ages and dries in the sun."
    },
    {
        "id": "mutinus-caninus",
        "name": "Dog Stinkhorn",
        "scientific_name": "Mutinus caninus",
        "aliases": [
            "dog phallus"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "phallus",
                "cylindrical"
            ],
            "colors": [
                "orange",
                "red",
                "pink"
            ],
            "diameter_cm": [
                2,
                10
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "orange",
                "pink"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "n/a",
        "habitat": "forest",
        "substrate": "litter",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A small, orange-tipped, phallus-shaped fungus covered in olive spore slime (gleba) at the tip that attracts flies for spore dispersal. Not poisonous but inedible and foul-smelling; related to the larger stinkhorns.",
        "lookalikes": [
            {
                "name": "Phallus impudicus (common stinkhorn)",
                "distinguish": "Much larger with a lacy skirt (indusium) and a more prominent smelly gleba."
            }
        ],
        "fun_fact": "Flies do the pollination job — they eat the slime and spread spores on their feet."
    },
    {
        "id": "battarrea-phalloides",
        "name": "Sand Warrior",
        "scientific_name": "Battarrea phalloides",
        "aliases": [
            "desert shaggy mane",
            "stalked puffball"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "puffball",
                "umbel"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                3,
                8
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "tan",
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "grassland",
        "substrate": "sand",
        "ecology": "saprotrophic",
        "season": [
            "autumn",
            "winter"
        ],
        "distribution": "Arid and semi-arid regions worldwide",
        "regions": [
            "global"
        ],
        "description": "A desert puffball on a tall, shaggy stem with a ragged skirt-like veil. Spores release from a powdery cap at the top. Too tough and insubstantial to eat; admired for its odd, sculptural form.",
        "lookalikes": [
            {
                "name": "Young puffballs (Calvatia)",
                "distinguish": "Lack the long stem and the torn skirt; Battarrea is all stalk."
            }
        ],
        "fun_fact": "It can push up through gravel and even asphalt thanks to its force-generating stem."
    },
    {
        "id": "xerocomellus-chrysenteron",
        "name": "Red-cracked Bolete",
        "scientific_name": "Xerocomellus chrysenteron",
        "aliases": [
            "boletus chrysenteron"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "olive",
                "tan"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "n/a",
            "colors": [
                "yellow",
                "olive"
            ]
        },
        "stem": {
            "colors": [
                "yellow",
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A common bolete whose brown cap cracks to reveal reddish flesh beneath. Mild and edible, though not as prized as porcini. A good beginner bolete to learn the pore-under-cap structure.",
        "lookalikes": [
            {
                "name": "Boletus edulis (porcini)",
                "distinguish": "Larger, paler, with a fine net pattern on the stem; both edible."
            },
            {
                "name": "Boletus satanas",
                "distinguish": "Poisonous; has a red-tinged stem and stains blue."
            }
        ],
        "fun_fact": "The red 'cracks' are how it got the name chrysenteron — 'golden inside'."
    },
    {
        "id": "stropharia-rugosoannulata",
        "name": "Wine Cap",
        "scientific_name": "Stropharia rugosoannulata",
        "aliases": [
            "king stropharia",
            "garden giant"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "maroon",
                "red-brown",
                "brown"
            ],
            "diameter_cm": [
                8,
                30
            ]
        },
        "gills": {
            "attachment": "adnate",
            "spacing": "crowded",
            "colors": [
                "purple-gray",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "gray"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "garden",
        "substrate": "woodchip",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn"
        ],
        "distribution": "Europe, North America; widely cultivated",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A large, wine-red capped mushroom that fruits on wood chips and mulched garden beds. Easy to cultivate and a reliable edible with a meaty texture. A favorite for permaculture gardens.",
        "lookalikes": [
            {
                "name": "Chlorophyllum molybdites",
                "distinguish": "Poisonous; has green spores and a scaly tan cap, not wine-red."
            },
            {
                "name": "Agaricus species",
                "distinguish": "Have pink-then-brown gills and a ring but a different cap color."
            }
        ],
        "fun_fact": "It's one of the few gourmet mushrooms you can grow in a backyard mulch bed."
    },
    {
        "id": "pleurotus-pulmonarius",
        "name": "Phoenix Oyster",
        "scientific_name": "Pleurotus pulmonarius",
        "aliases": [
            "lung oyster",
            "pale oyster"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "fan",
                "shelf"
            ],
            "colors": [
                "cream",
                "tan",
                "gray"
            ],
            "diameter_cm": [
                4,
                15
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "lilac-gray",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide",
        "regions": [
            "global"
        ],
        "description": "A pale, fan-shaped oyster mushroom that fruits on dead hardwoods, often in warm weather (unlike the cooler-loving pearl oyster). Excellent edible, mild and tender; nearly identical in use to the pearl oyster.",
        "lookalikes": [
            {
                "name": "Pleurotus ostreatus (pearl oyster)",
                "distinguish": "Very similar; distinguished mainly by season and spore print shade."
            },
            {
                "name": "Ivory funnel (Clitocybe dealbata)",
                "distinguish": "Poisonous; smaller, centrally stemmed, and grows on the ground."
            }
        ],
        "fun_fact": "Its lilac-gray spore print helps separate it from the white-spored poisonous lookalikes."
    },
    {
        "id": "grifola-frondosa",
        "name": "Hen of the Woods",
        "scientific_name": "Grifola frondosa",
        "aliases": [
            "maitake",
            "sheep's head"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "rosette",
                "shelf"
            ],
            "colors": [
                "gray",
                "brown",
                "tan"
            ],
            "diameter_cm": [
                10,
                60
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "gray"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn"
        ],
        "distribution": "Asia, Europe, North America",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A large, clustered 'rosette' of grayish fan caps at the base of oaks and other hardwoods. Prized edible (maitake) with a rich, earthy flavor and a celebrated status in Asian cuisine and medicine.",
        "lookalikes": [
            {
                "name": "Clustered Polyporus (Meripilus)",
                "distinguish": "Has pores rather than gills and blackens when bruised."
            },
            {
                "name": "Berkeley's polypore",
                "distinguish": "Pored, not gilled; both grow at tree bases."
            }
        ],
        "fun_fact": "A single clump can weigh several kilos — hence 'hen of the woods'."
    },
    {
        "id": "tuber-melanosporum",
        "name": "Black Truffle",
        "scientific_name": "Tuber melanosporum",
        "aliases": [
            "Périgord truffle",
            "black diamond"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "tuber",
                "subterranean"
            ],
            "colors": [
                "black",
                "brown"
            ],
            "diameter_cm": [
                2,
                9
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "n/a",
        "habitat": "forest",
        "substrate": "roots",
        "ecology": "mycorrhizal",
        "season": [
            "winter",
            "spring"
        ],
        "distribution": "Mediterranean Europe, cultivated worldwide",
        "regions": [
            "europe",
            "global"
        ],
        "description": "A subterranean, knobbly black fungus forming with oak and hazel roots. Among the most prized edibles in the world for its intense aroma. Found by trained dogs or pigs; never visible above ground.",
        "lookalikes": [
            {
                "name": "Tuber aestivum (summer truffle)",
                "distinguish": "Lighter, milder, and found in warmer months; similar but less aromatic."
            },
            {
                "name": "Deer truffle (Elaphomyces)",
                "distinguish": "Inedible False truffle with a different internal marbling; ID needs expertise."
            }
        ],
        "fun_fact": "Truffle hunters once used pigs, but dogs are preferred now — pigs tend to eat the prize."
    },
    {
        "id": "morchella-conica",
        "name": "Conical Morel",
        "scientific_name": "Morchella conica",
        "aliases": [
            "black morel",
            "pointed morel"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "cone",
                "honeycomb"
            ],
            "colors": [
                "gray",
                "brown",
                "black"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "spring"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A classic morel with a tall, conical, deeply pitted cap. A top-tier edible with a nutty, smoky flavor — but MUST be cooked; raw morels are toxic. Found in spring, often after disturbance or burns.",
        "lookalikes": [
            {
                "name": "Gyromitra esculenta (False morel)",
                "distinguish": "Brain-like wrinkled cap, not honeycomb pits; contains gyromitrin and is poisonous."
            },
            {
                "name": "Verpa bohemica",
                "distinguish": "Cap hangs like a thimble on a separate stem; less choice."
            }
        ],
        "fun_fact": "Morels and trees sometimes fruit in the same burned area the year after a fire."
    },
    {
        "id": "amanita-virosa",
        "name": "Death Angel (European)",
        "scientific_name": "Amanita virosa",
        "aliases": [
            "destroying angel",
            "white death cap"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "cream"
            ],
            "diameter_cm": [
                5,
                12
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": True
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, introduced N. America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "Pallid all-white destroying angel in the same lethal group as A. bisporigera and A. ocreata. Contains amatoxins; the white volva cup at the base is the tell-tale death sign.",
        "lookalikes": [
            {
                "name": "Amanita bisporigera",
                "distinguish": "Near-identical NA destroying angel; both deadly -- volva + white gills are the danger signal."
            },
            {
                "name": "Amanita caesarea (Caesar's mushroom)",
                "distinguish": "Edible Amanita has an orange cap/stem, never the stark white volva look."
            },
            {
                "name": "Calvatia (puffball)",
                "distinguish": "Young puffballs are solid white inside; destroying angels have gills + a stem."
            }
        ],
        "fun_fact": "Amatoxins resist cooking, freezing, and drying -- no preparation makes it safe."
    },
    {
        "id": "amanita-rubescens",
        "name": "The Blusher",
        "scientific_name": "Amanita rubescens",
        "aliases": [
            "blushing amanita"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "pinkish"
            ],
            "ring": True,
            "volva": True
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "One of the few edible Amanitas -- but only for the experienced. Flesh and stem bruise pink/red, and it keeps a skirt-like ring + volva remnants. A key teaching species: most Amanitas kill, this one is eaten.",
        "lookalikes": [
            {
                "name": "Amanita muscaria (fly agaric)",
                "distinguish": "Fly agaric is red-capped and poisonous; the Blusher is brown and reddens where bruised."
            },
            {
                "name": "Amanita phalloides (death cap)",
                "distinguish": "Death cap stays green/tan and does NOT redden; if in doubt, never eat an Amanita."
            }
        ],
        "fun_fact": "Its scientific name means 'reddening' -- the bruise colour is the ID clue."
    },
    {
        "id": "cortinarius-orellanus",
        "name": "Deadly Webcap",
        "scientific_name": "Cortinarius orellanus",
        "aliases": [
            "orange webcap"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "orange",
                "brown",
                "rust"
            ],
            "diameter_cm": [
                3,
                8
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "rust",
                "orange"
            ]
        },
        "stem": {
            "colors": [
                "orange",
                "rust"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "rust",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "autumn"
        ],
        "distribution": "Europe, N. America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "Ounce-for-ounce one of the most dangerous mushrooms: contains orellanine, which causes irreversible kidney failure with a delay of days to weeks. Rusty spores and an orange-brown cap.",
        "lookalikes": [
            {
                "name": "Many Cortinarius species",
                "distinguish": "Most webcaps are unsafe to eat; the genus is best avoided entirely."
            },
            {
                "name": "Cantharellus (chanterelle)",
                "distinguish": "Chanterelles are yellow with blunt False gills and a yellow spore print, not rusty."
            }
        ],
        "fun_fact": "Symptoms can appear up to 3 weeks later -- by then kidney damage is often permanent."
    },
    {
        "id": "lepiota-brunneoincarnata",
        "name": "Deadly Parasol",
        "scientific_name": "Lepiota brunneoincarnata",
        "aliases": [
            "browned parasol"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "umbonate"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                2,
                6
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "brown"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Europe, N. America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "Small, deadly Lepiota containing amatoxins, easily mistaken for an edible parasol or button mushroom. Brown scaly cap, a ring on the stem, and a bulbous base.",
        "lookalikes": [
            {
                "name": "Macrolepiota procera (parasol)",
                "distinguish": "True parasol is much larger (cap 10-25cm) with a shaggy brown-scaled cap and movable ring."
            },
            {
                "name": "Agaricus species (field/button mushrooms)",
                "distinguish": "Field mushrooms have pink-then-brown gills and a brown spore print; Lepiotas have white spores."
            }
        ],
        "fun_fact": "Several small Lepiota species are lethally poisonous despite looking like harmless fairy-ring mushrooms."
    },
    {
        "id": "galerina-autumnalis",
        "name": "Autumn Galerina",
        "scientific_name": "Galerina autumnalis",
        "aliases": [
            "deadly galerina"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan",
                "yellow-brown"
            ],
            "diameter_cm": [
                2,
                5
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "rust",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "yellowish"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "rust",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Amatoxin-containing little brown mushroom that grows on wood and is a classic fatal confusion with edible oysters and honey fungus. Rusty-brown spores and a ring on the stem.",
        "lookalikes": [
            {
                "name": "Pleurotus ostreatus (oyster mushroom)",
                "distinguish": "Oysters grow on wood too but have white decurrent gills and a white spore print, no ring."
            },
            {
                "name": "Armillaria mellea (honey fungus)",
                "distinguish": "Honey fungus has yellow-brown caps and a ring but whitish spore print and grows from a shared base."
            },
            {
                "name": "Kuehneromyces mutabilis",
                "distinguish": "Similar wood-loving brown mushroom with a ring; also best avoided by non-experts."
            }
        ],
        "fun_fact": "Its amatoxin load is so reliable that foragers use Galerina to test for amatoxins in new areas."
    },
    {
        "id": "kuehneromyces-mutabilis",
        "name": "Sheathed Woodtuft",
        "scientific_name": "Kuehneromyces mutabilis",
        "aliases": [
            "changing pholiota"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan",
                "yellow-brown"
            ],
            "diameter_cm": [
                2,
                6
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "tan",
                "rust"
            ]
        },
        "stem": {
            "colors": [
                "brown"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "rust",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Wood-growing brown mushroom with a ring, once eaten in parts of Europe but now widely considered toxic and a dangerous Galerina lookalike. Colour shifts from damp dark-brown to pale when dry.",
        "lookalikes": [
            {
                "name": "Galerina marginata (deadly galerina)",
                "distinguish": "Near-identical and amatoxin-deadly; the two are separated only by microscopy. Do not eat either without expert ID."
            },
            {
                "name": "Armillaria mellea (honey fungus)",
                "distinguish": "Honey fungus has a whitish spore print and lacks the strong ring of Kuehneromyces."
            }
        ],
        "fun_fact": "So similar to deadly Galerina that many guides simply say: if it grows on wood with a ring and rusty spores, leave it."
    },
    {
        "id": "entoloma-rhodopolium",
        "name": "Pinkgill",
        "scientific_name": "Entoloma rhodopolium",
        "aliases": [
            "wood pinkgill"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "grey",
                "brown",
                "tan"
            ],
            "diameter_cm": [
                3,
                9
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "pink",
                "salmon"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "grey"
            ]
        },
        "spore_print": "pink",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A grey-brown mushroom with pink gills and a pink spore print -- the hallmark of the Entoloma genus, many of which are poisonous. Causes severe gastrointestinal illness.",
        "lookalikes": [
            {
                "name": "Tricholoma species",
                "distinguish": "Some Tricholomas are edible but have white spores, not pink."
            },
            {
                "name": "Agaricus species",
                "distinguish": "Field mushrooms have brown spores and free gills, never pink."
            }
        ],
        "fun_fact": "The pink spore print is the single fastest way to rule a mushroom out of the 'safe edibles' group."
    },
    {
        "id": "hebeloma-crustuliniforme",
        "name": "Poison Pie",
        "scientific_name": "Hebeloma crustuliniforme",
        "aliases": [
            "snapping-turtle mushroom"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex"
            ],
            "colors": [
                "cream",
                "tan",
                "brown"
            ],
            "diameter_cm": [
                3,
                9
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "cream",
                "tan"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ]
        },
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Common mycorrhizal mushroom with a sticky pale cap and a mealy, radish-like smell. Poisonous, causing vomiting and diarrhea; a frequent accidental pickup by new foragers.",
        "lookalikes": [
            {
                "name": "Agaricus species (field/button mushrooms)",
                "distinguish": "Edible Agaricus have pink-then-brown gills and a brown spore print; Hebeloma gills stay pale and it smells of radish."
            },
            {
                "name": "Edible white fungi",
                "distinguish": "Many white gilled mushrooms are dangerous; the mealy odour is a Hebeloma clue."
            }
        ],
        "fun_fact": "Its Latin name means 'crust-like', a nod to the smooth, bun-like cap."
    },
    {
        "id": "tricholoma-equestre",
        "name": "Man-on-Horseback",
        "scientific_name": "Tricholoma equestre",
        "aliases": [
            "yellow tricholoma"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "yellow",
                "olive",
                "brown"
            ],
            "diameter_cm": [
                4,
                10
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "yellow",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "yellowish"
            ]
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Once considered a good edible, now linked to rhabdomyolysis (muscle breakdown) and at least one death when eaten repeatedly. Yellowish cap and yellow gills, growing under conifers.",
        "lookalikes": [
            {
                "name": "Cantharellus (chanterelle)",
                "distinguish": "Chanterelles are yellow but have blunt False gills and grow in moss/leaf litter, not with the white spores of Tricholoma."
            },
            {
                "name": "Tricholoma matsutake",
                "distinguish": "Matsutake is prizzed and edible but smells of cinnamon/spice; equestre smells faintly of flour."
            }
        ],
        "fun_fact": "A reminder that 'edible' can be conditional -- this one fails only after repeated meals."
    },
    {
        "id": "marasmius-oreades",
        "name": "Fairy Ring Mushroom",
        "scientific_name": "Marasmius oreades",
        "aliases": [
            "scotch bonnet"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat",
                "umbilicate"
            ],
            "colors": [
                "tan",
                "brown",
                "cream"
            ],
            "diameter_cm": [
                2,
                5
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "distant",
            "colors": [
                "cream",
                "tan"
            ]
        },
        "stem": {
            "colors": [
                "tan",
                "brown"
            ]
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Small, tough, fragrant mushroom that grows in rings on lawns and pastures -- the classic 'fairy ring'. A good edible with a nutty flavour, best dried. Must be well cooked.",
        "lookalikes": [
            {
                "name": "Clitocybe dealbata (ivory funnel)",
                "distinguish": "Deadly ivory funnel also forms rings in grass but has a mealy smell and is muscarine-poisonous."
            },
            {
                "name": "Agaricus campestris (field mushroom)",
                "distinguish": "Edible and also lawn-growing, but has pink-then-brown gills and a ring; no fairy-ring confusion risk since it is safe too."
            }
        ],
        "fun_fact": "The rings it forms can grow outward for decades -- some are centuries old."
    },
    {
        "id": "agaricus-arvensis",
        "name": "Horse Mushroom",
        "scientific_name": "Agaricus arvensis",
        "aliases": [
            "princess mushroom"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "cream",
                "tan"
            ],
            "diameter_cm": [
                8,
                20
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "pink",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A large, choice meadow Agaricus with a pleasant anise scent, closely related to the button mushroom. Flesh may yellow slightly when bruised. One of the best wild edibles.",
        "lookalikes": [
            {
                "name": "Agaricus xanthodermus (yellow stainer)",
                "distinguish": "Poisonous stainer also yellows but smells of phenol/ink; arvensis smells sweetly of anise."
            },
            {
                "name": "Amanita species",
                "distinguish": "Death caps can sit in grass too; Agaricus have brown spores and pink-then-brown gills, never a volva."
            }
        ],
        "fun_fact": "Its anise odour is the quick field test that separates it from the poisonous yellow stainer."
    },
    {
        "id": "pleurotus-eryngii",
        "name": "King Oyster",
        "scientific_name": "Pleurotus eryngii",
        "aliases": [
            "king trumpet",
            "eryngii"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan",
                "grey"
            ],
            "diameter_cm": [
                4,
                12
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "tan"
            ]
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn",
            "winter"
        ],
        "distribution": "Mediterranean, Europe, Asia",
        "regions": [
            "asia",
            "europe"
        ],
        "description": "Meaty, thick-stemmed oyster relative that grows on the roots of spiny shrubs (eryngo). Prized for its firm texture and umami flavour; widely cultivated.",
        "lookalikes": [
            {
                "name": "Pleurotus ostreatus (oyster mushroom)",
                "distinguish": "True oyster has a fan cap and the same edible status; eryngii is chunkier with a solid stem."
            },
            {
                "name": "Omphalotus (jack-o'-lantern)",
                "distinguish": "Jack-o'-lantern is poisonous and glows faintly in the dark; oysters do not."
            }
        ],
        "fun_fact": "The thick stem is the edible part most people throw away -- it is the best bit."
    },
    {
        "id": "craterellus-cornucopioides",
        "name": "Black Trumpet",
        "scientific_name": "Craterellus cornucopioides",
        "aliases": [
            "horn of plenty",
            "trumpet of death"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "funnel",
                "irregular"
            ],
            "colors": [
                "black",
                "dark grey",
                "brown"
            ],
            "diameter_cm": [
                2,
                7
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "distant",
            "colors": [
                "grey",
                "black"
            ]
        },
        "stem": {
            "colors": [
                "black",
                "grey"
            ]
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Fragrant, all-black funnel mushroom that hides in leaf litter and is easy to miss. Intensely flavoured, highly prizzed edible. No dangerous lookalikes share its combo of black colour and hollow funnel shape.",
        "lookalikes": [
            {
                "name": "Cantharellus (chanterelle)",
                "distinguish": "Chanterelles are yellow/orange; black trumpets are dark and have a smokier taste."
            },
            {
                "name": "Craterellus fallax (False black trumpet)",
                "distinguish": "Near-identical and also edible; the two are treated as interchangeable in the kitchen."
            }
        ],
        "fun_fact": "It is one of the few choice fungi with essentially no poisonous confusion -- a safe one to learn first."
    },
    {
        "id": "boletus-bicolor",
        "name": "Two-colored Bolete",
        "scientific_name": "Boletus bicolor",
        "aliases": [
            "red-cracked bolete"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex"
            ],
            "colors": [
                "red",
                "brown",
                "pink"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "crowded",
            "colors": [
                "yellow",
                "red"
            ]
        },
        "stem": {
            "colors": [
                "yellow",
                "red"
            ]
        },
        "spore_print": "olive",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "E. North America",
        "regions": [
            "north-america"
        ],
        "description": "Red-capped bolete with yellow pores that bruise blue. Edible and good when young, but the blue bruising must be told apart from the poisonous red-capped boletes.",
        "lookalikes": [
            {
                "name": "Boletus sensibilis",
                "distinguish": "Very similar and also blue-bruising but can cause illness; the two are hard to separate -- caution advised."
            },
            {
                "name": "Boletus satanas (devil's bolete)",
                "distinguish": "Devil's bolete is poisonous with a bulbous base and red pores on a fat stem; avoid all red-pored boletes when unsure."
            }
        ],
        "fun_fact": "The rule for boletes: red pores + blue bruising = be very careful; many are edible, some are not."
    },
    {
        "id": "suillus-americanus",
        "name": "American Slippery Jack",
        "scientific_name": "Suillus americanus",
        "aliases": [
            "chicken fat mushroom"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex"
            ],
            "colors": [
                "yellow",
                "brown",
                "tan"
            ],
            "diameter_cm": [
                4,
                10
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "crowded",
            "colors": [
                "yellow"
            ]
        },
        "stem": {
            "colors": [
                "yellow"
            ],
            "ring": True
        },
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "N. America (pine)",
        "regions": [
            "north-america"
        ],
        "description": "Slimy-capped, dotted-stemmed bolete under pines. Edible after the slimy cuticle and pore layer are removed; mild flavour. A safe, common beginner bolete.",
        "lookalikes": [
            {
                "name": "Suillus luteus (slippery jack)",
                "distinguish": "Nearly identical and also edible; americanus has dotted (not ring-only) stems and grows with eastern pines."
            },
            {
                "name": "Suillus spraguei (painted suillus)",
                "distinguish": "Red-scaled cap, also eastern pine + edible; the dotted stem on americanus separates them."
            }
        ],
        "fun_fact": "The slimy cap is the 'slippery' part -- peel it and the mushroom underneath is the meal."
    },
    {
        "id": "russula-brevipes",
        "name": "Short-stemmed Russula",
        "scientific_name": "Russula brevipes",
        "aliases": [
            "bread mushroom"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "cream",
                "tan"
            ],
            "diameter_cm": [
                5,
                20
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ]
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "N. America",
        "regions": [
            "north-america"
        ],
        "description": "Large, squat white Russula with a peppery taste raw (mild when cooked). Edible and common; the peppery bite is typical of many Russulas, most of which are at worst unpalatable, not deadly.",
        "lookalikes": [
            {
                "name": "Russula emetica (the sickener)",
                "distinguish": "The sickener is also white but intensely peppery and poisonous; brevipes is mild-to-moderate and edible cooked."
            },
            {
                "name": "Edible white fungi",
                "distinguish": "Its brittle flesh (snaps like chalk) is the Russula family trait -- useful but not enough alone to declare safe."
            }
        ],
        "fun_fact": "Underneath, this mushroom is sometimes parasitised into a 'lobster mushroom' by another fungus."
    },
    {
        "id": "armillaria-tabescens",
        "name": "Ringless Honey Fungus",
        "scientific_name": "Armillaria tabescens",
        "aliases": [
            "ringless honey mushroom"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan",
                "honey"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "tan"
            ],
            "ring": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": [
            "autumn"
        ],
        "distribution": "N. America, Europe, Asia",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Honey-coloured clustered mushroom like Honey Fungus but lacking the ring. Edible when cooked (the cause of many poisoning cases is eating it undercooked). Grows at the base of trees in big clumps.",
        "lookalikes": [
            {
                "name": "Armillaria mellea (honey fungus)",
                "distinguish": "The ringed cousin; both edible cooked, both confused with deadly Galerina on wood."
            },
            {
                "name": "Galerina marginata (deadly galerina)",
                "distinguish": "Rusty-spored and amatoxin-deadly; honey mushrooms have a white spore print -- check spores before eating."
            }
        ],
        "fun_fact": "Armillaria is the largest living organism on Earth -- a single clone in Oregon covers ~10 km2."
    },
    {
        "id": "psilocybe-semilanceata",
        "name": "Liberty Cap",
        "scientific_name": "Psilocybe semilanceata",
        "aliases": [
            "magic mushroom",
            "liberty cap"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "conical",
                "bell"
            ],
            "colors": [
                "brown",
                "tan",
                "cream"
            ],
            "diameter_cm": [
                1,
                2
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "purple-brown",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ]
        },
        "spore_print": "purple-brown",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "potency": "high",
        "description": "Small conical grassland mushroom containing psilocybin (a psychedelic). Legally restricted in many places and not food -- included here for education, not use. Bruises blue and has a distinct nipple on the cap.",
        "lookalikes": [
            {
                "name": "Panaeolus species",
                "distinguish": "Some Panaeolus are also psychoactive; many grassland little brown mushrooms are not -- microscopy is needed."
            },
            {
                "name": "Galerina marginata (deadly galerina)",
                "distinguish": "Rusty-spored and amatoxin-deadly; the danger of confusing the two is why ID here is expert-only."
            }
        ],
        "fun_fact": "One of the most widespread naturally occurring psychedelic mushrooms on the planet."
    },
    {
        "id": "ganoderma-lucidum",
        "name": "Reishi",
        "scientific_name": "Ganoderma lucidum",
        "aliases": [
            "lingzhi",
            "varnished conk"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "kidney",
                "shelf"
            ],
            "colors": [
                "red",
                "orange",
                "brown"
            ],
            "diameter_cm": [
                5,
                25
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "crowded",
            "colors": [
                "white",
                "tan"
            ]
        },
        "stem": {
            "colors": [
                "red",
                "brown"
            ]
        },
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide (temperate/tropical)",
        "regions": [
            "global"
        ],
        "description": "Glossy red-brown shelf fungus used in traditional medicine (usually as a tea/extract, not eaten). Too woody to eat but prizzed. Kidney-shaped cap with a lacquered sheen.",
        "lookalikes": [
            {
                "name": "Ganoderma tsugae",
                "distinguish": "Near-identical hemlock reishi, also medicinal; the two are used interchangeably."
            },
            {
                "name": "Trametes versicolor (turkey tail)",
                "distinguish": "Turkey tail is thinner, multicoloured, and inedible too; reishi is thicker with a shiny red coat."
            }
        ],
        "fun_fact": "Its Chinese name lingzhi means 'mushroom of immortality' -- valued for millennia as medicine."
    },
    {
        "id": "fistulina-hepatica",
        "name": "Beefsteak Fungus",
        "scientific_name": "Fistulina hepatica",
        "aliases": [
            "beefsteak mushroom",
            "ox tongue"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "shelf",
                "tongue"
            ],
            "colors": [
                "red",
                "brown",
                "pink"
            ],
            "diameter_cm": [
                5,
                25
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "crowded",
            "colors": [
                "pink",
                "red"
            ]
        },
        "stem": {
            "colors": [
                "red",
                "pink"
            ]
        },
        "spore_print": "pink",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Red, tongue-shaped bracket that bleeds a blood-red juice when cut and tastes faintly of beef. Edible and tangy; often grows on old oaks. Individual tubes (not a fused pore surface) are the giveaway.",
        "lookalikes": [
            {
                "name": "Ganoderma lucidum (reishi)",
                "distinguish": "Lacquered red-brown shelf, inedible/medicinal and never bleeds red juice when cut."
            },
            {
                "name": "Laetiporus sulphureus (chicken of the woods)",
                "distinguish": "Chicken of the woods is yellow and also edible; beefsteak is red and tongue-shaped."
            }
        ],
        "fun_fact": "Cut it and the juice really does look like blood -- hence 'beefsteak'."
    },
    {
        "id": "calocybe-gambosa",
        "name": "St George's Mushroom",
        "scientific_name": "Calocybe gambosa",
        "aliases": [
            "st george mushroom"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "cream",
                "tan"
            ],
            "diameter_cm": [
                4,
                12
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ]
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "spring"
        ],
        "distribution": "Europe, N. America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "Meaty, fragrant spring mushroom that appears around St George's Day (23 Apr). Choice edible with a strong floury smell. Grows in rings in grassy places.",
        "lookalikes": [
            {
                "name": "Clitocybe dealbata (ivory funnel)",
                "distinguish": "Deadly ivory funnel also rings in grass; St George's has a strong mealy/flour smell and white (not dangerously muscarine) profile -- but expert ID is essential."
            },
            {
                "name": "Marasmius oreades (fairy ring)",
                "distinguish": "Fairy ring is smaller, tougher, and less mealy; both can form rings."
            }
        ],
        "fun_fact": "Timed to St George's Day so reliably that foragers use the calendar as an ID clue."
    },
    {
        "id": "lactarius-piperatus",
        "name": "Peppery Milkcap",
        "scientific_name": "Lactarius piperatus",
        "aliases": [
            "pepper milkcap"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "convex",
                "flat",
                "umbilicate"
            ],
            "colors": [
                "white",
                "cream"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ]
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Pure white milkcap that exudes white latex and is ferociously peppery raw. Too acrid to eat for most, though some cultures salt-cure it. A classic 'beware' mushroom of the milkcap group.",
        "lookalikes": [
            {
                "name": "Lactarius deliciosus (saffron milkcap)",
                "distinguish": "Saffron milkcap is edible with orange milk and carrot-coloured stains; piperatus is white and searingly hot."
            },
            {
                "name": "Lactarius torminosus (woolly milkcap)",
                "distinguish": "Woolly milkcap is also inedible with a fuzzy cap edge; both are white and peppery."
            }
        ],
        "fun_fact": "The peppery burn is a defence chemical -- insects and mammals learn to leave milkcaps alone."
    },
    {
        "id": "chlorophyllum-brunneum",
        "name": "Shaggy Parasol",
        "scientific_name": "Chlorophyllum brunneum",
        "aliases": [
            "brown shaggy parasol"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "umbonate"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                8,
                25
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "white"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "N. America",
        "regions": [
            "north-america"
        ],
        "description": "Large parasol with a brown scaly cap, a movable ring, and a fat, often bulbous stem that bruises orange-yellow. Poisonous, causing severe GI upset -- easily confused with the edible True parasol.",
        "lookalikes": [
            {
                "name": "Macrolepiota procera (parasol)",
                "distinguish": "True parasol is edible with a slender, snake-skin stem; brunneum has a swollen stem that stains yellow."
            },
            {
                "name": "Chlorophyllum molybdites (green-spored parasol)",
                "distinguish": "Another poisonous parasol whose spores are green -- the key danger sign."
            }
        ],
        "fun_fact": "The bulbous, yellow-bruising stem is the trap: it looks like an edible parasol but is not."
    },
    {
        "id": "morchella-angusticeps",
        "name": "Black Morel",
        "scientific_name": "Morchella angusticeps",
        "aliases": [
            "eastern black morel"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "conical",
                "pitted"
            ],
            "colors": [
                "black",
                "dark brown",
                "grey"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "cream",
                "white"
            ]
        },
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "spring"
        ],
        "distribution": "E. North America",
        "regions": [
            "north-america"
        ],
        "description": "Prized black-capped morel of eastern North American springs. Top-tier edible with a deep, smoky flavour -- but MUST be cooked; raw morels are toxic. Honeycomb pits on a dark conical cap.",
        "lookalikes": [
            {
                "name": "Gyromitra esculenta (False morel)",
                "distinguish": "False morel has a lobed, brain-like cap, not honeycomb pits, and is deadly."
            },
            {
                "name": "Verpa bohemica (early morel)",
                "distinguish": "Verpa's cap hangs free like a thimble; True morels have a continuous pitted cap."
            }
        ],
        "fun_fact": "Morel hunters guard their spring spots like state secrets -- the best ones are never shared."
    },
    {
        "id": "tuber-aestivum",
        "name": "Summer Truffle",
        "scientific_name": "Tuber aestivum",
        "aliases": [
            "burgundy truffle"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "round",
                "lumpy"
            ],
            "colors": [
                "black",
                "brown"
            ],
            "diameter_cm": [
                2,
                7
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "black",
                "brown"
            ]
        },
        "spore_print": "n/a",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, N. Africa, Middle East",
        "regions": [
            "africa",
            "europe"
        ],
        "description": "Subterranean, aromatic truffle with a black warty skin and a pale marbled interior. Highly prizzed edible, hunted with trained dogs or pigs. Found by smell, not sight, under hardwoods.",
        "lookalikes": [
            {
                "name": "Tuber melanosporum (black truffle)",
                "distinguish": "The prizzed Perigord truffle, near-identical and also choice; aestivum is milder and ripens in summer."
            },
            {
                "name": "Deer truffle (Elaphomyces)",
                "distinguish": "A common False truffle that is inedible and lacks the aromatic interior."
            }
        ],
        "fun_fact": "Truffles have no cap, gills, or stem -- they are the underground fruit of a fungus, more like a potato than a mushroom."
    },
    {
        "id": "hericium-coralloides",
        "name": "Coral Tooth Fungus",
        "scientific_name": "Hericium coralloides",
        "aliases": [
            "comb tooth",
            "coral hericium"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "coral",
                "toothed"
            ],
            "colors": [
                "white",
                "cream"
            ],
            "diameter_cm": [
                5,
                30
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white"
            ]
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Cascading white mass of fine hanging teeth, like a frozen waterfall. Choice edible with a seafood-like flavour, closely related to Lion's Mane. Grows on dead hardwoods.",
        "lookalikes": [
            {
                "name": "Hericium erinaceus (lion's mane)",
                "distinguish": "Lion's mane has longer, shaggier single clusters; both are choice and nearly interchangeable in the kitchen."
            },
            {
                "name": "Artomyces pyxidatus (crown-tipped coral)",
                "distinguish": "Branched coral with little crown-tipped ends; edible but less choice than Hericium. Confusion is harmless."
            }
        ],
        "fun_fact": "All three Hericium species are edible -- a rare group where every member is a good meal."
    },
    {
        "id": "agrocybe-aegerita",
        "name": "Poplar Mushroom",
        "scientific_name": "Agrocybe aegerita",
        "aliases": [
            "agrocybe cylindracea",
            "black poplar mushroom"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                4,
                12
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "clay",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "tan"
            ],
            "ring": True
        },
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Brown capped mushroom in clusters on poplar and other hardwoods. Edible with a mild, pleasant flavour; widely cultivated in Asia (where it is called yanagi-matsutake).",
        "lookalikes": [
            {
                "name": "Kuehneromyces mutabilis",
                "distinguish": "Also wood-clustered and ringed but rusty-spored and best avoided; Agrocybe has a brown spore print."
            },
            {
                "name": "Galerina marginata (deadly galerina)",
                "distinguish": "Amatoxin-deadly and wood-loving; check the spore print (brown, not rusty) before any ID."
            }
        ],
        "fun_fact": "It is one of the few wild mushrooms successfully farmed at scale outside the usual button/oyster/shiitake trio."
    },
    {
        "id": "psilocybe-cyanescens",
        "name": "Wavy Cap",
        "scientific_name": "Psilocybe cyanescens",
        "aliases": [
            "cyans",
            "wavy cap"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "wavy"
            ],
            "colors": [
                "brown",
                "caramel",
                "tan"
            ],
            "diameter_cm": [
                1,
                4
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "purple",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "blue"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "urban",
        "substrate": "woodchips",
        "ecology": "saprotrophic",
        "season": [
            "autumn",
            "winter"
        ],
        "distribution": "Pacific Northwest (native), introduced to Europe with wood mulch",
        "regions": [
            "europe",
            "north-america"
        ],
        "potency": "high",
        "description": "Contains psilocybin and psilocin and is a controlled hallucinogen in most jurisdictions. Wavy caramel-brown caps with a distinctive wavy margin, growing in dense troops on wood chip mulch in parks and gardens. Bruises deep blue when handled. Listed here for education and harm reduction only -- not recommended or legal in many places.",
        "lookalikes": [
            {
                "name": "Galerina marginata",
                "distinguish": "DEADLY; also grows on wood/mulch but has rusty-brown spores and no blue bruising."
            },
            {
                "name": "Psilocybe azurescens",
                "distinguish": "Even more potent relative with a more pointed cap; similar bluing reaction."
            }
        ],
        "fun_fact": "It has spread widely outside its native Pacific Northwest range by hitchhiking in commercial wood-chip mulch."
    },
    {
        "id": "psilocybe-azurescens",
        "name": "Flying Saucer Mushroom",
        "scientific_name": "Psilocybe azurescens",
        "aliases": [
            "azzies",
            "flying saucers"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "conical"
            ],
            "colors": [
                "caramel",
                "brown",
                "gold"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "purple",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "blue"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "coastal dunes",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn",
            "winter"
        ],
        "distribution": "Pacific coast of Oregon and Washington, USA",
        "regions": [
            "north-america"
        ],
        "potency": "high",
        "description": "Contains one of the highest psilocybin concentrations of any known mushroom, making it a controlled and potent hallucinogen. Caramel-colored, caramel-to-chestnut caps growing in sandy soil among dune grasses and beach wood debris; bruises blue. Listed here for education and harm reduction only -- not recommended or legal in many places.",
        "lookalikes": [
            {
                "name": "Psilocybe cyanescens",
                "distinguish": "Close relative, less potent, prefers wood mulch inland rather than coastal dune sand."
            },
            {
                "name": "Galerina marginata",
                "distinguish": "DEADLY amatoxin-containing lookalike; check for rusty-brown (not purple-brown) spores."
            }
        ],
        "fun_fact": "Its native range is a narrow strip of Pacific coastline, but its spores are so hardy the species has since established in parts of Europe."
    },
    {
        "id": "psilocybe-mexicana",
        "name": "Mexican Liberty Cap",
        "scientific_name": "Psilocybe mexicana",
        "aliases": [
            "teonanacatl",
            "pajaritos"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "conical",
                "bell"
            ],
            "colors": [
                "brown",
                "tan",
                "cream"
            ],
            "diameter_cm": [
                1,
                3
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "close",
            "colors": [
                "purple",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "cream",
                "blue"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "grassland",
        "substrate": "soil",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Mexico and Central America",
        "regions": [
            "north-america"
        ],
        "potency": "low",
        "description": "Contains psilocybin and psilocin; the species used ceremonially by Mesoamerican cultures under the Nahuatl name teonanacatl (\"flesh of the gods\") and the mushroom Albert Hofmann first isolated psilocybin from. Small, slender, tan-brown caps growing in grassy, disturbed soil at higher elevations. Listed here for education and harm reduction only -- possession is illegal in most countries.",
        "lookalikes": [
            {
                "name": "Panaeolus species",
                "distinguish": "Similar size and habitat; mottled gill color and different spore surface texture under a scope."
            },
            {
                "name": "Conocybe species",
                "distinguish": "Some are deadly amatoxin-containing lookalikes; rusty-brown spore print differs from purple-brown."
            }
        ],
        "fun_fact": "This is the species Swiss chemist Albert Hofmann used in 1958 to first isolate and name psilocybin and psilocin."
    },
    {
        "id": "psilocybe-tampanensis",
        "name": "Philosopher's Stone",
        "scientific_name": "Psilocybe tampanensis",
        "aliases": [
            "philosopher's stones",
            "magic truffle"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "bell"
            ],
            "colors": [
                "brown",
                "caramel",
                "tan"
            ],
            "diameter_cm": [
                1,
                3
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "close",
            "colors": [
                "purple",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "cream",
                "blue"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "grassland",
        "substrate": "sandy soil",
        "ecology": "saprotrophic",
        "season": [
            "autumn"
        ],
        "distribution": "Originally found near Tampa, Florida, USA; now cultivated worldwide",
        "regions": [
            "global",
            "north-america"
        ],
        "potency": "moderate",
        "description": "Contains psilocybin and psilocin; famous for producing 'magic truffles' (sclerotia) -- hardened underground masses of mycelium that store the same compounds as the mushroom and are sold legally as truffles in some countries (e.g. the Netherlands) even where the mushroom itself is controlled. Listed here for education and harm reduction only.",
        "lookalikes": [
            {
                "name": "Psilocybe mexicana",
                "distinguish": "Close relative and also produces sclerotia; near-identical mushroom stage, distinguished mainly by spore/genetic data."
            }
        ],
        "fun_fact": "Only one wild collection of this species has ever been documented -- nearly all specimens today descend from sclerotia cultivated from that single 1977 Florida find."
    },
    {
        "id": "psilocybe-caerulescens",
        "name": "Landslide Mushroom",
        "scientific_name": "Psilocybe caerulescens",
        "aliases": [
            "derrumbe",
            "landslide mushroom"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "caramel",
                "orange"
            ],
            "diameter_cm": [
                2,
                6
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "close",
            "colors": [
                "purple",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "cream",
                "blue"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "roadside embankments",
        "substrate": "soil",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Mexico and Central America",
        "regions": [
            "north-america"
        ],
        "potency": "moderate",
        "description": "Contains psilocybin and is another of the traditional 'teonanacatl' mushrooms used ceremonially in Mexico, notably by Mazatec curandera Maria Sabina. Grows on eroded soil of landslides, banks, and roadcuts, bruising blue when handled. Listed here for education and harm reduction only -- not recommended or legal in many places.",
        "lookalikes": [
            {
                "name": "Psilocybe mexicana",
                "distinguish": "Similar habitat and use; smaller stature and slightly different cap coloration."
            },
            {
                "name": "Galerina species",
                "distinguish": "Some are deadly; check for the purple-brown (not rusty) spore print."
            }
        ],
        "fun_fact": "It was one of the sacred mushrooms shown to R. Gordon Wasson by Maria Sabina in the 1950s, sparking Western scientific interest in psilocybin mushrooms."
    },
    {
        "id": "psilocybe-baeocystis",
        "name": "Bottle Cap",
        "scientific_name": "Psilocybe baeocystis",
        "aliases": [
            "knobby tops",
            "bottle caps"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "bell"
            ],
            "colors": [
                "brown",
                "olive",
                "chestnut"
            ],
            "diameter_cm": [
                1,
                4
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "close",
            "colors": [
                "purple",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "cream",
                "blue"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "forest edge",
        "substrate": "woodchips",
        "ecology": "saprotrophic",
        "season": [
            "autumn"
        ],
        "distribution": "Pacific Northwest, USA",
        "regions": [
            "north-america"
        ],
        "potency": "high",
        "description": "Contains psilocybin, psilocin, and baeocystin, an alkaloid first identified in this species and named after it. Olive-brown, umbonate caps that bruise blue, found on mulch and wood debris. Listed here for education and harm reduction only -- not recommended or legal in many places.",
        "lookalikes": [
            {
                "name": "Psilocybe cyanescens",
                "distinguish": "Overlapping range and habitat; P. cyanescens has a more strongly wavy cap margin."
            },
            {
                "name": "Galerina marginata",
                "distinguish": "DEADLY; check for rusty-brown (not purple-brown) spore print before any ID."
            }
        ],
        "fun_fact": "The minor alkaloid baeocystin was first isolated from this species and takes its name from it."
    },
    {
        "id": "panaeolus-cyanescens",
        "name": "Blue Meanies",
        "scientific_name": "Panaeolus cyanescens",
        "aliases": [
            "blue meanies",
            "copelandia cyanescens"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "bell"
            ],
            "colors": [
                "gray",
                "cream",
                "white"
            ],
            "diameter_cm": [
                1,
                4
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "close",
            "colors": [
                "gray",
                "black",
                "mottled"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "blue"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "black",
        "habitat": "grassland",
        "substrate": "dung",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Pantropical; also found in warm temperate regions",
        "regions": [
            "africa",
            "asia",
            "oceania",
            "south-america"
        ],
        "potency": "high",
        "description": "Contains high levels of psilocybin and psilocin, among the most potent of the dung-loving hallucinogenic mushrooms, sometimes classified in the genus Copelandia. Pale gray-white cap, mottled black gills, and a black spore print; stains blue readily when bruised. Listed here for education and harm reduction only -- not recommended or legal in many places.",
        "lookalikes": [
            {
                "name": "Panaeolus species (non-psychoactive)",
                "distinguish": "Several close Panaeolus relatives lack psilocybin; microscopy and bruising reaction are needed to tell them apart."
            },
            {
                "name": "Psilocybe cubensis",
                "distinguish": "Also dung-loving and blues, but has a purple-brown spore print rather than black."
            }
        ],
        "fun_fact": "It is considered one of the most potent psilocybin mushrooms by weight, and has historically been classified under the separate genus Copelandia before molecular work folded it back into Panaeolus."
    },
    {
        "id": "gymnopilus-junonius",
        "name": "Laughing Gym",
        "scientific_name": "Gymnopilus junonius",
        "aliases": [
            "big laughing gym",
            "spectacular rustgill"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "orange",
                "gold",
                "rust"
            ],
            "diameter_cm": [
                5,
                20
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "orange",
                "rust",
                "yellow"
            ]
        },
        "stem": {
            "colors": [
                "yellow",
                "orange"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "rusty-orange",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn"
        ],
        "distribution": "Widespread in temperate regions worldwide",
        "regions": [
            "global"
        ],
        "potency": "low",
        "description": "A large, showy, bright orange mushroom that grows in dense clusters at the base of trees and stumps. Some populations of Gymnopilus contain low, variable levels of psilocybin and have a folk reputation for causing giddy, 'laughing' intoxication if eaten, though potency is unreliable and it also causes gastrointestinal upset. Not recommended for consumption.",
        "lookalikes": [
            {
                "name": "Galerina marginata",
                "distinguish": "DEADLY; smaller and duller than Gymnopilus junonius but shares a rusty spore print and woody habitat."
            },
            {
                "name": "Armillaria mellea (honey mushroom)",
                "distinguish": "Also grows in clusters at tree bases; honey mushroom has a white spore print, not rusty-orange."
            }
        ],
        "fun_fact": "Its common name, 'big laughing gym', comes from old reports of hilarity and altered mood after ingestion, though the psilocybin content varies wildly between collections."
    },
    {
        "id": "inocybe-erubescens",
        "name": "Deadly Fibrecap",
        "scientific_name": "Inocybe erubescens",
        "aliases": [
            "inosperma erubescens",
            "red-staining inocybe"
        ],
        "edibility": "deadly",
        "cap": {
            "shape": [
                "conical",
                "bell"
            ],
            "colors": [
                "cream",
                "pink",
                "red"
            ],
            "diameter_cm": [
                3,
                8
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "close",
            "colors": [
                "cream",
                "pink",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "pink"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "soil",
        "ecology": "mycorrhizal",
        "season": [
            "spring",
            "summer"
        ],
        "distribution": "Europe, in calcareous beech and lime woodland",
        "regions": [
            "europe"
        ],
        "description": "A pale, fibrous-capped mushroom that reddens or bruises pinkish-red with age and handling. Contains high levels of muscarine and is one of the most dangerous Inocybe species -- ingestion causes severe muscarinic poisoning (excessive sweating, salivation, blurred vision) that can be fatal without prompt atropine treatment.",
        "lookalikes": [
            {
                "name": "Calocybe gambosa (St. George's mushroom)",
                "distinguish": "Also fruits in spring in similar woodland but has a white spore print and no reddening/pinkish bruising."
            },
            {
                "name": "Other Inocybe species",
                "distinguish": "Most Inocybe species are also toxic to some degree; the whole genus is best avoided entirely."
            }
        ],
        "fun_fact": "Its reddening flesh gives it the alternate name 'red-staining inocybe' and is one of the clues used to separate it from edible spring mushrooms it can be mistaken for."
    },
    {
        "id": "clitocybe-nuda",
        "name": "Wood Blewit",
        "scientific_name": "Clitocybe nuda",
        "aliases": [
            "blewit",
            "lepista nuda"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "purple",
                "lilac",
                "brown"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "purple",
                "lilac"
            ]
        },
        "stem": {
            "colors": [
                "purple",
                "lilac"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "pinkish-cream",
        "habitat": "forest",
        "substrate": "leaf litter",
        "ecology": "saprotrophic",
        "season": [
            "autumn",
            "winter"
        ],
        "distribution": "Widespread in Europe and North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A striking violet-to-lilac mushroom found in leaf litter and compost piles in autumn. Edible and popular in Europe, but must be well cooked (raw or undercooked specimens can cause gastrointestinal upset) and correctly distinguished from purple Cortinarius species.",
        "lookalikes": [
            {
                "name": "Cortinarius species",
                "distinguish": "Some purple Cortinarius are toxic; Cortinarius has a rusty-brown spore print and a cobweb-like partial veil, unlike the pinkish-cream spores of blewit."
            },
            {
                "name": "Mycena pura",
                "distinguish": "Smaller, thinner, radish-scented purple mushroom, mildly toxic; blewit is much larger and meatier."
            }
        ],
        "fun_fact": "The name 'blewit' comes from its blue-violet coloring, and it was historically often sold in British markets alongside cultivated button mushrooms."
    },
    {
        "id": "pholiota-squarrosa",
        "name": "Shaggy Scalycap",
        "scientific_name": "Pholiota squarrosa",
        "aliases": [
            "shaggy pholiota"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "bell"
            ],
            "colors": [
                "yellow",
                "tan",
                "brown"
            ],
            "diameter_cm": [
                3,
                12
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "close",
            "colors": [
                "yellow",
                "brown",
                "rust"
            ]
        },
        "stem": {
            "colors": [
                "yellow",
                "brown"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "autumn"
        ],
        "distribution": "Widespread in temperate Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "Densely shaggy, upturned scales cover the yellow-brown cap and stem of this dense, clustering wood-rotter. Once considered edible, it is now regarded as poisonous by many authorities, especially in combination with alcohol, and causes gastrointestinal upset.",
        "lookalikes": [
            {
                "name": "Armillaria mellea (honey mushroom)",
                "distinguish": "Also grows in dense clusters at tree bases; honey mushroom lacks the shaggy upturned scales and has a white spore print."
            },
            {
                "name": "Pholiota species (edible)",
                "distinguish": "Other Pholiota can be edible but require careful microscopy; best avoided as a genus for beginners."
            }
        ],
        "fun_fact": "Its rough, shaggy cap scales resemble roof shingles and give the whole genus the common name 'scalycap'."
    },
    {
        "id": "mycena-haematopus",
        "name": "Bleeding Fairy Helmet",
        "scientific_name": "Mycena haematopus",
        "aliases": [
            "bleeding mycena",
            "burgundydrop bonnet"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "conical",
                "bell"
            ],
            "colors": [
                "red",
                "brown",
                "pink"
            ],
            "diameter_cm": [
                1,
                3
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "close",
            "colors": [
                "pink",
                "white"
            ]
        },
        "stem": {
            "colors": [
                "red",
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Widespread in Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A small, delicate reddish-brown mushroom found in clusters on rotting hardwood logs. Named for the dark red-purple latex ('blood') that oozes when the stem is cut or broken. Too small and insubstantial to be worth eating.",
        "lookalikes": [
            {
                "name": "Mycena sanguinolenta",
                "distinguish": "Also bleeds red latex but is smaller and grows on needle litter rather than wood."
            },
            {
                "name": "Other Mycena species",
                "distinguish": "Many small Mycena look similar; the bleeding reaction when cut is the key diagnostic feature."
            }
        ],
        "fun_fact": "The red 'blood' it exudes is a defining field character shared by only a handful of the hundreds of Mycena species."
    },
    {
        "id": "coprinellus-micaceus",
        "name": "Mica Cap",
        "scientific_name": "Coprinellus micaceus",
        "aliases": [
            "glistening inkcap",
            "mica inkcap"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "conical",
                "bell"
            ],
            "colors": [
                "tan",
                "brown",
                "orange"
            ],
            "diameter_cm": [
                2,
                5
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "cream",
                "brown",
                "black"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "black",
        "habitat": "urban",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide, common in cities and gardens",
        "regions": [
            "global"
        ],
        "description": "A common, tightly clustered mushroom that grows explosively from buried wood and stumps, often right through pavement cracks. Named for the glistening mica-like granules that dust the young cap. Edible when young and fresh, but like other inkcaps it dissolves into black liquid ('deliquesces') within hours as it ages.",
        "lookalikes": [
            {
                "name": "Coprinus comatus (shaggy mane)",
                "distinguish": "Much larger, shaggy white cylindrical cap; mica cap is smaller and tan-brown."
            },
            {
                "name": "Coprinopsis atramentaria (tippler's bane)",
                "distinguish": "Similar clustering habit but causes severe reaction with alcohol; mica cap does not have this effect."
            }
        ],
        "fun_fact": "Its glistening cap surface, caused by tiny mineral-like veil remnants, dissolves with the first rain or touch, giving the species its name."
    },
    {
        "id": "xerula-radicata",
        "name": "Rooting Shank",
        "scientific_name": "Xerula radicata",
        "aliases": [
            "oudemansiella radicata",
            "rooted collybia"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan",
                "olive"
            ],
            "diameter_cm": [
                3,
                8
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "distant",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "buried wood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Widespread in Europe and North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A slender mushroom with a wrinkled, greasy brown cap and a long, deeply rooting stem that tapers underground to buried wood or roots -- the root can be as long as the visible mushroom itself. Edible but thin-fleshed and not highly regarded.",
        "lookalikes": [
            {
                "name": "Xerula furfuracea",
                "distinguish": "Very similar rooting species with a slightly scurfy stem; distinguishing them reliably needs microscopy."
            },
            {
                "name": "Armillaria species",
                "distinguish": "Also wood-associated but grow in dense clusters without a single deep taproot-like base."
            }
        ],
        "fun_fact": "Digging up the entire rooting stem intact can require excavating 10+ cm of soil to reach the buried wood it's attached to."
    },
    {
        "id": "agaricus-augustus",
        "name": "The Prince",
        "scientific_name": "Agaricus augustus",
        "aliases": [
            "the prince"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "gold",
                "tan"
            ],
            "diameter_cm": [
                10,
                25
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "pink",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "forest edge",
        "substrate": "soil",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Widespread in Europe and North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A large, robust Agaricus with a golden-brown, scaly cap and a pleasant almond-like smell. One of the most prized wild Agaricus species for the table, with firm flesh and rich flavor superior to the common button mushroom.",
        "lookalikes": [
            {
                "name": "Agaricus xanthodermus (yellow stainer)",
                "distinguish": "Toxic lookalike that stains bright chrome-yellow at the stem base and smells of ink/phenol rather than almond."
            },
            {
                "name": "Amanita species",
                "distinguish": "Always check for free gills, a ring, and a brown spore print (not white) to rule out deadly Amanita."
            }
        ],
        "fun_fact": "Its pleasant almond or marzipan scent is one of the most reliable field clues that separate it from its poisonous, chemical-smelling relative the yellow stainer."
    },
    {
        "id": "boletus-luridiformis",
        "name": "Scarletina Bolete",
        "scientific_name": "Boletus luridiformis",
        "aliases": [
            "neoboletus erythropus",
            "dotted stem bolete"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex"
            ],
            "colors": [
                "brown",
                "olive",
                "orange"
            ],
            "diameter_cm": [
                6,
                20
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "close",
            "colors": [
                "orange",
                "red"
            ]
        },
        "stem": {
            "colors": [
                "yellow",
                "red"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "soil",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, in both coniferous and broadleaf woodland",
        "regions": [
            "europe"
        ],
        "description": "A stout bolete with an olive-brown cap, orange-red pores, and a yellow stem covered in small red dots. All cut or bruised surfaces instantly turn dark blue. Edible and popular once cooked, but must never be eaten raw -- it causes gastrointestinal upset uncooked.",
        "lookalikes": [
            {
                "name": "Boletus satanas (Satan's bolete)",
                "distinguish": "Also blues and has red pores but has a pale, whitish-gray cap rather than olive-brown, and is toxic."
            },
            {
                "name": "Boletus edulis (porcini)",
                "distinguish": "Does not blue when cut and has white-to-yellow pores rather than orange-red."
            }
        ],
        "fun_fact": "The instant, dramatic blue-black bruising of its flesh is one of the fastest color-change reactions of any bolete."
    },
    {
        "id": "amanita-pantherina",
        "name": "Panther Cap",
        "scientific_name": "Amanita pantherina",
        "aliases": [
            "panther amanita"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                5,
                12
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "close",
            "colors": [
                "white"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": True,
            "volva": True
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "soil",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, temperate Asia",
        "regions": [
            "asia",
            "europe"
        ],
        "description": "A brown-capped Amanita covered in small white warts, closely related to fly agaric and sharing its ibotenic acid/muscimol toxin profile. Causes serious neurotoxic poisoning -- confusion, delirium, and potential coma -- and has caused fatalities, especially when confused with edible brown-capped mushrooms.",
        "lookalikes": [
            {
                "name": "Amanita muscaria (fly agaric)",
                "distinguish": "Usually red or orange-capped rather than brown, though pale forms overlap; both share ibotenic acid toxicity."
            },
            {
                "name": "Amanita rubescens (blusher)",
                "distinguish": "Edible when cooked; flesh reddens/blushes when cut, unlike panther cap, and has a less prominent basal cup."
            }
        ],
        "fun_fact": "Despite the danger, its neurotoxins produce a distinctly different, more sedative intoxication than psilocybin mushrooms and it has a long history of recreational misuse in parts of Europe."
    },
    {
        "id": "cortinarius-violaceus",
        "name": "Violet Webcap",
        "scientific_name": "Cortinarius violaceus",
        "aliases": [
            "violet cort"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex"
            ],
            "colors": [
                "purple",
                "violet"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "distant",
            "colors": [
                "purple",
                "rust"
            ]
        },
        "stem": {
            "colors": [
                "purple"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "rusty-brown",
        "habitat": "forest",
        "substrate": "soil",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere conifer and birch forests",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A strikingly deep violet-purple mushroom covered in fine velvety scales, from cap to gills to stem. Technically edible and non-toxic, but its beauty and slow growth mean it is rarely collected for the table and is better appreciated in the woods.",
        "lookalikes": [
            {
                "name": "Cortinarius rubellus (deadly webcap)",
                "distinguish": "DEADLY; orange-brown rather than violet, and causes fatal kidney failure -- always double-check any purple Cortinarius under this genus's broad toxic reputation."
            },
            {
                "name": "Lepista nuda (wood blewit)",
                "distinguish": "Also purple but has a pinkish-cream (not rusty-brown) spore print and lacks the cobweb-like cortina veil."
            }
        ],
        "fun_fact": "Its intense violet color comes from pigments so striking that entire mushroom-hunting trips have been organized around finding it, even though it's rarely eaten."
    },
    {
        "id": "russula-virescens",
        "name": "Green-Cracking Russula",
        "scientific_name": "Russula virescens",
        "aliases": [
            "quilted green russula",
            "green brittlegill"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "green"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "close",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "soil",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, North America, Asia",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A distinctive mottled green Russula with a cracked, quilted-looking cap surface, easy to identify among the notoriously difficult Russula genus. One of the few Russulas widely considered a choice, safe edible.",
        "lookalikes": [
            {
                "name": "Amanita phalloides (death cap)",
                "distinguish": "DEADLY; can appear greenish but has free gills, a ring, and a volva at the base, none of which Russula virescens has."
            },
            {
                "name": "Other green Russula species",
                "distinguish": "Some greenish Russulas are mildly toxic; the cracked, patchwork cap texture is the key ID feature for this species."
            }
        ],
        "fun_fact": "Its cracked, jigsaw-puzzle cap pattern is unique enough among green mushrooms that it helps rule out confusion with the deadly death cap, which has a smooth cap."
    },
    {
        "id": "polyporus-squamosus",
        "name": "Dryad's Saddle",
        "scientific_name": "Polyporus squamosus",
        "aliases": [
            "pheasant back mushroom",
            "cerioporus squamosus"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "fan",
                "flat"
            ],
            "colors": [
                "tan",
                "brown",
                "cream"
            ],
            "diameter_cm": [
                10,
                40
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "close",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "black"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer"
        ],
        "distribution": "Widespread in Northern Hemisphere",
        "regions": [
            "asia",
            "europe",
            "north-america"
        ],
        "description": "A large shelf-forming polypore with tan feather-like scales resembling a pheasant's back, and a smell often compared to watermelon rind. Edible when young and tender, becoming tough and woody with age; best sliced thin and cooked.",
        "lookalikes": [
            {
                "name": "Polyporus tuberaster",
                "distinguish": "Similar scaly bracket but smaller and grows from a hard underground sclerotium; overall much less common."
            },
            {
                "name": "Cerioporus mori",
                "distinguish": "Similar honeycombed cap texture; typically smaller pore size distinguishes it under magnification."
            }
        ],
        "fun_fact": "Its common name 'pheasant back' comes from the feathered, scaly pattern on its cap, which closely resembles pheasant plumage."
    },
    {
        "id": "lycoperdon-pyriforme",
        "name": "Pear-Shaped Puffball",
        "scientific_name": "Lycoperdon pyriforme",
        "aliases": [
            "apioperdon pyriforme",
            "stump puffball"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "round"
            ],
            "colors": [
                "white",
                "tan",
                "brown"
            ],
            "diameter_cm": [
                1,
                4
            ]
        },
        "gills": {
            "attachment": "none",
            "spacing": "none",
            "colors": []
        },
        "stem": {
            "colors": [
                "white",
                "tan"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "olive-brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn",
            "winter"
        ],
        "distribution": "Worldwide on rotting wood",
        "regions": [
            "global"
        ],
        "description": "A small, pear-shaped puffball that grows in large clustered troops directly on decaying logs and stumps -- the only common puffball that fruits on wood rather than soil. Edible while the internal flesh is still pure white and firm throughout.",
        "lookalikes": [
            {
                "name": "Scleroderma citrinum (common earthball)",
                "distinguish": "Toxic; earthball has a thick, tough rind and dark purple-black spore mass, unlike the thin skin and pale flesh of pear puffball."
            },
            {
                "name": "Young Amanita eggs",
                "distinguish": "DEADLY if mistaken; always slice puffballs in half to confirm uniform white flesh with no mushroom outline inside."
            }
        ],
        "fun_fact": "It is the only widespread puffball species that grows specifically on wood rather than in soil, making substrate alone a useful first clue to its identity."
    },
    {
        "id": "tremella-mesenterica",
        "name": "Witch's Butter",
        "scientific_name": "Tremella mesenterica",
        "aliases": [
            "yellow brain",
            "golden jelly fungus"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "irregular"
            ],
            "colors": [
                "yellow",
                "orange"
            ],
            "diameter_cm": [
                2,
                8
            ]
        },
        "gills": {
            "attachment": "none",
            "spacing": "none",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": [
            "autumn",
            "winter",
            "spring"
        ],
        "distribution": "Worldwide on hardwood branches",
        "regions": [
            "global"
        ],
        "description": "A brain-like, gelatinous yellow-orange fungus that swells up plump and jelly-like after rain and shrivels to a hard orange flake in dry weather. It is actually a mycoparasite, feeding on other wood-decay fungi within the branch rather than the wood itself. Edible but flavorless, used mainly for texture in soups.",
        "lookalikes": [
            {
                "name": "Dacrymyces chrysospermus (orange jelly)",
                "distinguish": "Similar orange gelatinous blob on conifer wood rather than hardwood; smaller and firmer overall."
            },
            {
                "name": "Tremella aurantia",
                "distinguish": "Nearly identical yellow jelly fungus that specifically parasitizes Stereum hirsutum rather than other Tremella hosts."
            }
        ],
        "fun_fact": "It isn't decomposing the wood it grows on at all -- it's actually parasitizing other crust fungi living inside the branch, making it a fungus that eats fungus."
    },
    {
        "id": "agaricus-silvicola",
        "name": "Wood Mushroom",
        "scientific_name": "Agaricus silvicola",
        "aliases": [
            "silvicola",
            "alder wood mushroom"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "white",
                "cream",
                "tan"
            ],
            "diameter_cm": [
                5,
                12
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "pink",
                "brown",
                "chocolate"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "forest",
        "substrate": "litter",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere woodlands",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A pale, mild woodland Agaricus with a smooth cream cap and pink-then-chocolate gills. A good edible, milder than the shop button mushroom, but only foragers who can rule out the yellow-staining toxic lookalikes.",
        "lookalikes": [
            {
                "name": "Agaricus xanthodermus (yellow stainer)",
                "distinguish": "Bruises bright yellow at the base and smells of phenol/ink; poisonous -- the key danger to exclude."
            },
            {
                "name": "Agaricus arvensis (horse mushroom)",
                "distinguish": "Larger, grows in grassland rather than woods; also edible."
            }
        ],
        "fun_fact": "Closely related to the cultivated button mushroom but picked from the forest floor."
    },
    {
        "id": "agaricus-subrufescens",
        "name": "Almond Mushroom",
        "scientific_name": "Agaricus subrufescens",
        "aliases": [
            "almond portobello",
            "agaricus blazei",
            "himematsutake"
        ],
        "edibility": "choice",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "pink",
                "brown"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "brown",
        "habitat": "cultivated",
        "substrate": "soil",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Cultivated worldwide; native to Brazil/USA",
        "regions": [
            "global"
        ],
        "description": "A meaty, almond-scented Agaricus grown commercially for both eating and traditional medicine (popular in Brazil and Japan as 'Himematsutake'). Mild, nutty, and a reliable choice edible.",
        "lookalikes": [
            {
                "name": "Agaricus bisporus (button/portobello)",
                "distinguish": "Nearly identical cultivated cousin; both edible."
            },
            {
                "name": "Agaricus xanthodermus (yellow stainer)",
                "distinguish": "Wild toxic double that bruises yellow and smells of phenol."
            }
        ],
        "fun_fact": "Sold as a supplement more often than it is cooked, thanks to its medicinal reputation."
    },
    {
        "id": "bisporella-citrina",
        "name": "Lemon Disco",
        "scientific_name": "Bisporella citrina",
        "aliases": [
            "citron disco",
            "yellow fairy cups"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "cup",
                "sessile"
            ],
            "colors": [
                "yellow",
                "lemon"
            ],
            "diameter_cm": [
                0,
                1
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn",
            "winter"
        ],
        "distribution": "Worldwide on hardwood",
        "regions": [
            "global"
        ],
        "description": "Tiny brilliant-yellow cups that clamp onto decaying hardwood like little dropped lemons. Far too small to be worth eating, but unmistakable and a favourite of macro photographers.",
        "lookalikes": [
            {
                "name": "Other yellow Discomycetes (e.g. Octospora)",
                "distinguish": "Similar tiny cups; identification to species needs a microscope."
            }
        ],
        "fun_fact": "The 'disco' name is literal -- these are little saucers of pure lemon yellow."
    },
    {
        "id": "calocybe-carnea",
        "name": "Pinkfairing",
        "scientific_name": "Calocybe carnea",
        "aliases": [
            "pink clitocybe",
            "meadow puff"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "pink",
                "lilac"
            ],
            "diameter_cm": [
                2,
                6
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "pink",
                "white"
            ]
        },
        "stem": {
            "colors": [
                "pink",
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn"
        ],
        "distribution": "Europe, North America, Asia",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A small pink-capped meadow mushroom with white (not pink) spores -- the white spore print is what separates it from the deadly pink-gilled Entoloma lookalikes.",
        "lookalikes": [
            {
                "name": "Entoloma species (pinkgill)",
                "distinguish": "Look almost identical but have PINK spores and several are deadly; always check the print."
            },
            {
                "name": "Clitocybe nuda (wood blewit)",
                "distinguish": "Larger, lilac all over, woodland not meadow; edible."
            }
        ],
        "fun_fact": "Its pink cap with a clean white spore drop is the safest quick tell against poisonous pinkgills."
    },
    {
        "id": "chlorophyllum-rhacodes",
        "name": "Shaggy Parasol",
        "scientific_name": "Chlorophyllum rhacodes",
        "aliases": [
            "razorstrop fungus",
            "lepiota rhacodes"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat",
                "umbonate"
            ],
            "colors": [
                "brown",
                "tan"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "white"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "cream",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, Asia, North America, Australia",
        "regions": [
            "europe",
            "asia",
            "north-america",
            "oceania"
        ],
        "description": "A shaggy brown parasol whose flesh turns orange-red where cut. Excellent eating for most people, but it can cause stomach upset in a sensitive minority -- try a small amount first.",
        "lookalikes": [
            {
                "name": "Chlorophyllum molybdites (green-spored parasol)",
                "distinguish": "DEADLY double with green spore print; same shaggy look -- never eat a parasol without checking spores."
            },
            {
                "name": "Macrolepiota procera (parasol)",
                "distinguish": "Larger, scaly stem with a snake-skin pattern; edible."
            }
        ],
        "fun_fact": "The instant orange blush when you slice it is the species' party trick."
    },
    {
        "id": "clitocybe-geotropa",
        "name": "Trooping Funnel",
        "scientific_name": "Clitocybe geotropa",
        "aliases": [
            "monks-head",
            "big funnel"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "funnel",
                "convex"
            ],
            "colors": [
                "buff",
                "tan",
                "cream"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "cream",
                "white"
            ]
        },
        "stem": {
            "colors": [
                "buff",
                "cream"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "cream",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Europe, North America, Asia",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A large buff funnel that fruits in big arcs and fairy rings. Edible and good, but the genus holds some deadly small white funnels, so only experienced foragers should pick it.",
        "lookalikes": [
            {
                "name": "Clitocybe dealbata (ivory funnel)",
                "distinguish": "Smaller, deadly white funnel; the dangerous near-twin to avoid."
            },
            {
                "name": "Infundibulicybe gibba",
                "distinguish": "Similar grey funnel but smaller; edible."
            }
        ],
        "fun_fact": "A single troop can stretch metres across a field in a perfect arc."
    },
    {
        "id": "collybia-dryophila",
        "name": "Russet Toughshank",
        "scientific_name": "Collybia dryophila",
        "aliases": [
            "woodland toughshank",
            "oak-loving collybia"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "tan",
                "brown",
                "red-brown"
            ],
            "diameter_cm": [
                2,
                6
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "tan"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "litter",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Widespread in Northern Hemisphere",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "One of the commonest little brown mushrooms on the forest floor: a tan flexible cap on a tough stem. Technically edible but insubstantial; mainly useful as a 'this is a typical LBM' reference.",
        "lookalikes": [
            {
                "name": "Galerina marginata (deadly galerina)",
                "distinguish": "Grows on wood with a ring and brown spores; deadly -- never assume a small brown mushroom is safe."
            },
            {
                "name": "Marasmius oreades (fairy ring)",
                "distinguish": "Firmer, grows in rings in grass; edible."
            }
        ],
        "fun_fact": "'LBM' (little brown mushroom) is a mycologist's shorthand for this whole confusing crowd."
    },
    {
        "id": "coprinopsis-atramentaria",
        "name": "Common Inkcap",
        "scientific_name": "Coprinopsis atramentaria",
        "aliases": [
            "alcohol inkcap",
            "tippler's bane"
        ],
        "edibility": "poisonous",
        "cap": {
            "shape": [
                "oval",
                "bell"
            ],
            "colors": [
                "grey",
                "brown",
                "grey-brown"
            ],
            "diameter_cm": [
                3,
                7
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "grey",
                "black"
            ]
        },
        "stem": {
            "colors": [
                "grey",
                "white"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "black",
        "habitat": "urban",
        "substrate": "woodchip",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide in disturbed ground",
        "regions": [
            "global"
        ],
        "description": "A grey capped inkcap that self-digests into black ink from the edge inward. The flesh is edible on its own but contains coprine, which blocks alcohol metabolism -- drinking even hours later causes a violent disulfiram-like poisoning.",
        "lookalikes": [
            {
                "name": "Coprinus comatus (shaggy mane)",
                "distinguish": "Edible, shaggier white cap; the safe cousin and a choice spring food."
            },
            {
                "name": "Coprinellus micaceus (mica cap)",
                "distinguish": "Tiny glittery brown caps on wood; edible but insubstantial."
            }
        ],
        "fun_fact": "Old name 'tippler's bane' -- it was used to keep alcoholics from drinking."
    },
    {
        "id": "crepidotus-mollis",
        "name": "Soft Slipper Toadstool",
        "scientific_name": "Crepidotus mollis",
        "aliases": [
            "peeling oysterling",
            "mollis"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "fan",
                "shell",
                "sessile"
            ],
            "colors": [
                "cream",
                "tan",
                "brown"
            ],
            "diameter_cm": [
                2,
                6
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "cream",
                "tan"
            ]
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "rusty-brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide on hardwood",
        "regions": [
            "global"
        ],
        "description": "A stemless, fan-shaped bracket that lies flat on dead branches with rusty-brown gills underneath. Too thin and tough to eat; notable as a bracket-form gilled fungus.",
        "lookalikes": [
            {
                "name": "Pleurotus ostreatus (oyster)",
                "distinguish": "Edible oyster has WHITE spores and a thicker, meatier body."
            },
            {
                "name": "Trametes versicolor (turkey tail)",
                "distinguish": "Has pores, not gills, and is inedible."
            }
        ],
        "fun_fact": "It peels off wood like a soft little slipper -- hence the name."
    },
    {
        "id": "daedalea-quercina",
        "name": "Oak Mazegill",
        "scientific_name": "Daedalea quercina",
        "aliases": [
            "maze gill",
            "oak daedalea"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "shelf",
                "kidney"
            ],
            "colors": [
                "brown",
                "tan",
                "grey"
            ],
            "diameter_cm": [
                5,
                20
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "crowded",
            "colors": [
                "white",
                "tan",
                "brown"
            ]
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "year-round"
        ],
        "distribution": "Northern Hemisphere on oak",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A tough grey-brown shelf on oak whose pores are stretched into maze-like labyrinthines instead of neat tubes. A classic wood-decay fungus; far too hard to eat.",
        "lookalikes": [
            {
                "name": "Daedaleopsis confragosa",
                "distinguish": "Similar maze pores on non-oak hardwoods; also inedible."
            },
            {
                "name": "Trametes (bracket polypores)",
                "distinguish": "Round pores rather than a maze."
            }
        ],
        "fun_fact": "The maze pattern is where 'Daedalus' (the labyrinth builder of myth) lends the name."
    },
    {
        "id": "dacryopinax-spathularia",
        "name": "Spoon Jelly",
        "scientific_name": "Dacryopinax spathularia",
        "aliases": [
            "yellow fans",
            "spatula jelly"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "lobed",
                "jelly",
                "spatula"
            ],
            "colors": [
                "yellow",
                "orange"
            ],
            "diameter_cm": [
                1,
                4
            ]
        },
        "gills": {
            "attachment": "none",
            "spacing": "none",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide in tropics and warm temperate",
        "regions": [
            "global"
        ],
        "description": "A small translucent yellow jelly fungus shaped like a tiny spatula or fan, found glued to dead wood. Edible but insubstantial; it's a mycoparasite that feeds on other fungi in the wood.",
        "lookalikes": [
            {
                "name": "Tremella fuciformis (snow fungus)",
                "distinguish": "White ruffled jelly; edible and cultivated."
            },
            {
                "name": "Dacrymyces (orange jelly)",
                "distinguish": "Brighter orange blobby jelly on conifer wood."
            }
        ],
        "fun_fact": "It shrivels to nothing in dry weather and plumps back up after rain."
    },
    {
        "id": "exidia-glandulosa",
        "name": "Witches' Butter",
        "scientific_name": "Exidia glandulosa",
        "aliases": [
            "black jelly",
            "jet ear",
            "black witch's butter"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "lobed",
                "jelly",
                "brain-like"
            ],
            "colors": [
                "black",
                "dark brown"
            ],
            "diameter_cm": [
                2,
                8
            ]
        },
        "gills": {
            "attachment": "none",
            "spacing": "none",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": [
            "autumn",
            "winter"
        ],
        "distribution": "Worldwide on hardwood",
        "regions": [
            "global"
        ],
        "description": "A shiny black, rubbery jelly that bulges out of dead branches like cooled tar. Edible but tasteless; it's a mycoparasite on other wood-decay fungi and famously revives from bone-dry to plump after a single rain.",
        "lookalikes": [
            {
                "name": "Auricularia auricula-judae (wood ear)",
                "distinguish": "Brown ear-shaped jelly; edible and cultivated."
            },
            {
                "name": "Exidia nigricans",
                "distinguish": "Nearly identical smooth black jelly; lumped with this species by many."
            }
        ],
        "fun_fact": "The 'witches' butter' name comes from the old belief it was smeared on doors by witches."
    },
    {
        "id": "hypholoma-capnoides",
        "name": "Conifer Tuft",
        "scientific_name": "Hypholoma capnoides",
        "aliases": [
            "smoky tuft",
            "capnoides"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "yellow",
                "brown",
                "yellow-brown"
            ],
            "diameter_cm": [
                2,
                6
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "lilac",
                "grey",
                "grey-brown"
            ]
        },
        "stem": {
            "colors": [
                "yellow",
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "purple-brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere conifer forests",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A sulphur-free cluster mushroom on conifer stumps, with smoky lilac-grey gills and a purple-brown spore print. A safe, choice edible and the edible sibling of the poisonous sulfur tuft.",
        "lookalikes": [
            {
                "name": "Hypholoma fasciculare (sulfur tuft)",
                "distinguish": "DEADLY; identical clumps but with bright YELLOW gills and a bitter taste."
            },
            {
                "name": "Galerina marginata (deadly galerina)",
                "distinguish": "Brown gills and a ring; deadly."
            }
        ],
        "fun_fact": "If the gills are grey-lilac not yellow, you've likely got the safe one -- but verify the spore print."
    },
    {
        "id": "ischnoderma-resinosum",
        "name": "Resinous Polypore",
        "scientific_name": "Ischnoderma resinosum",
        "aliases": [
            "late-fall polypore",
            "resinous polyporus"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "shelf",
                "kidney"
            ],
            "colors": [
                "brown",
                "tan",
                "grey-brown"
            ],
            "diameter_cm": [
                5,
                20
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream",
                "brown"
            ]
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere hardwoods",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A velvety brown shelf that oozes clear resinous droplets when young, ageing to a black crusty conk. Inedible and woody, but a striking late-season bracket.",
        "lookalikes": [
            {
                "name": "Ganoderma lucidum (reishi)",
                "distinguish": "Lacquered red-brown shelf; also inedible but medicinal."
            },
            {
                "name": "Fomes fomentarius (hoof fungus)",
                "distinguish": "Grey hoof shape, no resin droplets."
            }
        ],
        "fun_fact": "The sticky droplets on young caps are where 'resinous' comes from."
    },
    {
        "id": "laccaria-amethystina",
        "name": "Amethyst Deceiver",
        "scientific_name": "Laccaria amethystina",
        "aliases": [
            "lilac laccaria",
            "amethyst laccaria"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat",
                "umbilicate"
            ],
            "colors": [
                "lilac",
                "violet",
                "purple"
            ],
            "diameter_cm": [
                1,
                6
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "distant",
            "colors": [
                "lilac",
                "violet"
            ]
        },
        "stem": {
            "colors": [
                "lilac",
                "violet"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "litter",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "An all-lilac mushroom that fades toward brown as it dries or ages, which is why it 'deceives' on identification. Edible but small and insubstantial; white spores confirm the ID.",
        "lookalikes": [
            {
                "name": "Laccaria laccata (deceiver)",
                "distinguish": "Same shape but tan/red, not lilac."
            },
            {
                "name": "Clitocybe nuda (wood blewit)",
                "distinguish": "Larger lilac mushroom in leaf litter; edible."
            }
        ],
        "fun_fact": "Its colour bleaches out in dry weather, fooling novice collectors -- hence 'deceiver'."
    },
    {
        "id": "laccaria-laccata",
        "name": "Deceiver",
        "scientific_name": "Laccaria laccata",
        "aliases": [
            "tawny laccaria",
            "reddish laccaria"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat",
                "umbilicate"
            ],
            "colors": [
                "tan",
                "red-brown",
                "orange-brown"
            ],
            "diameter_cm": [
                1,
                6
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "distant",
            "colors": [
                "tan",
                "pinkish",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "tan",
                "red-brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "litter",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn",
            "winter"
        ],
        "distribution": "Widespread, nearly worldwide",
        "regions": [
            "global"
        ],
        "description": "An extremely variable little tan-to-reddish cap whose shape and colour shift with weather -- the original 'deceiver'. Edible but tiny; white spores and distant gills are the reliable ID marks.",
        "lookalikes": [
            {
                "name": "Laccaria amethystina",
                "distinguish": "Lilac version of the same genus."
            },
            {
                "name": "Inocybe species",
                "distinguish": "Some small brown Inocybe are deadly; check spores and habitat."
            }
        ],
        "fun_fact": "No two seem to look alike, which is the whole point of the name."
    },
    {
        "id": "lactarius-quietus",
        "name": "Oak Milkcap",
        "scientific_name": "Lactarius quietus",
        "aliases": [
            "truffle milkcap",
            "oak lactarius"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "flat",
                "convex",
                "umbilicate"
            ],
            "colors": [
                "red-brown",
                "chestnut",
                "dark brown"
            ],
            "diameter_cm": [
                4,
                10
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "cream",
                "tan"
            ]
        },
        "stem": {
            "colors": [
                "red-brown",
                "tan"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "cream",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, introduced in North America",
        "regions": [
            "europe",
            "north-america"
        ],
        "description": "A dry, concentric-zoned brown milkcap under oaks that smells strongly of tainted truffles or latex when crushed. Edible but mediocre and slightly acrid; the truffle-like scent is the giveaway.",
        "lookalikes": [
            {
                "name": "Lactarius deliciosus (saffron milkcap)",
                "distinguish": "Orange with carrot-orange latex; choice edible."
            },
            {
                "name": "Lactarius piperatus (peppery milkcap)",
                "distinguish": "White, fierce hot taste; edible but needs treatment."
            }
        ],
        "fun_fact": "The odd 'truffle' perfume is why Europeans once called it the truffle milkcap."
    },
    {
        "id": "leucoagaricus-leucothites",
        "name": "Smooth Parasol",
        "scientific_name": "Leucoagaricus leucothites",
        "aliases": [
            "white parasol",
            "smooth lepiota"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat",
                "umbonate"
            ],
            "colors": [
                "white",
                "cream"
            ],
            "diameter_cm": [
                4,
                12
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "pink",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide in grassy/disturbed areas",
        "regions": [
            "global"
        ],
        "description": "A clean white parasol with a movable ring and white (not green) spores. A good edible, but it must be separated from deadly Amanitas, which differ by having a cup (volva) at the base.",
        "lookalikes": [
            {
                "name": "Amanita phalloides (death cap)",
                "distinguish": "DEADLY; has a volva cup at the base and a different stem ring -- never eat a white parasol without checking the base."
            },
            {
                "name": "Macrolepiota procera (parasol)",
                "distinguish": "Larger, scaly stem; edible."
            }
        ],
        "fun_fact": "White-spored parasols are the safe ones; green- or dark-spored parasols are the killers."
    },
    {
        "id": "macrolepiota-excoriata",
        "name": "Small Parasol",
        "scientific_name": "Macrolepiota excoriata",
        "aliases": [
            "meadow parasol",
            "little parasol"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat",
                "umbonate"
            ],
            "colors": [
                "buff",
                "tan",
                "cream"
            ],
            "diameter_cm": [
                4,
                10
            ]
        },
        "gills": {
            "attachment": "free",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "tan"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "grassland",
        "substrate": "ground",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Europe, North America, Asia",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A miniature version of the giant parasol: a scaly buff cap with a snake-skin patterned stem and a movable ring. A choice edible from meadows, smaller and less likely to be confused with toxic species than its big relative.",
        "lookalikes": [
            {
                "name": "Macrolepiota procera (parasol)",
                "distinguish": "Same but much larger; both edible."
            },
            {
                "name": "Chlorophyllum molybdites (green-spored parasol)",
                "distinguish": "DEADLY; green spores, woodland/lawn edges."
            }
        ],
        "fun_fact": "If the parasol fits in your palm, this is usually the one."
    },
    {
        "id": "marasmius-scorodonius",
        "name": "Garlic Parachute",
        "scientific_name": "Marasmius scorodonius",
        "aliases": [
            "garlic mushroom",
            "onus"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "convex",
                "flat",
                "umbilicate"
            ],
            "colors": [
                "red-brown",
                "tan",
                "orange-brown"
            ],
            "diameter_cm": [
                1,
                3
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "distant",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "red-brown",
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "litter",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A tiny parachute-shaped mushroom that smells and tastes strongly of garlic. Too small to be a meal but dried and crumbled as a seasoning; the scent survives drying.",
        "lookalikes": [
            {
                "name": "Marasmius oreades (fairy ring)",
                "distinguish": "Bigger, grows in grass rings, faintly mealy not garlicky; edible."
            },
            {
                "name": "Mycena species",
                "distinguish": "Many small Mycena lack the garlic smell and some are toxic."
            }
        ],
        "fun_fact": "Foragers dry it like a spice pod -- one cap will garlic-up a whole pot."
    },
    {
        "id": "meripilus-giganteus",
        "name": "Giant Polypore",
        "scientific_name": "Meripilus giganteus",
        "aliases": [
            "black-staining polypore",
            "giant cauliflower fungus"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "shelf",
                "rosette",
                "fan"
            ],
            "colors": [
                "brown",
                "tan",
                "grey"
            ],
            "diameter_cm": [
                10,
                60
            ]
        },
        "gills": {
            "attachment": "pores",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream",
                "yellow"
            ]
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "parasitic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere at tree bases",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A huge rosette of brown fan-shaped caps at the base of living oaks and other hardwoods, which stains black where handled. Inedible and causes tree decay, but easily confused with the prized edible hen of the woods.",
        "lookalikes": [
            {
                "name": "Grifola frondosa (hen of the woods)",
                "distinguish": "EDIBLE choice; grey, not brown, and does NOT stain black."
            },
            {
                "name": "Laetiporus sulphureus (chicken of the woods)",
                "distinguish": "Bright orange shelf; edible."
            }
        ],
        "fun_fact": "The black thumbprint you leave on it is the fastest way to tell it from the edible hen."
    },
    {
        "id": "mycena-galericulata",
        "name": "Common Bonnet",
        "scientific_name": "Mycena galericulata",
        "aliases": [
            "felted bonnet",
            "grey bonnet"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "conical",
                "bell",
                "umbonate"
            ],
            "colors": [
                "grey",
                "brown-grey",
                "tan"
            ],
            "diameter_cm": [
                1,
                4
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "grey",
                "white"
            ]
        },
        "stem": {
            "colors": [
                "grey",
                "brown"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "summer",
            "autumn",
            "winter"
        ],
        "distribution": "Worldwide on wood",
        "regions": [
            "global"
        ],
        "description": "A small grey bell-cap with a central bump, fruiting in troops on sticks and stumps almost year-round. Inedible and one of dozens of lookalike Mycenas; a standard 'little grey mushroom on wood' reference.",
        "lookalikes": [
            {
                "name": "Mycena haematopus (bleeding fairy helmet)",
                "distinguish": "Bleeds red latex when cut; inedible."
            },
            {
                "name": "Panaeolus (mottled gills)",
                "distinguish": "Dark mottled gills and a different habitat; some psychoactive."
            }
        ],
        "fun_fact": "If it's a tiny grey cone on a twig, odds are it's a Mycena -- there are hundreds."
    },
    {
        "id": "neolentinus-lepideus",
        "name": "Scaly Sawgill",
        "scientific_name": "Neolentinus lepideus",
        "aliases": [
            "train wrecker",
            "strawberry shelf"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "fan",
                "shelf"
            ],
            "colors": [
                "white",
                "cream",
                "tan"
            ],
            "diameter_cm": [
                4,
                12
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "distant",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "tan"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Worldwide on conifer/treated timber",
        "regions": [
            "global"
        ],
        "description": "A tough white fan with a scaly cap and serrated (toothed) gills that smells faintly of anise or lemon. Famously rots railway sleepers and treated timber; far too woody to eat.",
        "lookalikes": [
            {
                "name": "Pleurotus ostreatus (oyster)",
                "distinguish": "Edible oyster is softer with smooth gills and white spores."
            },
            {
                "name": "Lentinula edodes (shiitake)",
                "distinguish": "Cultivated edible with a shaggy umbrella cap."
            }
        ],
        "fun_fact": "Its taste for creosote-treated wood earned it the nickname 'train wrecker'."
    },
    {
        "id": "panus-neostrigosus",
        "name": "Velet Tooth",
        "scientific_name": "Panus neostrigosus",
        "aliases": [
            "hairy panus",
            "woolly panus"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "fan",
                "shelf"
            ],
            "colors": [
                "tan",
                "brown",
                "buff"
            ],
            "diameter_cm": [
                2,
                8
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "tan",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "tan"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Americas and beyond on hardwood",
        "regions": [
            "north-america",
            "south-america",
            "global"
        ],
        "description": "A hairy, leathery tan fan on dead branches with decurrent gills and a fuzzy stem. Too tough to eat; a typical tough bracket-form gilled fungus of warm regions.",
        "lookalikes": [
            {
                "name": "Pleurotus (oysters)",
                "distinguish": "Softer, edible, smooth not hairy."
            },
            {
                "name": "Lentinellus (toothed gills)",
                "distinguish": "Has actual tooth-like spines under the cap."
            }
        ],
        "fun_fact": "The velvety fuzz is why old books called it the 'woolly panus'."
    },
    {
        "id": "pholiota-aurivella",
        "name": "Golden Pholiota",
        "scientific_name": "Pholiota aurivella",
        "aliases": [
            "hemlock pholiota",
            "golden scale"
        ],
        "edibility": "inedible",
        "cap": {
            "shape": [
                "convex",
                "flat"
            ],
            "colors": [
                "gold",
                "orange-brown",
                "yellow-brown"
            ],
            "diameter_cm": [
                4,
                12
            ]
        },
        "gills": {
            "attachment": "attached",
            "spacing": "crowded",
            "colors": [
                "brown",
                "rusty",
                "olive"
            ]
        },
        "stem": {
            "colors": [
                "brown",
                "yellow"
            ],
            "ring": True,
            "volva": False
        },
        "spore_print": "rusty-brown",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "late summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere on conifers",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A slimy golden-brown scaly cap on living or dead conifers, with a ring and rusty-brown spores. Inedible and not choice; the showy cousin of the shaggy scalycap.",
        "lookalikes": [
            {
                "name": "Pholiota squarrosa (shaggy scalycap)",
                "distinguish": "Same genus, shaggier, on hardwood; inedible."
            },
            {
                "name": "Armillaria mellea (honey fungus)",
                "distinguish": "Honey-brown, edible when cooked, on wood in clusters."
            }
        ],
        "fun_fact": "After rain the gold cap turns slick and shiny like a lacquered coin."
    },
    {
        "id": "pleurotus-cornucopiae",
        "name": "Branch Oyster",
        "scientific_name": "Pleurotus cornucopiae",
        "aliases": [
            "cornucopia oyster",
            "funnel oyster"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "funnel",
                "fan",
                "shell"
            ],
            "colors": [
                "cream",
                "tan",
                "buff"
            ],
            "diameter_cm": [
                4,
                12
            ]
        },
        "gills": {
            "attachment": "decurrent",
            "spacing": "crowded",
            "colors": [
                "white",
                "cream"
            ]
        },
        "stem": {
            "colors": [
                "white",
                "cream"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "lilac-gray",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "spring",
            "autumn"
        ],
        "distribution": "Worldwide on hardwood",
        "regions": [
            "global"
        ],
        "description": "A funnel-shaped oyster relative with a lilac-grey spore print and deeply decurrent gills running down a short off-centre stem. A choice edible and a common cultivated species alongside the standard oyster.",
        "lookalikes": [
            {
                "name": "Pleurotus ostreatus (oyster)",
                "distinguish": "Same genus, flatter shell shape; edible."
            },
            {
                "name": "Clitocybe (funnel caps)",
                "distinguish": "Deadly white funnels have white spores, not lilac-grey."
            }
        ],
        "fun_fact": "Its horn-of-plenty shape is the 'cornucopia' in the name."
    },
    {
        "id": "pseudohydnum-gelatinosum",
        "name": "Tooth Jelly",
        "scientific_name": "Pseudohydnum gelatinosum",
        "aliases": [
            "jelly tooth",
            "cat's tongue"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "fan",
                "lobed",
                "jelly"
            ],
            "colors": [
                "white",
                "grey",
                "translucent"
            ],
            "diameter_cm": [
                2,
                8
            ]
        },
        "gills": {
            "attachment": "none",
            "spacing": "none",
            "colors": []
        },
        "stem": {
            "colors": [
                "white",
                "grey"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere conifers",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A translucent grey-white jelly fungus whose underside is covered in soft tooth-like spines instead of gills -- a gelatinous take on a hedgehog fungus. Edible but insubstantial; squishy and revives after rain.",
        "lookalikes": [
            {
                "name": "Hydnum repandum (hedgehog fungus)",
                "distinguish": "Edible tooth fungus but firm, not jelly."
            },
            {
                "name": "Tremella (jellies)",
                "distinguish": "Smooth jelly with no teeth underneath."
            }
        ],
        "fun_fact": "It feels exactly like a cat's tongue -- soft spines and all."
    },
    {
        "id": "ramaria-botrytis",
        "name": "Clustered Coral",
        "scientific_name": "Ramaria botrytis",
        "aliases": [
            "pink-tipped coral",
            "cauliflower coral"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "branched",
                "coral"
            ],
            "colors": [
                "buff",
                "cream",
                "pink"
            ],
            "diameter_cm": [
                5,
                15
            ]
        },
        "gills": {
            "attachment": "n/a",
            "spacing": "n/a",
            "colors": []
        },
        "stem": {
            "colors": [
                "white",
                "buff"
            ],
            "ring": False,
            "volva": False
        },
        "spore_print": "ochre",
        "habitat": "forest",
        "substrate": "ground",
        "ecology": "mycorrhizal",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "A coral mushroom with creamy branches tipped in pink, fruiting on the forest floor under hardwoods. A choice edible for many, though it can upset sensitive stomachs; the pink tips are the field mark.",
        "lookalikes": [
            {
                "name": "Ramaria formosa (beautiful coral)",
                "distinguish": "POISONOUS; pinkish but lacks the clean cream base and causes vomiting."
            },
            {
                "name": "Ramaria stricta (strict coral)",
                "distinguish": "Yellow-tan, on wood, inedible."
            }
        ],
        "fun_fact": "The pink tips are the 'botrytis' (grape-like) clue that this is the good one."
    },
    {
        "id": "tremiscus-helvelloides",
        "name": "Apricot Jelly",
        "scientific_name": "Tremiscus helvelloides",
        "aliases": [
            "orange jelly",
            "apricot jelly fungus"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "lobed",
                "jelly",
                "cup"
            ],
            "colors": [
                "apricot",
                "orange",
                "salmon"
            ],
            "diameter_cm": [
                2,
                10
            ]
        },
        "gills": {
            "attachment": "none",
            "spacing": "none",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "summer",
            "autumn"
        ],
        "distribution": "Northern Hemisphere",
        "regions": [
            "europe",
            "north-america",
            "asia"
        ],
        "description": "An apricot-orange lobed jelly that drapes over dead wood like a soft Sea anemone. Edible but insubstantial; the larger, more colourful cousin of witch's butter.",
        "lookalikes": [
            {
                "name": "Tremella mesenterica (witch's butter)",
                "distinguish": "Bright yellow jelly, smaller; edible but insubstantial."
            },
            {
                "name": "Calocera (staghorn jelly)",
                "distinguish": "Branched yellow-orange antler shapes, not lobed."
            }
        ],
        "fun_fact": "It goes from rock-hard to plump and jiggly within an hour of rain."
    },
    {
        "id": "auricularia-cornea",
        "name": "Cloud Ear",
        "scientific_name": "Auricularia cornea",
        "aliases": [
            "tree ear",
            "black fungus (cultivated)"
        ],
        "edibility": "edible",
        "cap": {
            "shape": [
                "ear",
                "shell",
                "sessile"
            ],
            "colors": [
                "brown",
                "dark brown",
                "black"
            ],
            "diameter_cm": [
                3,
                10
            ]
        },
        "gills": {
            "attachment": "none",
            "spacing": "none",
            "colors": []
        },
        "stem": {
            "colors": [],
            "ring": False,
            "volva": False
        },
        "spore_print": "white",
        "habitat": "forest",
        "substrate": "deadwood",
        "ecology": "saprotrophic",
        "season": [
            "year-round"
        ],
        "distribution": "Cultivated and wild in warm regions",
        "regions": [
            "asia",
            "global"
        ],
        "description": "The cultivated 'cloud ear' of Chinese cooking: a thin, wrinkled, ear-shaped brown jelly with a crunchy texture. Wild on subtropical hardwood, but mostly met as a dried supermarket ingredient; edible and mild.",
        "lookalikes": [
            {
                "name": "Auricularia auricula-judae (wood ear)",
                "distinguish": "The wild European sibling; both edible jellies."
            },
            {
                "name": "Exidia glandulosa (witches' butter)",
                "distinguish": "Shiny black blobby jelly, not ear-shaped."
            }
        ],
        "fun_fact": "It's sold dried by the kilo and rehydrates to a crunchy, flavour-soaking ear."
    }
]
