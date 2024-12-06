def input_to_list_with_dim(input):
    num_rows = 0
    num_col = 0

    with open(input, 'r') as f:
        content = f.read()
        num_rows = content.count('\n')
        num_col = int(len(content)/num_rows) - 1

    return (num_col, content.replace('\n',''))

def generate_searches(num_col, content):
    horizonal_searches = []
    vertical_searches = []
    bwd_diag_searches = []
    fwd_diag_searches = []
    word_len = 4
    vert_search_end = len(content) - int(3 * num_col)
    vert_search_offset_end = int(3 * num_col) + 1
    bwd_diag_step = num_col + 1
    bwd_diag_search_offset_end = int(3 * bwd_diag_step) + 1
    fwd_diag_step = num_col - 1
    fwd_diag_search_offset_end = int(3 * fwd_diag_step) + 1

    for i in range(len(content)):
        if (i % num_col) <= (num_col - word_len):
            horizonal_searches.append(content[i:i + word_len])
        if i < vert_search_end:
            vertical_searches.append(content[i:i + vert_search_offset_end:num_col])
        if ((i % num_col) <= (num_col - word_len)) and (i < vert_search_end):
            bwd_diag_searches.append(content[i:i + bwd_diag_search_offset_end:bwd_diag_step])
        if ((i % num_col) >= (word_len - 1)) and (i < vert_search_end):
            fwd_diag_searches.append(content[i:i + fwd_diag_search_offset_end:fwd_diag_step])
   
    all_searches = horizonal_searches + vertical_searches + bwd_diag_searches + fwd_diag_searches
    
    return all_searches

def count_xmas_matches(list):
    xmas_count = list.count('XMAS') + list.count('SAMX')
    return xmas_count

def generate_x_mas_searches(num_col, content):
    x_mas_searches = []
    word_len = 3
    vert_search_end = len(content) - int(2 * num_col)
    bwd_diag_step = num_col + 1
    bwd_diag_search_offset_end = int(2 * bwd_diag_step) + 1
    fwd_diag_step = num_col - 1
    fwd_diag_search_offset_end = int(2 * fwd_diag_step) + 3
    fwd_diag_search_offset_start = 2

    for i in range(len(content)):
        if ((i % num_col) <= (num_col - word_len)) and (i < vert_search_end):
            bwd_search = content[i:i + bwd_diag_search_offset_end:bwd_diag_step]
            fwd_search = content[i + fwd_diag_search_offset_start:i + fwd_diag_search_offset_end:fwd_diag_step]
            x_mas_searches.append(bwd_search + fwd_search)
    
    return x_mas_searches

def count_x_mas_matches(list):
    x_mas_count = list.count('MASMAS') + list.count('MASSAM') + list.count('SAMMAS') + list.count('SAMSAM')
    return x_mas_count
        

input = "input.txt"
(num_col, content) = input_to_list_with_dim(input)
searches = generate_searches(num_col, content)
xmas_count = count_xmas_matches(searches)
print("Part 1 Answer: " + str(xmas_count))

searches_x_mas = generate_x_mas_searches(num_col, content)
x_mas_count = count_x_mas_matches(searches_x_mas)
print("Part 2 Answer: " + str(x_mas_count))