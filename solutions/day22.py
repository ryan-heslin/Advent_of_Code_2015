# while stats["boss_hp"] > 0:
# stats["player_hp"] -= (stats["boss_damage"] - stats["player_armor"])
# for spell in ("poison", "shield", "recharge"):
# if effects[spell] > 0:
# actions[spell]()
# effects[spell] -= 1
# if effects["shield"] == 0:
# stats["player_armor"] = 0
# for spell in ("poison", "shield", "recharge"):
# if effects[spell] == 0 and stats["player_mana"] >= costs[spell]:
# effects[spell] = durations[spell]
# actions[spell]()
# mana_spent += costs[spell]
# stats["player_mana"] -= costs[spell]
# print(f"Casting {spell}")
# break
# else:
# actions["magic_missile"]()
# print(f"Casting magic missile")
# mana_spent += costs["magic_missile"]
# stats["player_mana"] -= costs["magic_missile"]
# stats["boss_hp"] -= 4
# print(stats)
# print(effects)
from collections import deque
from math import ceil
from math import inf

with open("inputs/day22.txt") as f:
    boss_hp, boss_damage = [int(x.split(" ")[-1]) for x in f.read().splitlines()]


spells = ("magic_missile", "drain", "shield", "poison", "recharge")
shield_armor = 7

def shield_effect(state):
    return {}

def dummy_cast(state): 
    return {}
# No-op
drain_effect = shield_cast = poison_cast = recharge_cast = magic_missile_effect = shield_effect


def poison_effect(state):
    return {"boss_hp": state["boss_hp"] - 3}


def recharge_effect(state):
    return {"player_mana": state["player_mana"] + 101}


def magic_missile_cast(state):
    return {"boss_hp": state["boss_hp"] - 4}


def drain_cast(state):
    return {"boss_hp": state["boss_hp"] - 2, "player_hp": min(state["player_hp"] + 2, start["player_hp"])}


costs = dict(zip(spells, (53, 73, 113, 173, 229)))
min_mana = min(costs.values())
effects = dict(
    zip(
        spells,
        [
            magic_missile_effect,
            drain_effect,
            shield_effect,
            poison_effect,
            recharge_effect,
        ],
    )
)
casts = dict(
    zip(
        spells,
        [magic_missile_cast, drain_cast, dummy_cast, dummy_cast, dummy_cast],
    )
)
durations = dict(zip(spells, (0, 0, 6, 6, 5)))

start = {
    "player_hp": 50,
    "player_mana": 500,
    "boss_hp": boss_hp,
    "boss_damage": boss_damage,
    "mana_spent": 0,
    "magic_missile": 0,
    "drain": 0,
    "shield": 0,
    "poison": 0,
    "recharge": 0,
}
S = deque()
lowest_mana = inf


def validate_state(state):
    return (
        state["mana_spent"] <= lowest_mana
        and state["player_hp"] > 0
        and (state["boss_hp"] < 1 or (state["player_mana"] >= min_mana))
    )


def boss_turn(state):
    return {
        **state,
        "player_hp": state["player_hp"]
        - (state["boss_damage"] - (shield_armor * (state["shield"] != 0))),
    }


def update(state):
    """Calculate status effects for turn"""
    new = {}
    # No need to update state for each effect
    for spell in ["poison", "recharge", "shield"]:
        if state[spell] > 0:
            new.update(effects[spell](state))
            new[spell] = state[spell] - 1
    return {**state, **new}

def confirm_win(state): 
    return state["boss_hp"] < 1  and state["player_hp"] > 0


def cast(state, spell):
    new = casts[spell](state)
    new["mana_spent"] = state["mana_spent"] + costs[spell]
    new["player_mana"] = state["player_mana"] - costs[spell]
    new[spell] = durations[spell]
    return {**state, **new}

def test_one(state): 
    state = update(state)
    state = cast(state, "poison")
    state = update(state)
    state = boss_turn(state)
    state = update(state)
    state = cast(state, "magic_missile")
    state = update(state)
    assert state["player_hp"] == 2 and state["boss_hp"] == 0 and state["player_mana"] == 24

test_one({**start, **{"player_hp" : 10, "player_mana" : 250, "boss_hp" : 13, "boss_damage" : 8}})

S.appendleft(start)

while S:
    # Apply effects before player turn
    current = update(S.popleft())
    # Shield wears off on player's turn
    for spell in spells:
        # Can only cast if effect expired
        if current[spell] == 0 and costs[spell] <= current["player_mana"]:
            new_state = cast(current, spell)
            # Apply effects before boss turn
            new_state = update(new_state)
            #print(spell)
            #print(new_state)
            if not (player_won := confirm_win(new_state)): 
                new_state = boss_turn(new_state)
                #print(new_state)
            if validate_state(new_state):
                # Winning state: note mana cost
                if player_won:
                    #print(new_state)
                    lowest_mana = min(lowest_mana, new_state["mana_spent"])
                    #print(lowest_mana)
                    # print(new_state)
                else:
                    S.appendleft(new_state)

part1 = lowest_mana
print(part1)

S = deque()
lowest_mana = inf
S.appendleft(start)

while S:
    # Apply effects before player turn
    current = S.popleft()
    current["player_hp"] -= 1
    if current["player_hp"] < 1: 
        continue
    current = update(current)
    # Shield wears off on player's turn
    for spell in spells:
        # Can only cast if effect expired
        if current[spell] == 0 and costs[spell] <= current["player_mana"]:
            new_state = cast(current, spell)
            # Apply effects before boss turn
            new_state = update(new_state)
            #print(spell)
            #print(new_state)
            if not (player_won := confirm_win(new_state)): 
                new_state = boss_turn(new_state)
                #print(new_state)
            if validate_state(new_state):
                # Winning state: note mana cost
                if player_won:
                    #print(new_state)
                    lowest_mana = min(lowest_mana, new_state["mana_spent"])
                    #print(lowest_mana)
                    # print(new_state)
                else:
                    S.appendleft(new_state)
part2 = lowest_mana
print(part2)
