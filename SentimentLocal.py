from textblob import TextBlob

file=input('Please enter the file name : ')

with open(file,'r') as f:
    text=f.read()

textblob=TextBlob(text)
sentiment=textblob.sentiment.polarity

print(sentiment)