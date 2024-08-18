from textblob import TextBlob

# Example text

# Create a TextBlob object
def sentiment_analyzer(text):
    blob = TextBlob(text)

    # Perform sentiment analysis
    sentiment = blob.sentiment

    # Output the result
    # print(f"{sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
    return sentiment.polarity, sentiment.subjectivity
'''from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Example text
text = "RIP to your friend. Stay strong we can see the pain in your eyes."


# Perform sentiment analysis
sentiment = sia.polarity_scores(text)

# Output the result
print(sentiment)
'''