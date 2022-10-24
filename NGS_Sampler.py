def NGS_Cleaner(fraction=0.01):
    #This function Appends and Cleans the NGS Data
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
    ngs_2016_pre = pd.read_csv('NFL_Punt/ngs-2016-pre.csv', dtype=dtypes)  # 1 million rows
    ngs = ngs_2016_pre.sample(n=int(fraction*len(ngs_2016_pre)))
    del ngs_2016_pre

    # The next process is to open the next csv, append to the df, then remove from memory before reading the next
    ngs_2016_early = pd.read_csv(
        'NFL_Punt/ngs-2016-reg-wk1-6.csv', dtype=dtypes)  # 8.7 million rows
    ngs = ngs.append(ngs_2016_early.sample(n=int(fraction*len(ngs_2016_early))))
    del ngs_2016_early

    ngs_2016_mid = pd.read_csv(
        'NFL_Punt/ngs-2016-reg-wk7-12.csv', dtype=dtypes)  # 8.4 million rows
    ngs = ngs.append(ngs_2016_mid.sample(n=int(fraction*len(ngs_2016_mid))))
    del ngs_2016_mid

    ngs_2016_late = pd.read_csv(
        'NFL_Punt/ngs-2016-reg-wk13-17.csv', dtype=dtypes)  # 7.6 million rows
    ngs = ngs.append(ngs_2016_late.sample(n=int(fraction*len(ngs_2016_late))))
    del ngs_2016_late

    ngs_2016_post = pd.read_csv(
        'NFL_Punt/ngs-2016-post.csv', dtype=dtypes)  # 900,000 rows
    ngs = ngs.append(ngs_2016_post.sample(n=int(fraction*len(ngs_2016_post))))
    del ngs_2016_post

    # Continue with the 2017 files
    ngs_2017_pre = pd.read_csv(
        'NFL_Punt/ngs-2017-pre.csv', dtype=dtypes)  # 6.6 million rows
    ngs = ngs.append(ngs_2017_pre.sample(n=int(fraction*len(ngs_2017_pre))))
    del ngs_2017_pre

    ngs_2017_early = pd.read_csv(
        'NFL_Punt/ngs-2017-reg-wk1-6.csv', dtype=dtypes)  # 9.4 million rows
    ngs = ngs.append(ngs_2017_early.sample(n=int(fraction*len(ngs_2017_early))))
    del ngs_2017_early

    ngs_2017_mid = pd.read_csv(
        'NFL_Punt/ngs-2017-reg-wk7-12.csv', dtype=dtypes)  # 8.6 million rows
    ngs = ngs.append(ngs_2017_mid.sample(n=int(fraction*len(ngs_2017_mid))))
    del ngs_2017_mid

    ngs_2017_late = pd.read_csv(
        'NFL_Punt/ngs-2017-reg-wk13-17.csv', dtype=dtypes)  # 8.3 million rows
    ngs = ngs.append(ngs_2017_late.sample(n=int(fraction*len(ngs_2017_late))))
    del ngs_2017_late

    ngs_2017_post = pd.read_csv(
        'NFL_Punt/ngs-2017-post.csv', dtype=dtypes)  # 1 million rows
    ngs = ngs.append(ngs_2017_post.sample(n=int(fraction*len(ngs_2017_post))))
    del ngs_2017_post


    # Drop the unnecessary columns 
    ngs.drop(columns=['Season_Year', 'Event', 'Time', 'dis'], inplace=True)

    

    # Clean the rows
    ngs = ngs.loc[ngs.GameKey.isna() == False]
    ngs = ngs.loc[ngs.PlayID.isna() == False]
    ngs = ngs.loc[ngs.GSISID.isna() == False]


    # Change the GSISID to Int type - it is currently float
    ngs.GSISID = ngs.GSISID.astype('int')

    # Add the Game_Play and GamePlay with GSISID to the video review
    ngs['Game_Play_ID'] = ngs[colspp].apply(lambda row: '-'.join(row.values.astype(str)), axis=1)

    ngs.drop(columns=['GameKey', 'PlayID', 'GSISID'], inplace=True)



    return ngs
