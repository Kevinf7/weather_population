import csv, json

csv_file = open('cities_final.csv', 'r')
json_file = open('cities_final.json', 'w')

reader = csv.DictReader(csv_file)

json_file.write('[\n')
for row in reader:
    json.dump(row, json_file)
    if reader.line_num <= 200:
        json_file.write(', \n')

json_file.write('\n]')
