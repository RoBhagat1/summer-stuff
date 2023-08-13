import nltk
from textblob import TextBlob

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    print(sentiment_score)
    if sentiment_score >= 0.5:
        return "Very Positive"
    elif sentiment_score <=0.2 and sentiment_score>=-0.2:
        return "Neutral"
    elif sentiment_score > 0:
        return "Positive"
    elif sentiment_score > -0.5:
        return "Negative"
    else:
        return "Very Negative"
    

if __name__ == "__main__":
    while True:
        user_text = input("Enter a sentence to analyze sentiment: ")
        if(user_text == "break"):
            break
        sentiment = analyze_sentiment(user_text)
        print(f"Sentiment: {sentiment}")