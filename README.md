# 🧠 Context-Aware AI Agent

This project demonstrates a simple yet powerful **context-aware AI agent** built using the Agentic AI framework.

The core idea is to enable an agent that can understand and use **structured context data** (in this case, user information like name, age, and UID) to provide accurate, relevant responses — instead of guessing or hallucinating.

## 💡 Why Context?

Most language models generate responses based only on the input prompt. But when we need them to work with **specific structured data**, we need to pass context.

This project uses:
- A `User_Info` context object to hold data
- A `fetch_user_data` tool function to access it
- An agent with clear instructions to **use the tool only when needed**, based on the user’s query
- Gemini 2.0 Flash as the LLM backend

## 🧠 How It Works

When the user asks something like:

> "What is the user's age and name?"

The agent:
- Recognizes the request
- Uses the registered tool `fetch_user_data`
- Fetches data from the context
- Responds with:  
  `User Name: Taha, Age: 24, UID: 335839`

This design ensures:
✅ Accuracy  
✅ Contextual awareness  
✅ Separation of logic, tools, and instructions

---

Built for learning and experimenting with **Agentic AI**, context management, and tool-based LLM orchestration.

