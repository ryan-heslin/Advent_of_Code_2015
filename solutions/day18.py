from functools import cache

# Read input as list of line strings
@cache
def in_range(x, lower=0, upper=99):
    return lower <= x <= upper


@cache
def get_neighbors(coord, offsets, min=0, max=99):

    neighbors = set()
    # (0, 0) => top left
    # (0, 99) => top right
    # (99, 0) => bottom left
    # (99, 99) => bottom right
    orig_y, orig_x = coord

    for coord in offsets:
        y, x = coord
        new_y = orig_y + y
        if not in_range(new_y, min, max):
            continue
        new_x = orig_x + x
        if not in_range(new_x, min, max):
            continue
        neighbors.add((new_y, new_x))
    return neighbors


# Get neighbors and read initial grid


def create_neighbors():
    neighbors = {}
    status = {}
    for y, row in enumerate(raw_input):
        for x, char in enumerate(row):
            key = (x, y)
            neighbors[key] = get_neighbors(key, offsets=offsets)
            status[key] = char == ON
    return neighbors, status


def simulate(status, neighbors, iterations=100, check_corners=False):

    corners = {(0, 0), (0, 99), (99, 0), (99, 99)}
    # Update grid
    for _ in range(iterations):
        to_change = {}
        # For each coord, find how many neighbors were on last iteration
        for coord, coord_neighbors in neighbors.items():
            neighbors_on = sum(status[neighbor] for neighbor in coord_neighbors)

            # on -> off
            # Keep corners on always
            if status[coord] and not in_range(neighbors_on, 2, 3):
                if not (check_corners and (coord in corners)):
                    to_change[coord] = False
            # off -> on
            elif not status[coord] and neighbors_on == 3:
                to_change[coord] = True
        # Update old status
        status.update(to_change)
    return sum(status.values())


with open("inputs/day18.txt") as f:
    raw_input = f.read().splitlines()

ON = "#"
# Y, x offsets of all 8 neighbors, counterclockwise from top left
offsets = tuple(
    zip(
        (
            -1,
            -1,
            -1,
            0,
            1,
            1,
            1,
            0,
        ),
        (-1, 0, 1, 1, 1, 0, -1, -1),
    )
)


neighbors, status = create_neighbors()
part1 = simulate(status, neighbors)
print(part1)

neighbors, status = create_neighbors()
part2 = simulate(status, neighbors, check_corners=True)
print(part2)
