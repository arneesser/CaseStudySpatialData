DD# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:02:44 2021

@author: Craig
"""

import csv
from tqdm.notebook import tqdm

path = 'C:/Users/Craig/Desktop/Case Study files/probeersel.csv'
storage = 'C:/Users/Craig/Desktop/Case Study files/'

RatioFloodedFloors = [] # Create a list that will contain the ratio of flooded floors
MonetaryDamage = [] # Create a list that will contain the number of floors affected

# Code to read and write the data.
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)
    with open(storage + 'damage_6m.csv', mode='w', newline = '') as output:
        output_writer = csv.writer(output, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in tqdm(csv_reader):
           BuildingArea = float(row[5]) # The area of the building
           BuildingFloors = int(row[6]) # The number of floors in the building
           FloodedFloors = int(row[7]) # The number of flooded floors in the building
           PropertyValue = int(row[8]) # A constant factor reflecting the property worth of the building in m2
           
           # Calculate the total percentage of flooded floors per building: 
           RatioFloodedFloor = FloodedFloors / BuildingFloors
           
           # Calculate the total monetary damage per building:
           BuildingDamage = BuildingArea * FloodedFloors * PropertyValue
           
           # Append new data
           RatioFloodedFloors.append(RatioFloodedFloor)
           MonetaryDamage.append(BuildingDamage)
           output_writer.writerow([row[0], row[1], row[7], RatioFloodedFloor, BuildingDamage])
