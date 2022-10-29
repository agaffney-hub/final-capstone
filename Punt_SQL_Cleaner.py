def punt_cleaner(punt):
    import pandas as pd
    import numpy as np
    from ColumnCapitals import column_capitalizer

    punt = column_capitalizer(punt, 'punt')

    # Set Dictionaries
    turfs = {
        'Grass': 'Natural',
        'Field Turf': 'Synthetic',
        'Natural Grass': 'Natural',
        'grass': 'Natural',
        'Artificial': 'Synthetic',
        'FieldTurf': 'Synthetic',
        'DD GrassMaster': 'Synthetic',
        'A-Turf Titan': 'Synthetic',
        'UBU Sports Speed S5-M': 'Synthetic',
        'UBU Speed Series S5-M': 'Synthetic',
        'Artifical': 'Synthetic',
        'UBU Speed Series-S5-M': 'Synthetic',
        'FieldTurf 360': 'Synthetic',
        'Natural grass': 'Natural',
        'Field turf': 'Synthetic',
        'Natural': 'Natural',
        'Natrual Grass': 'Natural',
        'Synthetic': 'Synthetic',
        'Natural Grass ': 'Natural',
        'Naturall Grass': 'Natural',
        'FieldTurf360': 'Synthetic'}

    stadium = {'Outdoor': 'Outdoor',
               'outdoor': 'Outdoor',
               'Indoors': 'Indoor',
               'Indoors (Domed)': 'Indoor',
               'Oudoor': 'Outdoor',
               'Outdoors': 'Outdoor',
               'Outdoors ': 'Outdoor',
               'Open': 'Outdoor',
               'Closed Dome': 'Indoor',
               'Domed, closed': 'Indoor',
               'Dome': 'Indoor',
               'Indoor': 'Indoor',
               'Domed': 'Indoor',
               'Retr. Roof-Closed': 'Indoor',
               'Outdoor Retr Roof-Open': 'Outdoor',
               'Retractable Roof': 'Indoor',
               'Ourdoor': 'Outdoor',
               'Indoor, Roof Closed': 'Indoor',
               'Retr. Roof - Closed': 'Indoor',
               'Bowl': 'Outdoor',
               'Outddors': 'Outdoor',
               'Retr. Roof-Open': 'Outdoor',
               'Dome, closed': 'Indoor',
               'Indoor, Open Roof': 'Outdoor',
               'Domed, Open': 'Outdoor',
               'Domed, open': 'Outdoor',
               'Heinz Field': 'Outdoor',
               'Cloudy': 'Outdoor',
               'Retr. Roof - Open': 'Outdoor',
               'Retr. Roof Closed': 'Indoor',
               'Outdor': 'Outdoor',
               'Outside': 'Outdoor',
               'Indoor, non-retractable roof': 'Indoor',
               'Retr. roof - closed': 'Indoor',
               'Indoor, fixed roof ': 'Indoor',
               'Indoor, Non-Retractable Dome': 'Indoor',
               'Indoor, Fixed Roof': 'Indoor',
               'Indoor, fixed roof': 'Indoor'}

    weather = {
        'Mostly Cloudy': 'Cloudy',
        'Sunny': 'Clear',
        'Rain': 'Rain',
        'cloudy': 'Cloudy',
        'Partly Cloudy': 'Cloudy',
        'Clear': 'Clear',
        'Cloudy': 'Cloudy',
        'Showers': 'Rain',
        'Clear skies': 'Clear',
        'Mostly cloudy': 'Cloudy',
        'Controlled Climate': 'Clear',
        'Partly cloudy': 'Cloudy',
        'Clear Skies': 'Clear',
        'Fair': 'Clear',
        'Mostly Coudy': 'Cloudy',
        'Partly sunny': 'Clear',
        'Partly cloudy, lows to upper 50s.': 'Cloudy',
        'Sunny and warm': 'Clear',
        'Scattered thunderstorms': 'Rain',
        'Indoor': 'Clear',
        'Mostly Sunny': 'Clear',
        '30% Chance of Rain': 'Rain',
        'Light Rain': 'Rain',
        'CLEAR': 'Clear',
        'Partly CLoudy': 'Cloudy',
        'Partly Sunny': 'Clear',
        'Chance of Showers': 'Rain',
        'Snow showers': 'Snow',
        'Cloudy, chance of rain': 'Cloudy',
        'Clear and Cold': 'Clear',
        'Party Cloudy': 'Cloudy',
        'Indoors': 'Clear',
        'Cloudy with rain': 'Rain',
        'Sunny intervals': 'Clear',
        'Clear and cool': 'Clear',
        'Cold': 'Cloudy',
        'Cloudy, Humid, Chance of Rain': 'Rain',
        'Cloudy and cold': 'Cloudy',
        'Cloudy and Cold': 'Cloudy',
        'Cloudy, fog started developing in 2nd quarter': 'Hazy/Fog',
        'Cloudy with patches of fog': 'Hazy/Fog',
        'Controlled': 'Clear',
        'Sunny and Clear': 'Clear',
        'Clear and warm': 'Clear',
        'Cloudy, Rain': 'Rain',
        'Cloudy with Possible Stray Showers/Thundershowers': 'Rain',
        'Suny': 'Clear',
        'Sunny Skies': 'Clear',
        'Heavy lake effect snow': 'Snow',
        'Sun & clouds': 'Cloudy',
        'T-Storms': 'Rain',
        'Sunny and cool': 'Clear',
        'Snow': 'Snow',
        'Coudy': 'Cloudy',
        'Cloudy with periods of rain, thunder possible. Winds shifting to WNW, 10-20 mph.': 'Windy',
        'Sunny, highs to upper 80s': 'Clear',
        'Cloudy, steady temps': 'Cloudy',
        'Hazy, hot and humid': 'Hazy/Fog',
        'Sunny Intervals': 'Clear',
        'Cloudy, light snow accumulating 1-3"': 'Cloudy',
        'Partly Cloudy, Chance of Rain 80%': 'Rain',
        'Mostly Clear. Gusting ot 14.': 'Windy',
        'Mostly CLoudy': 'Cloudy',
        'Snow Showers, 3 to 5 inches expected.': 'Snow',
        'Rain likely, temps in low 40s.': 'Rain'
    }


    # Create a Unique Identifier per player per play
    punt['Game_Play_ID'] = punt[['GameKey', 'PlayID', 'GSISID']].apply(
        lambda row: '-'.join(row.values.astype(str)), axis=1)

    # Adjust week numbers for the regular and post seasaon games; each season started at 1
    punt['Week'] = np.where(punt['Season_Type'] ==
                            'Reg', punt.Week + 5, punt.Week)
    
    punt['Week'] = np.where(punt['Season_Type'] == 'Post',
                        punt.Week + 22, punt.Week)


    # Remove rows with NAN values 
    punt = punt.loc[punt.Position.isna() == False]
    punt = punt.loc[punt.Temperature.isna() == False]
    punt = punt.loc[punt.Weather.isna() == False]
    punt = punt.loc[punt.StadiumType.isna() == False]
    punt = punt.loc[punt.Turf.isna() == False]

    # Remove stadiums listed as Turf
    punt = punt.loc[punt.StadiumType != 'Turf']

    # Map the Dictionary values to reduce the number of unique outputs
    punt.StadiumType = punt.StadiumType.map(stadium)
    punt.Turf = punt.Turf.map(turfs)
    punt.Weather = punt.Weather.map(weather)

    # Split the home-away scores to get the home score alone and the difference between them 
    punt['HomeScore'] = punt.Score_Home_Visiting.apply(
        lambda row: [int(s) for s in row.split() if s.isdigit()][0])

    punt['HomeAway_Difference'] = punt.Score_Home_Visiting.apply(
        lambda row: [int(s) for s in row.split() if s.isdigit()][0] - [int(s) for s in row.split() if s.isdigit()][1])

    # Drop the redundant columns
    punt.drop(columns=['Season_Type', 'Score_Home_Visiting'], inplace=True)


    # Reorganize the columns before the return
    columns = ['Game_Play_ID', 'GameKey', 'PlayID', 'GSISID', 'Position', 'Role', 'Quarter',
               'Week', 'HomeScore', 'HomeAway_Difference', 'StadiumType', 'Turf', 'Weather', 'Temperature']

    punt = punt.reindex(columns=columns)


    return punt
