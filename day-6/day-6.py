def input_to_lists(input):
    with open(input, 'r') as f:
        content = f.readlines()
        content = [line.rstrip('\n') for line in content]
    return content

def find_guard(map):
    guard_coord = []
    for i, row in enumerate(map):
        if row.find('^') != -1:
            guard_coord = (i, row.find('^'))

    return guard_coord

def get_guard_path(map, guard_coord):
    path = []
    num_rows = len(map)
    num_cols = len(map[0])
    curr_coord = guard_coord
    direction = "up"

    while True:
        path.append(curr_coord)
        if direction == "up":
            next_coord = (curr_coord[0] - 1, curr_coord[1])

            if next_coord[0] == -1:
                return path
            
            if map[next_coord[0]][next_coord[1]] == '#':
                direction = "right"
                next_coord = (curr_coord[0], curr_coord[1] + 1)

            curr_coord = next_coord
            continue
        if direction == "right":
            next_coord = (curr_coord[0], curr_coord[1] + 1)

            if next_coord[1] == num_cols:
                return path
            
            if map[next_coord[0]][next_coord[1]] == '#':
                direction = "down"
                next_coord = (curr_coord[0] + 1, curr_coord[1])

            curr_coord = next_coord
            continue
        if direction == "down":
            next_coord = (curr_coord[0] + 1, curr_coord[1])

            if next_coord[0] == num_rows:
                return path
            
            if map[next_coord[0]][next_coord[1]] == '#':
                direction = "left"
                next_coord = (curr_coord[0], curr_coord[1] - 1)

            curr_coord = next_coord
            continue
        if direction == "left":
            next_coord = (curr_coord[0], curr_coord[1] - 1)

            if next_coord[1] == -1:
                return path
            
            if map[next_coord[0]][next_coord[1]] == '#':
                direction = "up"
                next_coord = (curr_coord[0] - 1, curr_coord[1])

            curr_coord = next_coord
            continue
            
def count_unique_coord(path):
    return len(set(path))

def will_guard_loop(map, guard_coord):
    visited_cell_init_direction = {}
    num_rows = len(map)
    num_cols = len(map[0])
    curr_coord = guard_coord
    direction = "up"

    while True:
        if visited_cell_init_direction.get(curr_coord) == direction:
            return True

        if visited_cell_init_direction.get(curr_coord) == None:
            visited_cell_init_direction[curr_coord] = direction

        if direction == "up":
            next_coord = (curr_coord[0] - 1, curr_coord[1])

            if next_coord[0] == -1:
                return False
            
            if map[next_coord[0]][next_coord[1]] == '#':
                direction = "right"
                next_coord = (curr_coord[0], curr_coord[1] + 1)

            curr_coord = next_coord
            continue
        if direction == "right":
            next_coord = (curr_coord[0], curr_coord[1] + 1)

            if next_coord[1] == num_cols:
                return False
            
            if map[next_coord[0]][next_coord[1]] == '#':
                direction = "down"
                next_coord = (curr_coord[0] + 1, curr_coord[1])

            curr_coord = next_coord
            continue
        if direction == "down":
            next_coord = (curr_coord[0] + 1, curr_coord[1])

            if next_coord[0] == num_rows:
                return False
            
            if map[next_coord[0]][next_coord[1]] == '#':
                direction = "left"
                next_coord = (curr_coord[0], curr_coord[1] - 1)

            curr_coord = next_coord
            continue
        if direction == "left":
            next_coord = (curr_coord[0], curr_coord[1] - 1)

            if next_coord[1] == -1:
                return False
            
            if map[next_coord[0]][next_coord[1]] == '#':
                direction = "up"
                next_coord = (curr_coord[0] - 1, curr_coord[1])

            curr_coord = next_coord
            continue

    # path = []
    # right_turn_coord = []
    # down_turn_coord = []
    # left_turn_coord = []
    # up_turn_coord = []
    # num_rows = len(map)
    # num_cols = len(map[0])
    # curr_coord = guard_coord
    # direction = "up"

    # while True:
    #     path.append(curr_coord)
    #     if direction == "up":
    #         next_coord = (curr_coord[0] - 1, curr_coord[1])

    #         if next_coord[0] == -1:
    #             return False
            
    #         if map[next_coord[0]][next_coord[1]] == '#':
    #             right_turn_coord.append(curr_coord)
    #             if right_turn_coord.count(curr_coord) > 1:
    #                 return True
    #             direction = "right"
    #             next_coord = (curr_coord[0], curr_coord[1] + 1)

    #         curr_coord = next_coord
    #         continue
    #     if direction == "right":
    #         next_coord = (curr_coord[0], curr_coord[1] + 1)

    #         if next_coord[1] == num_cols:
    #             return False
            
    #         if map[next_coord[0]][next_coord[1]] == '#':
    #             down_turn_coord.append(curr_coord)
    #             if down_turn_coord.count(curr_coord) > 1:
    #                 return True
    #             direction = "down"
    #             next_coord = (curr_coord[0] + 1, curr_coord[1])

    #         curr_coord = next_coord
    #         continue
    #     if direction == "down":
    #         next_coord = (curr_coord[0] + 1, curr_coord[1])

    #         if next_coord[0] == num_rows:
    #             return False
            
    #         if map[next_coord[0]][next_coord[1]] == '#':
    #             left_turn_coord.append(curr_coord)
    #             if left_turn_coord.count(curr_coord) > 1:
    #                 return True
    #             direction = "left"
    #             next_coord = (curr_coord[0], curr_coord[1] - 1)

    #         curr_coord = next_coord
    #         continue
    #     if direction == "left":
    #         next_coord = (curr_coord[0], curr_coord[1] - 1)

    #         if next_coord[1] == -1:
    #             return False
            
    #         if map[next_coord[0]][next_coord[1]] == '#':
    #             up_turn_coord.append(curr_coord)
    #             if up_turn_coord.count(curr_coord) > 1:
    #                 return True
    #             direction = "up"
    #             next_coord = (curr_coord[0] - 1, curr_coord[1])

    #         curr_coord = next_coord
    #         continue

def check_obstruction_options(map, guard_coord):
    paths = get_guard_path(map, guard_coord)
    unique_paths = set(paths)
    num_loop = 0

    for path in unique_paths:
        if path == guard_coord:
            continue
        obstruction_map = map[:]
        map_list = list(obstruction_map[path[0]])
        map_list[path[1]] = '#'
        new_map_line = "".join(map_list)
        obstruction_map[path[0]] = new_map_line
        if will_guard_loop(obstruction_map, guard_coord):
            # print(obstruction_map)
            num_loop += 1
    return num_loop


input = "input.txt"
map = input_to_lists(input)
# print(map)
guard_coord = find_guard(map)
guard_path = get_guard_path(map, guard_coord)
# print(len(guard_path))
# print(guard_path)
unique_coord = count_unique_coord(guard_path)
# print(unique_coord)
print(check_obstruction_options(map, guard_coord))
