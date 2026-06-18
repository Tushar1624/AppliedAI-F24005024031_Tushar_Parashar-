from transformers import pipeline
generator=pipeline("text-generation",model="distilgpt2")
result=generator("Capital of India is",max_length=30)
print(result)