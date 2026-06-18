from transformers import pipeline
ner=pipeline("ner",model="dslim/bert-base-NER")
text="Elon Musk Founded SpaceX in the United States"
result=ner(text)
print(result)