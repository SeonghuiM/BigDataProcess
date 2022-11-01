#!/usr/bin/python3

import sys
from datetime import datetime, date

def what_day(date):
	datetime_date = datetime.strptime(date, "%Y-%m-%d")
	days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = datetime_date.weekday()
	return days[day]

result1 = dict()
result2 = dict()

with open(str(sys.argv[1]), "rt") as f:
	for row in f:
		uber_info = row.split(",")
		
		base_num = uber_info[0]

		date = uber_info[1]
		ds = date.split("/")
		dt = ds[2] + "-" + ds[0] + "-" + ds[1]
		day = what_day(dt)

		vehicles = int(uber_info[2])
		
		trips = int(uber_info[3].strip())
		
		if base_num not in result1:
			result1[base_num] = {}
			if day not in result1[base_num]:
				result1[base_num][day] = vehicles
		else:
			if day not in result1[base_num]:
				result1[base_num][day] = vehicles
			else:
				result1[base_num][day] += vehicles
		
		if base_num not in result2:
			result2[base_num] = {}
			if day not in result2[base_num]:
				result2[base_num][day] = trips
		else:
			if day not in result2[base_num]:
				result2[base_num][day] = trips
			else:
				result2[base_num][day] += trips

with open(str(sys.argv[2]), "wt") as fp:
	for key in result1:
		for a in result1[key]:
			fp.write(key + "," + a + " " + str(result1[key][a]) + "," + str(result2[key][a]) + "\n")

