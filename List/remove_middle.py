def remove_middle(lst, start, end):
  return lst[:start] + lst[end + 1:]


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
