def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date


for row in moma:
    begin_date = clean_and_convert(row[3])
    end_date = clean_and_convert(row[4])

    row[3] = begin_date
    row[4] = end_date
