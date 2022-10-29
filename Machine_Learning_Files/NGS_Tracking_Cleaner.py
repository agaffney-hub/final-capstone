def Tracking_Loader_Sampler(fraction = 1, random=42):
    
    # To call this, just set ngs = Tracking_Loader_Sampler(fraction=fraction)

    # IMPORTANT: The default fraction is 1.0 - thus unless specified, 
    # this WILL NOT sample the data, and it will import the full set of tables, 
    # yielding a dataframe with about 60 million rows. 

 
    # Feel Free to comment out parts of this function if you want to restrict  

    # This function imports the ngs data and samples it to a fraction
    # of the file's original size. The fraction can be adjusted as well as 
    # the random state by assigning them in the function parameters
    
    import pandas as pd
    import numpy as np

    colspp = ['GameKey', 'PlayID', 'GSISID']

    # The dtypes are entered to let the read_csv function know the data types it will be importing, so it doesn't throw up a low_memory warning
    dtypes = {'Season_Year': 'int64',
             'GameKey': 'int64',
             'PlayID': 'int64',
             'GSISID': 'float64',
             'Time': 'str',
             'x': 'float64',
             'y': 'float64',
             'dis': 'float64',
             'o': 'float64',
             'dir': 'float64',
             'Event': 'str'}

    # Read the first csv file, append to that file
    ngs_2016_pre = pd.read_csv(
        'NFL_Punt/ngs-2016-pre.csv', dtype=dtypes)  # 1 million rows
    ngs = ngs_2016_pre.sample(
        n=int(fraction*len(ngs_2016_pre)), random_state=random)
    del ngs_2016_pre

    # The next process is to open the next csv, append to the df, then remove from memory before reading the next
    ngs_2016_early = pd.read_csv(
        'NFL_Punt/ngs-2016-reg-wk1-6.csv', dtype=dtypes)  # 8.7 million rows
    ngs = ngs.append(ngs_2016_early.sample(
        n=int(fraction*len(ngs_2016_early)), random_state=random))
    del ngs_2016_early

    ngs_2016_mid = pd.read_csv(
        'NFL_Punt/ngs-2016-reg-wk7-12.csv', dtype=dtypes)  # 8.4 million rows
    ngs = ngs.append(ngs_2016_mid.sample(
        n=int(fraction*len(ngs_2016_mid)), random_state=random))
    del ngs_2016_mid

    ngs_2016_late = pd.read_csv(
        'NFL_Punt/ngs-2016-reg-wk13-17.csv', dtype=dtypes)  # 7.6 million rows
    ngs = ngs.append(ngs_2016_late.sample(
        n=int(fraction*len(ngs_2016_late)), random_state=random))
    del ngs_2016_late

    ngs_2016_post = pd.read_csv(
        'NFL_Punt/ngs-2016-post.csv', dtype=dtypes)  # 900,000 rows
    ngs = ngs.append(ngs_2016_post.sample(
        n=int(fraction*len(ngs_2016_post)), random_state=random))
    del ngs_2016_post

    # Continue with the 2017 files
    ngs_2017_pre = pd.read_csv(
        'NFL_Punt/ngs-2017-pre.csv', dtype=dtypes)  # 6.6 million rows
    ngs = ngs.append(ngs_2017_pre.sample(
        n=int(fraction*len(ngs_2017_pre)), random_state=random))
    del ngs_2017_pre

    ngs_2017_early = pd.read_csv(
        'NFL_Punt/ngs-2017-reg-wk1-6.csv', dtype=dtypes)  # 9.4 million rows
    ngs = ngs.append(ngs_2017_early.sample(
        n=int(fraction*len(ngs_2017_early)), random_state=random))
    del ngs_2017_early

    ngs_2017_mid = pd.read_csv(
        'NFL_Punt/ngs-2017-reg-wk7-12.csv', dtype=dtypes)  # 8.6 million rows
    ngs = ngs.append(ngs_2017_mid.sample(
        n=int(fraction*len(ngs_2017_mid)), random_state=random))
    del ngs_2017_mid

    ngs_2017_late = pd.read_csv(
        'NFL_Punt/ngs-2017-reg-wk13-17.csv', dtype=dtypes)  # 8.3 million rows
    ngs = ngs.append(ngs_2017_late.sample(
        n=int(fraction*len(ngs_2017_late)), random_state=random))
    del ngs_2017_late

    ngs_2017_post = pd.read_csv(
        'NFL_Punt/ngs-2017-post.csv', dtype=dtypes)  # 1 million rows
    ngs = ngs.append(ngs_2017_post.sample(
        n=int(fraction*len(ngs_2017_post)), random_state=random))
    del ngs_2017_post


    # Drop the unnecessary columns
    # I don't know if you will the need Time or dis...
    # Time: the time of play at the start, it should be set to zero at the start of each play
    # dis: the distance traveled from the prior point
    # Season_Year: this is adjusted for with the game weeks
    # Event: most are NA, gives a string with play details - this may give 
    # interesting info if you aggregate the full set, but to do that you would NOT want to sample the data first
    ngs.drop(columns=['Season_Year', 'Event', 'Time', 'dis'], inplace=True)

    # Remove NaN in necessary rows
    ngs = ngs.loc[ngs.GameKey.isna() == False]
    ngs = ngs.loc[ngs.PlayID.isna() == False]
    ngs = ngs.loc[ngs.GSISID.isna() == False]

    # Change the GSISID to Int type - it is currently float
    ngs.GSISID = ngs.GSISID.astype('int')

    # Add the Game_Play and GamePlay with GSISID - this will create a unique identifier for the play by each player
    ngs['Game_Play_ID'] = ngs[colspp].apply(
        lambda row: '-'.join(row.values.astype(str)), axis=1)


    # Create a new column that shows the player's Twist - the difference 
    # between the angles that the player is running (dir) and face orientation while running (o)
    ngs['Twist'] = abs(ngs.dir - ngs.o)



    # These will be duplicates when they are merged with the Punt data, so they should be removed here
    ngs.drop(columns=['GameKey', 'PlayID', 'GSISID'], inplace=True)

    
    # At this point, the Game_Play_ID should be the identifier per player per play
    # Role was not analyzed in ML, but may be useful to look into 
    # Game Day is Monday through Sunday - if you're going to use this, 
    # you'll have to somehow scale it, since there are more games played on 
    # Sundays than any other day, otherwise it becomes a strong predictor of injury 

    return ngs


