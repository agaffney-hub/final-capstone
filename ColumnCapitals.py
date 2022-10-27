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

    df = df.rename(columns=columns)

    return df