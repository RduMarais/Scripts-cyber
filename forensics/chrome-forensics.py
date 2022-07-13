#!/bin/python3 

import datetime

def to_time(timestamp):
	return (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=timestamp))

def to_timestamp(dt):
	a = dt-datetime.datetime(1601, 1, 1)
	b = '{0:f}'.format((a.total_seconds()*1000000))
	return b[:-7]

def convert_csv_historique(column_timestamp,in_filename,out_filename):
	with open(in_filename, mode ='r')as file:
		csvFile = csv.reader(file, delimiter=';',quotechar='"')
		for lines in csvFile:
			hist.append(lines)

	for lines in hist[1:]:
		lines.append(str(to_time(int(lines[column_timestamp]))))

	with open(out_filename,'w') as csvfile:
		csvwriter = csv.writer(csvfile,delimiter=';',quotechar='"')
		for lines in hist:
			csvwriter.writerow(lines)

