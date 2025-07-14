# AI Agent Grind 🚀

A learning sandbox for building and experimenting with AI agents. This repository contains various agent implementations, from simple examples to complex multi-tool systems.

## 📁 Projects

### [first_ReAct](./first_ReAct/)
A minimal ReAct (Reasoning + Acting) agent using LangChain and Google Gemini. Demonstrates:
- Custom tool creation with `@tool` decorator
- Web search integration (DuckDuckGo)
- Mathematical calculations with Python math library
- Multi-step reasoning and tool selection

## 🛠️ Tech Stack

- **LangChain** - Agent framework and tool integration
- **Google Gemini** - Language model (Gemini 2.0 Flash)
- **Python** - Core programming language
- **Jupyter Notebooks** - Interactive development and testing

## 🚀 Quick Start

1. **Clone and setup**:
   ```bash
   git clone <repo-url>
   cd AI-agent-grind
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

2. **Set environment variables**:
   ```bash
   # Create .env file
   GEMINI_API_KEY=your_api_key_here
   ```

3. **Explore projects**:
   - Start with `first_ReAct/math_agent.ipynb` for a complete ReAct agent example

## 🎯 Learning Goals

- Understand agent architectures and patterns
- Master tool integration and chaining
- Learn prompt engineering for agents
- Build practical AI applications

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

---

**More agent projects/learning coming soon! 🤖**