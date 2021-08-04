from csv import reader
opened_file = open("artworks.csv")
read_file = reader(opened_file)
moma = list(read_file)
opened_file.close()

moma = moma[1:]

for row in moma:
    # remove parentheses from the nationality column
    nationality = row[2]
    nationality = nationality.replace("(", "")
    nationality = nationality.replace(")", "")
    row[2] = nationality

    # remove parentheses from the gender column
    gender = row[5]
    gender = gender.replace("(", "")
    gender = gender.replace(")", "")
    row[5] = gender
