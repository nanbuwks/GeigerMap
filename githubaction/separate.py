#!/usr/bin/env python3
import sys
import re
import subprocess
# ex, https://docs.google.com/spreadsheets/d/1QrHuwErRRwYp5uthg2U_YsF2byZq2F9pomVaQw7EUfs/edit?usp=sharing

args = sys.argv

f = open(args[1], 'r')
pattern='https://docs.google.com/spreadsheets/d/(.*)/edit\?usp=sharing'
# pattern='https://docs.google.com/spreadsheets/d/(.*)'
datalist = f.readlines()
for data in datalist:
  result = re.match(pattern, data)

  if result:
    sheetsid=result.group(1)
# get tsv file
    cmdstr = "wget -O "+sheetsid+".tsv https://docs.google.com/spreadsheets/d/"+sheetsid+"/export?format=tsv"
    subprocess.run(cmdstr,shell=True)
# get node name
    cmdstr = "awk -F'\\t' 'NR == 2 {print $2}' "+sheetsid+".tsv"
    nodename = subprocess.run(cmdstr,shell=True, stdout=subprocess.PIPE, check=True).stdout.decode()
    print(nodename)
# get altitude,latitude name
    cmdstr = "awk -F'\\t' 'NR == 11 {print $2}' "+sheetsid+".tsv"
    altilatitude = subprocess.run(cmdstr,shell=True, stdout=subprocess.PIPE, check=True).stdout.decode()
    print(altilatitude)
    print(result.group(1)+".png,",end="")
    print("https://docs.google.com/spreadsheets/d/"+result.group(1)+"/edit?usp=sharing,",end="")
    print("https://docs.google.com/spreadsheets/d/"+result.group(1)+"/export?format=csv&gid=0",end="")
    print()
f.close()


