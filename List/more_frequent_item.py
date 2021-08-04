def more_frequent_item(lst, item1, item2):
  item1_count = lst.count(item1)
  item2_count = lst.count(item2)

  if item1_count >= item2_count:
    return item1
  return item2

# 2nd version

def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
