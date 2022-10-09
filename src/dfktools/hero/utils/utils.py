
import json

FAIL_ON_NOT_FOUND = False

ALPHABET = '123456789abcdefghijkmnopqrstuvwx'

CRYSTALEVALE_HERO_OFFSET = 1_000_000_000_000

rarity = {
    0: "common",
    1: "uncommon",
    2: "rare",
    3: "legendary",
    4: "mythic",
}

_class = {
    0: "warrior",
    1: "knight",
    2: "thief",
    3: "archer",
    4: "priest",
    5: "wizard",
    6: "monk",
    7: "pirate",
    8: "berserker",
    9: "seer",
    16: "paladin",
    17: "darkknight",
    18: "summoner",
    19: "ninja",
    20: "shapeshifter",
    24: "dragoon",
    25: "sage",
    28: "dreadknight"
}

visual_traits = {
    0: 'gender',
    1: 'headAppendage',
    2: 'backAppendage',
    3: 'background',
    4: 'hairStyle',
    5: 'hairColor',
    6: 'visualUnknown1',
    7: 'eyeColor',
    8: 'skinColor',
    9: 'appendageColor',
    10: 'backAppendageColor',
    11: 'visualUnknown2'
}

stat_traits = {
    0: "class",
    1: "subClass",
    2: "profession",
    3: "passive1",
    4: "passive2",
    5: "active1",
    6: "active2",
    7: "statBoost1",
    8: "statBoost2",
    9: "statsUnknown1",
    10: "element",
    11: "statsUnknown2"
}

ability_traits = {
    0: "basic1",
    1: "basic2",
    2: "basic3",
    3: "basic4",
    4: "basic5",
    5: "basic6",
    6: "basic7",
    7: "basic8",
    16: "advanced1",
    17: "advanced2",
    18: "advanced3",
    19: "advanced4",
    24: "elite1",
    25: "elite2",
    28: "transcendant1"
}

professions = {
    0: 'mining',
    2: 'gardening',
    4: 'fishing',
    6: 'foraging',
}

stats = {
    0: 'strength',
    2: 'agility',
    4: 'intelligence',
    6: 'wisdom',
    8: 'luck',
    10: 'vitality',
    12: 'endurance',
    14: 'dexterity'
}

elements = {
    0: 'fire',
    2: 'water',
    4: 'earth',
    6: 'wind',
    8: 'lightning',
    10: 'ice',
    12: 'light',
    14: 'dark',
}

background = {
    0: "desert",
    2: "forest",
    4: "plains",
    6: "island",
    8: "swamp",
    10: "mountains",
    12: "city",
    14: "arctic"
}

head_app = {
    0: "none",
    1: "kitsune ears",
    2: "satyr horns",
    3: "ram horns",
    4: "imp horns",
    5: "cat ears",
    6: "minotaur horns",
    7: "faun horns",
    8: "draconic horns",
    9: "fae circlet",
    16: "jagged horns",
    17: "spindle horns",
    18: "bear ears",
    19: "antennae",
    20: "fallen angel coronet",
    24: "wood elf ears",
    25: "snow elf ears",
    28: "insight jewel",
}

back_app = {
    0: "none",
    1: "monkey tail",
    2: "cat tail",
    3: "imp tail",
    4: "minotaur tail",
    5: "daisho",
    6: "kitsune tail",
    7: "zweihander",
    8: "skeletal wings",
    9: "skeletal tail",
    16: "gryphon wings",
    17: "draconic wings",
    18: "butterfly wings",
    19: "phoenix wings",
    20: "fallen angel",
    24: "aura of the inner grove",
    25: "ancient orbs",
    28: "cecaelia tentacles",
}

app_color = { 
    0: "#c5bfa7",
    1: "#a88b47",
    2: "#58381e",
    3: "#566f7d",
    4: "#2a386d",
    5: "#3f2e40",
    6: "#830e18",
    7: "#6f3a3c",
    8: "#cddef0",
    9: "#df7126",
    16: "#6b173c",
    17: "#a0304d",
    18: "#78547c",
    19: "#352a51",
    20: "#147256",
    24: "#c29d35",
    25: "#211f1f",
    28: "#d7d7d7",
}

hair_style = {
    "male": {
        0: "battle hawk",
        1: "wolf mane",
        2: "enchanter",
        3: "wild growth",
        4: "pixel",
        5: "sunrise",
        6: "bouffant",
        7: "agleam spike",
        8: "wayfinder",
        9: "faded topknot",
        16: "gruff",
        17: "rogue locs",
        18: "stone cold",
        19: "zinra's tail",
        20: "hedgehog",
        24: "skegg",
        25: "shinobi",
        28: "perfect form",
    },
    "female": {
        0: "windswept",
        1: "fauna",
        2: "enchantress",
        3: "pineapple top",
        4: "pixie",
        5: "darkweave plait",
        6: "dejanira",
        7: "courtly updo",
        8: "centaur tail",
        9: "lamia",
        16: "vogue locs",
        17: "twin vine loops",
        18: "sweeping willow",
        19: "odango",
        20: "goddess locks",
        24: "ethereal waterfall",
        25: "kunoichi",
        28: "lunar light odango",
    }
}

hair_color = {
    0: "#ab9159",
    1: "#af3853",
    2: "#578761",
    3: "#068483",
    4: "#48321e",
    5: "#66489e",
    6: "#ca93a7",
    7: "#62a7e6",
    8: "#c34b1e",
    9: "#326988",
    16: "#d7bc65",
    17: "#9b68ab",
    18: "#8d6b3a",
    19: "#566377",
    20: "#275435",
    24: "#880016",
    25: "#353132",
    28: "#8f9bb3",
}

eye_color = {
    0: "#203997",
    2: "#896693",
    4: "#bb3f55",
    6: "#0d7634",
    8: "#8d7136",
    10: "#613d8a",
    12: "#2494a2",
    14: "#a41e12",
}

skin_color = {
    0: "#c58135",
    2: "#f1ca9e",
    4: "#985e1c",
    6: "#57340c",
    8: "#e6a861",
    10: "#7b4a11",
    12: "#e5ac91",
    14: "#aa5c38",
}


def cv2sd_cv_hero_id(cv_hero_id):
    return cv_hero_id - CRYSTALEVALE_HERO_OFFSET


def sd2cv_cv_hero_id(cv_hero_id):
    return cv_hero_id + CRYSTALEVALE_HERO_OFFSET


def parse_rarity(id):
    value = rarity.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Rarity not found")
    return value


def parse_class(id):
    value = _class.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Class not found")
    return value


def parse_profession(id):
    value = professions.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Profession not found")
    return value


def parse_stat(id):
    value = stats.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Stat not found")
    return value


def parse_ability(id):
    value = ability_traits.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Ability not found")
    return value


def parse_element(id):
    value = elements.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Element not found")
    return value


def parse_background(id):
    value = background.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Background not found")
    return value


def parse_head_app(id):
    value = head_app.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Head Appendage not found")
    return value


def parse_back_app(id):
    value = back_app.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Back Appendage not found")
    return value


def parse_app_color(id):
    value = app_color.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Appendage color not found")
    return value


def parse_hair_style(id, gender):
    value = hair_style[gender].get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Hair style not found")
    return value


def parse_hair_color(id):
    value = hair_color.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Hair color not found")
    return value


def parse_eye_color(id):
    value = eye_color.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Eye color not found")
    return value


def parse_skin_color(id):
    value = skin_color.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Skin color not found")
    return value


def genes2traits(genes):
    traits = []

    stat_raw_kai = "".join(__genesToKai(genes).split(' '))
    for ki in range(0, len(stat_raw_kai)):
        kai = stat_raw_kai[ki]
        value_num = __kai2dec(kai)
        traits.append(value_num)

    assert len(traits) == 48
    arranged_traits = [[], [], [], []]
    for i in range(0, 12):
        index = i << 2
        for j in range(0, len(arranged_traits)):
            arranged_traits[j].append(traits[index + j])

    arranged_traits.reverse()
    return arranged_traits


def parse_stat_genes(genes):
    traits = genes2traits(genes)
    stats = parse_stat_trait(traits[0])
    r1 = parse_stat_trait(traits[1])
    r2 = parse_stat_trait(traits[2])
    r3 = parse_stat_trait(traits[3])

    stats['r1'] = r1
    stats['r2'] = r2
    stats['r3'] = r3
    stats['raw'] = genes

    return stats


def parse_stat_trait(trait):

    if len(trait) != 12:
        raise Exception("Traits must be an array of 12")

    stats = {}
    for i in range(0, 12):
        stat_trait = stat_traits.get(i, None)
        stats[stat_trait] = trait[i]

    stats['class'] = parse_class(stats['class'])
    stats['subClass'] = parse_class(stats['subClass'])

    stats['profession'] = parse_profession(stats['profession'])

    stats['passive1'] = parse_ability(stats['passive1'])
    stats['passive2'] = parse_ability(stats['passive2'])
    stats['active1'] = parse_ability(stats['active1'])
    stats['active2'] = parse_ability(stats['active2'])

    stats['statBoost1'] = parse_stat(stats['statBoost1'])
    stats['statBoost2'] = parse_stat(stats['statBoost2'])
    stats['statsUnknown1'] = parse_ability(stats['statsUnknown1']) # stats.get(stats['statsUnknown1'], None)
    stats['statsUnknown2'] = parse_ability(stats['statsUnknown2']) # stats.get(stats['statsUnknown2'], None)
    stats['element'] = parse_element(stats['element'])

    return stats


def parse_visual_genes(genes):
    visual_genes = {}
    visual_genes['raw'] = genes

    visual_raw_kai = "".join(__genesToKai(visual_genes['raw']).split(' '))

    for ki in range(0, len(visual_raw_kai)):
        stat_trait = visual_traits.get(int(ki / 4), None)
        kai = visual_raw_kai[ki]
        value_num = __kai2dec(kai)
        visual_genes[stat_trait] = value_num

    visual_genes['gender'] = 'male' if visual_genes['gender'] == 1 else 'female'
    
    visual_genes['background'] = parse_background(visual_genes['background'])
    visual_genes['hairStyle'] = parse_hair_style(visual_genes['hairStyle'], visual_genes['gender'])
    visual_genes['headAppendage'] = parse_head_app(visual_genes['headAppendage'])
    visual_genes['backAppendage'] = parse_back_app(visual_genes['backAppendage'])
    
    visual_genes['hairColor'] = parse_hair_color(visual_genes['hairColor'])
    visual_genes['appendageColor'] = parse_app_color(visual_genes['appendageColor'])
    visual_genes['backAppendageColor'] = parse_app_color(visual_genes['backAppendageColor'])
    visual_genes['eyeColor'] = parse_eye_color(visual_genes['eyeColor'])
    visual_genes['skinColor'] = parse_skin_color(visual_genes['skinColor'])
    
    visual_genes['visualUnknown1'] = parse_ability(visual_genes['visualUnknown1'])
    visual_genes['visualUnknown2'] = parse_ability(visual_genes['visualUnknown2'])
    
    return visual_genes


def hero2str(hero):

    if isinstance(hero['info']['class'], int):
        c = parse_class(hero['info']['class'])
        sc = parse_class(hero['info']['subClass'])
        r = parse_rarity(hero['info']['rarity'])
        l = hero['state']['level']
    else:
        c = hero['info']['class']
        sc = hero['info']['subClass']
        r = hero['info']['rarity']
        l = hero['state']['level']

    return str(hero['id']) + " " + r.title() + " " + c.title() + "/" + sc.title() + " lvl " + str(l)


def __genesToKai(genes):
    BASE = len(ALPHABET)

    buf = ''
    while genes >= BASE:
        mod = int(genes % BASE)
        buf = ALPHABET[int(mod)] + buf
        genes = (genes - mod) // BASE

    # Add the last 4 (finally).
    buf = ALPHABET[int(genes)] + buf

    # Pad with leading 1s.
    buf = buf.rjust(48, '1')
    buf = buf[0:48]

    return ' '.join(buf[i:i + 4] for i in range(0, len(buf), 4))


def __kai2dec(kai):
    return ALPHABET.index(kai)


def parse_names(names_raw_string):
    names_raw_string = names_raw_string\
        .replace("\\xf3", "ó") \
        .replace("\\xf2", "ò") \
        .replace("\\xe9", "é") \
        .replace("\\xe1", "á") \
        .replace("\\xc9", "É") \
        .replace("\\xed", "í") \
        .replace("\\xfa", "ú") \
        .replace("\\xec", "ì")

    if "\\x" in names_raw_string:
        raise Exception("Unhandled unicode found")

    return json.loads(names_raw_string)
