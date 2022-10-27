# Files for Final GitHub:

## Necessary Program Files for Exploratory Data Analysis:
- Review_Preliminary_Injury_Analysis.ipynb, 
    - replaces Supervised_Clean.ipynb
    - Initial clean using OneHotEncoder, no tracking
- Review_Preliminary_Supervised_ML.ipynb
    - Preliminary_Supervised.ipynb
    - initial supervised model using the output from supervised clean, yielded a 58% accuracy with almost all false negatives
- EDA - provides a head() for each of the files we used as well as a description of the data contained within
    - Redundant with firstanfutureexplore.ipynb
    - Redundant with puntexplore.ipynb
- Review_Preliminary_Injury_ML
    - Replaces Preliminary_Injury_ML and Preliminary_ML
    - Unsupervised set that also shows the exploratory phase and decision-making for processing data
    - Also performs feature importance analysis

## Necessary Program Files for Databases:
- SQLAlchemy_Connection - sets up connections to SQL Alchemy, also need to write two .sql files for the tables setup within postgres, added at the bottom of this file

## Necessary Data Processing Python Files: 
- NGS_Cleaner.py
- NGS_Sampler.py
- NGS_Tracking_Cleaner.py
- NFL_Injury_Cleaning_Functions.py
- Punt_Cleaner.py

## Necessary Machine Learning Files: 
- Review_Injury_Supervised_ML.ipynb - the random forest analysis with feature analysis
- Review_Injury_Supervised_NN.ipynb - neural network model, improving the precision on the random forest model
- Concussion_Analysis.ipynb - Unsupervised models for the concussion datasets
- NeuralNetwork_Results.csv
- RandomForest_Results.csv

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
- Preliminary_ML - an unsupervised analysis that defined 2 main groups for the injury data, not yet done with Supervised feature extraction
- Preliminary_Injury_ML - another unsupervised set that also shows the exploratory phase and decision-making for processing data

--- 

## Need to create new files for the following: 
### Cleaning
- Show Cleaning Functions with Markdown
    - Explain Feature Selection
    - Explain changes
    - Export tables to SQL

### Supervised Injury
- Show initial Model with crappy results
    - Show results
    - Explain changes to be made
- Showcase final Model 
    - Explain Changes made
    - Show results
    - Compare to unsupervised feature analysis

### Unsupervised Injury
- Show findings from Unsupervised
    - Add one more Unsupervised injury analysis similar to the Concussion

### Unsupervised Concussion
- Showcase final model
    - Merge Tables in SQL
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