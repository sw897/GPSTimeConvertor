#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Define GPS leap seconds
leaps = [46828800, 78364801, 109900802, 173059203, 252028804, 315187205, 346723206, 393984007, 425520008, 457056009, 504489610, 551750411, 599184012, 820108813, 914803214, 1025136015]

# Test to see if a GPS second is a leap second
def isleap(gpsTime):
  isLeap = False
  for leap in leaps:
    if gpsTime == leap:
      isLeap = True
      break
  return isLeap

# Count number of leap seconds that have passed
def countleaps(gpsTime, u2g=True):
  nleaps = 0 # number of leap seconds prior to gpsTime
  i = 0
  for leap in leaps:
    if u2g:
      if gpsTime >= leap - i:
        nleaps += 1
    else:
      if gpsTime >= leap:
        nleaps += 1
    i += 1
  return nleaps

# Convert Unix Time to GPS Time
def unix2gps(unixTime):
  # Add offset in seconds
  if (unixTime % 1) != 0:
    unixTime = unixTime - 0.5
    isLeap = 1
  else:
    isLeap = 0
  gpsTime = unixTime - 315964800
  nleaps = countleaps(gpsTime, True)
  gpsTime = gpsTime + nleaps + isLeap
  return gpsTime

# Convert GPS Time to Unix Time
def gps2unix(gpsTime):
  # Add offset in seconds
  unixTime = gpsTime + 315964800
  nleaps = countleaps(gpsTime, False)
  unixTime = unixTime - nleaps
  if isleap(gpsTime):
    unixTime = unixTime + 0.5
  return unixTime

def unix2datetime(unixTime):
  import datetime
  return datetime.datetime.fromtimestamp(unixTime)


def main():
  unix = gps2unix(1081408443)
  print unix2datetime(unix)

if __name__ == '__main__':
  main()
