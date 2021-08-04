def more_than_n(lst, item, n):
  count = 0
  for l in lst:
    if l == item:
      count += 1
  if count > n:
    return True
  return False


#2nd version

def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  return False
