#!/usr/bin/env python

from xlrd import open_workbook
import csv
import os

def convert(inputfile, outputfile):
	print "Converting", inputfile
	book = open_workbook(inputfile)

	sheet = book.sheet_by_name('mutations')

	output_values = []

	for r in range(sheet.nrows):
		if r == 0:
			header = sheet.row(r)
		else:
			row = sheet.row(r)

			d = row[0].value.replace('-', '/')
			raw_amount = row[2].value
			inout = row[3].value

			if inout == u'Debet':
				amount = 0 - raw_amount
			else:
				amount = raw_amount

			description = row[7].value

			print "Found values", d, amount, description

			output_values.append([d, amount, description])

	writer = csv.writer(open(outputfile, 'w'))
	writer.writerows(output_values)

if __name__ == '__main__':
	sources = [name for name in os.listdir(os.getcwd()) if '.xls' in name]

	for source in sources:
		convert(source, '%s.csv' % source[:-4])