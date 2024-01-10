# Ender V3 Prusa Preview Data
Post script for generating metadata displayed on Ender 3 V3 SE in PrusaSlicer. Written and tested on Ender 3 V3 SE.
This script adds information to gcode file needed for preview menu to display filament used, layer height and print time.

# Installation

1. Install [python](https://www.python.org/downloads/)
2. Copy the `EnderV3PrusaPreviewData.py` to any location. For example:
```C:\Users\Username\AppData\Roaming\PrusaSlicer\scripts\EnderV3PrusaPreviewData.py```
3. In PrusaSlicer go to PrintSettings -> OutputOptions -> Post-processing scripts and paste link to your python installation directory and file. 
For example:
```C:\Users\Username\AppData\Local\Programs\Python\Python312\python.exe C:\Users\Username\AppData\Roaming\PrusaSlicer\scripts\EnderV3PrusaPreviewData.py;```

Your slicer will then automatically run the script after each time you save gcode file to enrich it with additional data.