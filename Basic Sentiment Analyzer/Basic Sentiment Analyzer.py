# Define sentiment lexicon
positive_words = {"happy", "love", "good", "excellent", "great", "fantastic", "amazing", "joyful"}
negative_words = {"bad", "sad", "terrible", "awful", "worst", "horrible", "hate", "angry"}

def sentiment_analysis(text):
    words = text.lower().split()  # Convert to lowercase and split into words
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)

    # Determine sentiment
    if pos_count > neg_count:
        return "Positive Sentiment 😊"
    elif neg_count > pos_count:
        return "Negative Sentiment ☹️"
    else:
        return "Neutral Sentiment 😐"

# Example Usage
text1 = "I love this fantastic product, it makes me so happy!"
text2 = "This is the worst experience, I hate it!"
text3 = "It was an okay day, nothing special."

print(sentiment_analysis(text1))  # Output: Positive Sentiment 😊
print(sentiment_analysis(text2))  # Output: Negative Sentiment ☹️
print(sentiment_analysis(text3))  # Output: Neutral Sentiment 😐
