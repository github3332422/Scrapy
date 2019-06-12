import csv
from csv import writer
def write_csv_two():
		headers = {'username','age','height'}
		values = [
			{'username': 'zs', 'age': 15, 'height': 60},
			{'username': 'ls', 'age': 15, 'height': 60}
		]
		with open('demo2.csv', 'w',encoding='utf-8',newline='')as fp:
			writer = csv.DictWriter(fp,headers)
			writer.writeheader()
			writer.writerows(values)

def write_csv_one():
		headers = {'username','age','height'}
		values = {
			('zs',15,60),
			('ls', 15, 60),
			('ww', 15, 60)
		}
		with open('demo.csv', 'w',encoding='utf-8',newline='')as fp:
			writer = csv.writer(fp)
			writer.writerow(headers)
			writer.writerows(values)

def write_csv():
	values = {
		('zs', 15, 60),
		('ls', 15, 60),
		('ww', 15, 60)
	}
	with open("Dd.csv", 'w')as fp:
		wrtr = csv.writer(fp)
		for r in values:
			wrtr.writerow(r)

def writer_csv_file(data,file_name):
    with open(file_name,'w') as new_csv_file:
        w = csv.writer(new_csv_file)
        for row in data:
            w.writerow(row)

write_csv()
