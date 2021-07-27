opened_file = open("AppleStore.csv")
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()


def freq_table(column):
    frequency_table = {}
    for value in column:
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    return frequency_table


genres_ft = freq_table(genres)
