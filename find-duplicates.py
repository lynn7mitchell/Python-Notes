some_list = ['a', 'n', 'd', 'n', 'g', 'q', 'w', 'd']

duplicates = []

for item in some_list:
  if some_list.count(item) > 1:
    if item not in duplicates:
      duplicates.append(item)

print(duplicates)
  