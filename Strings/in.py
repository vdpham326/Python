def contains(big_string, little_string):
  if little_string in big_string:
    return True
  return False

def common_letters(string_one, string_two):
  new_lst = []
  for letter in string_one:
    if letter in string_two and letter not in new_lst:
      new_lst.append(letter)
  return new_lst


# 2nd version
def contains(big_string, little_string):
  return little_string in big_string


def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
