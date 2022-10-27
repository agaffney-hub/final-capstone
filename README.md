# NFL Injury Analysis
***Using Machine Learning and Data Analysis to Visualize and Identify Conditions Leading to Injuries in Football***
#### *by* Amy Gaffney, Izzy Irazoque, Kevin Ytturalde, Vincent Fan, and Justin Papreck

---
## Update for 10/19/22
- Presentation: Information added to Google Slides with images for the Dashboard
- Presentation: Visuals produced in both Python and Tableau from exploratory analysis and ML
- Database: Integrated with the ML models using SQLAlchemy both for retrieval and storage of cleaned datasets for Tableau
- Database: Joined 4 tables on SQL to be exported and used in the Punt Analytics analysis
- GitHub: Was updated before all of the changes were lost. Will redo next week. 
- Dashboard: Blueprint created - multiple page design, one for index, then Interactive Maps, Exploratory Graphs, Injury Stats, and ML
- Dashboard: JS/html created, working rough draft 
- Machine Learning: Supervised model for Injury Data using Random Forests, predictive models reaching 99% with only False positives, which is ideal for this analysis

-- 
## Update for 10/26/22
- Presentation
- Database
- GitHub
- Dashboard
- Machine Learning


---
## Topic and Reason

In recent years, more concern has grown over sustained injuries that impact the athletes lives long after their athletic career ends. The NFL is looking to identify what changes should be made to minimize the risk of player injury, while not completely altering America's favorite pastime. There are several types of injuries that are incurred - there are gross physiological injuries such as knee, foot, and ankle injuries, and there are also more subtle injuries such as concussions, which can have a much longer-lasting impact on the players, occasionally leading to personality changes and unfortanately, even suicide. It's clear that changes need to be made to address these concerns, but the conflicting view is that the NFL is a multi-billion dollar industry, generating a revenue of over 17 billion dollars in 2021 alone. While changes need to be made, they only impact a fraction of the players. In order to minimize the risk of all players, it's important for the NFL to maintain most of the features of the game if they can modify only certain aspects in order to better ensure the medical safety of their players.

The purpose of this analysis is to identify the aspects of the game that best predict the occurrence of injury, whether it is a short-term injury, long-term injury, or a traumatic brain injury. Unsupervised analysis is initially used to identify clusters in the data, and which predictors may have a greater influence on the injuries. Following this, supervised analysis is used to predict the conditions that can lead to such short-term, long-term, and traumatic brain injuries using the data provided by the NFL via 2 Kaggle Competitions. 


--- 
## Data Source and Hypothesis

The data sources are from two Kaggle Challenges: 
- [NFL 1st and Future - Analytics](https://www.kaggle.com/competitions/nfl-playing-surface-analytics/data)
- [NFL Punt Analytics Competition](https://www.kaggle.com/competitions/NFL-Punt-Analytics-Competition/data)

The first sets of data provide information on gross physiological injuries such as foot and knee injuries, whereas the second sets of data provide information regarding concussive injuries. It is likely that the conditions for each of these types of injuries are different, so this will involve a multi-step analysis to assess the parameters that have the highest impact on each type of injury and the severity of the injuries. 

We hypothesize that there is a relationship between the field conditions, player position, time during the season, duration of play during the game, and location on the field that can predict the occurrence, type, and severity of lower body injury. We plan to show this with a predictive supervised machine learning model.

We also hypothesize that there is a relationship between the field conditions, player position, location, time within the season or game, as well as the impact of home/away games and the point distribution at the time of injury that correlates with the incidence of traumatic brain injuries. We will be using PCA and unsupervised machine learning with k-means and agglomerative clustering to analyze these relationships.  


--- 
## Database Sample Data

The database selected for use with the organized data is PostgreSQL, which will interface with python via SQLAlchemy. Our data comes from 2 Kaggle sources:

- 1st and Future - Analytics: 

![Injury_DB](https://user-images.githubusercontent.com/33167541/195506808-d0ace675-ed27-4e9f-b83f-ac66cc95f80f.png)


- NFL Punt Analytics Competition

![PuntAnalytics_DB](https://user-images.githubusercontent.com/33167541/195506911-01ae9c29-2574-40ec-a4f2-d26dd83e8eb5.png)

For the Punt Analytics dataset, due to the number of different files that need to be connected and merged, using SQL to do this is much more efficient than doing so in python, particulary for exporting to Tableau. We were able to quickly join the 4 tables for export and cleaning. 

![SQL_Punt_Join](https://user-images.githubusercontent.com/33167541/196871369-72a6b6c8-5946-4f94-85c7-b05084129882.png)


--- 
## Machine Learning Design

We will be using both unsupervised learning with PCA analysis to identify predictors of the injuries to prioritize the factors that do influence the groupings of injuries and removing those that do not have an impact. The Unsupervised analysis will utilize K-Means clustering and PCA. We will subsequently use supervised machine learning to create a predictive model that can predict which game parameters are likely to predict a specific type of injury and, if applicable, the severity of the injury. 

The Machine Learning models that will be used will be Random Forests and Neural Networks. Random Forests is an acceptable model for both binary and numerical classification. We were able to use Random Forests to make predictive models to predict whether an injury occurred, if it was severe, what body part was injured, and the duration of injury.  

  Finally, Deep Learning with Neural Networks is an excellent choice for analysis in this situation, as it can also be used for both binary classification as well as sorting into *n* possible outcomes. 

For the sampling, because there is a very unbalanced dataset regarding positions on the field, we will most likely have use random sampling to perform an undersampled datafram, and then stratify the samples containing both information regarding the injury and non-injury plays. We will be using scikit-learn's test_train_split to stratify and split the data into training sets. The models will be trained, fit, and validated using the appropriate methods per machine learning model. 

To perform the data cleaning, we will be using the following libraries:
```
pandas
numpy
SQLAlchemy
```

To perform the unsupervised learning analysis, we will be using the following libraries:
```
pandas
numpy
sklearn
hvplot
plotly.express
```

To perform the supervised learning analyses, we will be using the following librarries: 
```
pandas
numpy
sklearn
collections
imblearn
tensorflow
```

To provide the visualizations and analysis:
```
matplotlib
hvplot
plotly
Tableau
```

The general process flow for the machine learning models is:
- Clean the data from individual datasets
- Merge the data to gather the appropriate parameters for analysis
- Assess where binning and encoding is neccessary
- Process accordingly for the analysis
- Split the data into testing and training sets for supervised learning
- Apply to the ML model
- Evaluate results both analytically and graphically

From the outputs of the Machine Learning models and the exploratory analysis, graphics for the dashboard will be created using a combination of python generated plots and interactive features, which will be imbedded into a webpage using JavaScript, HTML, and CSS. 


---
## Machine Learning Models

### Unsupervised Learning

K-Means Clustering was used to perform the unsupervised analysis, using a PCA feature extraction to group the features to 3, for the ability to create a 3D visualization. The initial model analyzed all of the data, including all plays without injuries and those with injuries. To determine the ideal number of k classifiers, we employed an elbow-curve analysis. There was a strong curve delineation at k=2, so this was performed and shown below. 

![Elbow_Curve1](https://user-images.githubusercontent.com/33167541/195501892-e3600a8b-01d6-42db-8be4-74be9457a3d5.png)

![2-means-all-data](https://user-images.githubusercontent.com/33167541/195502047-22a06e8f-1a21-4127-afe1-b82cc0311cbc.png)


Unfortuantely, the injuries were not successfully classified, and the differences between the groups largely had to do with the number of games played. 
The next model removed all of the non-injury data from the dataset, to try to isolate the features that had the greatest influence on these data. The main joints occurred at k=3 and k=6. The grouping with k=3 left one group with very ambiguous correlations, so the results from the k=6 analysis are reported below. 

![6-means-injury-data](https://user-images.githubusercontent.com/33167541/195502957-9b868884-267a-4d7c-804b-d6e4e8edfcf4.png)


Group 1: 
- All injuries were relatively minor, less than 28 days
- The specific game play was in the first half of the game
- There were no foot injuries
- All temperatures were under 60 degrees

Group 2: 
- All injuries were severe, longer than 42 days
- A much higher proportion of these injuries occurred on Synthetic Turf (2:1)
- Plays were all in the first half of the game
- Temperatures were mostly between 30 and 49 degrees

Group 3: 
- All injuries were relatively minor, less than 28 days
- Most injuries occurred on Natural Turf (7:3)
- All game plays were in the second half of the game
- There were no foot injuries
- Almost all plays were Passing

Group 4:
- All injuries were relatively minor, less than 28 days
- More of the injuries occurred on Natural Turf
- All plays were in the first half of the game
- All temperatures were over 60 degrees, with 5 over 78 degrees

Group 5: 
- All injuries were severe, all over 28 days
- All plays were in the second half of the game
- Almost all of the injuries were sustained on Synthetic Turf

Group 6:
- All injuries were severe, most over 42 days
- All plays in the first half of the game
- All temperatures were at least 70 degrees

---
### Supervised Machine Learning

Supervised Learning Models were performed using Random Forests, Complement Naive Bayes, and EasyEnsemble Boosting to predict the binary outcome of whether the model could predict that an injury did or did not occur. With the very imbalanced dataset, the accuracy acheieved in this preliminary model only reached 54% using both the Random Forest and Naive Bayes models. 

The output parameter for the predictive test was the "IsInjured" column, where 0 denoted the player was not injured, and 1 denoted an injury. In future analyses, we would like to predict what type of injury or whether the injury was a severe injury based on the input data. 

![Naive_Bayes_Confusion](https://user-images.githubusercontent.com/33167541/195505857-6ca4b12a-c335-4664-b2e4-28637a2862ac.png)


Futher development of the dataset included the spatial parameters that should gave more predictive capabilityindicating the great impact on the potential for injury. Using these data with random sampling the non-injury data were reduced to achieve a 100:1 distribution from the 3000:1 distribution we started with. Once the spatial data were added, this dataset expanded substantially, making a big impact on processing. Each of the Random Forest models was able to predict with 99% accuracy, and few to no false negatives: 

- Was there an injury?

![RF_IsInjured](https://user-images.githubusercontent.com/33167541/196870316-d1da98c5-35fa-4d50-bf86-95e334c4e8a9.png)

- Was there a severe injury?
![RF_IsSevere](https://user-images.githubusercontent.com/33167541/196870375-b4c37c10-d2be-4226-a7e6-269a436f49cb.png)

- What body part was injured? 
![RF_InjuryType](https://user-images.githubusercontent.com/33167541/196870409-dc59d14f-e26d-4d09-a7a0-b78e7f48ac81.png)

- How long was the player out? 
![RF_InjuryDuration](https://user-images.githubusercontent.com/33167541/196870473-c93f4f22-a61b-40e5-82d9-7f2db68a9370.png)


Because the initial analysis planned for a Deep Learning Model, which would accommodate more complex parameters, we fitted the data for a Neural Network analysis, taking in 16 inputs, passing through 2 hidden layers with 16, and then 8 nodes, predicting the four outcomes for injury types. This model achieved a 99.95% accuracy with only 2 epochs. 

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
