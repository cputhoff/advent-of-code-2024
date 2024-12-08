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
    

input = "input.txt"
map = input_to_lists(input)
# print(map)
guard_coord = find_guard(map)
guard_path = get_guard_path(map, guard_coord)
# print(len(guard_path))
# print(guard_path)
unique_coord = count_unique_coord(guard_path)
print(unique_coord)
