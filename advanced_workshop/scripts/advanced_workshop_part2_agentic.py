#!/usr/bin/env python3
"""
🚀 Advanced LLM Workshop: Part 2 - Why Agentic Systems Matter
Duration: ~30 minutes
Level: Intermediate/Advanced
Audience: Technical IT teams (UI, backend, full stack, data scientists, PO, PM, scrum master)

IMPORTANT: Make sure your virtual environment is activated!
If you haven't set up the environment yet, run: python3 ../basic_workshop/scripts/workshop_setup.py
"""

import requests
import json
import os
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# 🤖 PART 2: WHY AGENTIC SYSTEMS MATTER
# ============================================================================

print("🚀 ADVANCED LLM WORKSHOP - PART 2: Why Agentic Systems Matter")
print("=" * 70)
print("Duration: ~30 minutes | Level: Intermediate/Advanced")
print("Audience: Technical IT teams (UI, backend, full stack, data scientists, PO, PM, scrum master)")
print("=" * 70)

# ============================================================================
# 🔑 YOUR API CONFIGURATION
# ============================================================================

print("\n🔑 Setting up your API configuration...")

# Your API configuration from environment variables
BASE_URL = os.getenv("BASE_URL", "https://yylh5vmmm0.execute-api.eu-central-1.amazonaws.com/prod")
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
# 🤖 WHAT MAKES A SYSTEM "AGENTIC"?
# ============================================================================

print("\n" + "=" * 70)
print("🤖 WHAT MAKES A SYSTEM 'AGENTIC'?")
print("=" * 70)

print("""
🎯 ELI5: An agent is like an intern who can use the phone, search the web, 
and remember what you said 5 minutes ago. An agentic system is a whole team 
of such interns with a manager making sure they follow the plan.

🔑 KEY CHARACTERISTICS OF AGENTIC SYSTEMS:

1. **Memory**: Can remember conversations, facts, and context
2. **Tools**: Can use external services, APIs, and databases
3. **Planning**: Can break down complex tasks into steps
4. **Reasoning**: Can think through problems and make decisions
5. **Adaptation**: Can learn from feedback and adjust behavior

🔄 COMPARISON: Basic LLM vs Agentic System

📝 BASIC LLM:
- Responds to prompts
- No memory between calls
- No access to external tools
- No planning or reasoning
- Like talking to a very smart person with amnesia

🤖 AGENTIC SYSTEM:
- Maintains conversation context
- Can use tools and APIs
- Plans multi-step tasks
- Reasons about complex problems
- Like working with a smart assistant who remembers everything
""")

# ============================================================================
# 🧠 MEMORY TYPES IN AGENTIC SYSTEMS
# ============================================================================

print("\n" + "=" * 70)
print("🧠 MEMORY TYPES IN AGENTIC SYSTEMS")
print("=" * 70)

def demonstrate_memory_types():
    """Demonstrate different types of memory in agentic systems"""
    
    print("🧠 MEMORY TYPES:")
    print("-" * 50)
    
    memory_types = {
        "Short-term": {
            "description": "Conversation so far",
            "example": "User asked about laptops, then mentioned budget",
            "use_case": "Maintain context within a session"
        },
        "Long-term": {
            "description": "Facts learned before",
            "example": "User prefers Apple products, has budget constraints",
            "use_case": "Personalize responses across sessions"
        },
        "Semantic": {
            "description": "Topics & meaning",
            "example": "User is interested in technology and productivity",
            "use_case": "Understand user intent and preferences"
        }
    }
    
    for memory_type, details in memory_types.items():
        print(f"\n📚 {memory_type} Memory:")
        print(f"   Description: {details['description']}")
        print(f"   Example: {details['example']}")
        print(f"   Use Case: {details['use_case']}")

demonstrate_memory_types()

# ============================================================================
# 🛠 TOOLS YOUR AGENT WOULD NEED
# ============================================================================

print("\n" + "=" * 70)
print("🛠 TOOLS YOUR AGENT WOULD NEED")
print("=" * 70)

print("""
🎯 TASK: List tools your agent would need to solve your earlier customer questions.

Think about what your agent would need to:
- Search for information
- Calculate or compute
- Access external services
- Validate data
- Generate responses

🔧 COMMON AGENT TOOLS:

1. **Search Tools**
   - Web search (Google, Bing)
   - Internal knowledge base
   - Document search
   - Product catalog search

2. **Computation Tools**
   - Calculator
   - Unit converter
   - Date/time utilities
   - Statistical analysis

3. **External APIs**
   - Weather data
   - Stock prices
   - Maps and location
   - Social media

4. **Validation Tools**
   - Data format checking
   - Business rule validation
   - User input validation
   - Compliance checking

5. **Communication Tools**
   - Email sending
   - SMS notifications
   - Slack/Teams integration
   - Voice synthesis
""")

# ============================================================================
# 🎯 YOUR TURN: AGENT TOOLS FOR YOUR DOMAIN
# ============================================================================

print("\n" + "=" * 70)
print("🎯 YOUR TURN: Agent Tools for Your Domain")
print("=" * 70)

print("""
🎯 THINK ABOUT YOUR CUSTOMER QUESTIONS FROM PART 1:

What tools would your agent need to answer them effectively?

Example for E-commerce:
Question: "I need a laptop for video editing under $1000"

Required Tools:
1. **Product Search Tool** - Search laptop catalog
2. **Specification Tool** - Get detailed laptop specs
3. **Review Tool** - Access customer reviews
4. **Price Tool** - Check current prices and deals
5. **Recommendation Tool** - Rank options by suitability
6. **Budget Calculator** - Calculate total cost with accessories

💡 YOUR DOMAIN: List the tools your agent would need:
""")

# Interactive input for participants
print("📝 Tools your agent would need (replace with your actual tools):")
print("1. _________________________________________________")
print("2. _________________________________________________")
print("3. _________________________________________________")
print("4. _________________________________________________")
print("5. _________________________________________________")

# ============================================================================
# 🧩 AGENTIC SYSTEM ARCHITECTURE
# ============================================================================

print("\n" + "=" * 70)
print("🧩 AGENTIC SYSTEM ARCHITECTURE")
print("=" * 70)

print("""
🏗️ HOW AGENTIC SYSTEMS ARE BUILT:

1. **Core LLM**: The brain that understands and reasons
2. **Memory System**: Stores context and learns over time
3. **Tool Registry**: Available tools and their capabilities
4. **Planning Engine**: Breaks down complex tasks
5. **Execution Engine**: Runs tools and manages workflow
6. **Guardrails**: Safety and compliance checks

🔄 WORKFLOW EXAMPLE:

User: "I need a laptop for video editing under $1000"

Agent Workflow:
1. **Understand**: Parse request, extract requirements
2. **Plan**: Break into search, filter, rank, recommend
3. **Execute**: Use tools to gather information
4. **Reason**: Analyze options and constraints
5. **Present**: Provide ranked recommendations with explanations

🛡️ GUARDRAILS:
- Budget validation
- Safety checks
- Compliance verification
- Fallback handling
""")

# ============================================================================
# 🧪 DEMONSTRATION: AGENTIC VS NON-AGENTIC RESPONSES
# ============================================================================

print("\n" + "=" * 70)
print("🧪 DEMONSTRATION: Agentic vs Non-Agentic Responses")
print("=" * 70)

def demonstrate_agentic_vs_non_agentic():
    """Show the difference between agentic and non-agentic responses"""
    
    query = "I need a laptop for video editing under $1000"
    
    print(f"🔍 QUERY: {query}")
    print()
    
    print("🔴 NON-AGENTIC RESPONSE (Basic LLM):")
    print("-" * 50)
    print("  ❌ 'Here are some general laptop recommendations for video editing...'")
    print("  ❌ No specific product search")
    print("  ❌ No price validation")
    print("  ❌ No current availability check")
    print("  ❌ Generic advice, not actionable")
    
    print("\n🟢 AGENTIC RESPONSE:")
    print("-" * 50)
    print("  ✅ Searches current laptop inventory")
    print("  ✅ Filters by video editing requirements")
    print("  ✅ Validates price constraints")
    print("  ✅ Checks availability and shipping")
    print("  ✅ Provides ranked recommendations with explanations")
    print("  ✅ Suggests accessories within budget")
    
    print("\n🎯 KEY DIFFERENCE:")
    print("  Non-Agentic: Generic information, user does the work")
    print("  Agentic: Specific, actionable, personalized results")

demonstrate_agentic_vs_non_agentic()

# ============================================================================
# 🚀 REAL-WORLD AGENTIC SYSTEM EXAMPLES
# ============================================================================

print("\n" + "=" * 70)
print("🚀 REAL-WORLD AGENTIC SYSTEM EXAMPLES")
print("=" * 70)

print("""
🌍 WHERE AGENTIC SYSTEMS ARE USED TODAY:

1. **Customer Service**
   - Chatbots that remember conversation history
   - Can access customer database and order history
   - Can escalate to human agents when needed
   - Learn from interactions to improve responses

2. **E-commerce**
   - Product recommendation engines
   - Shopping assistants that understand preferences
   - Inventory and pricing management
   - Customer support automation

3. **Healthcare**
   - Symptom checkers with medical knowledge
   - Appointment scheduling and reminders
   - Patient education and guidance
   - Clinical decision support

4. **Finance**
   - Investment advisors that understand risk tolerance
   - Budget planning and expense tracking
   - Fraud detection and prevention
   - Customer service and support

5. **Education**
   - Personalized learning assistants
   - Homework help and tutoring
   - Progress tracking and assessment
   - Administrative support

💡 YOUR INDUSTRY: Where could agentic systems help?
""")

# ============================================================================
# 🎯 TASK 2: AGENTIC SYSTEM USE CASE
# ============================================================================

print("\n" + "=" * 70)
print("🎯 TASK 2: Agentic System Use Case")
print("=" * 70)

print("""
🎯 YOUR TASK: Design an agentic system for your domain.

Think about:
1. **What problem** would it solve?
2. **What tools** would it need?
3. **What memory** would it maintain?
4. **What guardrails** would it have?
5. **What ROI** would it provide?

Example Framework:

🏥 HEALTHCARE USE CASE:
Problem: Patients struggle to understand medical instructions
Tools: Medical knowledge base, appointment scheduler, reminder system
Memory: Patient history, preferences, compliance tracking
Guardrails: HIPAA compliance, medical accuracy validation
ROI: Reduced readmissions, better patient outcomes, staff efficiency

💻 YOUR USE CASE: Fill in the framework below:
""")

# Interactive input for participants
print("📝 Your Agentic System Use Case:")
print("Problem: _________________________________________________")
print("Tools: _________________________________________________")
print("Memory: _________________________________________________")
print("Guardrails: _________________________________________________")
print("ROI: _________________________________________________")

# ============================================================================
# 📝 PART 2 SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("📝 PART 2 SUMMARY")
print("=" * 70)

print("""
✅ WHAT WE COVERED:

1. **Agentic System Characteristics**
   - Memory, tools, planning, reasoning, adaptation
   - Comparison with basic LLMs

2. **Memory Types**
   - Short-term: Conversation context
   - Long-term: Learned facts
   - Semantic: Topics and meaning

3. **Required Tools**
   - Search, computation, APIs, validation, communication
   - Domain-specific tool requirements

4. **System Architecture**
   - Core LLM, memory, tools, planning, execution, guardrails
   - Workflow and safety considerations

5. **Real-World Examples**
   - Customer service, e-commerce, healthcare, finance, education
   - Industry-specific applications

🎯 KEY INSIGHTS:

- **Agents are like smart interns** with memory and tools
- **Memory enables personalization** and context awareness
- **Tools extend capabilities** beyond text generation
- **Guardrails ensure safety** and compliance
- **ROI comes from automation** and personalization

🚀 NEXT UP: Library vs Framework vs Platform!

In Part 3, you'll learn:
- Differences between libraries, frameworks, and platforms
- LangChain, LangGraph, and LangSmith overview
- How to choose the right tools for your use case
- Hands-on setup and configuration
""")

print("\n🎉 Part 2 Complete! Ready for Part 3: Library vs Framework vs Platform?")

# ============================================================================
# 🎯 HANDS-ON PREPARATION
# ============================================================================

print("\n" + "=" * 70)
print("🎯 HANDS-ON PREPARATION")
print("=" * 70)

print("""
💡 BEFORE PART 3, THINK ABOUT:

1. **Agent Tools**: Have you listed the tools your agent would need?
2. **Use Case Design**: Have you designed your agentic system use case?
3. **Memory Requirements**: What should your agent remember?
4. **Guardrails**: What safety measures would you need?

🧪 OPTIONAL: Research agentic systems in your industry
   to see what's already being built.

📚 RESOURCES:
- [LangChain Agents](https://python.langchain.com/docs/use_cases/autonomous_agents/)
- [Agentic Systems Paper](https://arxiv.org/abs/2304.03442)
- [Memory in AI Systems](https://arxiv.org/abs/2305.19842)

🚀 See you in Part 3! 🎯
""")
