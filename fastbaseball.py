#!/usr/bin/python

from lxml import html
import requests
import random
import re
import sys

# get the date that the game was played, MMDD
# regex checking only allows chars 0-9, and len() check only allows 4 chars 
datePlayed = raw_input("What date was this game played, for example 0513, MMDD? ")
if not re.match("^[0-9]*$", datePlayed):
	print "Error! Only numbers 0-9 are allowed!"
	sys.exit()
elif len(datePlayed) > 4:
	print "Error! Only 4 characters allowed!"
	sys.exit()

# get the game the user wants to view CHC@NYM, etc
# no error checking setup, user can enter whatever they want
teamsPlaying = raw_input("What game do you want to view, for example NYM@CHC, or CHC@NYM? ")

# scrape website using xpath

page = requests.get('http://www.cbssports.com/mlb/gametracker/playbyplay/MLB_2015' + datePlayed + "_" + teamsPlaying.upper())
tree = html.fromstring(page.text)

scores = tree.xpath('//*[@id="inning"]/td/text()')

runsHometeam = ""
runsVisteam = ""

hitsHometeam = ""
hitsVisteam = ""

# 1st inning

if len(scores) >= 1:
	if "0 Runs" in scores[0]:
		runsVisteam = [1]

if len(scores) >= 2:
	if "0 Runs" in scores[1]:
		runsHometeam = [1]

# 2nd innning

if len(scores) >= 3:
	if "0 Runs" in scores[2]:
		runsVisteam.append(2)


if len(scores) >= 4:
	if "0 Runs" in scores[3]:
		runsHometeam.append(2)

# 3rd inning

if len(scores) >= 5:
	if "0 Runs" in scores[4]:
		runsVisteam.append(3)

if len(scores) >= 6:
	if "0 Runs" in scores[5]:
		runsHometeam.append(3)

# 4th inning

if len(scores) >= 7:
	if "0 Runs" in scores[6]:
		runsVisteam.append(4)

if len(scores) >= 8:
	if "0 Runs" in scores[7]:
		runsHometeam.append(4)

# 5th inning

if len(scores) >= 9:
	if "0 Runs" in scores[8]:
		runsVisteam.append(5)

if len(scores) >= 10:
	if "0 Runs" in scores[9]:
		runsHometeam.append(5)

#6th inning

if len(scores) >= 11:
	if "0 Runs" in scores[10]:
		runsVisteam.append(6)

if len(scores) >= 12:
	if "0 Runs" in scores[11]:
		runsHometeam.append(6)

# 7th inning

if len(scores) >= 13:
	if "0 Runs" in scores[12]:
		runsVisteam.append(7)

if len(scores) >= 14:
	if "0 Runs" in scores[13]:
		runsHometeam.append(7)

# 8th inning

if len(scores) >= 15:
	if "0 Runs" in scores[14]:
		runsVisteam.append(8)

if len(scores) >= 16:
	if "0 Runs" in scores[15]:
		runsHometeam.append(8)

# 9th inning

if len(scores) >= 17:
	if "0 Runs" in scores[16]:
		runsVisteam.append(9)

if len(scores) >= 18:
	if "0 Runs" in scores[17]:
		runsHometeam.append(9)

# pull 3 random innings

skipNowhome = random.sample(runsHometeam, 3)
skipNowvisitor = random.sample(runsVisteam, 3)

#print "Innings where the visiting team didn't get any hits: %s" % hitsVisteam
#print "Innings where the home team didn't get any hits: %s" % hitsHometeam

# ask user what team they want to know about Home or Visitor

userTeam = raw_input("What team do you want, Home or Visitor? ")

# checks if user entered home or visitor, and uses the lower() function on the inputted user variable

if "home" in userTeam.lower():
	print "You can skip the home team bottom inning numbers: %s" % skipNowhome
elif "visitor" in userTeam.lower():
	print "You can skip the vistor team top inning numbers: %s" % skipNowvisitor
else:
	print "Unrecognized team, please enter either Home or Visitor"
