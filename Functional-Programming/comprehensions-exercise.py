some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# set() makes it a set so it can't have duplicates
# list(set())
duplicates = list(set(value for value in some_list if some_list.count(value)>1))


print(duplicates)