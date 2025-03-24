# Define sentiment lexicon
POSITIVE_WORDS = {"happy", "love", "good", "excellent", "great", "fantastic", "amazing", "joyful", "awesome"}
NEGATIVE_WORDS = {"bad", "sad", "terrible", "awful", "worst", "horrible", "hate", "angry", "disappointing"}

import re
def preprocess_sentence(sentence):
    words = re.split(r"[ , . ! ]", sentence.lower())
    #words2 = re.split(r"\W", sentence)
    return list(filter(None, words))

def sent_anlayze(sentence):
    words = preprocess_sentence(sentence)
    pos_words = sum(1 for word in words if word in POSITIVE_WORDS)
    neg_words = sum(1 for word in words if word in NEGATIVE_WORDS )
    if neg_words > pos_words :
        print(f"we have {pos_words} Positive words and we have {neg_words} negative words")
        return "The sentence is Negative!"
    elif pos_words > neg_words :
        print(f"we have {pos_words} Positive words and we have {neg_words} negative words")
        return "The sentence is Positive!"
    else:
        print(f"we have {pos_words} Positive words and we have {neg_words} negative words")
        return "Natural Sentence!"