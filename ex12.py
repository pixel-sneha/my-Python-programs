input_list = input().split(', ')
if len(input_list) >= 5:
    print([input_list[0], input_list[1], input_list[len(input_list) - 2], input_list[len(input_list) - 1]])
else:
    print([input_list[0], input_list[len(input_list) - 1]])

