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
## Topic and Reason

In recent years, more concern has grown over sustained injuries that impact the athletes lives long after their athletic career ends. The NFL is looking to identify what changes should be made to minimize the risk of player injury, while not completely altering America's favorite pastime. There are several types of injuries that are incurred - there are gross physiological injuries such as knee, foot, and ankle injuries, and there are also more subtle injuries such as concussions, which can have a much longer-lasting impact on the players, occasionally leading to personality changes and unfortanately, even suicide. It's clear that changes need to be made to address these concerns, but the conflicting view is that the NFL is a multi-billion dollar industry, generating a revenue of over 17 billion dollars in 2021 alone. While changes need to be made, they only impact a fraction of the players. In order to minimize the risk of all players, it's important for the NFL to maintain most of the features of the game if they can modify only certain aspects in order to better ensure the medical safety of their players.

There are several questions we seek to answer: 
- Are the lower-body injuries strictly associated with a combination or play, field type, weather, and temperature, or is the specific movement on the field required to precisely identify the occurrence of such injuries? 
- Which features have the strongest correlation with both the lower-body injuries and the concussive injuries? 
- Are there similar features with both the concussion injuries and lower-body injuries that could be addressed for overall safer play? 
- Are there predictors to whether an injury is more or less likely to impair a player for over one month? 
- Can we accurately and precisely predict which types of injuries are prone to occur given the set of features we have used to train a machine learning model? 

To address the lower-body injuries, we applied Random Forest Machine Learning models and Neural Network models, as with these data we had a large control group of non-injured players. To address the concussive injuries, we ultimately used Principal Component Analysis (PCA) in conjunction with K-Means Clustering to determine the major groupings of the concussion injuries. Subsequently, we used a supervised Random Forest model to identify the primary features that separate the classifications. 


--- 
## Data Source and Hypothesis

The data sources are from two Kaggle Challenges: 
- [NFL 1st and Future - Analytics](https://www.kaggle.com/competitions/nfl-playing-surface-analytics/data)
- [NFL Punt Analytics Competition](https://www.kaggle.com/competitions/NFL-Punt-Analytics-Competition/data)


The first sets of data provide information on gross physiological injuries such as foot and knee injuries, whereas the second sets of data provide information regarding concussive injuries. It is likely that the conditions for each of these types of injuries are different, so this will involve a multi-step analysis to assess the parameters that have the highest impact on each type of injury and the severity of the injuries. 

We hypothesize that there is a relationship between the field conditions, player position, time during the season, duration of play during the game, location on the field, and the orientation the player is facing with respect to the direction of their movement (twist) that can predict the occurrence, type, and severity of lower body injury. 

We also hypothesize that there is a relationship between the field conditions, player position, location, time within the season or game, the orientation the player is facing with respect to the direction of their movement (twist), as well as the impact of home/away games and the point distribution at the time of injury that correlates with the incidence of traumatic brain injuries. 

We additionally anticipate that some of the features that lead to the lower-body injuries will overlap with those of the concussion injuries. 


--- 
## Database Structure and Utilization

For this project, after acquiring the data, it was stored in a PostgreSQL database. Each of the databases were organized as follows: 

#### The Injury Analytics Dataset:

The Injury dataset was pulled directly from the SQL database using SQL Alchemy to pull the data from each table for processing, with the exception of the tracking data. The size of the tracking data was prohibitively large for sqlalchemy on a local server, with over 76 million rows. To import this data in the Python files, the data table was downloaded as a csv file from the sql server into a folder labeled NFL_Turf, prior to being read into the python file. The data were connected with the following Entity Relational Diagram (ERD). 
 - INSERT INJURY ERD

#### The Concussion Dataset: 
For the Punt Analytics dataset, 4 tables were merged using PG Admin and used to create a new table called punt_analytics. This table was imported into the python files using SQL Alchemy as were done with the Injury tables. Also similar to the Injury data, the ngs table (tracking data) were too large to import using SQL Alchemy and again were downloaded locally and imported to python using pandas into a folder labeled NFL_Punt. Only the original data are represented in the ERD.     
- SQL JOIN
- INSERT Concussion ERD

#### Outputs: 
To maintain the fidelity of the original data, result tables following data processing were saved into a new database called NFL_Injuries. The data saved were the Random_Forest_Outputs, Neural_Network_Outputs, Concussion_Analysis, and clean_play_injuries. These tables were pushed to the SQL server using SQL Alchemy. 

---
## Exploratory Data Analysis and Data Cleaning
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
## Data Visualization 
Several key factors have been clearly demonstrated with visualizations produced both using Python and Tableau: 
- [NFL Injury Data](https://public.tableau.com/app/profile/aj5583/viz/NFLInjuryData_16660655174710/Story1?publish=yes)
- Visuals_2.ipynb
- Visuals_3.ipynb

--- 
## Machine Learning Design

The Machine Learning Design was broken up into two parts, as the Lower-Body Injury data and Concussion data presented different aspects that only allowed for different types of machine learning analyses. The final Model Designs were as follows: 

#### Lower-Body Injury Analysis
1. Neural Network - Deep Learning with 2 hidden layers of 256 nodes and 128 nodes

The lower-body injury analysis was a very unbalanced dataset containing a small number of injuries with a large set of plays without injuries. The data without injuries functioned as a control group used for classification in a supervised analysis. The initial model used Random Forests, as it produced a very high accuracy. However, the precision was the more important consideration with the imbalanced data, and the neural network model provided a much higher precision than did the ensemble learning.  

#### Concussion Analysis
1. PCA feature extraction
2. K-Means Clustering (Unsupervised)
3. Random Forest Feature Analysis

All instances of the concussion data were incidents with concussions, preventing us from using a supervised model. The best results were achieved with a PCA feature extraction, reducing the features to 3 dimensions, more ideal for visualization. Following the feature extraction, K-Means clustering was used to classify the data into the groups. Both a dendogram and an elbow curve were used to determine the number of cluseters to use. Because of the ambiguity incurred with the feature extraction, we used a Random Forest classifier to determine which features had the strongest association with each of the outputs.  

--- 
## Machine Learning Preliminary Findings 
### Unsupervised Learning
We initially used unsupervised learning to see what features would lead to clusters with the Injury data. K-Means Clustering was used to perform the unsupervised analysis, using a PCA feature extraction to group the features to 3, for the ability to create a 3D visualization. The initial model analyzed all of the data, including all plays without injuries and those with injuries. To determine the ideal number of k classifiers, we employed an elbow-curve analysis. There was a strong curve delineation at k=2, so this was performed and shown below. 

![Elbow_Curve1](https://user-images.githubusercontent.com/33167541/195501892-e3600a8b-01d6-42db-8be4-74be9457a3d5.png)

![2-means-all-data](https://user-images.githubusercontent.com/33167541/195502047-22a06e8f-1a21-4127-afe1-b82cc0311cbc.png)

Unfortuantely, the injuries were not successfully classified, and the differences between the groups largely had to do with the number of games played. 
The next model removed all of the non-injury data from the dataset, to try to isolate the features that had the greatest influence on these data. The main joints occurred at k=3 and k=6. The grouping with k=3 left one group with very ambiguous correlations, so the results from the k=6 analysis are reported below. 

![6-means-injury-data](https://user-images.githubusercontent.com/33167541/195502957-9b868884-267a-4d7c-804b-d6e4e8edfcf4.png)


### Supervised Learning
The following files are a composite of those in the Preliminary Models, and are themselves contained in Machine_Learning_Files:
- Preliminary_Injury_Supervised_Learning.ipynb
- Preliminary_Injury_Unsupervised_Learning.ipynb

These initially analyses did not incorporate tracking information. The goal was to determine whether the features not including the tracking data could provide a model with high enough accuracy and precision. 

Due to the nature of the Injury Dataset being extremely imbalanced, we used the Balanced Random Forest Classifier from the imbalanced learn library. In preparing the data for processing, the positions were encoded in a single column by numbers, as described above, however the plays were encoded with OneHotEncoder, giving us 3 columns for each of the plays.

The original dataset contained 260,000 rows with only 77 injuries. Because of this large difference, we tried several approaches, including Undersampling and SMOTEENN, but ultimately, we just split the data using train_test_split() from the scikit learn library both with and without stratification.

**Determine whether an injury occurred**
The original model achieved a 58% accuracy and worse precision. We further analyzed the feature importances. 

**INSERT THE BAD RANDOM FOREST MATRIX** 

The next analyses utilized a Complement Naive Bayes analysis; this type of Naive Bayes is more suitable for extremely imbalanced datasets. Similar to the Random Forest model, the results only provided a 58% accuracy. Likewise, an EasyEnsemble Boosting algorithm was tested again with similar results. From these analyses, we concluded that additional information would be necessary to further improve our models. The Random Forest and Complement Naive Bayes are shown below:

![RF_IsInjured](https://user-images.githubusercontent.com/33167541/196870316-d1da98c5-35fa-4d50-bf86-95e334c4e8a9.png)

![Naive_Bayes_Confusion](https://user-images.githubusercontent.com/33167541/195505857-6ca4b12a-c335-4664-b2e4-28637a2862ac.png)


Futher development of the dataset included the spatial parameters that should gave more predictive capability, indicating the great impact on the potential for injury. Using these data with random sampling the non-injury data were reduced to achieve a 100:1 distribution from the 3000:1 distribution we started with. Once the spatial data were added, this dataset expanded substantially, making a big impact on processing. Each of the Random Forest models was able to predict with 99% accuracy, and few to no false negatives: 

**Was there a severe injury?**
![RF_IsSevere](https://user-images.githubusercontent.com/33167541/196870375-b4c37c10-d2be-4226-a7e6-269a436f49cb.png)

**What body part was injured?** 
![RF_InjuryType](https://user-images.githubusercontent.com/33167541/196870409-dc59d14f-e26d-4d09-a7a0-b78e7f48ac81.png)

**How long was the player out?** 
![RF_InjuryDuration](https://user-images.githubusercontent.com/33167541/196870473-c93f4f22-a61b-40e5-82d9-7f2db68a9370.png)


 From the outputs of the Machine Learning models and the exploratory analysis, graphics for the dashboard will be created using a combination of python generated plots and interactive features, which will be imbedded into a webpage using JavaScript, HTML, and CSS. 

#### Random Forest Adaptation
- Injury_Supervised_Random_Forest.ipynb

**Was the player injured?**
The adaptations from the original model to the final models for the Injury Data was the addition and cleaning of the tracking data. With the addition of the tracking information, the Balanced Random Forest Classifier with 10 estimators provided a 99.96% accuracy, a much higher accuracy than was achieved with the any of the models not including the tracking data. With the addition of the tracking data, the number of rows increased to several thousand. In addition to the 99.97% accuracy, this model yielded under 5 false negatives, and 145 false positives from the dataset including 550,000 true negatives and 5500 true positives. 

In the feature analysis, we confirmed that the strongest feature in the feature analysis was the number of days played, closely followed by the temperature, and the time of the play during the game. Other stronger predictors were the player's position and the location along the length of the field. 

**Was the injury severe?**
The same process as above was followed, yielding a 99.97% accuracy and a lower, 90.35% precision. 

**What type of injury was predicted?**
The overall accuracy of this model with 4 outputs was again 98.59%, but the precision started to really drop: 
- Foot injury, 78.94% precision
- Ankle injury, 42.61% precision
- Knee injury, 27.25% precision

**What was the predicted duration of injury?**
The overall accuracy remains high at 99.77%, but the precision continues to drop: 
- Under 1 day, 60.00% precision
- Under 1 week, 35.67% precision
- Under 4 weeks, 56.12% precision
- Under 6 weeks, 63.75% precision

#### Final Random Forest Results Summarized
The Random Forest Classifiers predicting multiple outcomes were more difficult to predict the accuracy and recall specifically, and they were not possible to evaluate like this for the neural network model. These results were summarized in the following table: 
 

**INSERT RESULTS TABLE**


---
## Machine Learning - Working Models:
### Deep Learning/Neural Network Analysis
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

**INSERT RESULTS TABLE**

---
### Unsupervised Concussion Analysis
Similar to the Injury Analysis, the tables were merged including the tracking data, creating a very large dataset. In order to perform the clustering analysis, there are several ways to break the data into different clusters. The first approach was using Agglomerative Clustering, which required a size reduction to create a dendogram. The dendogram shows the highest break at two, followed by three clear clusters. 

This analysis was performed with 3 clusters prior to breaking up into two sets using train_test_split for feature classification. A Balanced Random Forest Classifier was used with 100 estimators to determine which features have the highest correlation with the different classes. In this case, the highest correlation was the Twist, the difference between the orientation of the player and the direction of movement. 

Following the Agglomerative Clustering, we used PCA data extraction to reduce the dimensions to 3 components. Testing for the ideal number of clusters for K-Means analysis, we utilized an elbow curve, where there was a very distinct bend at k=2. The K-Means clustering was performed with 2 clusters. The K-Means analysis was plotted using hvplot as shown below: 

**INSERT HV 3D PLOT**


The highest predictor was, again, the Twist, with about 98% importance with the feature analysis. 


--- 
## Project Showcase 

We will communicate findings to a webpage using Javascript, CSS and HTML. Our interactive dashboard will enable the user select injuries by parameters, such as; field type, surface type, location, and duration of play during the game. Currently, we have a frame for the webpage shown below, and the Presentation slides will be available via [Google Slides](https://docs.google.com/presentation/d/1JuRKtG8ZdwiY1gHwosXbu1rs_UrsjU8sO4iqMHOnGEc/edit?usp=sharing).


Anticipated Dashboard Features Include: 
- Machine Learning Outcomes
- Interactive Multilayer Map, allowing user to see all or select individual injury locations on the field
- Additional Visualizations to help identify high risk parameters

<div class='tableauPlaceholder' id='viz1666138420638' style='position: relative'><noscript><a href='#'><img alt='NFL Injury Data ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NF&#47;NFLInjuryData_16660655174710&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='NFLInjuryData_16660655174710&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NF&#47;NFLInjuryData_16660655174710&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                

<br><br><br>


## Website pre-view 
#### Description of the webpage
###### The flip function is added on the image of Each part for summary 
###### Each part of our project's page is added in order to describe and present the results or analysis distinct and convenient.
###### Tableau's review of story was linked to the specific webpage.



<img width="1271" alt="Screen Shot 2022-10-19 at 9 06 04 PM" src="https://user-images.githubusercontent.com/106010498/196854243-487f5eed-076e-4925-b1de-2356ec8b6c69.png">
<img width="1274" alt="Screen Shot 2022-10-19 at 9 06 18 PM" src="https://user-images.githubusercontent.com/106010498/196854251-3f3c573b-4854-48c7-acb9-2d86422de40c.png">
<img width="1256" alt="Screen Shot 2022-10-19 at 9 22 01 PM" src="https://user-images.githubusercontent.com/106010498/196855898-0732c4d4-690a-413d-8734-38ce6316b406.png">


#### Interactive element
###### embedcodeing was founded from the web version tableau and added it to the webpage for linked the result from tableau to our webpage
<img width="951" alt="Screen Shot 2022-10-19 at 9 39 28 PM" src="https://user-images.githubusercontent.com/106010498/196858364-64e12e38-aeaf-49fa-8405-0356280c930d.png">
<img width="1265" alt="Screen Shot 2022-10-19 at 9 39 37 PM" src="https://user-images.githubusercontent.com/106010498/196858373-dbfd6b41-0445-4ba3-ae1d-76351741dfab.png">




#### what need to keep doing 
    1.connect database, machine learning and presentation on the specific webpage. 
    2.add commit for each part.
