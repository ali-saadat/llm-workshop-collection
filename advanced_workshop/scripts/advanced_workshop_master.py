#!/usr/bin/env python3
"""
🚀 Advanced LLM Workshop: Complete Master Edition
Duration: 3 hours
Level: Intermediate/Advanced
Audience: Technical IT teams (UI, backend, full stack, data scientists, PO, PM, scrum master)

IMPORTANT: Make sure your virtual environment is activated!
If you haven't set up the environment yet, run: python3 ../basic_workshop/scripts/workshop_setup.py

This master file combines all advanced workshop parts:
- Part 1: Macro View & Search Evolution
- Part 2: Why Agentic Systems Matter
- Part 3: Library vs Framework vs Platform (Coming Soon)
- Part 4: Hands-on Labs (Coming Soon)
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
# 🎯 ADVANCED WORKSHOP OVERVIEW
# ============================================================================

print("🚀 ADVANCED LLM WORKSHOP: COMPLETE MASTER EDITION")
print("=" * 70)
print("Duration: 3 hours | Level: Intermediate/Advanced")
print("Audience: Technical IT teams (UI, backend, full stack, data scientists, PO, PM, scrum master)")
print("=" * 70)

print("""
🎯 What You'll Learn:

Part 1: Macro View & Search Evolution (30 min)
- Why search evolution matters now
- From keywords to questions to reasoning
- Modern AI patterns (RAG, evaluation, tools)

Part 2: Why Agentic Systems Matter (30 min)
- What makes a system "agentic"
- Memory types and reasoning capabilities
- Agentic system architecture and examples

Part 3: Library vs Framework vs Platform (30 min)
- LangChain, LangGraph, LangSmith overview
- How to choose the right tools
- Hands-on setup and configuration

Part 4: Hands-on Labs (90 min)
- Lab A: Hello Agent in LangChain
- Lab B: Form-filling Chatbot in LangGraph
- Observability & Evaluation with LangSmith
- Production deployment with LangServe

Let's get started! 🎉
""")

# ============================================================================
# 🔑 YOUR API CONFIGURATION
# ============================================================================

print("\n" + "=" * 70)
print("🔑 YOUR API CONFIGURATION")
print("=" * 70)

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
# 🗺 PART 1: MACRO VIEW - WHY THIS MATTERS NOW
# ============================================================================

print("\n" + "=" * 70)
print("🗺 PART 1: Macro View - Why This Matters Now")
print("=" * 70)

print("""
🎯 ELI5: People used to search like robots ("yogurt cake recipe"), 
now they search like humans ("what is the recipe for yogurt cake?"). 
AI has to be smart enough to understand full questions, images, 
even ideas — and give a straight answer.

🔄 KEY SHIFTS IN SEARCH & UX:

1. **From keywords → full questions**
   - Old: "yogurt cake recipe"
   - New: "What's a good recipe for yogurt cake that's not too sweet?"

2. **From static filters → interactive, natural filters**
   - Old: Checkboxes for "vegetarian", "gluten-free"
   - New: "I'm vegetarian and allergic to nuts, what can I cook?"

3. **From static results → conversational guidance**
   - Old: List of links
   - New: AI works like a guide, not just a librarian

❌ WHY ELASTICSEARCH ALONE WON'T CUT IT:

It's like trying to find a movie by shouting a whole plot at a DVD store 
clerk who only listens for exact words.
""")

# ============================================================================
# 🧪 PART 1: DEMONSTRATION - OLD VS NEW SEARCH PATTERNS
# ============================================================================

print("\n" + "=" * 70)
print("🧪 PART 1: Demonstration - Old vs New Search Patterns")
print("=" * 70)

def demonstrate_search_evolution():
    """Demonstrate the evolution from keyword to semantic search"""
    
    print("🔍 OLD SEARCH PATTERN (Keyword-based):")
    print("-" * 50)
    
    old_queries = [
        "yogurt cake recipe",
        "vegetarian dinner",
        "budget travel europe",
        "python tutorial",
        "project management tools"
    ]
    
    for query in old_queries:
        print(f"  ❌ '{query}' → Returns exact matches only")
    
    print("\n🤖 NEW SEARCH PATTERN (Semantic + Reasoning):")
    print("-" * 50)
    
    new_queries = [
        "I want to bake a cake but only have yogurt and eggs, what can I make?",
        "I'm vegetarian and my kids don't like spicy food, dinner ideas?",
        "I have $2000 and 2 weeks, where should I travel in Europe?",
        "I'm a beginner programmer, what's the best way to learn Python?",
        "I need to manage a team of 5 developers, what tools should I use?"
    ]
    
    for query in new_queries:
        print(f"  ✅ '{query}' → AI understands context and provides guidance")

demonstrate_search_evolution()

# ============================================================================
# 🎯 PART 1: TASK - REAL CUSTOMER QUESTIONS
# ============================================================================

print("\n" + "=" * 70)
print("🎯 PART 1: Task - Real Customer Questions from Your Domain")
print("=" * 70)

print("""
🎯 YOUR TASK: Write 3 real customer questions from your domain 
that would require multi-step reasoning to answer.

Think about questions that:
- Have multiple constraints or requirements
- Need context from different sources
- Require reasoning, not just retrieval
- Would be impossible with traditional keyword search

Examples from different domains:

🏥 HEALTHCARE:
- "I have diabetes and high blood pressure, what exercises are safe for me?"
- "My child has a fever and rash, when should I call the doctor?"

🏦 FINANCE:
- "I'm 25, earn $60k, and want to buy a house in 5 years, what should I do?"
- "I have $10k in savings, what's the best investment strategy for my risk tolerance?"

🛒 E-COMMERCE:
- "I need a laptop for video editing under $1000, what's the best option?"
- "I'm planning a camping trip, what gear do I need for 4 people in winter?"

💻 YOUR DOMAIN: Write 3 questions below:
""")

# Interactive input for participants
print("📝 Your 3 customer questions (replace with your actual questions):")
print("1. _________________________________________________")
print("2. _________________________________________________")
print("3. _________________________________________________")

# ============================================================================
# 🛠 PART 1: MODERN AI PATTERNS
# ============================================================================

print("\n" + "=" * 70)
print("🛠 PART 1: Modern AI Patterns")
print("=" * 70)

print("""
🔴 OLD STACK LIMITATIONS:

- **ElasticSearch/BM25** = great for keywords
- **Chokes on long, multi-step, conversational asks**
- **No understanding of context or intent**
- **Static ranking that doesn't adapt to user needs**

🟢 MODERN STACK SOLUTIONS:

1. **RAG (Retrieval Augmented Generation)**
   - Pull facts + let LLM reason
   - Like looking in the right book before answering the question

2. **Add Evaluation (RAG-Triad)**
   - Groundedness: Is the answer based on retrieved facts?
   - Context Relevance: Are the retrieved facts relevant?
   - Answer Relevance: Does the answer address the question?

3. **Add Tools + Planning**
   - APIs, DB queries, external services
   - Multi-step reasoning and execution
   - Fallback and error handling
""")

# ============================================================================
# 📝 PART 1 SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("📝 PART 1 SUMMARY")
print("=" * 70)

print("""
✅ WHAT WE COVERED:

1. **Macro View**: Why search evolution matters now
   - From keywords to full questions
   - From static filters to natural language
   - From results to conversational guidance

2. **Search Evolution**: Keywords → Questions → Reasoning
   - Ranking ≠ solving
   - Semantic understanding > exact match
   - Need for retrieval + reasoning

3. **Modern AI Patterns**: RAG + Evaluation + Tools
   - RAG: Pull facts + let LLM reason
   - RAG-Triad: Groundedness, context relevance, answer relevance
   - Tools: APIs, DB queries, planning

🎯 KEY INSIGHTS:

- **ElasticSearch alone won't cut it** for modern user expectations
- **Users expect answers, not links**
- **AI needs to work like a guide, not a librarian**
- **Multi-step reasoning is essential**

🚀 NEXT UP: Why Agentic Systems Matter!
""")

print("\n🎉 Part 1 Complete! Moving to Part 2...")

# ============================================================================
# 🤖 PART 2: WHY AGENTIC SYSTEMS MATTER
# ============================================================================

print("\n" + "=" * 70)
print("🤖 PART 2: Why Agentic Systems Matter")
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
# 🧠 PART 2: MEMORY TYPES IN AGENTIC SYSTEMS
# ============================================================================

print("\n" + "=" * 70)
print("🧠 PART 2: Memory Types in Agentic Systems")
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
# 🛠 PART 2: TOOLS YOUR AGENT WOULD NEED
# ============================================================================

print("\n" + "=" * 70)
print("🛠 PART 2: Tools Your Agent Would Need")
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
# 🎯 PART 2: YOUR TURN - AGENT TOOLS FOR YOUR DOMAIN
# ============================================================================

print("\n" + "=" * 70)
print("🎯 PART 2: Your Turn - Agent Tools for Your Domain")
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
# 🧩 PART 2: AGENTIC SYSTEM ARCHITECTURE
# ============================================================================

print("\n" + "=" * 70)
print("🧩 PART 2: Agentic System Architecture")
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

🎯 KEY INSIGHTS:

- **Agents are like smart interns** with memory and tools
- **Memory enables personalization** and context awareness
- **Tools extend capabilities** beyond text generation
- **Guardrails ensure safety** and compliance
- **ROI comes from automation** and personalization

🚀 NEXT UP: Library vs Framework vs Platform!
""")

print("\n🎉 Part 2 Complete! Moving to Part 3...")

# ============================================================================
# 📚 PART 3: LIBRARY VS FRAMEWORK VS PLATFORM
# ============================================================================

print("\n" + "=" * 70)
print("📚 PART 3: Library vs Framework vs Platform")
print("=" * 70)

print("""
🎯 ELI5:
- **Library:** A toolbox (you figure out what to build).
- **Framework:** IKEA furniture (you follow a pattern).
- **Platform:** Amazon Prime (everything delivered & hosted).

🔧 THE LANGCHAIN ECOSYSTEM:

1. **LangChain** - Lego bricks for prompts, tools, memory, retrieval
2. **LangGraph** - The Lego instruction booklet — step-by-step building with control flow
3. **LangSmith** - CCTV + notebook — watch every step, replay mistakes, improve
4. **LangServe** - Turn your Lego creation into a web service for others

📊 EXAMPLES BY CATEGORY:

Library: Transformers, FAISS
Framework: LangChain, LangGraph
Platform: AWS Bedrock, Vertex AI

💡 HOW TO CHOOSE:

- **Start with LangChain** if you're building basic agents
- **Move to LangGraph** when you need complex workflows
- **Add LangSmith** for observability and debugging
- **Use LangServe** when you're ready to deploy
""")

# ============================================================================
# 🎯 PART 3: TASK - CHOOSE YOUR TOOLS
# ============================================================================

print("\n" + "=" * 70)
print("🎯 PART 3: Task - Choose Your Tools")
print("=" * 70)

print("""
🎯 YOUR TASK: Based on your agentic system use case from Part 2,
choose which LangChain ecosystem tools you would use.

Think about:
1. **What complexity** does your system need?
2. **What observability** do you require?
3. **What deployment** model fits your needs?

Example Framework:

🏥 HEALTHCARE USE CASE:
Problem: Patient symptom checker with medical knowledge
LangChain: Basic agent with medical tools
LangGraph: Multi-step diagnosis workflow
LangSmith: Track accuracy and compliance
LangServe: Deploy as patient-facing API

💻 YOUR USE CASE: Fill in the framework below:
""")

# Interactive input for participants
print("📝 Your Tool Selection:")
print("Problem: _________________________________________________")
print("LangChain: _________________________________________________")
print("LangGraph: _________________________________________________")
print("LangSmith: _________________________________________________")
print("LangServe: _________________________________________________")

# ============================================================================
# 📝 PART 3 SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("📝 PART 3 SUMMARY")
print("=" * 70)

print("""
✅ WHAT WE COVERED:

1. **Tool Categories**
   - Library: Building blocks
   - Framework: Structured patterns
   - Platform: Complete solutions

2. **LangChain Ecosystem**
   - LangChain: Basic agent building
   - LangGraph: Complex workflows
   - LangSmith: Observability
   - LangServe: Deployment

3. **Tool Selection**
   - Match complexity to needs
   - Consider observability requirements
   - Plan for deployment

🎯 KEY INSIGHTS:

- **Start simple** with LangChain
- **Add complexity** with LangGraph when needed
- **Monitor everything** with LangSmith
- **Deploy easily** with LangServe

🚀 NEXT UP: Hands-on Labs!
""")

print("\n🎉 Part 3 Complete! Moving to Hands-on Labs...")

# ============================================================================
# 💻 PART 4: HANDS-ON LABS PREVIEW
# ============================================================================

print("\n" + "=" * 70)
print("💻 PART 4: Hands-on Labs Preview")
print("=" * 70)

print("""
🎯 WHAT'S COMING IN THE LABS:

**Lab A: Hello Agent in LangChain (30 min)**
- Turn a plain LLM into an agent that can call a tool
- Install LangChain + API key setup
- Create a tool (e.g., calculator, KB search)
- Wrap LLM with tool access
- Run and inspect with LangSmith

**Lab B: Form-filling Chatbot in LangGraph (30 min)**
- A deterministic, 5-field form bot (e.g., return request)
- Flow: Collect → Validate → Enrich → Confirm → Submit
- Guardrails: retries, timeouts, human fallback
- Like the supermarket self-checkout, but for data entry

**Lab C: Observability & Evaluation (15 min)**
- Watch all agent runs (like black box for AI)
- Set KPIs: resolution rate, time-to-first-action
- Create saved views for failed runs & slow tools

**Lab D: Production Deployment (15 min)**
- Wrap graph/agent in FastAPI endpoint with LangServe
- Handle multi-channel sessions (web, WhatsApp, mobile)
- Deploy and test your agentic system
""")

# ============================================================================
# 🎯 WORKSHOP COMPLETION
# ============================================================================

print("\n" + "=" * 70)
print("🎯 WORKSHOP COMPLETION")
print("=" * 70)

print("""
🌟 **CONGRATULATIONS!** 🌟

You've completed the Advanced LLM Workshop and now understand:

✅ **Search Evolution**: Why modern AI patterns matter
✅ **Agentic Systems**: How to build intelligent assistants
✅ **Tool Selection**: Choosing the right LangChain ecosystem tools
✅ **Production Ready**: Understanding deployment and observability

**What You've Learned:**

1. **Macro View**: Search has evolved from keywords to reasoning
2. **Agentic Patterns**: Memory, tools, planning, and guardrails
3. **Tool Ecosystem**: LangChain, LangGraph, LangSmith, LangServe
4. **Business Impact**: ROI through automation and personalization

**Next Steps:**

1. **Complete the Hands-on Labs** to build working systems
2. **Apply to Your Domain** using the frameworks we discussed
3. **Start Small** with LangChain, then scale with LangGraph
4. **Measure Everything** with LangSmith for continuous improvement

**Ready to Build Amazing AI Systems! 🚀**

---

**Workshop Files Created:**
- `advanced_workshop_part1_macro.ipynb` - Macro view and search evolution
- `advanced_workshop_part2_agentic.ipynb` - Agentic systems and architecture
- `advanced_workshop_master.ipynb` - Complete workshop (this file)

**Resources:**
- Check the individual notebooks for focused learning
- Use the master notebook for the complete experience
- Apply the frameworks to your business use cases

**Happy Building! 🎯**
""")

print("\n🎯 **Ready to build amazing AI systems!** 🚀")
