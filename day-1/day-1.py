def input_to_lists(input):
    with open(input, 'r') as f:
        content = f.read()
        all_content = content.split()
        left_list = list(map(int, all_content[::2]))
        right_list = list(map(int, all_content[1::2]))
        return ((left_list, right_list))

def calc_dist_input(left_list, right_list):
    dist_sum = 0
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    for left, right in zip(left_list, right_list):
        dist_sum += abs(left - right)
    print(dist_sum)

def calc_similar_input(left_list, right_list):
    similar_sum = 0
    for left_elt in left_list:
        similar_sum += left_elt * right_list.count(left_elt)
    print(similar_sum)

left_list, right_list = input_to_lists("input.txt")    
calc_dist_input(left_list, right_list)
calc_similar_input(left_list, right_list)