FAIL_ON_NOT_FOUND = False

egg_types = {
    0: "blue",
    1: "grey",
    2: "green",
    3: "yellow",
    4: "golden",
}

egg_rarity = {
    0: "common",
    1: "uncommon",
    2: "rare",
    3: "legendary",
    4: "mythic",
}

egg_elements = {
    0: 'fire',
    1: 'water',
    2: 'earth',
    3: 'wind',
    4: 'lightning',
    5: 'ice',
    6: 'light',
    7: 'dark',
}

pet_background = {
    0: "stillwood meadow",
    1: "forest trail",
    2: "swamp of eoxis",
    3: "vithraven outskirts",
    4: "path of fire",
    5: "reyalin mountain pass",
    6: "adelyn side street",
    7: "bloater falls",
    8: "haywood farmstead",
    9: "inner grove",
    10: "vuhlmira ruins"
}

bonus_rarity = {
    1: "common",
    80: "rare",
    160: "mythic"
}


def parse_egg_type(egg_type):
    value = egg_types.get(egg_type, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Egg type not found")
    return value


def parse_egg_rarity(rarity):
    value = egg_rarity.get(rarity, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Egg rarity not found")
    return value


def parse_egg_element(element):
    value = egg_elements.get(element, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Egg element not found")
    return value


def parse_pet_background(background):
    value = pet_background.get(background, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Background not found")
    return value


def parse_bonus_rarity(rarity):
    value = bonus_rarity.get(rarity, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Bonus rarity not found")
    return value


def human_readable_pet(raw_pet):
    if raw_pet is None:
        return None

    pet = {}
    i = 0

    pet['id'] = raw_pet[i]
    i = i + 1
    pet['originId'] = raw_pet[i]
    i = i + 1
    pet['name'] = raw_pet[i]
    i = i + 1
    pet['season'] = raw_pet[i]
    i = i + 1
    pet['eggType'] = parse_egg_type(raw_pet[i])
    i = i + 1
    pet['rarity'] = parse_egg_rarity(raw_pet[i])
    i = i + 1
    pet['element'] = parse_egg_element(raw_pet[i])
    i = i + 1
    pet['bonusCount'] = raw_pet[i]
    i = i + 1
    pet['profBonus'] = parse_bonus_rarity(raw_pet[i])
    i = i + 1
    pet['profBonusScalar'] = raw_pet[i]
    i = i + 1
    pet['craftBonus'] = parse_bonus_rarity(raw_pet[i])
    i = i + 1
    pet['craftBonusScalar'] = raw_pet[i]
    i = i + 1
    pet['combatBonus'] = parse_bonus_rarity(raw_pet[i])
    i = i + 1
    pet['combatBonusScalar'] = raw_pet[i]
    i = i + 1
    pet['appearance'] = raw_pet[i]
    i = i + 1
    pet['background'] = parse_pet_background(raw_pet[i])
    i = i + 1
    pet['shiny'] = raw_pet[i]
    i = i + 1
    pet['hungryAt'] = raw_pet[i]
    i = i + 1
    pet['equippableAt'] = raw_pet[i]
    i = i + 1
    pet['equippedTo'] = raw_pet[i]
    i = i + 1

    return pet