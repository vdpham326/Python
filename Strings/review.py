def username_generator(first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    return first_name + last_name
  return first_name[:3] + last_name[:4]


def password_generator(username):
  password = ""
  for i in range(0, len(username)):
    password += username[i - 1]
  return password

# 2nd version


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name


def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
