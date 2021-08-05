def same_values(lst1, lst2):
  new_lst = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      new_lst.append(i)
  return new_lst
