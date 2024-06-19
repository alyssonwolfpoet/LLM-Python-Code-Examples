from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze the sentiment of a few sentences
sentences = [
    "This movie is absolutely fantastic! I loved it.",
    "The food was disappointing. It was bland and overpriced.",
    "This book is a must-read for anyone interested in history.",
    "The service at this hotel was terrible. I wouldn't stay here again.",
]

# Analyze the sentiment of each sentence
for sentence in sentences:
    sentiment = sentiment_analyzer(sentence)[0]
    print(f"Sentence: {sentence}")
    print(f"Sentiment: {sentiment['label']} ({sentiment['score']:.2f})")