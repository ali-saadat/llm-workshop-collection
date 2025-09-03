#!/usr/bin/env python3
"""
🚀 LLM Workshop: Part 2 - LLM Agents with LangChain
Duration: ~45 minutes
Level: Beginner

IMPORTANT: Make sure your virtual environment is activated!
If you haven't set up the environment yet, run: python3 workshop_setup.py
"""

import os
import json
from typing import List, Dict, Any
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# 🔧 SECTION 2: LLM AGENTS WITH LANGCHAIN
# ============================================================================

print("🎯 LLM WORKSHOP - PART 2: LLM Agents with LangChain")
print("=" * 60)

# ============================================================================
# 🛠️ CUSTOM TOOLS FOR OUR AGENT
# ============================================================================

print("🛠️ Creating Custom Tools for Our Agent")
print("-" * 40)

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
print("🤖 AGENT 1: Tool-Calling Agent")
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
print("🤖 AGENT 2: Conversational Agent with Memory")
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
# 🎯 HANDS-ON EXERCISE
# ============================================================================

print("\n" + "=" * 60)
print("🎯 HANDS-ON EXERCISE")
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
# 🔍 AGENT REASONING DEMONSTRATION
# ============================================================================

print("\n" + "=" * 60)
print("🔍 Agent Reasoning Demonstration")
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
# 📝 SUMMARY
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
