def combine_sort(lst1, lst2):
  for i in lst2:
    lst1.append(i)
  return sorted(lst1)

# 2nd version
def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sortedList = sorted(unsorted)
  return sortedList
