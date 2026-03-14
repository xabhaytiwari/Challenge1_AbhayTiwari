from transformers import pipeline
def top_text_sentiment(textString:str):
    instructions = []
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
    output = classifier(textString)
    instructions.append(output[0][0]['label'])
    return instructions