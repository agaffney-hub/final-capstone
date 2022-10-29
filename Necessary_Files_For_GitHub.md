# Files for Final GitHub:

## Necessary Program Files for Exploratory Data Analysis:
- Review_Preliminary_Injury_Analysis.ipynb, 
    - replaces Supervised_Clean.ipynb
    - Initial clean using OneHotEncoder, no tracking
- Review_Preliminary_Supervised_ML.ipynb
    - Preliminary_Supervised.ipynb
    - initial supervised model using the output from supervised clean, yielded a 58% accuracy with almost all false negatives
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
- Review_Concussion_Analysis.ipynb - Unsupervised models for the concussion datasets
- 
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