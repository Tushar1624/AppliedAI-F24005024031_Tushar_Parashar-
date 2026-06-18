from transformers import pipeline
classifier=pipeline("sentiment-analysis")
result=classifier("I hate Machine Learning")
print(result)