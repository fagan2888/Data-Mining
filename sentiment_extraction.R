#! /usr/bin/Rscript
require(syuzhet)

today_news <- read.csv("C:/Users/seeme/Desktop/Data Mining Project/DJ and Daily News Predictions/Today_News.csv") # CHANGE PATH TO DATA FILE

#Sentiments words table:
records <- as.character(today_news$News)
sentiment <- get_nrc_sentiment(records)

sent <- cbind(today_news$Date, sentiment)
colnames(sent)<-c("Date","Anger", "Anticipation", "Disgust", "Fear", "Joy", "Sadness", "Surprise", "Trust", "Negative", "Positive")
sentiment_data <- as.data.frame(colSums(sent[,-1]))
sentiment_df <- do.call(rbind, sentiment_data)
colnames(sentiment_df)<-c("Anger", "Anticipation", "Disgust", "Fear", "Joy", "Sadness", "Surprise", "Trust", "Negative", "Positive")
write.csv(sentiment_df, file = "new_sentiment_data.csv")
file.remove("C:/Users/seeme/Desktop/Data Mining Project/DJ and Daily News Predictions/Today_News.csv")
