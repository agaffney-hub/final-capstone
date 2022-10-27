# NFL_Injury_Cleaning_Functions
# This contains all of the functions for data cleaning for the 1st and Future Analytics data


# HOW TO USE: 
# 1. In dependencies, you will type: 
#     from NFL_Cleaning_Functions import *
# 2. To use this file, the only functions that need to be called will be the Vis_Data_Cleaner or 
# the ML_Data_Cleaner, which each call on the playlist.csv and injuryrecords.cvs, outputting a 
# cleaned and merged dataframe. All other functions are required to run those functions


########################## Primary Cleaning Functions ############################

# This will clean and merge the injury data with an outer merge, containing all injury and 
# non-injury data from playlist.cvs and injuryrecord.csv, maintaining categorical data in the Vis_ 
# function and changing all to numeric data for the ML_ function. 
# PlayKey is the primary key to merge with the tracking data


# This is the overall function for cleaning and merging the data for Visualizations
def vis_data_cleaner(playlist, injuries):
    # This is the overall function for cleaning and merging the data for Visualizations 

    import pandas as pd
    import numpy as np

    playlist = vis_process_playlist_data(playlist)
    injuries = vis_process_injury_data(injuries)

    Vis_outer = pd.merge(playlist, injuries, on='PlayKey', how='outer')

    Vis_outer.BodyPart.fillna("NoInjury", inplace=True)
    Vis_outer.InjuryDuration.fillna(0, inplace=True)
    Vis_outer.SevereInjury.fillna(0, inplace=True)

    return Vis_outer



# This is the overall function that cleans and merges the data for Machine Learning data processing
def ml_data_cleaner(playlist, injuries):
    import pandas as pd
    import numpy as np
    
    playlist = ml_process_playlist_data(playlist)
    injuries = ml_process_injury_data(injuries)
    
    ML_outer = pd.merge(playlist, injuries, on='PlayKey', how='outer')
    
    ML_outer.InjuryType.fillna(0, inplace=True)
    ML_outer.InjuryDuration.fillna(0, inplace=True)
    ML_outer.SevereInjury.fillna(0, inplace=True)

    return ML_outer






############################## Functions for ALL ANALYSES #############################
# This Codes the Stadium Stype as either Indoor or Outdoor, necessary for ALL analysis

# stadium_coder: This function changes the stadium type to either Outdoor or Indoor, maintaining the categorical label
def stadium_coder(df):
    df.StadiumType.fillna('Outdoor', inplace=True)
    
    dict = {'Outdoor': 'Outdoor',
        'Indoors': 'Indoor',
        'Oudoor': 'Outdoor',
        'Outdoors': 'Outdoor',
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
        'Outside': 'Outdoor'}

    df.StadiumType.replace(dict, inplace=True)

    # Create a new column with stadiums coded numerically
    stadium = {
        'Outdoor': 1, 
        'Indoor': 0
    }
    
    # Map the stadiumtype for outdoor as 1 = True and 0 = false
    df['Outdoor'] = df.StadiumType.map(stadium)
    return df



# temperature_adjuster: This function also fixes the -999 temperature issue for all indoor stadiums
def temperature_adjuster(df):   
    
    import numpy as np
    # Fix the temperature from -999 at any indoor stadium to 70
    df['Temperature'] = np.where(
        (df['Temperature'] == -999) & (df['StadiumType'] == 'Indoor'), 70, df.Temperature)

    # Extract all values that are not -999 degrees
    df_filtered = df[df['Temperature'] != -999]
    return df_filtered


# weather_coder: This function changes the weather into a smaller subset of categorical groups
def weather_coder(df):
    weather_dict = {'Clear and warm': 'Clear',
                    'Mostly Cloudy': 'Cloudy',
                    'Sunny': 'Clear',
                    'Clear': 'Clear',
                    'Cloudy': 'Cloudy',
                    'Cloudy, fog started developing in 2nd quarter': 'Hazy/Fog',
                    'Rain': 'Rain',
                    'Partly Cloudy': 'Cloudy',
                    'Mostly cloudy': 'Cloudy',
                    'Cloudy and cold': 'Cloudy',
                    'Cloudy and Cool': 'Cloudy',
                    'Rain Chance 40%': 'Rain',
                    'Controlled Climate': 'Indoor',
                    'Sunny and warm': 'Clear',
                    'Partly cloudy': 'Cloudy',
                    'Clear and Cool': 'Cloudy',
                    'Clear and cold': 'Cloudy',
                    'Sunny and cold': 'Clear',
                    'Indoor': 'Indoor',
                    'Partly Sunny': 'Clear',
                    'N/A (Indoors)': 'Indoor',
                    'Mostly Sunny': 'Clear',
                    'Indoors': 'Indoor',
                    'Clear Skies': 'Clear',
                    'Partly sunny': 'Clear',
                    'Showers': 'Rain',
                    'N/A Indoor': 'Indoor',
                    'Sunny and clear': 'Clear',
                    'Snow': 'Snow',
                    'Scattered Showers': 'Rain',
                    'Party Cloudy': 'Cloudy',
                    'Clear skies': 'Clear',
                    'Rain likely, temps in low 40s.': 'Rain',
                    'Hazy': 'Hazy/Fog',
                    'Partly Clouidy': 'Cloudy',
                    'Sunny Skies': 'Clear',
                    'Overcast': 'Cloudy',
                    'Cloudy, 50% change of rain': 'Cloudy',
                    'Fair': 'Clear',
                    'Light Rain': 'Rain',
                    'Partly clear': 'Clear',
                    'Mostly Coudy': 'Cloudy',
                    '10% Chance of Rain': 'Cloudy',
                    'Cloudy, chance of rain': 'Cloudy',
                    'Heat Index 95': 'Clear',
                    'Sunny, highs to upper 80s': 'Clear',
                    'Sun & clouds': 'Cloudy',
                    'Heavy lake effect snow': 'Snow',
                    'Mostly sunny': 'Clear',
                    'Cloudy, Rain': 'Rain',
                    'Sunny, Windy': 'Windy',
                    'Mostly Sunny Skies': 'Clear',
                    'Rainy': 'Rain',
                    '30% Chance of Rain': 'Rain',
                    'Cloudy, light snow accumulating 1-3"': 'Snow',
                    'cloudy': 'Cloudy',
                    'Clear and Sunny': 'Clear',
                    'Coudy': 'Cloudy',
                    'Clear and sunny': 'Clear',
                    'Clear to Partly Cloudy': 'Clear',
                    'Cloudy with periods of rain, thunder possible. Winds shifting to WNW, 10-20 mph.': 'Windy',
                    'Rain shower': 'Rain',
                    'Cold': 'Clear'}

    df.Weather.replace(weather_dict, inplace=True)

    # There are still na values within the weather group that need to be addressed
    df.loc[df.StadiumType == 'Indoor', 'Weather'] = df.loc[df.StadiumType == 'Indoor', 'Weather'].fillna('Indoor')

    # Because we can't make a determination on the type of weather for outdoor, drop the remaining na values
    df = df.loc[df.Weather.isna() == False]
    return df


# Add a column for the presence of precipitation, that will ultimately be used for numerical analysis of the weather
def precipitation_coder(df):
    precipitation = {
        'Indoor': 0,
        'Clear': 0,
        'Cloudy': 0,
        'Windy': 0,
        'Hazy/Fog': 0,
        'Rain': 1,
        'Snow': 1
    }

    df['Precipitation'] = df.Weather.map(precipitation)
    df = df.loc[df.Precipitation.isna() == False]
    return df


# playerday_adjuster: This function adjusts the player day to remove the negative values
def playerday_adjuster(df):
    df['DaysPlayed'] = df['PlayerDay'].apply(lambda x: x + 63 if x < 200 else x - 273)

    df.drop(columns='PlayerDay', inplace=True)

    return df


# play_coder: This function creates a categorical grouping for the different types of plays, grouping into passing, rushing, or kicking plays
def play_coder(df):    
    play_type = {
        'Pass': 'Pass',
        'Rush': 'Rush',
        'Extra Point': 'Kick',
        'Kickoff': 'Kick',
        'Punt': 'Kick',
        'Field Goal': 'Kick',
        'Kickoff Not Returned': 'Kick',
        'Punt Not Returned': 'Kick',
        'Kickoff Returned': 'Kick',
        'Punt Returned': 'Kick',
        '0': 'Kick'
    }

    play_map = {
        'Pass': 0, 
        'Rush': 1, 
        'Kick': 2
    }

    df.PlayType.replace(play_type, inplace=True)
    df['PlayCode'] = df.PlayType.map(play_map)

    df = df.loc[df.PlayType.isna() == False]
    df.PlayCode.astype(int)

    return df


# Injury_Coder: This function codifies the injury types based on their frequency of occurrence, adding this as a new column called "InjuryType"
def injury_coder(df):
    knee_freq = df.BodyPart.value_counts()['Knee']
    ankle_freq = df.BodyPart.value_counts()['Ankle']
    foot_freq = df.BodyPart.value_counts()['Foot']
        
    injury_map = {
        'NoInjury': 0, 
        'Foot': foot_freq, 
        'Ankle': ankle_freq, 
        'Knee': knee_freq
    }

    df['InjuryType'] = df.BodyPart.map(injury_map)

    # Remove any injuries not associated with a play
    df = df.loc[df.PlayKey.isna() == False]
    return df


# Injury_Duration_Classifier: This creates a new list of numerical values as the shortest number of days of injury
def injury_duration_classifier(row):
    injury_duration = 0
    if row["DM_M42"] == 1:
        injury_duration = 42
    else:
        if row["DM_M28"] == 1:
            injury_duration = 28
        else:
            if row["DM_M7"] == 1:
                injury_duration = 7
            else: 
                injury_duration = 1
    
    return injury_duration


def injury_duration_coder(df): 
    # Injury_Duration_Coder: Apply the Injury Duration Classifier to the dataframe

    df['InjuryDuration'] = df.apply(injury_duration_classifier, axis=1)

    severity_map = {
        42: 1, 
        28: 1,
        7: 0, 
        1: 0 
    }
    df['SevereInjury'] = df.InjuryDuration.map(severity_map)
    df.InjuryDuration.astype(int)
    df.SevereInjury.astype(int)

    return df



############################## Functions for NON-Machine Learning #############################

# vis_position_coder: This function replaces nan position with rosterposition and drops the position group column
def vis_position_coder(df):    
    import numpy as np
    
    df['Position'] = np.where(df['Position'] == 'Missing Data', df['RosterPosition'], df['Position'])
    
    position = {
        'Quarterback': 'QB',
        'Running Back': 'RB',
        'Wide Receiver': 'WR',
        'Tight End': 'TE',
        'Offensive Lineman': 'OL',
        'Kicker': 'K',
        'Defensive Lineman': 'DL',
        'Linebacker': 'LB',
        'Cornerback': 'CB',
        'Safety': 'S'
         }
    
    df.Position.replace(position, inplace=True)
    df.drop(columns='PositionGroup', inplace=True)
    return df


# vis_process_playlist_data: Create cleaning function to apply all of the other functions to the single df input for visualizations
def vis_process_playlist_data(df):
    
    df = stadium_coder(df)
    df = temperature_adjuster(df)
    df = weather_coder(df)
    df = vis_position_coder(df)
    df = playerday_adjuster(df)
    df = play_coder(df)

    df.drop(columns=['PlayerKey', 'GameID', 'PlayerGame', 'Outdoor', 'PlayCode'], inplace=True)
    return df


# Process_Injury_Data: This function applies all of the InjuryRecord table processing Functions
def vis_process_injury_data(df):
    df = injury_coder(df)
    df = injury_duration_coder(df)

    # Drop any PlayKey NaN values
    df.PlayKey.dropna(inplace=True)

    # Drop the columns that are redundant with those from the Playlist Dataframe inpreparation for the Merge.
    df.drop(columns=['GameID',
                     'PlayerKey',
                     'InjuryType',
                     'Surface',
                     'DM_M1',
                     'DM_M7',
                     'DM_M28',
                     'DM_M42'], inplace=True)
    return df



############################## Functions for Machine Learning ONLY #############################

# This codes the Surface from Categorical to Numerical
def surface_coder(df):
    # surface_coder: Function that encodes the Field Surface to identify natural or synthetic
    surface_map = {
        'Natural': 0,
        'Synthetic': 1
    }
    df['SyntheticField'] = df.FieldType.map(surface_map)
    return df    

# ml_position_coder: This function encodes the players by position and rosterposition
def ml_position_coder(df): 
    import numpy as np
    
    df['Position'] = np.where(df['Position'] == 'Missing Data', df['RosterPosition'], df['Position'])

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
        'HB': 30
    }

    df.RosterPosition.replace(position, inplace=True)
    df.Position.replace(position, inplace=True)
    df.Position.astype(int)
    df.drop(columns='PositionGroup', inplace=True)
    return df
    
# ml_process_playlist_data: Create cleaning function to apply all of the other functions to the single df input for Machine Learning
def ml_process_playlist_data(df):
    df = stadium_coder(df)
    df = temperature_adjuster(df)
    df = weather_coder(df)
    df = precipitation_coder(df)
    df = ml_position_coder(df)
    df = playerday_adjuster(df)
    df = play_coder(df)

    df.drop(columns=['PlayerKey', 'GameID', 'PlayerGame', 'StadiumType',
            'FieldType', 'Weather', 'PlayType'], inplace=True)
    return df


# ml_process_injury_data: This function applies all of the InjuryRecord table processing Functions
def ml_process_injury_data(df): 
    df = injury_coder(df)
    df = injury_duration_coder(df)

    # Drop any PlayKey NaN values
    df = df.loc[df.PlayKey.isna() == False]    


    # Drop the columns that are redundant with those from the Playlist Dataframe inpreparation for the Merge.
    df.drop(columns=['GameID',
                       'PlayerKey',
                       'Surface',
                       'BodyPart',
                       'DM_M1',
                       'DM_M7',
                       'DM_M28',
                       'DM_M42'], inplace=True)
    return df


