#!/usr/bin/python

from lxml import html
import requests
import random

page = requests.get('http://www.cbssports.com/mlb/gametracker/playbyplay/MLB_20150512_NYM@CHC')
tree = html.fromstring(page.text)

#print page.text #prints the entire HTML

scores = tree.xpath('//*[@id="inning"]/td/text()')
skip = ""


if len(scores) >= 1:
    firstTop = scores[0]

if len(scores) >= 2:
    firstBottom = scores[1]
    if "0 Runs" in firstBottom:
        skip = [1]

if len(scores) >= 3:
    secondTop = scores[2]

if len(scores) >= 4:
    secondBottom = scores[3]
    if "0 Runs" in secondBottom:
        skip.append(2)

if len(scores) >= 5:
    thirdTop = scores[4]

if len(scores) >= 6:
    thirdBottom = scores[5]
    if "0 Runs" in thirdBottom:
        skip.append(3)

if len(scores) >= 7:
    fourthTop = scores[6]

if len(scores) >= 8:
    fourthBottom = scores[7]
    if "0 Runs" in fourthBottom:
        skip.append(4)
        
if len(scores) >= 9:
    fifthTop = scores[8]

if len(scores) >= 10:
    fifthBottom = scores[9]
    if "0 Runs" in fifthBottom:
        skip.append(5)

if len(scores) >= 11:
    sixthTop = scores[10]

if len(scores) >= 12:
    sixthBottom = scores[11]
    if "0 Runs" in sixthBottom:
        skip.append(6)

if len(scores) >= 13:
    seventhTop = scores[12]

if len(scores) >= 14:
    seventhBottom = scores[13]
    if "0 Runs" in seventhBottom:
        skip.append(7)
        
if len(scores) >= 15:
    eighthTop = scores[14]

if len(scores) >= 16:
    eighthBottom = scores[15]
    if "0 Runs" in eighthBottom:
        skip.append(8)

if len(scores) >= 17:
    ninthTop = scores[16]

if len(scores) >= 18:
    ninthBottom = scores[17]
    if "0 Runs" in ninthBottom:
        skip.append(9)


skipNow = random.sample(skip, 3)

print "You can skip bottom inning numbers: %s" % skipNow
        
