def get_series():
    len_of_list = int(input("Enter the Input: "))
    output_list = []
    if len_of_list % 2 == 0:
        len_of_list -= 1
    j = 1
    while len(output_list) != len_of_list:
        output_list.append(str(j))
        j += 2
    print("Output:", ', '.join(map(str, output_list)))
get_series()