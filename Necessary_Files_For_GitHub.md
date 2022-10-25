# Files for Final GitHub:

## Necessary Program Files for Exploratory Data Analysis:
- Supervised_Clean.ipynb - the initial clean using dummies
- Preliminary_Supervised.ipynb - the initial supervised model using the output from supervised clean, yielded a 53% accuracy with almost all false negatives
- EDA - provides a head() for each of the files we used as well as a description of the data contained within
    - Redundant with firstanfutureexplore.ipynb
    - Redundant with puntexplore.ipynb
- Preliminary_ML - an unsupervised analysis that defined 2 main groups for the injury data, not yet done with Supervised feature extraction
- Preliminary_Injury_ML - another unsupervised set that also shows the exploratory phase and decision-making for processing data

## Necessary Program Files for Databases:
- SQLAlchemy_Connection - sets up connections to SQL Alchemy, also need to write two .sql files for the tables setup within postgres, added at the bottom of this file

## Necessary Data Processing Python Files: 
- NGS_Cleaner.py
- NGS_Sampler.py
- NGS_Tracking_Cleaner.py
- NFL_Injury_Cleaning_Functions.py
- Punt_Cleaner.py

## Necessary Visualization Files: 
- Visuals_2.ipynb
- Visuals_3.ipynb

## Necessary Webpage Files: 
- webpage/
- Images/
- Dashboard/

## To Be Removed: 
- NGS_Clean_and_Connect.ipynb - this was replaced with the NGS_xxx.py functions
- puntexplore.ipynb
- firstandfutureexplore.ipynb
- Data_Cleaners.ipynb - this just demonstrates that NGS_Cleaner and NGS_Sampler work, but isn't necessary to the model
- play_injuries_inner.csv
- play_injuries_super.csv
- play_injuries.csv
    Is anyone using any of these 3 files? 
- FF_ERD.txt - this file is empty
- Shared_Tables/  - this folder should be removed by final, since this data will be acquired using the raw data - those tables will be exported to the db, and then called from the db for processing
- solo_vis_injury_tracking.csv/.xlsm - instead of writing to file, we should export these to the db

--- 

## Need to create new files for the following: 
### Cleaning
- Show Cleaning Functions with Markdown
    - Explain Feature Selection
    - Explain changes
    - Export tables to SQL

### Supervised Injury
- Show initial Model with crappy results
    - Import from SQL
    - Show results
    - Explain changes to be made
- Showcase final Model 
    - Connect to SQL
    - Explain Changes made
    - Show results
    - Compare to unsupervised feature analysis
    - Analyze

### Unsupervised Injury
- Show findings from Unsupervised
    - Import from SQL 
    - Add supervised feature analysis

### Unsupervised Concussion
- Showcase final model
    - Import from SQL 
    - Show results
    - Compare to Injury data
    - Analyze

### Database
- New .sql files
    - Punt 
    - Injuries
    - Merges and new table creation

### Visualizations
- Publication quality visuals for: 
    - everything