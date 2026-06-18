from transformers import pipelinename
summarizer = pipeline("summarization", model="t5-small")
text = "summarize: Artificial Intelligence is transforming industries across healthcare, finance, and manufacturing."
result = summarizer(text)
print(result)