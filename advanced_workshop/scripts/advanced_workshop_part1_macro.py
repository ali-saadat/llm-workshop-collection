#!/usr/bin/env python3
"""
🚀 Advanced LLM Workshop: Part 1 - Macro View & Search Evolution
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
# 🎯 PART 1: MACRO VIEW - WHY THIS MATTERS NOW
# ============================================================================

print("🚀 ADVANCED LLM WORKSHOP - PART 1: Macro View & Search Evolution")
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
# 🗺 MACRO VIEW: WHY THIS MATTERS NOW
# ============================================================================

print("\n" + "=" * 70)
print("🗺 MACRO VIEW: Why This Matters Now")
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
# 🧪 DEMONSTRATION: OLD VS NEW SEARCH PATTERNS
# ============================================================================

print("\n" + "=" * 70)
print("🧪 DEMONSTRATION: Old vs New Search Patterns")
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
# 🎯 TASK 1: REAL CUSTOMER QUESTIONS
# ============================================================================

print("\n" + "=" * 70)
print("🎯 TASK 1: Real Customer Questions from Your Domain")
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
# 🔍 FROM KEYWORDS TO QUESTIONS
# ============================================================================

print("\n" + "=" * 70)
print("🔍 FROM KEYWORDS TO QUESTIONS")
print("=" * 70)

print("""
🎯 ELI5: If old search was like looking for a book by exact title, 
new search is like asking the librarian "What's a good book for a 
rainy Sunday that's funny and short?"

🔑 IMPLICATIONS FOR TECH TEAMS:

1. **Ranking ≠ solving**
   - Old: Find the most relevant document
   - New: Understand the question and provide an answer

2. **Semantic understanding > exact match**
   - Old: "python tutorial" matches "python tutorial"
   - New: "how to learn python" matches "python tutorial", "beginner guide", etc.

3. **Need for retrieval + reasoning**
   - Old: Find documents, user figures out the answer
   - New: Find documents, AI reasons about them, provides answer

🔄 MINI-EXERCISE: Rewrite a product search flow from your site 
into natural language queries.
""")

# ============================================================================
# 🧪 MINI-EXERCISE: PRODUCT SEARCH FLOW TRANSFORMATION
# ============================================================================

print("\n" + "=" * 70)
print("🧪 MINI-EXERCISE: Product Search Flow Transformation")
print("=" * 70)

def demonstrate_search_flow_transformation():
    """Show how to transform product search flows"""
    
    print("🛒 EXAMPLE: E-commerce Product Search")
    print("-" * 50)
    
    print("OLD FLOW (Keyword-based):")
    print("  1. User types: 'laptop'")
    print("  2. System shows: All laptops")
    print("  3. User filters: Price, brand, etc.")
    print("  4. User browses: Multiple pages")
    print("  5. User decides: Based on limited info")
    
    print("\nNEW FLOW (Natural Language + AI):")
    print("  1. User asks: 'I need a laptop for video editing under $1000'")
    print("  2. AI understands: Purpose, budget, requirements")
    print("  3. AI searches: Relevant products + reviews + specs")
    print("  4. AI reasons: Which options best match needs")
    print("  5. AI presents: Ranked recommendations with explanations")
    
    print("\n🎯 YOUR TURN: Think about a search flow from your domain...")
    print("   How would you transform it from keywords to natural language?")

demonstrate_search_flow_transformation()

# ============================================================================
# 🛠 WHY CLASSIC SEARCH BREAKS
# ============================================================================

print("\n" + "=" * 70)
print("🛠 WHY CLASSIC SEARCH BREAKS — AND MODERN AI PATTERNS")
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
# 🧪 DEMONSTRATION: RAG VS TRADITIONAL SEARCH
# ============================================================================

print("\n" + "=" * 70)
print("🧪 DEMONSTRATION: RAG vs Traditional Search")
print("=" * 70)

def demonstrate_rag_vs_traditional():
    """Demonstrate RAG vs traditional search capabilities"""
    
    query = "What's the best way to learn machine learning if I'm a beginner programmer?"
    
    print(f"🔍 QUERY: {query}")
    print()
    
    print("🔴 TRADITIONAL SEARCH (ElasticSearch):")
    print("-" * 50)
    print("  ❌ Returns: 'machine learning tutorial', 'beginner guide'")
    print("  ❌ Problem: No understanding of 'beginner programmer' context")
    print("  ❌ Result: User has to figure out what's relevant")
    
    print("\n🟢 RAG APPROACH:")
    print("-" * 50)
    print("  ✅ Retrieves: Relevant tutorials, skill assessments, learning paths")
    print("  ✅ Understands: 'beginner programmer' = needs programming basics first")
    print("  ✅ Reasons: ML requires math + programming, suggests prerequisites")
    print("  ✅ Provides: Structured learning path with explanations")
    
    print("\n🎯 KEY DIFFERENCE:")
    print("  Traditional: Find documents, user figures it out")
    print("  RAG: Find documents, AI reasons about them, provides answer")

demonstrate_rag_vs_traditional()

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

In Part 2, you'll learn:
- What makes a system "agentic"
- Types of memory and reasoning
- How agents can use tools and plan
- Real-world agentic system examples
""")

print("\n🎉 Part 1 Complete! Ready for Part 2: Why Agentic Systems Matter?")

# ============================================================================
# 🎯 HANDS-ON PREPARATION
# ============================================================================

print("\n" + "=" * 70)
print("🎯 HANDS-ON PREPARATION")
print("=" * 70)

print("""
💡 BEFORE PART 2, THINK ABOUT:

1. **Your Customer Questions**: Have you written down 3 real questions?
2. **Search Flow Transformation**: How would you change your current search?
3. **RAG Applications**: Where could RAG help in your domain?

🧪 OPTIONAL: Test your current search system with the new query patterns
   to see where it breaks down.

📚 RESOURCES:
- [RAG Paper](https://arxiv.org/abs/2005.11401)
- [RAG-Triad Evaluation](https://arxiv.org/abs/2309.15217)
- [Search Evolution Trends](https://searchengineland.com/)

🚀 See you in Part 2! 🎯
""")
