# my_list = [1,2,3,4,5]
#
#
#
# def length(list:list):
#     len = 0
#     for elements in list:
#         len += 1
#     return len
#
# new_list = [0] * (length(my_list)-1)
# for i in range(length(my_list)-1):
#     new_list[i] = my_list[i]
#
# # another method
# # for i in range(length(my_list)-1):
# #     new_list = new_list + [my_list[i]]
#
# my_list = new_list
#
# print(new_list)
# print(my_list)

''' Insert Method '''

my_list = [1, 2, 3, 5]

# Manually insert the element 4 at position 3
position_to_insert = 3
element_to_insert = 4

new_list = []
for i in range(len(my_list)):
    if i == position_to_insert:
        new_list.append(element_to_insert)
    new_list.append(my_list[i])

my_list = new_list

print(my_list)
