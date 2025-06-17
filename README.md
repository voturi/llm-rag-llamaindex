# llm-rag-llamaindex

Build an LLM-powered Chatbot with RAG using LlamaIndex
This chat assistant utilizes Retrieval Augmented Generation (RAG) to answer questions based on a Wikipedia page of your choice. RAG has proven to be an effective method for reducing hallucinations and providing large language models (LLMs) with up-to-date knowledge without the need for retraining. The end-to-end workflow of the chat assistant can be seen below:

![image](https://github.com/user-attachments/assets/9734c8bf-f72c-4cf8-b003-1f8573dc962c)



We will employ the ReAct (Reasoning and Act) prompting framework. This framework assists the agent in reasoning about tool usage, observing the outcomes of the tool usage, and then responding appropriately to answer the question, as shown below:

![image](https://github.com/user-attachments/assets/42d19649-954a-4e41-a0ec-6ce4a120deaf)

We will use Python modules in this project to build your chat assistant. Therefore, some template .py files are provided in the Visual Studio Code, available on the right side of the workspace:

utils.py: This file will be used to read the OpenAI API key, allowing you to use the ChatGPT API from OpenAI.

index_wikipages.py: This file will be used to load Wikipedia pages of your choice into memory and index them, allowing your agent to search through them.

chat_agent.py: This file contains a script that creates a ReAct (Reason and Act) agent with a chat UI. The ReAct agent uses LLMs from OpenAI to answer complex questions about a topic of your choice by searching the relevant Wikipedia page.
