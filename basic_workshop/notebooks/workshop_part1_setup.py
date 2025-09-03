#!/usr/bin/env python3
"""
🚀 LLM Workshop: Part 1 - Setup and LLM Hello World
Duration: ~45 minutes
Level: Beginner

IMPORTANT: Make sure your virtual environment is activated!
If you haven't set up the environment yet, run: python3 workshop_setup.py
"""

import requests
import json
import os
from typing import Dict, Any

# ============================================================================
# 🔧 SECTION 1: SETUP AND CONFIGURATION
# ============================================================================

print("🎯 LLM WORKSHOP - PART 1: Setup and LLM Hello World")
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
# 🧪 TEST 1: Check Available Models
# ============================================================================

print("\n" + "=" * 60)
print("🧪 TEST 1: Check Available Models")
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
# 🌟 LLM HELLO WORLD: Basic Text Generation
# ============================================================================

print("\n" + "=" * 60)
print("🌟 LLM HELLO WORLD: Basic Text Generation")
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
# 🔄 LLM HELLO WORLD: Chat Completion
# ============================================================================

print("\n" + "=" * 60)
print("🔄 LLM HELLO WORLD: Chat Completion")
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
# 🎯 HANDS-ON EXERCISE
# ============================================================================

print("\n" + "=" * 60)
print("🎯 HANDS-ON EXERCISE")
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
# 📝 SUMMARY
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
