#!/usr/bin/python3

import sys

names = {}

def addName(name):
	global names
	if not name in names:
		names[name] = "city" + str(len(names))

def humanify(line):
	if line[0] == "#" or len(line.strip()) == 0:
		return ""
	
	global names
	words = line.strip().split(";")
	comm = words[0]
	if comm == "newRoute":
		comm, rid, name1, name2 = words
		addName(name1)
		addName(name2)
		return " ".join([comm, rid, names[name1], names[name2]])
	elif comm == "addRoad":
		comm, name1, name2, length, year = words
		addName(name1)
		addName(name2)
		return " ".join([comm, names[name1], names[name2], length, year])
	elif comm == "repairRoad":
		comm, name1, name2, year = words
		addName(name1)
		addName(name2)
		return " ".join([comm, names[name1], names[name2], year])
	elif comm == "removeRoad":
		comm, name1, name2 = words
		addName(name1)
		addName(name2)
		return " ".join([comm, names[name1], names[name2]])
	elif comm == "extendRoute":
		comm, rid, name = words
		addName(name)
		return " ".join([comm, rid, names[name]])
	elif comm == "getRouteDescription":
		comm, rid = words
		return " ".join([comm, rid])
	else:
		return "DUPNA KOMENDA"

if len(sys.argv) < 2:
	print("Give file.")

lines = open(sys.argv[1], 'r').readlines()

for nr, line in enumerate(lines):
	print("%d: %s" % (nr + 1, humanify(line)))
	
