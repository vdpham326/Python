def every_three_nums(start):
  lst = []
  if start > 100:
    return []
  for i in range(start, 101, 3):
      lst.append(i)
  return lst

# 2nd version
def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))
