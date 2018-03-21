import requests
from bs4 import BeautifulSoup
from collections import defaultdict


"""
[https://www.dart.org/schedules/]

Red
 -> To Parker(Weekday) [w600no.htm]
 -> To Parker(Weekend) [s600no.htm]
 -> To Westmoreland(Weekday) [w600so.htm]
 -> To Westmoreland(Weekend) [s600so.htm]
Blue
 -> To Downtown Rowlett Station (Weekday)[w601no.htm]
 -> To Downtown Rowlett Station (Weekend)[s601no.htm]
 -> To UNT Dallas (Weekday) [w601so.htm]
 -> To UNT Dallas (Weekend) [s601so.htm]
Green
 -> To Buckner Station (Weekday) [w602so.htm]
 -> To Buckner Station (Weekday) [s602so.htm]
 -> To N.Carrolton/Frankford (Weekday) [w602no.htm]
 -> To N.Carrolton/Frankford (Weekend) [s602no.htm]
Orange
 -> To Parker Rd (Weekday) [w603no.htm]
 -> To LBJ/Central (Weekends) [s603no.htm]
 -> To DFW Airport (Weekday) [w603so.htm]
 -> To DFW Airport (Weekend) [s603so.htm]
 
"""

#Begin a really tedious block of code, assigning addresses to different lines, days and directions.

def tree(): return defaultdict(tree)

line = ['Red', 'Blue', 'Green', 'Orange']
day = ['Weekday', 'Weekend']
direction = ['North Bound', 'South Bound']
schedule = 'https://www.dart.org/schedules'

rail = tree()

#Red
rail['Red']['Weekday']['North Bound'] = 'w600no.htm'
rail['Red']['Weekend']['North Bound'] = 's600no.htm'
rail['Red']['Weekday']['South Bound'] = 'w600so.htm'
rail['Red']['Weekend']['South Bound'] = 's600so.htm'
#Blue
rail['Blue']['Weekday']['North Bound'] = 'w601no.htm'
rail['Blue']['Weekend']['North Bound'] = 's601no.htm'
rail['Blue']['Weekday']['South Bound'] = 'w601so.htm'
rail['Blue']['Weekend']['South Bound'] = 'w601so.htm'
#Green
rail['Green']['Weekday']['North Bound'] = 'w602no.htm'
rail['Green']['Weekend']['North Bound'] = 's602no.htm'
rail['Green']['Weekday']['South Bound'] = 'w602so.htm'
rail['Green']['Weekend']['South Bound'] = 's602so.htm'
#Orange
rail['Orange']['Weekday']['North Bound'] = 'w603no.htm'
rail['Orange']['Weekend']['North Bound'] = 's603no.htm'
rail['Orange']['Weekday']['South Bound'] = 'w603so.htm'
rail['Orange']['Weekend']['South Bound'] = 's603so.htm'

def print_tree()
    for x in line:
        for y in day:
            for z in direction:
                print(x + '|' + y + '|' + z + ': ' + str(rail[x][y][z]))
