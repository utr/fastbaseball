#!/usr/bin/python

from lxml import html
import requests
import random

page = requests.get('http://www.cbssports.com/mlb/gametracker/playbyplay/MLB_20150512_NYM@CHC')
tree = html.fromstring(page.text)

#print page.text #prints the entire HTML

scores = tree.xpath('//*[@id="inning"]/td/text()')

firstTop = scores[0]
firstBottom = scores[1]
secondTop = scores[2]
secondBottom = scores[3]
thirdTop = scores[4]
thirdBottom = scores[5]
fourthTop = scores[6]
fourthBottom = scores[7]
fifthTop = scores[8]
fifthBottom = scores[9]
sixthTop = scores[10]
sixthBottom = scores[11]
seventhTop = scores[12]
seventhBottom = scores[13]
eighthTop = scores[14]
eighthBottom = scores[15]
ninthTop = scores[16]

#if not scores[17]:
#   print "Empty Element"

#print scores

#ninthBottom = scores[17] // create an if statement that shows or doesn't show this

skip = ""

if "0 Runs" in firstBottom:
    skip = [1]
#   print "You can skip the bottom of the 1st"

if "0 Runs" in secondBottom:
    skip.append(2)
#   print "You can skip the bottom of the 2nd"

if "0 Runs" in thirdBottom:
    skip.append(3)
#   print "You can skip the bottom of the 3rd"

if "0 Runs" in fourthBottom:
    skip.append(4)
#   print "You can skip the bottom of the 4th"

if "0 Runs" in fifthBottom:
    skip.append(5)
#   print "You can skip the bottom of the 5th"

if "0 Runs" in sixthBottom:
    skip.append(6)
#   print "You can skip the bottom of the 6th"

if "0 Runs" in seventhBottom:
    skip.append(7)
#   print "You can skip the bottom of the 7th"

if "0 Runs" in eighthBottom:
    skip.append(8)
#   print "You can skip the bottom of the 8th"

skipNow = random.sample(skip, 3)

print "You can skip inning number %s" % skipNow
