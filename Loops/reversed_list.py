def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    if lst1[i] != lst2[(len(lst2) -1) - i]:
      return False
  return True

#print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
