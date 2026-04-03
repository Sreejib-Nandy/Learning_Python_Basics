color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

indexes_to_remove = [0, 4, 5]

new_list = [color_list[i] for i in range(len(color_list)) if i not in indexes_to_remove]

print(new_list)
