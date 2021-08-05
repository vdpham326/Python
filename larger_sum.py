def larger_sum(lst1, lst2):
  sum_lst1 = 0
  sum_lst2 = 0

  for val in lst1:
    sum_lst1 += val
  for val in lst2:
    sum_lst2 += val

  if sum_lst1 >= sum_lst2:
    return lst1
  return lst2
