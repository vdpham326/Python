def over_nine_thousand(lst):
  sum = 0
  if len(lst) == 0:
    return 0
  for num in lst:
    if sum < 9000:
      sum += num
  return sum

# 2nd version


def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))
