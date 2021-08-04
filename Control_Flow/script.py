test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(a_string):
    for char in bad_chars:
        a_string = a_string.replace(char,"")
    return a_string

stripped_test_data = []

for year in test_data:
    yr = strip_characters(year)
    stripped_test_data.append(yr)

print(stripped_test_data)
