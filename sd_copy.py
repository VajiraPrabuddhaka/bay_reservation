import copy

# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = old_list
old_list = 23
new_list = copy.copy(old_list)


print("Old list:", id(old_list))
print("New list:", id(new_list))