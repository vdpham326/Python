def append_sum(lst):
  for i in range(3):
    sum = lst[-1] + lst[-2]
    lst.append(sum)
  return lst

print(append_sum([1, 2]))
# for i in range(1, 10):
#   print(i)
