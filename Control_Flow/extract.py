def extract(index):
  app = []
  for row in apps_data[1:]:
    val = row[index]
    app.append(val)
  return app

opened_file = open("AppleStore.csv")
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()
