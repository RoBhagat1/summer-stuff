import nltk
from textblob import TextBlob

"""Code from ChatGPT for me to explore sentiment analysis"""
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"
    

if __name__ == "__main__":
    while True:
        user_text = input("Enter a sentence to analyze sentiment: ")
        if(user_text == "break"):
            break
        sentiment = analyze_sentiment(user_text)
        print(f"Sentiment: {sentiment}")