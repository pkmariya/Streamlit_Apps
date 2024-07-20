
# Ref: https://www.natasshaselvaraj.com/twitter-sentiment-analysis-with-python/

import pandas as pd
import twint
import nest_asyncio

nest_asyncio.apply()

c = twint.Config()

c.Search = ['#viratkohli']
c.Limit = 1000
c.Store_csv = True
c.Since = '2020-01-01'
c.Output = "virattweets.csv"

twint.run.Search(c)

print("file downloaded successfully")

tweet_data_df = pd.read_csv('virattweets.csv')

# Shape of the data
print("This dataset contains, {0} Rows and {1} Columns.".format(tweet_data_df.shape[0], tweet_data_df.shape[1]))

# Top 5 rows of the dataset
print(tweet_data_df.head())

# Information about the dataset columns
print(tweet_data_df.info())


# Sentiment Analysis; to do this import NLTK library

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

import re
nltk.download('words')
words = set(nltk.corpus.words.words())

sentence = tweet_data_df['tweet'][0]
sid.polarity_scores(sentence)['compund']




