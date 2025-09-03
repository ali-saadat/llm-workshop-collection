#!/usr/bin/env python3
"""
🚀 LLM Workshop: Complete Master Edition
Duration: 3 hours
Level: Beginner
Tools: VS Code, Cursor, or WindSurf

IMPORTANT: Make sure your virtual environment is activated!
If you haven't set up the environment yet, run: python3 workshop_setup.py

This master file combines all three workshop parts:
- Part 1: LLM Hello World
- Part 2: LLM Agents  
- Part 3: MCP Server Development
"""

import requests
import json
import os
import asyncio
import subprocess
import sys
from typing import Dict, Any, List, Optional
from datetime import datetime

# ============================================================================
# 🎯 WORKSHOP OVERVIEW
# ============================================================================

print("🚀 LLM WORKSHOP: COMPLETE MASTER EDITION")
print("=" * 60)
print("Duration: 3 hours | Level: Beginner")
print("=" * 60)

print("""
🎯 What You'll Learn:

Part 1: LLM Hello World (45 min)
- Connect to your LLM endpoint
- Check available models  
- Generate text with simple prompts
- Have conversations with the LLM
- Experiment with temperature and tokens

Part 2: LLM Agents (45 min)
- Create custom tools (calculator, weather, time)
- Build a tool-calling agent with LangChain
- Create a conversational agent with memory
- See how agents reason through complex tasks

Part 3: MCP Server (45 min)
- Learn what MCP is and why it's useful
- Create a simple MCP server with 3 tools
- Understand how to connect from VS Code/Cursor
- Explore advanced MCP capabilities

Let's get started! 🎉
""")

# ============================================================================
# 🔧 PART 1: SETUP AND CONFIGURATION
# ============================================================================

print("\n" + "=" * 60)
print("🔧 PART 1: Setup and Configuration")
print("=" * 60)

# Load from environment variables
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://yylh5vmmm0.execute-api.eu-central-1.amazonaws.com/prod/v1")
API_KEY = os.getenv("API_KEY", "ALI-CLASS-2025")

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("✅ Configuration loaded!")
print(f"🌐 Base URL: {BASE_URL}")
print(f"🔑 API Key: {API_KEY[:10]}...")

# ============================================================================
# 🧪 PART 1: TEST 1 - Check Available Models
# ============================================================================

print("\n" + "=" * 60)
print("🧪 PART 1: Test 1 - Check Available Models")
print("=" * 60)

def check_models():
    """Check what models are available on your endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/v1/models", headers=headers)
        if response.status_code == 200:
            models = response.json()
            print("✅ Successfully connected to your endpoint!")
            print("📋 Available models:")
            for model in models.get('data', []):
                print(f"   - {model.get('id', 'Unknown')}")
            return models
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return None

# Test the connection
models = check_models()

# ============================================================================
# 🌟 PART 1: LLM Hello World - Basic Text Generation
# ============================================================================

print("\n" + "=" * 60)
print("🌟 PART 1: LLM Hello World - Basic Text Generation")
print("=" * 60)

def generate_text(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """Generate text using your LLM endpoint"""
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(f"{BASE_URL}/v1/chat/completions", 
                               headers=headers, 
                               json=payload)
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Exception: {e}"

# Test 1: Simple greeting
print("🤖 Test 1: Simple Greeting")
prompt1 = "Hello! Can you give me a friendly greeting in 2 sentences?"
response1 = generate_text(prompt1)
print(f"Prompt: {prompt1}")
print(f"Response: {response1}")

# Test 2: Creative writing
print("\n🤖 Test 2: Creative Writing")
prompt2 = "Write a short, fun story about a robot learning to cook (max 3 sentences)"
response2 = generate_text(prompt2)
print(f"Prompt: {prompt2}")
print(f"Response: {response2}")

# Test 3: Code explanation
print("\n🤖 Test 3: Code Explanation")
prompt3 = "Explain what a Python function is in simple terms (max 2 sentences)"
response3 = generate_text(prompt3)
print(f"Prompt: {prompt3}")
print(f"Response: {response3}")

# ============================================================================
# 🔄 PART 1: LLM Hello World - Chat Completion
# ============================================================================

print("\n" + "=" * 60)
print("🔄 PART 1: LLM Hello World - Chat Completion")
print("=" * 60)

def chat_completion(messages: list, model: str = "gpt-3.5-turbo") -> str:
    """Have a conversation with your LLM"""
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": 100,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(f"{BASE_URL}/v1/chat/completions", 
                               headers=headers, 
                               json=payload)
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Exception: {e}"

# Start a conversation
print("💬 Starting a conversation...")

conversation = [
    {"role": "user", "content": "Hi! I'm learning about LLMs. Can you help me?"}
]

# First response
response = chat_completion(conversation)
print(f"🤖 Assistant: {response}")

# Add to conversation and continue
conversation.append({"role": "assistant", "content": response})
conversation.append({"role": "user", "content": "What's the most exciting thing about LLMs?"})

response2 = chat_completion(conversation)
print(f"🤖 Assistant: {response2}")

# ============================================================================
# 🎯 PART 1: Hands-On Exercise
# ============================================================================

print("\n" + "=" * 60)
print("🎯 PART 1: Hands-On Exercise")
print("=" * 60)

print("""
🎯 Your Turn! Try these exercises:

1. **Custom Prompt**: Create your own prompt and see what the LLM generates
   - Try asking about your favorite hobby
   - Ask for a recipe or travel tip
   - Request a poem or joke

2. **Temperature Experiment**: Change the temperature value (0.1 to 1.0)
   - Lower = more focused/consistent
   - Higher = more creative/varied

3. **Token Limit**: Experiment with max_tokens
   - Try 50, 100, 200 tokens
   - See how it affects response length

4. **Model Comparison**: If you have multiple models, compare their outputs

💡 Tips:
- Keep prompts clear and specific
- Start with simple requests
- Don't worry about perfect responses - this is learning!
""")

# ============================================================================
# 📝 PART 1 SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("📝 PART 1 SUMMARY")
print("=" * 60)

print("""
✅ What We Accomplished:
- Connected to your LLM endpoint
- Checked available models
- Generated text with simple prompts
- Had a conversation with the LLM
- Learned about temperature and tokens

🔑 Key Concepts:
- API endpoints and authentication
- Text generation vs chat completion
- Prompt engineering basics
- Model parameters (temperature, max_tokens)

🚀 Next Up: LLM Agents with LangChain!
""")

print("\n🎉 Part 1 Complete! Ready for Part 2: LLM Agents?")

# ============================================================================
# 🤖 PART 2: LLM AGENTS WITH LANGCHAIN
# ============================================================================

print("\n" + "=" * 60)
print("🤖 PART 2: LLM Agents with LangChain")
print("=" * 60)

print("🛠️ Creating Custom Tools for Our Agent")
print("-" * 40)

# Try to import LangChain components
try:
    from langchain.agents import initialize_agent, AgentType, Tool
    from langchain.tools import BaseTool
    from langchain_openai import ChatOpenAI
    from langchain.schema import HumanMessage, AIMessage
    from langchain.memory import ConversationBufferMemory
    
    print("✅ LangChain imports successful!")
    
    # ============================================================================
    # 🛠️ CUSTOM TOOLS FOR OUR AGENT
    # ============================================================================
    
    class CalculatorTool(BaseTool):
        """Simple calculator tool for the agent"""
        name: str = "calculator"
        description: str = "Useful for doing math calculations. Input should be a mathematical expression like '2 + 2' or '10 * 5'"
        
        def _run(self, query: str) -> str:
            """Execute the calculation"""
            try:
                # Simple and safe evaluation - only basic math operations
                allowed_chars = set('0123456789+-*/.() ')
                if not all(c in allowed_chars for c in query):
                    return "Error: Only basic math operations (+, -, *, /, .) and numbers are allowed"
                
                result = eval(query)
                return f"Result: {result}"
            except Exception as e:
                return f"Error calculating {query}: {str(e)}"

    class WeatherTool(BaseTool):
        """Mock weather tool for demonstration"""
        name: str = "weather"
        description: str = "Get weather information for a city. Input should be a city name like 'London' or 'New York'"
        
        def _run(self, city: str) -> str:
            """Mock weather response"""
            # In a real scenario, this would call a weather API
            weather_data = {
                "London": "🌧️ Cloudy with rain, 15°C",
                "New York": "☀️ Sunny, 22°C", 
                "Tokyo": "⛅ Partly cloudy, 18°C",
                "Sydney": "🌤️ Mostly sunny, 25°C"
            }
            
            if city in weather_data:
                return f"Weather in {city}: {weather_data[city]}"
            else:
                return f"Weather for {city}: ☀️ Nice weather, 20°C (mock data)"

    class TimeTool(BaseTool):
        """Simple time tool"""
        name: str = "get_time"
        description: str = "Get the current time. No input needed."
        
        def _run(self, query: str = "") -> str:
            """Get current time"""
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            return f"Current time: {current_time}"

    # Create our tools
    tools = [
        CalculatorTool(),
        WeatherTool(),
        TimeTool()
    ]

    print("✅ Created 3 custom tools:")
    for tool in tools:
        print(f"   - {tool.name}: {tool.description}")

    # ============================================================================
    # 🤖 AGENT 1: TOOL-CALLING AGENT
    # ============================================================================

    print("\n" + "=" * 60)
    print("🤖 PART 2: Agent 1 - Tool-Calling Agent")
    print("=" * 60)

    # Configure the LLM (using your endpoint)
    llm = ChatOpenAI(
        base_url=os.getenv("BASE_URL", "https://yylh5vmmm0.execute-api.eu-central-1.amazonaws.com/prod/v1"),
        api_key=os.getenv("API_KEY", "ALI-CLASS-2025"),
        model="anthropic.claude-3-haiku-20240307-v1:0",
        temperature=0.1
    )

    # Initialize the agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

    print("✅ Agent initialized with tools!")
    print("🤖 Testing tool calling capabilities...")

    # Test 1: Math calculation
    print("\n🧮 Test 1: Math Calculation")
    try:
        response1 = agent.run("What is 15 * 8 + 3?")
        print(f"Agent Response: {response1}")
    except Exception as e:
        print(f"Error: {e}")

    # Test 2: Weather information
    print("\n🌤️ Test 2: Weather Information")
    try:
        response2 = agent.run("What's the weather like in London?")
        print(f"Agent Response: {response2}")
    except Exception as e:
        print(f"Error: {e}")

    # Test 3: Time request
    print("\n⏰ Test 3: Time Request")
    try:
        response3 = agent.run("What time is it right now?")
        print(f"Agent Response: {response3}")
    except Exception as e:
        print(f"Error: {e}")

    # ============================================================================
    # 🤖 AGENT 2: CONVERSATIONAL AGENT WITH MEMORY
    # ============================================================================

    print("\n" + "=" * 60)
    print("🤖 PART 2: Agent 2 - Conversational Agent with Memory")
    print("=" * 60)

    # Create a memory component
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    # Create a conversational agent
    conversational_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        handle_parsing_errors=True
    )

    print("✅ Conversational agent with memory initialized!")
    print("💬 Testing conversation flow...")

    # Start a conversation
    print("\n💬 Starting conversation...")

    try:
        # First message
        response1 = conversational_agent.run("Hi! I'm planning a trip. Can you help me?")
        print(f"🤖 Agent: {response1}")
        
        # Second message (agent should remember context)
        response2 = conversational_agent.run("What's the weather like in Tokyo?")
        print(f"🤖 Agent: {response2}")
        
        # Third message (testing memory)
        response3 = conversational_agent.run("And what about the weather in London?")
        print(f"🤖 Agent: {response3}")
        
        # Fourth message (testing tool combination)
        response4 = conversational_agent.run("If I have 500 dollars and spend 120 on flights, how much do I have left?")
        print(f"🤖 Agent: {response4}")
        
    except Exception as e:
        print(f"Error in conversation: {e}")

    # ============================================================================
    # 🎯 PART 2: Hands-On Exercise
    # ============================================================================

    print("\n" + "=" * 60)
    print("🎯 PART 2: Hands-On Exercise")
    print("=" * 60)

    print("""
🎯 Your Turn! Try these exercises:

1. **Tool Testing**: Ask the agent to use different tools
   - "Calculate 25 * 4 / 2"
   - "What's the weather in Sydney?"
   - "What time is it?"

2. **Multi-Step Tasks**: Give the agent complex requests
   - "If I have $1000 and spend $300 on a hotel, $150 on food, how much do I have left?"
   - "What's the weather in New York and what time is it there?"

3. **Conversation Flow**: Have a natural conversation
   - Ask about planning a weekend trip
   - Request calculations for a budget
   - Ask about weather in different cities

4. **Custom Tool**: Try creating your own simple tool
   - A tool that returns random facts
   - A tool that converts units
   - A tool that gives motivational quotes

💡 Tips:
- Be specific in your requests
- Let the agent use multiple tools when needed
- Watch how it reasons through complex tasks
- Don't worry if it makes mistakes - this is learning!
""")

    # ============================================================================
    # 🔍 PART 2: Agent Reasoning Demonstration
    # ============================================================================

    print("\n" + "=" * 60)
    print("🔍 PART 2: Agent Reasoning Demonstration")
    print("=" * 60)

    print("""
🔍 Let's see how the agent thinks through a complex task:

Task: "I have $500 and want to plan a weekend trip. 
I need to spend $200 on accommodation, $100 on food, 
and I want to know how much I'll have left for activities."

The agent should:
1. Use the calculator to subtract expenses: $500 - $200 - $100
2. Give you the remaining budget
3. Suggest what you could do with the remaining money

This shows the agent's ability to:
- Break down complex requests
- Use multiple tools
- Provide helpful, contextual responses
""")

    # Test the complex task
    print("\n🧪 Testing Complex Task...")
    try:
        complex_response = conversational_agent.run(
            "I have $500 and want to plan a weekend trip. "
            "I need to spend $200 on accommodation, $100 on food, "
            "and I want to know how much I'll have left for activities."
        )
        print(f"🤖 Agent Response: {complex_response}")
    except Exception as e:
        print(f"Error: {e}")

    # ============================================================================
    # 📝 PART 2 SUMMARY
    # ============================================================================

    print("\n" + "=" * 60)
    print("📝 PART 2 SUMMARY")
    print("=" * 60)

    print("""
✅ What We Accomplished:
- Created custom tools (calculator, weather, time)
- Built a tool-calling agent with LangChain
- Created a conversational agent with memory
- Saw how agents reason through complex tasks
- Tested multi-step problem solving

🔑 Key Concepts:
- Tools: Functions agents can call
- Agents: LLMs that can use tools
- Memory: How agents remember conversations
- Reasoning: How agents break down complex tasks

🚀 Next Up: Building Your Own MCP Server!
""")

    print("\n🎉 Part 2 Complete! Ready for Part 3: MCP Server Development?")

except ImportError as e:
    print(f"⚠️  LangChain not available: {e}")
    print("💡 Install with: pip install langchain langchain-openai")
    print("🚀 Continuing to Part 3...")

# ============================================================================
# 🔌 PART 3: MCP SERVER DEVELOPMENT
# ============================================================================

print("\n" + "=" * 60)
print("🔌 PART 3: MCP Server Development")
print("=" * 60)

print("📚 Understanding MCP (Model Context Protocol)")
print("-" * 40)

print("""
🔍 MCP (Model Context Protocol) is a way for AI models to:
- Connect to external tools and resources
- Access real-time information
- Interact with your local system
- Extend their capabilities beyond just text

💡 Think of it as giving your AI a "remote control" to your computer!
""")

# ============================================================================
# 🛠️ PART 3: Installing MCP Requirements
# ============================================================================

print("\n" + "=" * 60)
print("🛠️ PART 3: Installing MCP Requirements")
print("=" * 60)

def install_mcp_requirements():
    """Install required packages for MCP development"""
    packages = [
        "mcp"
    ]
    
    print("📦 Installing MCP packages...")
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            print("💡 You may need to install manually: pip install mcp")

# Uncomment the line below to install packages
# install_mcp_requirements()

print("💡 If you haven't installed MCP packages yet, run:")
print("   pip install mcp")

# ============================================================================
# 🚀 PART 3: Creating Your First MCP Server
# ============================================================================

print("\n" + "=" * 60)
print("🚀 PART 3: Creating Your First MCP Server")
print("=" * 60)

# Create a simple MCP server
mcp_server_code = '''#!/usr/bin/env python3
"""
🎯 Simple MCP Server - Hello World
This server provides basic tools for demonstration
"""

import asyncio
import json
import sys
from typing import Any, Dict, List
from datetime import datetime

class SimpleMCPServer:
    """Simple MCP Server implementation"""
    
    def __init__(self):
        self.tools = {
            "hello_world": {
                "description": "A simple hello world tool that greets the user",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Your name (optional)"
                        }
                    }
                }
            },
            "get_current_time": {
                "description": "Get the current date and time",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            "calculate": {
                "description": "Perform basic mathematical calculations",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Mathematical expression to evaluate"
                        }
                    },
                    "required": ["expression"]
                }
            }
        }
    
    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming MCP requests"""
        
        method = request.get("method")
        request_id = request.get("id")
        
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "workshop-mcp-server",
                        "version": "1.0.0"
                    }
                }
            }
        
        elif method == "tools/list":
            tools_list = []
            for name, tool_info in self.tools.items():
                tools_list.append({
                    "name": name,
                    "description": tool_info["description"],
                    "inputSchema": tool_info["inputSchema"]
                })
            
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "tools": tools_list
                }
            }
        
        elif method == "tools/call":
            tool_name = request.get("params", {}).get("name")
            arguments = request.get("params", {}).get("arguments", {})
            
            result = await self.execute_tool(tool_name, arguments)
            
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": result
                        }
                    ]
                }
            }
        
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                }
            }
    
    async def execute_tool(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        """Execute the requested tool"""
        
        if tool_name == "hello_world":
            name = arguments.get("name", "there")
            return f"Hello {name}! 👋 Welcome to your first MCP server!"
        
        elif tool_name == "get_current_time":
            now = datetime.now()
            return f"🕐 Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
        
        elif tool_name == "calculate":
            expression = arguments.get("expression", "")
            try:
                # Simple and safe evaluation for basic math
                allowed_chars = set('0123456789+-*/.() ')
                if not all(c in allowed_chars for c in expression):
                    return "❌ Error: Only basic mathematical expressions are allowed"
                
                result = eval(expression)
                return f"🧮 {expression} = {result}"
            except Exception as e:
                return f"❌ Error calculating '{expression}': {str(e)}"
        
        else:
            return f"❌ Unknown tool: {tool_name}"
    
    async def run(self):
        """Run the MCP server"""
        print("🚀 Starting Simple MCP Server...", file=sys.stderr)
        print("📋 Available tools:", file=sys.stderr)
        for name, tool_info in self.tools.items():
            print(f"   - {name}: {tool_info['description']}", file=sys.stderr)
        print("🔌 Server ready for connections!", file=sys.stderr)
        
        while True:
            try:
                # Read request from stdin
                line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                if not line:
                    break
                
                request = json.loads(line.strip())
                response = await self.handle_request(request)
                
                # Send response to stdout
                print(json.dumps(response))
                sys.stdout.flush()
                
            except json.JSONDecodeError:
                continue
            except Exception as e:
                print(f"Error: {e}", file=sys.stderr)
                break

async def main():
    """Main entry point"""
    server = SimpleMCPServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())

'''

# Save the MCP server code
with open("workshop_mcp_server.py", "w") as f:
    f.write(mcp_server_code)

print("✅ Created workshop_mcp_server.py")
print("📋 This server provides 3 simple tools:")
print("   - hello_world: Greet the user")
print("   - get_current_time: Get current time")
print("   - calculate_simple: Do math calculations")

# ============================================================================
# 🧪 PART 3: Testing Your MCP Server
# ============================================================================

print("\n" + "=" * 60)
print("🧪 PART 3: Testing Your MCP Server")
print("=" * 60)

print("""
🧪 To test your MCP server:

1. **Start the server** (in a new terminal):
   python workshop_mcp_server.py

2. **Test with curl** (in another terminal):
   curl -X POST http://localhost:8000/call_tool \\
        -H "Content-Type: application/json" \\
        -d '{"name": "hello_world", "arguments": {"name": "Alice"}}'

3. **Or use the MCP client**:
   python -c "
   from mcp.client.stdio import stdio_client
   import asyncio
   
   async def test():
       async with stdio_client(['python', 'workshop_mcp_server.py']) as client:
           tools = await client.list_tools()
           print('Available tools:', tools)
   
   asyncio.run(test())
   "
""")

# ============================================================================
# 🔌 PART 3: Connecting from VS Code/Cursor
# ============================================================================

print("\n" + "=" * 60)
print("🔌 PART 3: Connecting from VS Code/Cursor")
print("=" * 60)

print("""
🔌 To connect your MCP server to VS Code/Cursor:

1. **Install MCP Extension**:
   - VS Code: Search for "MCP" in extensions
   - Cursor: Should have MCP support built-in

2. **Configure MCP Client**:
   Create ~/.config/mcp/clients.json:
   {
     "workshop-server": {
       "command": "python",
       "args": ["/path/to/your/workshop_mcp_server.py"],
       "env": {}
     }
   }

3. **Restart VS Code/Cursor**:
   - The MCP server should now be available
   - You can ask the AI to use your custom tools!

4. **Test the Connection**:
   Ask: "What time is it?" or "Calculate 15 * 3"
   The AI should use your MCP server tools!
""")

# ============================================================================
# 🎯 PART 3: Hands-On Exercise
# ============================================================================

print("\n" + "=" * 60)
print("🎯 PART 3: Hands-On Exercise")
print("=" * 60)

print("""
🎯 Your Turn! Try these exercises:

1. **Run Your Server**:
   - Start the MCP server in a terminal
   - Test it with simple requests
   - Make sure it responds correctly

2. **Add a New Tool**:
   - Create a tool that returns random facts
   - Add a tool that converts temperatures
   - Build a tool that gives motivational quotes

3. **Connect to VS Code/Cursor**:
   - Set up the MCP client configuration
   - Restart your editor
   - Ask the AI to use your tools

4. **Debug and Improve**:
   - Add error handling to your tools
   - Improve the tool descriptions
   - Add input validation

💡 Tips:
- Start simple and build up
- Test each tool individually
- Check the MCP documentation for more features
- Don't worry about perfection - focus on learning!
""")

# ============================================================================
# 🔍 PART 3: Advanced MCP Features
# ============================================================================

print("\n" + "=" * 60)
print("🔍 PART 3: Advanced MCP Features")
print("=" * 60)

print("""
🔍 Once you're comfortable with basics, explore:

1. **Resources**: Provide access to files, databases, APIs
2. **Prompts**: Create reusable prompt templates
3. **Logging**: Add structured logging to your server
4. **Authentication**: Secure your server with proper auth
5. **Streaming**: Handle long-running operations
6. **Error Handling**: Graceful error handling and recovery

🚀 **Real-World Examples**:
- File system access (read/write files)
- Database queries (SQL, NoSQL)
- API integrations (weather, news, etc.)
- System monitoring (CPU, memory, processes)
- Custom business logic tools
""")

# ============================================================================
# 📝 PART 3 SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("📝 PART 3 SUMMARY")
print("=" * 60)

print("""
✅ What We Accomplished:
- Learned what MCP is and why it's useful
- Created a simple MCP server with 3 tools
- Understood how to connect from VS Code/Cursor
- Explored advanced MCP capabilities

🔑 Key Concepts:
- MCP Server: Provides tools and resources
- MCP Client: Connects to servers (VS Code, etc.)
- Tools: Functions the AI can call
- Resources: Data the AI can access

🚀 Next Steps:
- Run your server and test it
- Connect it to VS Code/Cursor
- Build more sophisticated tools
- Explore the MCP ecosystem
""")

print("\n🎉 Part 3 Complete! You now have a working MCP server!")

# ============================================================================
# 🎉 WORKSHOP COMPLETE!
# ============================================================================

print("\n" + "=" * 60)
print("🎉 WORKSHOP COMPLETE!")
print("=" * 60)

print("""
🌟 **CONGRATULATIONS!** 🌟

You've completed the complete LLM workshop and now have:

✅ A working connection to your LLM endpoint  
✅ Experience with LangChain agents and tools  
✅ Your own MCP server with custom tools  
✅ Knowledge of how to integrate everything  

**What You've Built:**
1. **LLM Connection**: Direct API access to your endpoint
2. **Custom Tools**: Calculator, weather, time tools
3. **Smart Agents**: Agents that can reason and use tools
4. **MCP Server**: Your own server that VS Code/Cursor can use

**Next Steps:**
- Customize your tools and agents
- Build more sophisticated MCP servers
- Integrate with real APIs and databases
- Create your own AI-powered applications

**Time to build something amazing! 🚀**

---

**Workshop Files Created:**
- `workshop_mcp_server.py` - Your working MCP server
- All workshop code is now in Jupiter notebook format

**Resources:**
- Check README.md for detailed instructions
- Use QUICK_START.md for quick reference
- Explore the individual notebook parts for focused learning
""")

print("\n🎯 **Happy coding and building!** 🚀")
