def max_num(num1, num2, num3):
  if (num1 == num2 or num2 == num3 or num3 == num1):
    return "It's a tie!"

  if num1 > num2:
    if num1 > num3:
      return num1
    else:
      return num3
  elif num2 > num3:
    return num2
  else:
    return num3


#version 2
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
