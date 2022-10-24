def Punt_Cleaner():
    import pandas as pd
    import numpy as np


    # Read the csv files in
    games = pd.read_csv("NFL_Punt/game_data.csv")  # 666 rows  Week, StadiumType, Turf, GameWeather, Temperature, OutdoorWeather
    play_info = pd.read_csv("NFL_Punt/play_information.csv")  # 6681 rows  Season_Type, Week, PlayID, Quarter, Play_Type, Score_Home_Visiting
    punt = pd.read_csv('NFL_Punt/player_punt_data.csv')  # 3259 rows Position
    play_player = pd.read_csv('NFL_Punt/play_player_role_data.csv')  # 146,573 rows Play+ID and Role


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

    
    # Create unique identifiers
    cols = ['GameKey', 'PlayID']
    colspp = ['GameKey', 'PlayID', 'GSISID']


    # Add the Game_Play and GamePlay with GSISID to the play_player
    play_player['Game_Play'] = play_player[cols].apply(lambda row: '-'.join(row.values.astype(str)), axis=1)
    play_player['Game_Play_ID'] = play_player[colspp].apply(lambda row: '-'.join(row.values.astype(str)), axis=1)


    # Add the GameKey+PlayID to play_info
    play_info['Game_Play'] = play_info[cols].apply(lambda row: '-'.join(row.values.astype(str)), axis=1)

    # The weeks are registered per season, but the players play continuously, so we need to add 5 to regular and 22 to post
    games['Week'] = np.where(games['Season_Type'] == 'Reg', games.Week + 5, games.Week)
    games['Week'] = np.where(games['Season_Type'] == 'Post', games.Week + 22, games.Week)

    # Drop unnecessary columns
    play_player.drop(columns='Season_Year', inplace=True)

    punt.drop(columns='Number', inplace=True)
    positions = dict(punt.values)

    games.drop(columns=['Season_Year',
                        'Game_Date',
                        'Start_Time',
                        'Game_Site',
                        'Home_Team',
                        'HomeTeamCode',
                        'Visit_Team',
                        'VisitTeamCode',
                        'Stadium',
                        'OutdoorWeather'],
            inplace=True)

    play_info.drop(columns=['Season_Year',
                            'Season_Type',
                            'Week',
                            'GameKey', 
                            'PlayID',
                            'Play_Type',
                            'Game_Date',
                            'Game_Clock',
                            'YardLine',
                            'Poss_Team',
                            'Home_Team_Visit_Team',
                            'PlayDescription'],
                inplace=True)



    # Merge the Player Info with the Player Plays using an inner merge - reduces the NaN values from the collected info grom play-player
    merged_df = pd.merge(play_player, play_info, on='Game_Play', how='inner')

    # This uses the positions from the punt list to set positions for the player and if known, the primary partner
    merged_df['Position'] = merged_df.GSISID.map(positions)

    # Merge the game plays
    merged_df = pd.merge(merged_df, games, on='GameKey', how='left')

    # Drop the rows where we don't know the position, weather, stadium type, or temperature
    merged_df = merged_df.loc[merged_df.Position.isna() == False]
    merged_df = merged_df.loc[merged_df.Temperature.isna() == False]
    merged_df = merged_df.loc[merged_df.GameWeather.isna() == False]
    merged_df = merged_df.loc[merged_df.StadiumType.isna() == False]
    merged_df = merged_df.loc[merged_df.StadiumType != 'Turf']

    # Merge the weather, stadium type, and turf
    
    merged_df.StadiumType.replace(stadium, inplace=True)
    merged_df.Turf.replace(turfs, inplace=True)
    merged_df.GameWeather = merged_df.GameWeather.map(weather)

    # Remove the nas from the Turf data
    merged_df = merged_df.loc[merged_df.Turf.isna() == False]
    

    # One last thing we need to do is change the Score_Home_Visiting to a continuous score range. There are currently 515 unique score sets, but the differences in scores will reduce this and be a better indicator of how close the games are
    del cols, colspp, games, play_info, play_player, positions, punt, stadium, turfs, weather #, video_review


    # We will be removing the string of the home/visiting scores, since there are over 500 different score sets. 
    # But there is the potential that the score each home team has, as well as the difference between the scores will make a difference. 
    # Since the next function will contain the difference between the scores, including both the home and away would have 
    # dependencies, and skew the data, we're only adding a column with the home score, and then one for the score difference, representing
    # whether the home team is ahead or down (using negative values)

    merged_df['HomeScore'] = merged_df['Score_Home_Visiting'].apply(lambda row: [int(
        s) for s in row.split() if s.isdigit()][0])

    # merged_df[H-A_D] sets a new column using the 'ScoreHomeVisiting' column data
    # the lambda will apply this to all rows in the dataframe
    # The list comprehension will read the string, for example '21 - 14' as a string in each row...
    # it will split the row string with split per space, if the parsed text is a digit, it will convert the digits to integer form and return only the integers in a list
    # For each row in the lambda function, it will take the index 0 from this list and subtract index 1. 
    # For our example with '21 - 14', this will parse and return [21, 14], then index 0 is 21, index 1 is 14, so [0] - [1], or 21-14 returns merged[HAD] = 7
    # Negative values mean that the home team is losing. 
    
    merged_df['Home-Away_Difference'] = merged_df['Score_Home_Visiting'].apply(lambda row: [int(
        s) for s in row.split() if s.isdigit()][0] - [int(s) for s in row.split() if s.isdigit()][1])

    # Remove the Score_Home_Visiting Column
    merged_df.drop(columns="Score_Home_Visiting", inplace=True)

    return merged_df

