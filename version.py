from transformers.pipelines import SUPPORTED_TASKS

print("question-answering" in SUPPORTED_TASKS)
print(SUPPORTED_TASKS.keys())