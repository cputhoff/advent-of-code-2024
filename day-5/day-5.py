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
        for i, page in enumerate(update):
            if page not in rule_map:
                break
            next_pages = set(update[i + 1:len(update)])
            successors_in_next_pages = set(rule_map[page]) & next_pages
            if successors_in_next_pages != next_pages:
                break
            if i == (len(update) - 2):
                valid_updates.append(update)

    return valid_updates

def is_update_valid(update):
    for i, page in enumerate(update):
        if page not in rule_map:
            return False
        next_pages = set(update[i + 1:len(update)])
        successors_in_next_pages = set(rule_map[page]) & next_pages
        if successors_in_next_pages != next_pages:
            return False
    return True

def get_invalid_updates(updates, rule_map):
    invalid_updates = []

    for update in updates:
        for i, page in enumerate(update):
            if page not in rule_map:
                break
    return invalid_updates

def sum_middle_pages(updates):
    sum = 0

    for update in updates:
        sum += int(update[int(len(update) / 2)])
    return sum


input = "input.txt"
(rules, updates) = extract_rules_and_updates_from_input(input)
rule_map = create_rule_map(rules)
#print(rule_map)
valid_updates = get_valid_updates(updates, rule_map)
#print(valid_updates)
middle_page_sum = sum_middle_pages(valid_updates)
print(middle_page_sum)