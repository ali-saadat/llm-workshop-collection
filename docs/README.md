# 📚 Basic LLM Workshop: From Hello World to MCP Servers

**Duration:** 3 hours  
**Level:** Beginner  
**Tools:** VS Code, Cursor, or WindSurf

---

## 🎯 Workshop Overview

This comprehensive workshop takes you from basic LLM interactions to building your own MCP (Model Context Protocol) server. Perfect for beginners who want to understand the full LLM development stack!

### What You'll Learn

1. **LLM Hello World** (45 min) - Connect to your endpoint and generate text
2. **LLM Agents** (45 min) - Create simple agents that can use tools  
3. **MCP Server** (45 min) - Build your own server and connect from VS Code
4. **Integration** (45 min) - Combine everything into a working system

---

## 📋 Prerequisites

- Python 3.8+ installed
- VS Code, Cursor, or WindSurf
- Your API endpoint and key ready
- Basic Python knowledge (variables, functions, classes)

---

## 🔑 Your API Configuration

```bash
BASE_URL = "https://yylh5vmmm0.execute-api.eu-central-1.amazonaws.com/prod"
API_KEY = "ALI-CLASS-2025"
```

---

## 🚀 Getting Started

### 0. Quick Start with Master Notebook

**Want to run everything in one go?**
```bash
# Open the complete workshop notebook
workshop_master.ipynb
```

This single notebook contains all three parts and can be run sequentially!

### 1. Setup Virtual Environment (Recommended)

**For macOS/Linux users experiencing "externally-managed-environment" error:**

```bash
# Run the setup script (handles everything automatically)
python3 workshop_setup.py

# Or manually:
python3 -m venv llm_workshop_env
source llm_workshop_env/bin/activate
pip install -r requirements.txt
```

**For Windows users:**
```bash
python -m venv llm_workshop_env
llm_workshop_env\\Scripts\\activate
pip install -r requirements.txt
```

### 2. Install Dependencies

```bash
# Make sure your virtual environment is activated, then:
pip install -r requirements.txt
```

### 2. Workshop Structure

The workshop is available in both Python script and Jupiter notebook formats:

**Jupiter Notebooks (Recommended):**
- **`workshop_master.ipynb`** - Complete workshop in one notebook (3 hours)
- **`workshop_part1_setup.ipynb`** - LLM basics and API connection (45 min)
- **`workshop_part2_agents.ipynb`** - LangChain agents and tools (45 min)
- **`workshop_part3_mcp_server.ipynb`** - MCP server development (45 min)

**Python Scripts:**
- **`workshop_part1_setup.py`** - LLM basics and API connection
- **`workshop_part2_agents.py`** - LangChain agents and tools
- **`workshop_part3_mcp_server.py`** - MCP server development

---

## 📚 Part 1: LLM Hello World (45 min)

**File:** `workshop_part1_setup.py`

### What You'll Do
- Connect to your LLM endpoint
- Check available models
- Generate text with simple prompts
- Have conversations with the LLM
- Experiment with temperature and tokens

### Run It

**Option 1: Jupiter Notebook (Recommended)**
```bash
# Open in VS Code, Cursor, or Jupyter Lab
workshop_part1_setup.ipynb
```

**Option 2: Python Script**
```bash
python workshop_part1_setup.py
```

### Key Concepts
- API endpoints and authentication
- Text generation vs chat completion
- Prompt engineering basics
- Model parameters (temperature, max_tokens)

---

## 🤖 Part 2: LLM Agents (45 min)

**File:** `workshop_part2_agents.py`

### What You'll Do
- Create custom tools (calculator, weather, time)
- Build a tool-calling agent with LangChain
- Create a conversational agent with memory
- See how agents reason through complex tasks

### Run It

**Option 1: Jupiter Notebook (Recommended)**
```bash
# Open in VS Code, Cursor, or Jupyter Lab
workshop_part2_agents.ipynb
```

**Option 2: Python Script**
```bash
python workshop_part2_agents.py
```

### Key Concepts
- Tools: Functions agents can call
- Agents: LLMs that can use tools
- Memory: How agents remember conversations
- Reasoning: How agents break down complex tasks

---

## 🔌 Part 3: MCP Server (45 min)

**File:** `workshop_part3_mcp_server.py`

### What You'll Do
- Learn what MCP is and why it's useful
- Create a simple MCP server with 3 tools
- Understand how to connect from VS Code/Cursor
- Explore advanced MCP capabilities

### Run It

**Option 1: Jupiter Notebook (Recommended)**
```bash
# Open in VS Code, Cursor, or Jupyter Lab
workshop_part3_mcp_server.ipynb
```

**Option 2: Python Script**
```bash
python workshop_part3_mcp_server.py
```

### Generated Files
- `workshop_mcp_server.py` - Your working MCP server

### Key Concepts
- MCP Server: Provides tools and resources
- MCP Client: Connects to servers (VS Code, etc.)
- Tools: Functions the AI can call
- Resources: Data the AI can access

---

## 🔌 Connecting Your MCP Server to VS Code/Cursor

### 1. Install MCP Extension
- **VS Code**: Search for "MCP" in extensions
- **Cursor**: Should have MCP support built-in

### 2. Configure MCP Client
Create `~/.config/mcp/clients.json`:

```json
{
  "workshop-server": {
    "command": "python",
    "args": ["/path/to/your/workshop_mcp_server.py"],
    "env": {}
  }
}
```

### 3. Restart Your Editor
The MCP server should now be available!

### 4. Test the Connection
Ask: "What time is it?" or "Calculate 15 * 3"
The AI should use your MCP server tools!

---

## 🎯 Hands-On Exercises

### Part 1 Exercises
1. **Custom Prompts**: Create your own prompts
2. **Temperature Experiment**: Try different temperature values
3. **Token Limits**: Experiment with max_tokens
4. **Model Comparison**: Compare different models

### Part 2 Exercises
1. **Tool Testing**: Ask the agent to use different tools
2. **Multi-Step Tasks**: Give complex requests
3. **Conversation Flow**: Have natural conversations
4. **Custom Tools**: Create your own tools

### Part 3 Exercises
1. **Run Your Server**: Start and test your MCP server
2. **Add New Tools**: Create additional tools
3. **Connect to Editor**: Set up VS Code/Cursor connection
4. **Debug and Improve**: Add error handling

---

## 🚀 Advanced Features

Once you're comfortable with basics, explore:

- **Resources**: Provide access to files, databases, APIs
- **Prompts**: Create reusable prompt templates
- **Logging**: Add structured logging to your server
- **Authentication**: Secure your server with proper auth
- **Streaming**: Handle long-running operations

---

## 🐛 Troubleshooting

### Common Issues

1. **Externally-Managed-Environment Error**: 
   - Use the virtual environment setup: `python3 workshop_setup.py`
   - Or manually create a virtual environment (see Getting Started section)

2. **Import Errors**: Make sure all packages are installed in your virtual environment
3. **API Connection**: Verify your endpoint and API key
4. **MCP Connection**: Check your client configuration
5. **Tool Errors**: Ensure your tools handle errors gracefully

### Pydantic Type Annotation Errors

If you see errors like:
```
PydanticUserError: Field 'name' defined on a base class was overridden by a non-annotated attribute
```

**Solution**: The workshop files have been updated with proper type annotations. Make sure you're using the latest versions.

### API 404 Errors

If you see:
```
Error: Error code: 404 - {'error': {'message': 'No route for POST /prod/chat/completions'}}
```

**This is normal!** The custom tools work independently of the LLM API. The 404 errors occur when the agent tries to use the LLM for reasoning, but your tools (calculator, weather, time) work perfectly.

**Test your tools independently:**
```bash
python demo_tools_simple.py
```

### Getting Help

- Check the error messages carefully
- Verify your API configuration
- Test each component individually
- Use the hands-on exercises to debug

---

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [MCP Specification](https://modelcontextprotocol.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [VS Code MCP Extension](https://marketplace.visualstudio.com/items?itemName=modelcontextprotocol.vscode-mcp)

---

## 🎉 Workshop Completion

Congratulations! You've completed the LLM workshop and now have:

✅ A working connection to your LLM endpoint  
✅ Experience with LangChain agents and tools  
✅ Your own MCP server with custom tools  
✅ Knowledge of how to integrate everything  

**Time to build something amazing! 🚀**

---

## 📝 Workshop Notes

Use this space to jot down your learnings, ideas, and next steps:

```
Part 1 Notes:
- 

Part 2 Notes:
- 

Part 3 Notes:
- 

Next Steps:
- 

Ideas for Projects:
- 
```
