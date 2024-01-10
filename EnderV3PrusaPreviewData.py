#!/usr/bin/env python

"""
@author: Maciej Wanat
"""

import re
import sys

def parseTimeString(timeComponents):
    days = 0
    hours = 0
    minutes = 0
    seconds = 0

    for value, unit in timeComponents:
        value = int(value)
        if unit == 'd':
            days += value
        elif unit == 'h':
            hours += value
        elif unit == 'm':
            minutes += value
        elif unit == 's':
            seconds += value

    totalSeconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
    return totalSeconds

add_count = 0
header = ""

# we only need tail for processing
bottomLinesAnalyzedAmount = 400

sourceFile = sys.argv[1]
print(sourceFile)
with open(sourceFile, 'r+') as file:
    # this could be optimized with reading only tail, instead of reading a whole file
    content = file.read()
    lines = '\n'.join(content.splitlines()[-bottomLinesAnalyzedAmount:])

    # expected example: -> ; estimated printing time (normal mode) = 9h 56m 19s
    timeEstimatedPrusaData = re.findall(r'; estimated printing time \(normal mode\) = .*', lines)[0]
    # expected example: -> ; filament used [mm] = 19112.15
    filamentUsedMmPrusaData = re.findall(r'; filament used \[mm\] = \d+\.\d+', lines)[0]
    # expected example => ; layer_height = 0.1
    layerHeightPrusaData = re.findall(r'; layer_height = \d+\.\d+', lines)[0]

    timeComponents = re.findall(r'(\d+)([dhms])', timeEstimatedPrusaData)
    secondsTotal = parseTimeString(timeComponents)

    filamentUsedMm = re.split(r' ', filamentUsedMmPrusaData)[-1:][0]
    filamentUsedM = float(filamentUsedMm) / 1000

    layerHeight = re.split(r' ', layerHeightPrusaData)[-1:][0]

    header += ';FLAVOR:Marlin\n'
    header += f';TIME:{secondsTotal}\n'
    header += f';Filament used: {filamentUsedM}m\n'
    header += f';Layer height: {layerHeight}\n'
    header += ';TARGET_MACHINE.NAME:Creality Ender-3 V3 SE\n'
    header += ';Generated by EnderV3SEPrusaPostScript by Maciej Wanat\n\n'
   
    file.seek(0, 0)
    file.write(header + content)