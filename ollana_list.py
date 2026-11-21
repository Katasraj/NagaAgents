import ollama

models = ollama.list()["models"]
print("Models found:", len(models))

for m in models:
    print(m["model"], "---", m["size"])

