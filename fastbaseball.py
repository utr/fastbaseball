#!/usr/bin/python

from lxml import html
import requests
import random

# scrape the website

page = requests.get('http://www.cbssports.com/mlb/gametracker/playbyplay/MLB_20150513_NYM@CHC')
tree = html.fromstring(page.text)

scores = tree.xpath('//*[@id="inning"]/td/text()')
skipHometeam = ""
skipVisteam = ""

# 1st inning

if len(scores) >= 1:
	firstTop = scores[0]
	if "0 Runs" in firstTop:
		skipVisteam = [1]

if len(scores) >= 2:
	firstBottom = scores[1]
	if "0 Runs" in firstBottom:
		skipHometeam = [1]

# 2nd innning

if len(scores) >= 3:
	secondTop = scores[2]
	if "0 Runs" in secondTop:
		skipVisteam.append(2)

if len(scores) >= 4:
	secondBottom = scores[3]
	if "0 Runs" in secondBottom:
		skipHometeam.append(2)

# 3rd inning

if len(scores) >= 5:
	thirdTop = scores[4]
	if "0 Runs" in thirdTop:
		skipVisteam.append(3)

if len(scores) >= 6:
	thirdBottom = scores[5]
	if "0 Runs" in thirdBottom:
		skipHometeam.append(3)

# 4th inning

if len(scores) >= 7:
	fourthTop = scores[6]
	if "0 Runs" in fourthTop:
		skipVisteam.append(4)

if len(scores) >= 8:
	fourthBottom = scores[7]
	if "0 Runs" in fourthBottom:
		skipHometeam.append(4)

# 5th inning

if len(scores) >= 9:
	fifthTop = scores[8]
	if "0 Runs" in fifthTop:
		skipVisteam.append(5)

if len(scores) >= 10:
	fifthBottom = scores[9]
	if "0 Runs" in fifthBottom:
		skipHometeam.append(5)

#6th inning

if len(scores) >= 11:
	sixthTop = scores[10]
	if "0 Runs" in sixthTop:
		skipVisteam.append(6)

if len(scores) >= 12:
	sixthBottom = scores[11]
	if "0 Runs" in sixthBottom:
		skipHometeam.append(6)

# 7th inning

if len(scores) >= 13:
	seventhTop = scores[12]
	if "0 Runs" in seventhTop:
		skipVisteam.append(7)

if len(scores) >= 14:
	seventhBottom = scores[13]
	if "0 Runs" in seventhBottom:
		skipHometeam.append(7)

# 8th inning

if len(scores) >= 15:
	eighthTop = scores[14]
	if "0 Runs" in eighthTop:
		skipVisteam.append(8)

if len(scores) >= 16:
	eighthBottom = scores[15]
	if "0 Runs" in eighthBottom:
		skipHometeam.append(8)

# 9th inning

if len(scores) >= 17:
	ninthTop = scores[16]
	if "0 Runs" in ninthTop:
		skipVisteam.append(9)

if len(scores) >= 18:
	ninthBottom = scores[17]
	if "0 Runs" in ninthBottom:
		skipHometeam.append(9)

# pull 3 random innings

skipNowhome = random.sample(skipHometeam, 3)
skipNowvisitor = random.sample(skipVisteam, 3)

# ask user what team they want to know about Home or Visitor

userTeam = raw_input("what team do you want, Home or Visitor? ")

if "Home" in userTeam:
	print "You can skip the home team bottom inning numbers: %s" % skipNowhome
else:
	if "Visitor" in userTeam:
		print "You can skip the vistor team top inning numbers: %s" % skipNowvisitor

