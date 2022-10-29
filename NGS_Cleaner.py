def merge_cleaner(merged_ngs):
    #This function Appends and Cleans the NGS Data
    import pandas as pd
    import numpy as np

    # Change the directional data to Twist
    merged_ngs['Twist'] = abs(merged_ngs.dir - merged_ngs.o)
    merged_ngs.drop(columns=['o', 'dir'], inplace=True)


    # Drop the unnecessary columns 
    merged_ngs.drop(columns=[
        'GameKey',
        'PlayID',
        'GSISID',
        'Game_Play',
        'Game_Play_ID',
        'Season_Type', 
        'Role', 
        'Game_Day'
        ], inplace=True)


    # Change the positions to numerical
    position = {
        'Quarterback': 0,
        'QB': 0,
        'Running Back': 1,
        'RB': 1,
        'FB': 2,
        'Wide Receiver': 3,
        'WR': 3,
        'Tight End': 4,
        'TE': 4,
        'Offensive Lineman': 5,
        'OL': 5,
        'C': 6,
        'G': 7,
        'LG': 8,
        'RG': 9,
        'T': 10,
        'LT': 11,
        'RT': 12,
        'Kicker': 13,
        'K': 13,
        'KR': 14,
        'Defensive Lineman': 15,
        'DL': 15,
        'DE': 16,
        'DT': 17,
        'NT': 18,
        'Linebacker': 19,
        'LB': 19,
        'OLB': 20,
        'ILB': 21,
        'MLB': 22,
        'DB': 23,
        'Cornerback': 24,
        'CB': 24,
        'Safety': 25,
        'S': 25,
        'SS': 26,
        'FS': 27,
        'P': 28,
        'PR': 29,
        'HB': 30,
        'LS': 31
    }

    merged_ngs.Position = merged_ngs.Position.map(position)

    # Change the Surfaces to numerical
    surface_map = {
        'Natural': 0,
        'Synthetic': 1
    }

    merged_ngs.Turf = merged_ngs.Turf.map(surface_map)


    # Code the Weather numerically
    weather_code = {
        'Clear': 0,
        'Cloudy': 1,
        'Windy': 2,
        'Hazy/Fog': 3,
        'Rain': 4,
        'Snow': 5
    }

    merged_ngs.GameWeather = merged_ngs.GameWeather.map(weather_code)

    # Code the stadiums
    stadium = {
        'Outdoor': 1,
        'Indoor': 0
    }

    # Map the stadiumtype for outdoor as 1 = True and 0 = false
    merged_ngs.StadiumType = merged_ngs.StadiumType.map(stadium)


    return merged_ngs
