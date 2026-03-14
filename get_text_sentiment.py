from transformers import pipeline
def top_text_sentiment(textString:str) -> str:
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
    output = classifier(textString)

    return output[0][0]['label']