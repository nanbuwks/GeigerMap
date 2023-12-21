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
# output title line uMap csv file to stdout
print ("name,Latitude,Longitude,description")
for data in datalist:
  result = re.match(pattern, data)

  if result:
    sheetsid=result.group(1)
# get tsv file
    cmdstr = "wget -O "+sheetsid+".tsv https://docs.google.com/spreadsheets/d/"+sheetsid+"/export?format=tsv"
    subprocess.run(cmdstr,shell=True)
# get node name
    cmdstr = "awk -F'\\t' 'NR == 2 {print $2}' "+sheetsid+".tsv"
    nodename = subprocess.run(cmdstr,shell=True, stdout=subprocess.PIPE, check=True).stdout.decode().strip()
# get altitude,latitude name
    cmdstr = "awk -F'\\t' 'NR == 11 {print $2}' "+sheetsid+".tsv"
    altilatitude = subprocess.run(cmdstr,shell=True, stdout=subprocess.PIPE, check=True).stdout.decode().strip()
# make measure tsv file
    cmdstr = "tail +10 "+sheetsid+".tsv | head -100 > "+sheetsid+"-100.tsv"
    subprocess.run(cmdstr,shell=True)
# make graph png file
    cmdstr = "Rscript makegraph.R "+sheetsid+"-100.tsv "+sheetsid+".png > /dev/null"
    subprocess.run(cmdstr,shell=True)
# output uMap csv file to stdout
    print(nodename+",",end="")
    print(altilatitude+",",end="")
    print("{{{https://nanbuwks.github.io/GeigerMap/data/"+sheetsid+".png}}}",end="")
    print("{{{https://docs.google.com/spreadsheets/d/"+sheetsid+"/edit?usp=sharing}}}",end="")
    print(",",end="")
    print()
f.close()


