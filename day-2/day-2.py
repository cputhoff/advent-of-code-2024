def input_to_lists(input):
    with open(input, 'r') as f:
        content = f.readlines()
        content_list = [[int(x) for x in list] for list in list(map(str.split, content))]
        return content_list

def is_safe(list):
    safe = False
    increasing = True
    for i in range(len(list) - 1):
        step_size = list[i+1] - list[i]
        if i == 0 and step_size < 0:
            increasing = False
        if (step_size < 1 or step_size > 3) and increasing:
            break
        if (step_size > -1 or step_size < -3) and not increasing:
            break
        if i == len(list) - 2:
            safe = True
    return safe

def safe_count(report_list):
    safe_list = list(map(is_safe, report_list))
    return sum(safe_list)

def safe_with_dampener(list):
    if is_safe(list):
        return True
    
    for i in range(len(list)):
        if is_safe(list[:i] + list[i+1:]):
            return True
        
    return False

def safe_with_dampener_count(report_list):
    safe_list = list(map(safe_with_dampener, report_list))
    return sum(safe_list)


report_list = input_to_lists("input.txt")
print(safe_count(report_list))
print(safe_with_dampener_count(report_list))