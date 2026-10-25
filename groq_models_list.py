""" List out the Groq models"""

import os
from dotenv import load_dotenv
from groq import Groq        #pip3 install groq

load_dotenv()  # reads .env into os.environ

client = Groq(api_key=os.environ['GROQ_API_KEY'])

for m in client.models.list().data:
    print(m.id)

"""
Chat/text LLMs (the ones for LangChain work)
- openai/gpt-oss-120b: the largest and strongest on your list. Use it for reasoning, complex tasks, and as a judge model in evaluations.
- openai/gpt-oss-20b: smaller and faster, with good quality. A good default for development and quick iteration.
- qwen/qwen3.8-27b: a mid-size general model. It's worth comparing against the gpt-oss models.
- allam-2-7b: an Arabic-focused model. It's less useful unless you need Arabic.

Safety/guardrail models (classifiers, not chatbots)
- openai/gpt-oss-safeguard-20b: checks content against a policy you write.
- meta-llama/llama-prompt-guard-2-22m and -86m: detect prompt injection and jailbreak attempts.

These are useful for LLM safety and evaluation, which fits your QA-to-NLP direction. You wouldn't use them for normal chat.

Speech models (audio, not text)
- whisper-large-v3 and whisper-large-v3-turbo: speech-to-text. The turbo version is faster.


"""