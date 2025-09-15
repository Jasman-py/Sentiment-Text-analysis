from textblob import TextBlob
from newspaper import Article

try:
    selection = int(input("Please select a source:\n1. URL\n2. File Path\nEnter your choice: "))

    if selection == 1:
        url = input("Enter the URL of the article: ").strip()
        article = Article(url)
        article.download()
        article.parse()
        text = article.text

    elif selection == 2:
        file = input("Enter the file path: ").strip()
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        print("Invalid selection! Please choose 1 or 2.")
        exit()

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Display a more human-friendly sentiment result
    if sentiment > 0:
        print(f"Sentiment Score: {sentiment:.2f} → Positive 😊")
    elif sentiment < 0:
        print(f"Sentiment Score: {sentiment:.2f} → Negative 😠")
    else:
        print(f"Sentiment Score: {sentiment:.2f} → Neutral 😐")

except Exception as e:
    print(f"⚠️ An error occurred : {e}")
