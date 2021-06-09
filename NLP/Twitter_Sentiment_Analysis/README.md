# Twitter-Sentiment-Analysis
An end to end project implementing Twitter Sentiment Analysis to identify if a tweet is Racist/Sexist.

Application Link: https://twitter-sentiment-bysaurav.herokuapp.com/

The Data Practice problem Data for Twitter Sentiment analysis pulled from analyticsvidhya.com
https://datahack.analyticsvidhya.com/contest/practice-problem-twitter-sentiment-analysis/

The project uses Natural Language Processing(NLP) along with Logistic Regression to classify the sentiments

The basic process followed are:

    -Text analytics using NLTK library

    -Data(Tweet) Cleaning by removing usernames, punctuation, stopwords, lemmatization

    -Vectorization to convert text data into vectors

    -Data Balancing is done by oversampling to increase the negative samples to match the positive samples ultimately resulting to give a better F1-Score

    -Proper steps to prevent Data Leakage by doing train test split before doing oversampling using SMOTE

    -Logistic Regression is chosen over Naive Bayes as the results from the former were better 

    -Model is evaluated using Precision, Recall and F1-Score.
  
  
The final model is deployed on Heroku Platform on the link provided above.
