def extract_rules_and_updates_from_input(input):
    rules = []
    updates = []

    with open(input, 'r') as f:
        line = f.readline()
        
        while line:
            if line.find('|') != -1:
                rules.append(line.rstrip('\n').split('|'))
            elif line.find(',') != -1:
                updates.append(line.rstrip('\n').split(','))
            line = f.readline()

    return (rules, updates)

def create_rule_map(rules):
    rule_map = {}

    for rule in rules:
        if rule[0] in rule_map:
            rule_map[rule[0]].append(rule[1])
        else:
            rule_map.update({rule[0]: [rule[1]]})

    return rule_map

def get_valid_updates(updates, rule_map):
    valid_updates = []

    for update in updates:
        if is_update_valid(update, rule_map):
            valid_updates.append(update)

    return valid_updates

def is_update_valid(update, rule_map):
    for i, page in enumerate(update):
        if page not in rule_map:
            return False
        next_pages = set(update[i + 1:len(update)])
        successors_in_next_pages = set(rule_map[page]) & next_pages
        if successors_in_next_pages != next_pages:
            return False
        if i == len(update) - 2:
            return True
    return True

def get_invalid_updates(updates, rule_map):
    invalid_updates = []

    for update in updates:
        if is_update_valid(update, rule_map) == False:
            invalid_updates.append(update)

    return invalid_updates

def fix_update(update, rule_map):
    fixed_update = update
    i = 0

    while i < len(fixed_update):
        if is_update_valid(fixed_update, rule_map):
            return fixed_update
        if fixed_update[i] not in rule_map:
            fixed_update = fixed_update[:i] + fixed_update[i + 1:] + fixed_update[i:i + 1]
            continue
        next_pages = set(fixed_update[i + 1:len(fixed_update)])
        successors_in_next_pages = set(rule_map[fixed_update[i]]) & next_pages
        if successors_in_next_pages != next_pages:
            should_be_predecessors = next_pages - successors_in_next_pages
            max_predecessor_index = max([fixed_update.index(predecessor) for predecessor in should_be_predecessors])
            fixed_update = (fixed_update[:i]
                            + fixed_update[max_predecessor_index:max_predecessor_index + 1]
                            + fixed_update[i:i + 1]
                            + fixed_update[i + 1:max_predecessor_index]
                            + fixed_update[max_predecessor_index + 1:])
        else:
            i += 1
    
    return fixed_update

def fix_all_updates(invalid_updates, rule_map):
    fixed_updates = []

    for update in invalid_updates:
        fixed_updates.append(fix_update(update, rule_map))

    return fixed_updates

def sum_middle_pages(updates):
    sum = 0

    for update in updates:
        sum += int(update[int(len(update) / 2)])
    return sum


input = "input.txt"
(rules, updates) = extract_rules_and_updates_from_input(input)
rule_map = create_rule_map(rules)
valid_updates = get_valid_updates(updates, rule_map)
middle_page_sum = sum_middle_pages(valid_updates)
print("Part 1: " + str(middle_page_sum))
invalid_updates = get_invalid_updates(updates, rule_map)
fixed_updates = fix_all_updates(invalid_updates, rule_map)
fixed_middle_page_sum = sum_middle_pages(fixed_updates)
print("Part 2: " + str(fixed_middle_page_sum))