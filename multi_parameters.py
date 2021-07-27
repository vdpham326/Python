from csv import reader
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION


def freq_table(data_set, index):
    frequency_table = {}

    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1

    return frequency_table


ratings_ft = freq_table(data_set=apps_data, index=7)
