from transformers import pipeline
qa=pipeline("question-answering",model="deepset/roberta-base-squad2")
result= qa(
    question="What is AI",
    context="Artificial Intelligence is the simpulation of human intelligence")
print(result)