# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:02:44 2021

@author: Craig
"""

import csv
import math

path = 'C:/Users/Craig/Desktop/Case Study files/zonalstatistics1_5m.csv'
storage = 'C:/Users/Craig/Desktop/Case Study files/'

n_floors = [] # Create a list to that will contain the total number of floors in building
floors = [] # Create a list that will contain the number of floors affected

# Code to read and write the data.
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)
    with open(storage + 'floors_1_5m.csv', mode='w', newline = '') as output:
        output_writer = csv.writer(output, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in csv_reader:
            TerrainDifference = float(row[4]) 
            BuildingHeight = float(row[3])
            # Calculate the total number of floors in a building using the building height.
            n_floor = math.ceil(BuildingHeight / 2.6)
            n_floors.append(n_floor)
            # In case the building is completely flooded.
            if abs(TerrainDifference) >= BuildingHeight and TerrainDifference < 0: 
                floor = math.ceil(BuildingHeight / 2.6)
            # In case the building is not touched by water
            elif TerrainDifference > 0: 
                floor = 0
            # In case the building is partially flooded
            elif abs(TerrainDifference) <= BuildingHeight and TerrainDifference < 0: 
                floor = math.ceil(abs(TerrainDifference) / 2.6)
            # Append floor to list and write to new file.
            floors.append(floor)
            output_writer.writerow([row[0], row[1], n_floor, floor])
    
    