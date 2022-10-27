#!/usr/bin/python3

import sys

result = dict()

with open(str(sys.argv[1]), "rt") as f:
	for row in f:
		movie_info = row.split("::")

		genres = movie_info[2]
		genre = genres.split("|")

		for g in genre:
			g = g.strip()
			if g not in result:
				result[g] = 1
			else:
				result[g] += 1

with open(str(sys.argv[2]), "wt") as fp:
	for key, value in result.items():
		fp.write(key + " " + str(value) + "\n")

