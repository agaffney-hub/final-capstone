# NFL Injury Analysis

---
## Topic and Reason

In recent years, more concern has grown over sustained injuries that impact the athletes lives long after their athletic career ends. The NFL is looking to identify what changes should be made to minimize the risk of player injury, while not completely altering America's favorite pastime. There are several types of injuries that are incurred - there are gross physiological injuries such as knee, foot, and ankle injuries, and there are also more subtle injuries such as concussions, which can have a much longer-lasting impact on the players, occasionally leading to personality changes and unfortanately, even suicide. It's clear that changes need to be made to address these concerns, but the conflicting view is that the NFL is a multi-billion dollar industry, generating a revenue of over 17 billion dollars in 2021 alone. While changes need to be made, they only impact a fraction of the players. In order to minimize the risk of all players, it's important for the NFL to maintain most of the features of the game if they can modify only certain aspects in order to better ensure the medical safety of their players.

The purpose of this analysis is to identify the aspects of the game that best predict the occurrence of injury, whether it is a short-term injury, long-term injury, or a traumatic brain injury. Unsupervised analysis is initially used to identify clusters in the data, and which predictors may have a greater influence on the injuries. Following this, supervised analysis is used to predict the conditions that can lead to such short-term, long-term, and traumatic brain injuries using the data provided by the NFL via 2 Kaggle Competitions. 

--- 
## Data Source and Hypothesis

The data sources are from two Kaggle Challenges: 
- NFL 1st and Future - Analytics
    - https://www.kaggle.com/competitions/nfl-playing-surface-analytics/data
- NFL Punt Analytics Competition
    - https://www.kaggle.com/competitions/NFL-Punt-Analytics-Competition/data

The first sets of data provide information on gross physiological injuries such as foot and knee injuries, whereas the second sets of data provide information regarding concussive injuries. It is likely that the conditions for each of these types of injuries are different, so this will involve a multi-step analysis to assess the parameters that have the highest impact on each type of injury and the severity of the injuries. 

We hypothesize that there is a relationship between the field type, surface type, location, and duration of play during the game that impacts the type and and severity of the gross physiological injury. We also hypothesize that there is a relationship between the field type, surface, location, and duration of play during the game that influences the likeliness of occurrence of traumatic brain injuries on the field.  


--- 
## Communication Protocols

We are using Trello to track our weekly deliverables on a Kanban board, with tasks assigned by Role as well as by person, so each individual knows their responsibilities per shared task. We are using a group chat feature on Slack to provide updates on anything that others may need to use in their own weekly roles. We have also agreed upon meeting on _______ on video, to discuss what we have done, what we have found, what needs to be done, and any challenges encountered. At the beginning of each meeting, we will each get 3-5 minutes to do this prior to having a group discussion, to make sure that everyone has had an opportunity to speak and ask questions. At the end of each meeting, we will decide on each person's deliverables, which will then be added to the Trello Board. We have also agreed on providing updates on Slack every other day, just to confirm that group members are keeping up with their responsibilities or transferring them to someone else if necessary.  



--- 
## Machine Learning Design

We will be using both unsupervised learning with PCA analysis to identify predictors of the injuries to prioritize the factors that do influence the groupings of injuries and removing those that do not have an impact. The Unsupervised analysis will utilize K-Means clustering and PCA. We will subsequently use supervised machine learning to create a predictive model that can predict which game parameters are likely to predict a specific type of injury and, if applicable, the severity of the injury. The Machine Learning models that will be used will be Random Forests and Neural Networks. For the sampling, because there is a very unbalanced dataset regarding positions on the field, we will have to stratify the samples containing both information regarding the injury and non-injury plays. 

To perform the data cleaning, we will be using the following libraries:
```
pandas
numpy
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

The general process flow for the machine learning models is to clean the data from individual datasets. Merge the data to gather the appropriate parameters for analysis. Assess whether binning or encoding is necessary, then process accordingly for the analysis. Split the data into testing and training sets for supervised learning. Apply to the ML model. Evaluate results both analytically and graphically. 