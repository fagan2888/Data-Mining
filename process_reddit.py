"""
This script will process reddit news data downloaded from the Reddit Data Extractor into a csv file.
Perform Sentiment Analysis on it using a separate R script
Collect Stock data from yahoo finance
Join the sentiment analysis and yahoo finance data together
"""
import os
import subprocess
from datetime import datetime
import time
import shutil

########################################################################################################################
# execute yahoo-finance to get the DJIA data first
# Parameters that can be changed: Stock Ticker and Data Timeframe for Extraction
# Currently set to DJIA and Data for Today
def get_yahoo_data():
    from pandas_datareader import data as pdr
    from datetime import datetime, timedelta
    import fix_yahoo_finance as yf
    yf.pdr_override()

    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    end_day = now - timedelta(days=1)

    # download dataframe from yahoo
    data = pdr.get_data_yahoo("^DJI", start=end_day.strftime("%Y-%m-%d"), end=now.strftime("%Y-%m-%d"))
    data['change'] = ((int(data['Close'].values) - int(data['Open'].values)) / int(data['Open'].values)) * 100
    return data
new_djia_data = get_yahoo_data()
########################################################################################################################
# re-import pandas to reset the override that is needed for yahoo-finance
# set the path to where the reddit news data is
# set the paths to Rscript.exe from your R build and path to the sentiment_extraction.r file
import pandas as pd
dir_name = r'C:\Users\seeme\Desktop\Data Mining Project\Datasets\worldnews'  # change to where the reddit files are
data_path = os.listdir(dir_name)
date = time.strftime("%Y-%m-%d")
df_cols = ['Date', 'News']
master_df = pd.DataFrame(columns=df_cols)

# This chunk process the reddit news data into one master csv file for sentiment analysis ##############################
for item in data_path:
    string = str(item)
    if string[-4:] == ".txt" and len(string) > 10:
        news = string.replace('.txt', '')
        temp_data = {'Date': date,
                     'News': news}
        temp_df = pd.DataFrame(temp_data, columns=df_cols, index=[0])
        master_df = master_df.append(temp_data, ignore_index=True)

master_df.to_csv('Today_News.csv', encoding='utf-8', index=False, sep=',')
# The above file will be made where this python script is
# The absolute path to this file must be used in the sentiment_extraction.R file (please revise the R file)

# shutil.rmtree(dir_name)  # removes all the files collected from the reddit web scraper
########################################################################################################################
# run R script and return new_sentiment_data.csv
# NOTE: param1 = path to Rscript.exe from the R build, param2 is the path to the R file to execute
subprocess.call(["C:/Users/seeme/Documents/R/R-3.4.0/bin/Rscript",
                 "C:/Users/seeme/Desktop/Data Mining Project/DJ and Daily News Predictions/sentiment_extraction.r"])

sentiment = pd.read_csv("new_sentiment_data.csv")
sentiment.drop('Unnamed: 0', axis=1, inplace=True)
########################################################################################################################
# Format DJIA dataframe to original dataset format
new_djia_data = new_djia_data.reset_index(drop=True)
now = datetime.now()
new_djia_data['Date'] = now.strftime("%Y-%m-%d")
cols = new_djia_data.columns.tolist()
cols = cols[-1:] + cols[:-1]
new_djia_data = new_djia_data[cols]

# Append Sentiment Dataframe columns to DJIA Dataframe columns
new_djia_data['Anger'] = sentiment['Anger']
new_djia_data['Anticipation'] = sentiment['Anticipation']
new_djia_data['Disgust'] = sentiment['Disgust']
new_djia_data['Fear'] = sentiment['Fear']
new_djia_data['Joy'] = sentiment['Joy']
new_djia_data['Sadness'] = sentiment['Sadness']
new_djia_data['Surprise'] = sentiment['Surprise']
new_djia_data['Trust'] = sentiment['Trust']
new_djia_data['Negative'] = sentiment['Negative']
new_djia_data['Positive'] = sentiment['Positive']

# os.remove('new_sentiment_data.csv')  # removes the combined DJIA and sentiment data file
# Complete
print(new_djia_data)

__author__ = 'Matt Wilchek'