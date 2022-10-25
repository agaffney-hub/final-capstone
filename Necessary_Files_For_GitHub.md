# Files for Final GitHub:

Necessary Program Files for Exploratory Data Analysis:

- Supervised_Clean.ipynb - the initial clean using dummies
- Preliminary_Supervised.ipynb - the initial supervised model using the output from supervised clean, yielded a 53% accuracy with almost all false negatives
- EDA - provides a head() for each of the files we used as well as a description of the data contained within
    - Redundant with firstanfutureexplore.ipynb
    - Redundant with puntexplore.ipynb
- Preliminary_ML - an unsupervised analysis that defined 2 main groups for the injury data, not yet done with Supervised feature extraction
- Preliminary_Injury_ML - another unsupervised set that also shows the exploratory phase and decision-making for processing data

Necessary Program Files for Databases:

- SQLAlchemy_Connection - sets up connections to SQL Alchemy, also need to write two .sql files for the tables setup within postgres, added at the bottom of this file

Necessary Data Processing Python Files: 
- NGS_Cleaner.py
- NGS_Sampler.py
- NGS_Tracking_Cleaner.py
- NFL_Injury_Cleaning_Functions.py
- Punt_Cleaner.py