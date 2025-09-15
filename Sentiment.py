from textblob import TextBlob
from newspaper import Article

selection=int(input("Please Select from the source following \n URL(Enter 1) \n File path(Enter 2) \n "))

if selection==1:
    url=input("Enter the URL of the article: ")
    article = Article(url)
    article.download()
    article.parse()
    text=article.text
else:
    file = input('Please enter the file name : ')

    with open(file, 'r') as f:
        text = f.read()

blob = TextBlob(text)
sentiment=blob.sentiment.polarity
print(sentiment)