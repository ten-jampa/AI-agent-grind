# First ReAct AI Agent

A minimal implementation of a ReAct (Reasoning + Acting) AI agent using LangChain and Google's Gemini model. This project demonstrates how to build an intelligent agent that can reason about user queries and use appropriate tools to find answers.

## 🎯 Project Overview

This agent can:
- **Perform mathematical calculations** using a custom calculator tool with Python's math library
- **Search the web** for factual information using DuckDuckGo
- **Combine multiple tools** to solve complex, multi-step problems
- **Reason step-by-step** about which tool to use for each query

## 📁 Project Structure

```
first_ReAct/
├── math_agent.ipynb          # Main ReAct agent implementation
├── google_genai_demo.ipynb   # Basic LangChain + Gemini examples
├── load_env.py              # Environment variable loader
└── README.md                # This file
```

## 🚀 Quick Start

### Prerequisites

1. **Python Environment**: Ensure you have Python 3.8+ installed
2. **API Key**: Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Virtual Environment**: (Recommended) Create and activate a virtual environment

### Installation

1. **Install Dependencies**:
   ```bash
   pip install langchain langchain-google-genai langchain-community duckduckgo-search python-dotenv
   ```

2. **Set Up Environment Variables**:
   Create a `.env` file in the project root:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Run the Agent**:
   Open `math_agent.ipynb` in Jupyter and run the cells sequentially.

## 🛠️ Components

### 1. Calculator Tool (`@tool`)
- **Purpose**: Evaluates mathematical expressions using Python's math library
- **Capabilities**: Basic arithmetic, trigonometric functions, logarithms, constants (π, e)
- **Usage**: `calculate.invoke("sin(30 * pi / 180)")`

### 2. Web Search Tool
- **Purpose**: Searches the web for factual information
- **Provider**: DuckDuckGo (no API key required)
- **Usage**: `search.invoke("Who is the president of France?")`

### 3. ReAct Agent
- **Framework**: LangChain's `AgentType.ZERO_SHOT_REACT_DESCRIPTION`
- **Model**: Google Gemini 2.0 Flash
- **Reasoning**: Step-by-step decision making about tool usage

## 📊 Example Queries

### Mathematical Queries
```python
# Basic arithmetic
"What is 12 multiplied by 15?"

# Complex calculations
"What is the square of 144, raised to the power of 1/3?"

# Trigonometric functions
"What is the sin of 30 degrees?"
```

### Factual Queries
```python
# Current information
"Who is the president of France?"
"What is the capital of Tibet?"
```

### Multi-step Problems
```python
# Combines search + calculation
"What is the population of Germany divided by 2?"

# Unit conversion
"My height in cm is 165cm. What is my height in yards?"
```

## 🔧 Technical Details

### Rate Limiting
- **Free Tier Limit**: 15 requests per minute
- **Solution**: Built-in retry logic with exponential backoff
- **Handling**: `safe_agent_invoke()` function with automatic retries

### Tool Integration
- **LangChain Tools**: Uses `@tool` decorator for custom tools
- **Community Tools**: Integrates `DuckDuckGoSearchRun` from `langchain_community`
- **Error Handling**: Graceful fallback when tools fail

### Model Configuration
```python
llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    api_key=gemini_api_key,
    temperature=0.3,
    max_tokens=1500,
    timeout=None,
    max_retries=2
)
```

## 🎓 Learning Objectives

This project demonstrates:

1. **ReAct Pattern**: Reasoning + Acting for intelligent tool selection
2. **LangChain Integration**: Using LangChain's agent framework
3. **Tool Development**: Creating custom tools with the `@tool` decorator
4. **Error Handling**: Managing API rate limits and tool failures
5. **Multi-step Reasoning**: Combining multiple tools for complex queries

## 🚧 Known Issues & Limitations

1. **Math Functions**: Some trigonometric functions require `math.` prefix
2. **Rate Limiting**: Free tier has 15 requests/minute limit
3. **Search Accuracy**: DuckDuckGo results may vary in quality
4. **Tool Fallbacks**: Agent may not always choose optimal tools

## 🔮 Future Enhancements

- [ ] Add more tools (Wikipedia, weather, unit conversion)
- [ ] Implement conversation memory
- [ ] Add structured output parsing
- [ ] Create a web interface with Streamlit
- [ ] Migrate to LangGraph for advanced workflows
- [ ] Add support for file uploads and document Q&A

## 📚 Related Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [LangGraph (Next Generation)](https://langchain-ai.github.io/langgraph/)

## 🤝 Contributing

Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Share your own agent implementations

## 📄 License

This project is for educational purposes. Please respect the terms of service for all APIs used.

---

**Happy Agent Building! 🤖✨**
