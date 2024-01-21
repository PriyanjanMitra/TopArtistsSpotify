import csv
file= open('topartists.csv', 'a')
csv_writer=csv.writer(file)
csv_writer.writerow(['Artist','Appearances'])
file.close()