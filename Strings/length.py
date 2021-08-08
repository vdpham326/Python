def get_length(str):
  str_size = 0
  for letter in str:
    str_size += 1
  return str_size


print(get_length("Hello"))
