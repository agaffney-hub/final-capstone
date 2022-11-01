# NFL Injury Analysis
***Using Machine Learning and Data Analysis to Visualize and Identify Conditions Leading to Injuries in Football***
#### *by* Amy Gaffney, Izzy Irazoque, Kevin Ytturalde, Vincent Fan, and Justin Papreck

--- 
***Contents***
1. Topic and Reason
2. Data Source and Hypothesis 
3. Database Structure and Utilization
4. Exploratory Data Analysis
5. Data Visualization via Tableau
5. Machine Learning Design
6. Machine Learning - Preliminary Findings
7. Machine Learning - Final Models
8. Results and Analysis
9. Project Showcase - Webpage Design


---
# Topic and Reason

In recent years, more concern has grown over sustained injuries that impact the athletes lives long after their athletic career ends. The NFL is looking to identify what changes should be made to minimize the risk of player injury, while not completely altering America's favorite pastime. There are several types of injuries that are incurred - there are gross physiological injuries such as knee, foot, and ankle injuries, and there are also more subtle injuries such as concussions, which can have a much longer-lasting impact on the players, occasionally leading to personality changes and unfortanately, even suicide. It's clear that changes need to be made to address these concerns, but the conflicting view is that the NFL is a multi-billion dollar industry, generating a revenue of over 17 billion dollars in 2021 alone. While changes need to be made, they only impact a fraction of the players. In order to minimize the risk of all players, it's important for the NFL to maintain most of the features of the game if they can modify only certain aspects in order to better ensure the medical safety of their players.

There are several questions we seek to answer: 
1. Are the lower-body injuries strictly associated with a combination or play, field type, weather, and temperature, or is the specific movement on the field required to precisely identify the occurrence of such injuries? 
2. Which features have the strongest correlation with both the lower-body injuries and the concussive injuries? 
3. Are there similar features with both the concussion injuries and lower-body injuries that could be addressed for overall safer play? 
4. Are there predictors to whether an injury is more or less likely to impair a player for over one month? 
5. Can we accurately and precisely predict which types of injuries are prone to occur given the set of features we have used to train a machine learning model? 

To address the lower-body injuries, we applied Random Forest Machine Learning models and Neural Network models, as with these data we had a large control group of non-injured players. To address the concussive injuries, we ultimately used Principal Component Analysis (PCA) in conjunction with K-Means Clustering to determine the major groupings of the concussion injuries. Subsequently, we used a supervised Random Forest model to identify the primary features that separate the classifications. 


--- 
# Data Source and Hypothesis

The data sources are from two Kaggle Challenges: 
- [NFL 1st and Future - Analytics](https://www.kaggle.com/competitions/nfl-playing-surface-analytics/data)
- [NFL Punt Analytics Competition](https://www.kaggle.com/competitions/NFL-Punt-Analytics-Competition/data)


The first sets of data provide information on gross physiological injuries such as foot and knee injuries, whereas the second sets of data provide information regarding concussive injuries. It is likely that the conditions for each of these types of injuries are different, so this will involve a multi-step analysis to assess the parameters that have the highest impact on each type of injury and the severity of the injuries. 

We hypothesize that there is a relationship between the field conditions, player position, time during the season, duration of play during the game, location on the field, and the orientation the player is facing with respect to the direction of their movement (twist) that can predict the occurrence, type, and severity of lower body injury. 

We also hypothesize that there is a relationship between the field conditions, player position, location, time within the season or game, the orientation the player is facing with respect to the direction of their movement (twist), as well as the impact of home/away games and the point distribution at the time of injury that correlates with the incidence of traumatic brain injuries. 

We additionally anticipate that some of the features that lead to the lower-body injuries will overlap with those of the concussion injuries. 


--- 
# Database Structure and Utilization

For this project, after acquiring the data, it was stored in a PostgreSQL database. Each of the databases were organized as follows: 

#### The Injury Analytics Dataset:

The Injury dataset was pulled directly from the SQL database using SQL Alchemy to pull the data from each table for processing, with the exception of the tracking data. The size of the tracking data was prohibitively large for sqlalchemy on a local server, with over 76 million rows. To import this data in the Python files, the data table was downloaded as a csv file from the sql server into a folder labeled NFL_Turf, prior to being read into the python file. The data were connected with the following Entity Relational Diagram (ERD). 
<br><br>
 
 ![Injury_DB](https://user-images.githubusercontent.com/33167541/199137667-6823248c-0ff1-4b82-a58f-9f979658a9ef.png)
 <br><br>

#### The Concussion Dataset: 
For the Punt Analytics dataset, 4 tables were merged using PG Admin and used to create a new table called punt_analytics. This table was imported into the python files using SQL Alchemy as were done with the Injury tables. Also similar to the Injury data, the ngs table (tracking data) were too large to import using SQL Alchemy and again were downloaded locally and imported to python using pandas into a folder labeled NFL_Punt. Only the original data are represented in the ERD.     

<br><br>
![PuntAnalytics_DB](https://user-images.githubusercontent.com/33167541/199137679-8020e74f-1dcf-4f6e-b9ff-364244e785fc.png)
<br><br>

```
CREATE TABLE punt_analytics AS
SELECT
	ppr.gamekey, 
	ppr.playid, 
	ppr.gsisid,
	pi.season_type, 
	pi.quarter, 
	pi.score_home_visiting, 
	gms.stadiumtype, 
	gms.turf, 
	gms.gameweather, 
	gms.temperature, 
	pp.p_position
FROM play_player_role AS ppr
INNER JOIN play_info AS pi
	ON (ppr.gamekey = pi.gamekey AND  ppr.playid = pi.playid)
LEFT JOIN game_data AS gms
	ON (ppr.gamekey = gms.gamekey)
LEFT JOIN player_punt_data AS pp
	ON (ppr.gsisid = pp.gsisid);
```
 
#### Outputs: 
To maintain the fidelity of the original data, result tables following data processing were saved into a new database called NFL_Injuries. The data saved were the Random_Forest_Outputs, Neural_Network_Outputs, Concussion_Analysis, and clean_play_injuries. These tables were pushed to the SQL server using SQL Alchemy. 

---
# Exploratory Data Analysis and Data Cleaning
This Section refers to the files in the Exploratory_Analysis folder: 
- EDA.ipynb
- Preliminary_Injury_Analysis.ipynb

In the exploratory data analysis, we found several inconsistencies and issues within the data tables. Issues that needed to be resolved from the Injuries data were as follows: 
- There were 30 different types of stadiums listed
  - These were altered to either Indoor or Outdoor
- There were 64 unique weather types
  - These were classified categorically as Clear, Indoor, Cloudy, Windy, Hazy/Fog, Rain, Snow
  - These were futher classified dichotomously as Precipitation or No Precipitation
- PlayType had 12 unique plays, but most were different identifications of the same plays
  - These were classified as Pass, Run, or Kick plays
- RosterPosition and Position were listed as either words or abbreviations
  - All positions were converted to the appropriate NFL abbreviations
  - Positions were converted to numerical position types for analysis
- The minimum temperature was listed as -999
  - All temperatures for indoor fields listed as -999 were converted to the average indoor temperature
  - All rowls with temperature labeled -999 for outdoor fields were removed from the dataset
- PlayerGame represented the number game per player, but the weeks continued through the second year, while new players on the same teams starter their first season with a week 1
  - All PlayerGames for each of the two years started at game 1

In the exploratory analysis of the Concussion data, there were additional inconsistencies: 
- There were 24 different types of turf listed in the game_data table
  - This was converted to Natural or Synthetic
  - All unknown were dropped
- Weeks - the weeks started at 1 for each part of the season: preseason, regular season, and post season 
  - The number of weeks of preseason was added to the regular season values
  - The number of weeks of preseason and regular season was added to the post season values
- Weather was similar to the Injury findings
  - Weather was categorizes as were the injury data
- The GSISID was input as an integer value in all of the tables except for the ngs table, which made it difficult to set as a key
  - GSISID was converted to integer type to merge the ngs data with the other imported merged tables
- Video_Footage tables were included in the original data
  - These were not used in our analysis and were not included in the database

This section refers to the python files used for data cleaning in the different analyses, found in the Machine_Learning_Files, and in Main:
- ColumnCapitals.py: some data imported from SQL drops the capitalizations from the Headers; back to the original format
- MergeCleaner.py: Merges and maps positions as numerical from the NGS in the Punt data
- NGS_Sampler.py: Opens each of the NGS files, appends to the same csv, and creates a unique identifier, and samples the data before returning the df
- Punt_SQL_Cleaner.py: Classifies turfs, stadiums, and weather, fixes the weeks, and separates the home score and score difference between the teams with data acquired from SQL Alchemy
- Punt_Cleaner.py: Identical to the above file, only for the case when sqlalchemy isn't used and the 4 files must be opened and merged
- InjuryCleaningFunctions.py - this contains a set of functions used for data cleaning
  - vis_data_cleaner produces outputs necessary for visualization using the appropriate functions
  - ml_data_cleaner does the same as vis_data_cleaner, only changes all categorical features into numerical for machine learning
  - Cleaning Subroutines: 
    - stadium_coder: changes stadium to indoor/outdoor
    - temperature_adjuster: fixes the -999 issue
    - weather_coder: encodes the weather
    - precipitation_coder: creates the precipitation column
    - playerday_adjuster: changes the days the player has played adjusting for the year
    - play_coder: categorizes plays as Rush, Pass, or Kick
    - injury_coder: classifies injury types and adds 'NoInjury' to the merged values and removes all na
    - injury_duration_classifier: takes the 4 columns for duration and creates a single column with the 4 values
    - injury_duration_coder: classifies injuries as either Severe (over 28 days) or not in a new columns 'SevereInjury
  - Visualization Subroutines
    - vis_position_coder: changes RosterPositions to the NFL abbreviations
    - vis_process_playlist_data: runs the appropriate Cleaning Subroutines from the playlist dataframe
    - vis_process_injury_data: runs the appropriate Cleaning Subroutines from the injury dataframe
  - Machine Learning Subroutines
    - suface_coder: maps the surfaces as 0 or 1 for 'SyntheticField'
    - ml_position_coder: changes positions from abbreviations or names to numerical 
    - ml_process_playlist_data: applies appropriate Cleaning Subroutines to the playlist dataframe
    - ml_process_injury_data: applies appropriate Cleaning Subroutines to the injury data and drops future redundant columns prior to merge
 
---
# Data Visualization 
Several key factors have been clearly demonstrated with visualizations produced both using Python and Tableau: 
- [NFL Injury Data](https://public.tableau.com/app/profile/aj5583/viz/NFLInjuryData_16660655174710/Story1?publish=yes)
- Visuals_2.ipynb
- Visuals_3.ipynb

During the creation of visuals both in Tableau and using MatplotLib, we were able to work through the datasets in search of any correlations that may lead to insight in factors associated with the injuries: 
- Which parts of the field were more prone to the different types of injuries
<br><br>
![End_of_play](https://user-images.githubusercontent.com/33167541/199360777-272c66fa-ea33-4387-9939-e6f07b6518ac.png)
<br><br>

- Where on the field different certain defensive and offensive positions were sustaining more injuries and where they were least likely to occur

<br><br>
![Linebacker_Knee](https://user-images.githubusercontent.com/33167541/199360875-9f38905e-2923-40a8-87d1-687d4a4798cc.png)
<br><br>
![Runningback_ankle](https://user-images.githubusercontent.com/33167541/199360923-29c9bf65-2ff7-441a-bf90-ed3dd282d220.png)
<br><br>
<img width="918" alt="FieldInjuryPlaysTab" src="https://user-images.githubusercontent.com/33167541/199361022-8a96f2de-ab6d-4130-a66b-9cfd2ecc3478.png">
<br><br>

- We noticed that concussions in punt plays alone vastly outnumbered the lower-body injuries in a 2 season period
- The temperatures with the highest number of injuries were 68 and 70 degrees - though it should be noted that indoor fields are kept at these temperatures, so it may not be a valid predictor of injury

<br><br>
![Injury_Temp](https://user-images.githubusercontent.com/33167541/199361377-3ee8b130-0c13-49f3-9dc4-48ca3d3b4cd1.png)
<br><br>

- Foot injuries were the least frequently occurring injuries from the datasets

<br><br>
<img width="566" alt="InjuryChartsTab" src="https://user-images.githubusercontent.com/33167541/199361450-ebce037a-ab18-4702-8b60-1924fae540e6.png">
<br><br>

- There was a correlation with severe injuries, resulting in over 4 week recovery and synthetic turf

<br><br>
![Field_Type_Duration](https://user-images.githubusercontent.com/33167541/199361494-c36dab8f-4042-4af1-ae88-4a3b2ebe623d.png)
<br><br>

Implementing the interactive models using Tableau allows a user to select from different parameters (position, injury type, etc.) and see the movement of a player on the field to give better depth in understanding of how the injury was sustained. 

In the future, we would like to create a visualization to the the direction of movement and player orientation with vectors throughtout the play to show the player's path prior to concussion - as the twist was the primary factor that correlated with the learning model.




--- 
# Machine Learning Design

The Machine Learning Design was broken up into two parts, as the Lower-Body Injury data and Concussion data presented different aspects that only allowed for different types of machine learning analyses. The final Model Designs were as follows: 

### Lower-Body Injury Analysis
1. Neural Network - Deep Learning with 2 hidden layers of 256 nodes and 128 nodes

The lower-body injury analysis was a very unbalanced dataset containing a small number of injuries with a large set of plays without injuries. The data without injuries functioned as a control group used for classification in a supervised analysis. The initial model used Random Forests, as it produced a very high accuracy. However, the precision was the more important consideration with the imbalanced data, and the neural network model provided a much higher precision than did the ensemble learning.  

### Concussion Analysis
1. PCA feature extraction
2. K-Means Clustering (Unsupervised)
3. Random Forest Feature Analysis

All instances of the concussion data were incidents with concussions, preventing us from using a supervised model. The best results were achieved with a PCA feature extraction, reducing the features to 3 dimensions, more ideal for visualization. Following the feature extraction, K-Means clustering was used to classify the data into the groups. Both a dendogram and an elbow curve were used to determine the number of cluseters to use. Because of the ambiguity incurred with the feature extraction, we used a Random Forest classifier to determine which features had the strongest association with each of the outputs.  

--- 
# Machine Learning Preliminary Findings 
## Unsupervised Learning
We initially used unsupervised learning to see what features would lead to clusters with the Injury data. K-Means Clustering was used to perform the unsupervised analysis, using a PCA feature extraction to group the features to 3, for the ability to create a 3D visualization. The initial model analyzed all of the data, including all plays without injuries and those with injuries. To determine the ideal number of k classifiers, we employed an elbow-curve analysis. There was a strong curve delineation at k=2, so this was performed and shown below. 

![Elbow_Curve1](https://user-images.githubusercontent.com/33167541/195501892-e3600a8b-01d6-42db-8be4-74be9457a3d5.png)

![2-means-all-data](https://user-images.githubusercontent.com/33167541/195502047-22a06e8f-1a21-4127-afe1-b82cc0311cbc.png)

Unfortuantely, the injuries were not successfully classified, and the differences between the groups largely had to do with the number of games played. 
The next model removed all of the non-injury data from the dataset, to try to isolate the features that had the greatest influence on these data. The main joints occurred at k=3 and k=6. The grouping with k=3 left one group with very ambiguous correlations, so the results from the k=6 analysis are reported below. 

![6-means-injury-data](https://user-images.githubusercontent.com/33167541/195502957-9b868884-267a-4d7c-804b-d6e4e8edfcf4.png)


## Supervised Learning
The following files are a composite of those in the Preliminary Models, and are themselves contained in Machine_Learning_Files:
- Preliminary_Injury_Supervised_Learning.ipynb
- Preliminary_Injury_Unsupervised_Learning.ipynb

These initially analyses did not incorporate tracking information. The goal was to determine whether the features not including the tracking data could provide a model with high enough accuracy and precision. 

Due to the nature of the Injury Dataset being extremely imbalanced, we used the Balanced Random Forest Classifier from the imbalanced learn library. In preparing the data for processing, the positions were encoded in a single column by numbers, as described above, however the plays were encoded with OneHotEncoder, giving us 3 columns for each of the plays.

The original dataset contained 260,000 rows with only 77 injuries. Because of this large difference, we tried several approaches, including Undersampling and SMOTEENN, but ultimately, we just split the data using train_test_split() from the scikit learn library both with and without stratification.

**Determine whether an injury occurred**
The original model achieved a 58% accuracy and worse precision. We further analyzed the feature importances. 

![Prelim_RF](https://user-images.githubusercontent.com/33167541/199139830-d8ecd68f-b623-41be-92de-61376e859c32.png)


The next analyses utilized a Complement Naive Bayes analysis; this type of Naive Bayes is more suitable for extremely imbalanced datasets. Similar to the Random Forest model, the results only provided a 58% accuracy. Likewise, an EasyEnsemble Boosting algorithm was tested again with similar results. From these analyses, we concluded that additional information would be necessary to further improve our models. The Random Forest and Complement Naive Bayes are shown below:

![Naive_Bayes_Confusion](https://user-images.githubusercontent.com/33167541/199350852-23d4ee01-39bb-4f44-b925-35c97e8bccd6.png)

Futher development of the dataset included the spatial parameters that should gave more predictive capability, indicating the great impact on the potential for injury. Using these data with random sampling the non-injury data were reduced to achieve a 100:1 distribution from the 3000:1 distribution we started with. Once the spatial data were added, this dataset expanded substantially, making a big impact on processing. Each of the Random Forest models was able to predict with 99% accuracy, and few to no false negatives: 

**Was there a severe injury?**
<br><br>
![RF_IsSevere](https://user-images.githubusercontent.com/33167541/196870375-b4c37c10-d2be-4226-a7e6-269a436f49cb.png)
<br><br>

**What body part was injured?** 
<br><br>
![RF_InjuryType](https://user-images.githubusercontent.com/33167541/196870409-dc59d14f-e26d-4d09-a7a0-b78e7f48ac81.png)
<br><br>

**How long was the player out?** 
<br><br>
![RF_InjuryDuration](https://user-images.githubusercontent.com/33167541/196870473-c93f4f22-a61b-40e5-82d9-7f2db68a9370.png)
<br><br>

 From the outputs of the Machine Learning models and the exploratory analysis, graphics for the dashboard will be created using a combination of python generated plots and interactive features, which will be imbedded into a webpage using JavaScript, HTML, and CSS. 

## Random Forest Adaptation
- Injury_Supervised_Random_Forest.ipynb

**Was the player injured?**
The adaptations from the original model to the final models for the Injury Data was the addition and cleaning of the tracking data. With the addition of the tracking information, the Balanced Random Forest Classifier with 10 estimators provided a 99.96% accuracy, a much higher accuracy than was achieved with the any of the models not including the tracking data. With the addition of the tracking data, the number of rows increased to several thousand. In addition to the 99.97% accuracy, this model yielded under 5 false negatives, and 145 false positives from the dataset including 550,000 true negatives and 5500 true positives. 

In the feature analysis, we confirmed that the strongest feature in the feature analysis was the number of days played, closely followed by the temperature, and the time of the play during the game. Other stronger predictors were the player's position and the location along the length of the field. 

<br><br>
![RF_IsInjured](https://user-images.githubusercontent.com/33167541/199139918-20a5c6de-9055-4a10-9be0-31d731e30dce.png)
<br><br>


**Was the injury severe?**
The same process as above was followed, yielding a 99.97% accuracy and a lower, 90.35% precision. 

<br><br>
![RF_IsSevere](https://user-images.githubusercontent.com/33167541/199140001-d34df505-999a-42b1-bde9-6f7ab8c77472.png)
<br><br>

**What type of injury was predicted?**
The overall accuracy of this model with 4 outputs was again 98.59%, but the precision started to really drop: 
- Foot injury, 78.94% precision
- Ankle injury, 42.61% precision
- Knee injury, 27.25% precision

<br><br>
![RF_InjuryType](https://user-images.githubusercontent.com/33167541/199140053-1cbfb00d-22e5-47ab-bbdb-03d05758bcc4.png)
<br><br>

**What was the predicted duration of injury?**
The overall accuracy remains high at 99.77%, but the precision continues to drop: 
- Under 1 day, 60.00% precision
- Under 1 week, 35.67% precision
- Under 4 weeks, 56.12% precision
- Under 6 weeks, 63.75% precision

<br><br>
![RF_InjuryDuration](https://user-images.githubusercontent.com/33167541/199140090-656235a8-0c10-46ca-bc51-76e244cee6ba.png)
<br><br>

### Final Random Forest Results Summarized
The Random Forest Classifiers predicting multiple outcomes were more difficult to predict the accuracy and recall specifically, and they were not possible to evaluate like this for the neural network model. These results were summarized in the following table: 
 
<br><br>
![RandomForestResults](https://user-images.githubusercontent.com/33167541/199140164-b025c02a-3616-4ccc-8c15-55eb2abdbf3f.png)
<br><br>


---
# Machine Learning - Working Models:
## Deep Learning/Neural Network Analysis
In the final model, there were some changes made from the preliminary models:
1. The positive injury data were removed, a random sampler was used to reduce the non-injury data, reducing the control data such that there would be a 99:1 balance of data. The injuries were then added back to the dataset
2. When splitting the data in the test_train_split, the data was stratified based on the injury data
3. The data were scaled using StandardScaler before creating the neural network model

Several different parameter configurations were tested with the neural networks, starting with the lowest complexity - a single layer with increasing numbers of nodes - to higher complexity - two layers with increasing the numbers of nodes in either layer. The final model used 256 nodes in the first hidden layer and 128 nodes in the second hidden layer of a sequential model. The hidden layers each used Relu activation and a Sigmoid output. Compiling used a binary crossentropy loss model because each of the outputs were binary outcomes, as opposed to a categorical crossentropy model. Though there were categorical ouputs in some of the models, each of the outputs remained a binary classification. The optimizer used was an adam optimizer. In order to compare the outcomes of this model with the Random Forest model, the metrics tracked were accuracy, precision and recall.  

The Tests Performed: 
- **Was the player injured?**
- **Was the injury severe?**
- **What type of injury was predicted?**, a 4-class output
- **Was the injury a foot injury?**
- **Was the injury an ankle injury?**
- **Was the injury a knee injury?**
- **What was the predicted duration of injury?**, a 5-class output

The Results: 
<br>
![NeuralNetworkResults](https://user-images.githubusercontent.com/33167541/199140459-d237b0e0-b02d-4153-bbd0-7435cb6b9777.png)
<br>
---
## Unsupervised Concussion Analysis
Similar to the Injury Analysis, the tables were merged including the tracking data, creating a very large dataset. In order to perform the clustering analysis, there are several ways to break the data into different clusters. The first approach was using Agglomerative Clustering, which required a size reduction to create a dendogram. The dendogram shows the highest break at two, followed by three clear clusters. 

This analysis was performed with 3 clusters prior to breaking up into two sets using train_test_split for feature classification. A Balanced Random Forest Classifier was used with 100 estimators to determine which features have the highest correlation with the different classes. In this case, the highest correlation was the Twist, the difference between the orientation of the player and the direction of movement. 

<br><br>
![Dendogram_Concussion_Data](https://user-images.githubusercontent.com/33167541/199140744-346dc35f-a509-4bd3-9170-fb591dba6710.png)
<br><br>

Following the Agglomerative Clustering, we used PCA data extraction to reduce the dimensions to 3 components. Testing for the ideal number of clusters for K-Means analysis, we utilized an elbow curve, where there was a very distinct bend at k=2. The K-Means clustering was performed with 2 clusters. The K-Means analysis was plotted using hvplot as shown below: 
<br>
![Elbow_Curve1](https://user-images.githubusercontent.com/33167541/199140785-effcfeeb-eb92-4869-91ec-1af541682aca.png)
<br>
![K-Means_Cluster](https://user-images.githubusercontent.com/33167541/199140821-8ea6a78a-d6f4-401a-ae3f-8ef2570485b3.png)
<br>

The highest predictor was, again, the Twist, with about 98% importance with the feature analysis. 

---
# Results and Analysis
Considerations that were made during these analyses. Because of the nature of the analyses being of medical nature, and furthermode the investigations were of the presence, identification and duration of injuries, the measure of accuracy is not a particularly reliable measure. While accuracy is important, it only highlights how accuate the models were in identifying the non-injured players. In fact, if the model had miscategorized all of the injured players as non-injured, the model would still achieve a 99.97% accuracy based on the balanced accuracy report due to the imbalance in the number of true positive and true negative values. The validation test results without the positional data only contained 18 injured values, but 59098 non-injury plays for comparison. 
In this study, the precision is a much better statistic to measure, as it looks at the True Positives compared to all Positives labeled (True Positives + False Positives). Recall, on the other hand, is the ratio of True Positives to True Measurements (True Positives + False Negatives). The prediction of a False Positive is much more desirable than the prediction of a False Negative. A False Positive signifies that the model predicted an injury when no injury occurred, whereas a False Negative predicts that no injury occurred, when one actually did. Our interpretation of the the False Positives in the findings were that those plays could be classified as "High Risk" plays: since the model predicted them as plays associated with injuries, all of the features that could lead to an injury were there, but no player incurred an injury. A False Negative, on the other hand, would suggest that the model is insufficient in its predictive capabilities. Therefore, our goal was to achieve a model with the highest possible precision in the predicition of injury, injury types, and severity of the injury. 
From our non-machine learning data analysis, we found 



Our findings address the questions both within the datasets and between the datasets, answering the original questions we posed: 

1. Are the lower-body injuries strictly associated with non-spatial features across the football field? 
  - The original supervised machine learning model had a very low accuracy, with the maximum accuracy of around 60% with the EasyEnsemble Boosting Algorithm. Worse than the accuracy, however, was that the precision in this model was only around 50%. To answer the initial question: no, the model without tracking data was insufficient in predicting lower-body injuries on the football field. 
  -  The modified supervised machine learning model incorporating the NGS tracking data achieved accuracies over 98% for all Random Forest Models, but had a broad range of Precision, ranging from 27% Precision (identifying Foot Injury) to 97% Precision (identifying the occurrence of any Injury). 
  -  The Final Neural Network model incorporating the NGS tracking data yielded over 99% accuracy for all tests, but had a much tighter range of precision with the lowest of 91.7% Precision (predicting whether an injury is Severe) to 99.9% Precision on multiple tests. 

2. Which features had the strongest correlations with the lower-body injuries and the concussive injuries?
  -  The features that maintained the highest influence across the presence of and prediction of the lower body injuries were the number of days played, temperature, play in the game, field location, and roster position. The higher number of days played indicates how far into the season the player has been playing. The play in the game what time during the game the injury occurred. Field location is specifically accross the length of the field, the position along the width of the field did not seem to have a major impact. And the temperature of the game. 
  -  In the concussion analysis, the primary feature associated with the injury were the twist of the player, a measure of the orientation the player was facing compared to the direction of movement. The other features, to a much lesser scale, were the location on the field, temperature, and player position.

3. Are there similar features between the concussion and lower-body injury datasets that could be addressed for overall safer play? 
  - The main indicators that overlapped as influencial features were the temperature and the distance across the field.
  - The locations on the field are not something that can be changed, as it seems to be a 'wrong place at the wrong time' set of conditions that led to the injuries
  - The temperature issue can be addressed by updating the outdoor stadiums to retractable-rood dome stadiums, where the climate can be better controlled during parts of the year when conditions are more prone to injury.
  - Linebackers are nearly 3 times more likely to get a concussion than most other positions, making up 26% of all concussion injuries, followed by Cornerbacks at 16% and Wide Receivers at 10%. 
  - Linebackers are similarly disproportionately higher in sustaining lower-body injuries, representing 27% of injuries, followed by Wide Receivers at 21% and Safeties at 14%. 
  - Linebackers have the highest incidence of both concussions and lower body injuries, making this by far the highest risk position on the field (LB, OLB, MLB, ILB combined)
  - Wide Receivers have the highest incidence of offensive play injuries, and are likely due to different circumstances than the linebackers given the differences in the play styles of the positions


4. Are there any predictors to whether an injury is more or less likely to impair a player for over four weeks?
  - The biggest difference between the duration of the injuries was the type of turf the games were played on
  - Games played on natural fields yielded a higher number of injuries that lasted under 7 days and up to one month
  - The majority of all incurred injuries that lasted longer than 4 weeks, most of which were longer than 6 weeks, were incurred on synthetic turf
  
<br><br>
![Field_Type_Duration](https://user-images.githubusercontent.com/33167541/199140861-bce26c8a-6c05-4a97-9570-e199a82f1128.png)

<br><br>

5. Can we accurately and precisely predict which types of injuries are prone to occur given the set of features we have used to train a machine learning model? 
  - Yes, the Neural Network model was able to predict conditions leading to a Foot, Ankle, or Knee injury within 99.9% accuracy with 99.5% Precision
  - We also know that certain positions and plays are much more prone to incidence of each type of injury


## Future Directions
We would like to further assess the predictive capabilities of which exact conditions would both maximize and minimize the chances of injury. Our current model can predict whether certain given parameters will predict high risk or injury. To do this we will need to perform Regression analyses to determine what Temperatures parameters lead to injuries, in order to best inform the NFL and players what precautions to take.

Limitations of our Neural Network model is the ambiguity associated, while it was easier to extract feature importances from the Random Forest algorithm, we have not been able to directly extract the feature importances from the Neural Network model. In future analyses, we would like to remove the lowest impact features found with the Random Forests analyses to see whether we can maintain the high accuracy and precision with the deep learning model, better reinforcing our understanding of the feature importance of the model. 

Finally, our concussion analysis was unsupervised because of a lack of control data without sustained concussion injuries. Although the data from the lower-body injuries and the concussion injuries were collected from two different sets of years, we do have information from the lower-body dataset of many plays with the same known parameters where no injuries were incurred. We would like to use these data to create a predictive model extracting only the non-injury punt plays from the initial dataset to use to establish a Predictive Supervised model with a more robust feature analysis for the concussion dataset. 


--- 
# Project Showcase 

To communicate our findings, we have designed a webpage using Javascript, CSS and HTML. Our interactive dashboard enables the user to select injuries by parameters, such as field type, surface type, location, and duration of play during the game. Our webpage allows the user to explore the different features of our exploratory study of injuries in the NFL. The main interactive elements of our page are connected to the Tableau link, where the user can explore the different charts, making the selections they desire to see, along with a description of the results that we've extrapolated from these findings. 
The machine learning page presents the findings of the final models for the Injury Analysis as well as the Concussion Analysis with images from the Unsupervised analyses as well as tables presenting the Accuracy, Precision, and Recall from the Final Supervised models. The presentation page links to the Google Slides Presentaiton that functioned as our Stakeholder Presentation. 
  The database link describes the data, its storage, and how it was used in the analysis???? 


<div class='tableauPlaceholder' id='viz1666138420638' style='position: relative'><noscript><a href='#'><img alt='NFL Injury Data ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NF&#47;NFLInjuryData_16660655174710&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='NFLInjuryData_16660655174710&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NF&#47;NFLInjuryData_16660655174710&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                

<br><br><br>

### Home Page

<img width="1271" alt="Screen Shot 2022-10-19 at 9 06 04 PM" src="https://user-images.githubusercontent.com/106010498/196854243-487f5eed-076e-4925-b1de-2356ec8b6c69.png">
<img width="1274" alt="Screen Shot 2022-10-19 at 9 06 18 PM" src="https://user-images.githubusercontent.com/106010498/196854251-3f3c573b-4854-48c7-acb9-2d86422de40c.png">
<img width="1256" alt="Screen Shot 2022-10-19 at 9 22 01 PM" src="https://user-images.githubusercontent.com/106010498/196855898-0732c4d4-690a-413d-8734-38ce6316b406.png">


### Interactive Elements via Tableau
To connect the Tableau page to our site, embedcodeing was applied from the web version tableau and added it to the webpage. 


<img width="951" alt="Screen Shot 2022-10-19 at 9 39 28 PM" src="https://user-images.githubusercontent.com/106010498/196858364-64e12e38-aeaf-49fa-8405-0356280c930d.png">

*THIS CODE IS BROKEN*
<img width="1265" alt="Screen Shot 2022-10-19 at 9 39 37 PM" src="https://user-images.githubusercontent.com/106010498/196858373-dbfd6b41-0445-4ba3-ae1d-76351741dfab.png">


### Machine Learning


### Database


### Presentation
The stakeholder presentation is available on Google Slides: 
[NFL Injury Analysis](https://docs.google.com/presentation/d/1JuRKtG8ZdwiY1gHwosXbu1rs_UrsjU8sO4iqMHOnGEc/edit?usp=sharing)

**INSERT PRESENTATION SLIDE1 HERE**
