def input_to_lists(input):
    with open(input, 'r') as f:
        content = f.readlines()
        content_list = [[int(x) for x in list] for list in list(map(str.split, content))]
        return content_list

def safe_count(report_list):
    safe_counter = 0
    for report in report_list:
        increasing = True
        for i in range(len(report) - 1):
            step_size = report[i+1] - report[i]
            if i == 0 and step_size < 0:
                increasing = False
            if (step_size < 1 or step_size > 3) and increasing:
                break
            if (step_size > -1 or step_size < -3) and not increasing:
                break
            if i == len(report) - 2:
                safe_counter += 1
    return safe_counter



"""
def safe_with_dampener_count(report_list):
    safe_counter = 0
    for report in report_list:
        increasing = True
        bad_level_count = 0
        step_increasing = True
        skip_second = False
        for i in range(len(report) - 1):
            step_size = report[i+1] - report[i]
            if skip_second:
                step_size = report[i+1] - report[i-1]
                skip_second = False
            next_step_size = None
            next_step_increasing = True
            if step_size < 1:
                step_increasing = False
            else: step_increasing = True
            if i == 0 and step_size < 1:
                increasing = False
            # if i == 1 and bad_level_count == 1 and step_size < 1:
            #     increasing = False
            # if i == 1 and bad_level_count == 1 and step_size >= 1:
            #     increasing = True
            if (i < len(report) - 2) and (step_increasing == increasing):
                next_step_size = report[i+2] - report[i+1]
                if (next_step_size < 1):
                    next_step_increasing = False
            if (i < len(report) - 2) and ((step_increasing != increasing) or abs(step_size) > 3):
                next_step_size = report[i+2] - report[i]
                skip_second = True
                if (next_step_size < 1):
                    next_step_increasing = False
            if (i == 1 and (step_increasing != increasing) and (step_increasing == next_step_increasing)):
                increasing = step_increasing

            #print(str(i) + ": " + str(report[i]) + " step: " + str(step_size) + " skip: " + str(skip_second) + " inc: " + str(increasing) + " step_inc: " + str(step_increasing) + " bad: " + str(bad_level_count) + " next_step: " + str(next_step_size))

            if (step_size < 1 or step_size > 3) and increasing:
                bad_level_count += 1
                if next_step_size is not None and (next_step_size < 1 or next_step_size > 3) and increasing:
                    break
            if (step_size > -1 or step_size < -3) and not increasing:
                bad_level_count += 1
                if next_step_size is not None and (next_step_size > -1 or next_step_size < -3) and not increasing:
                    break
            if bad_level_count > 1:
                break
            if i == len(report) - 2:
                safe_counter += 1
    return safe_counter
"""

report_list = input_to_lists("input.txt")
# print(safe_count(report_list))
#print(safe_with_dampener_count(report_list))

#test_list = [[3, 4, 2, 5, 6]]
#test_list = [[3, 4, 5, 6]]
#test_list = [[3, 2, 4, 5, 6]]
# test_list = [[3, 4, 5, 6, 6]]
test_list = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
#test_list = [[1, 2, 7, 8, 9]]
# print(test_list[0][3])
# print(len(test_list[0]))
#print(safe_with_dampener_count(test_list))

#print(safe_with_dampener_count(report_list[:5]))