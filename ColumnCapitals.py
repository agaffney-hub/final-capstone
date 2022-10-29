def column_capitalizer(df, df_name):
    
    if df_name == 'playlist':
        columns = {
            'playerkey': 'PlayerKey',
            'gameid': 'GameID',
            'playkey': 'PlayKey',
            'rosterposition': 'RosterPosition',
            'playerday': 'PlayerDay',
            'playergame': 'PlayerGame',
            'stadiumtype': 'StadiumType',
            'fieldtype': 'FieldType',
            'temperature': 'Temperature',
            'weather': 'Weather',
            'playtype':'PlayType', 
            'playergameplay': 'PlayerGamePlay', 
            'position': 'Position', 
            'postiongroup': 'PositionGroup',
        }

    elif df_name == 'injuries': 
        columns = {
            'playerkey': 'PlayerKey',
            'gameid': 'GameID',
            'playkey': 'PlayKey',
            'bodypart': 'BodyPart',
            'fieldtype': 'Surface',
            'dm_m1': 'DM_M1',
            'dm_m7': 'DM_M7',
            'dm_m28': 'DM_M28',
            'dm_m42': 'DM_M42'       
        }

    elif df_name == 'punt':
        columns= {
            'gamekey': 'GameKey', 
            'playid': 'PlayID', 
            'gsisid': 'GSISID', 
            'p_position': 'Position',
            'prole': 'Role',
            'season_type': 'Season_Type', 
            'quarter': 'Quarter', 
            'week': 'Week', 
            'stadiumtype': 'StadiumType', 
            'turf': 'Turf', 
            'gameweather': 'Weather',
            'temperature': 'Temperature', 
            'score_home_visiting': 'Score_Home_Visiting'
        }



    df = df.rename(columns=columns)

    return df