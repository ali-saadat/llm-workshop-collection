#!/usr/bin/env python3
"""
🔍 LangSmith Demo: Observability and Evaluation
Duration: ~20 minutes
Level: Intermediate/Advanced

IMPORTANT: Make sure your virtual environment is activated!
"""

import os
import requests
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# 🔍 LANGSMITH DEMO: OBSERVABILITY AND EVALUATION
# ============================================================================

print("🔍 LANGSMITH DEMO: Observability and Evaluation")
print("=" * 70)
print("Duration: ~20 minutes | Level: Intermediate/Advanced")
print("=" * 70)

# ============================================================================
# 🔑 LANGSMITH CONFIGURATION
# ============================================================================

print("\n🔑 Setting up LangSmith configuration...")

# LangSmith configuration from environment variables
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY", "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")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "pr-candid-passing-65")
LANGSMITH_TRACING_V2 = os.getenv("LANGSMITH_TRACING_V2", "true")

print("✅ LangSmith configuration loaded!")
print(f"🔑 API Key: {LANGSMITH_API_KEY[:10]}...")
print(f"📊 Project: {LANGSMITH_PROJECT}")
print(f"🔍 Tracing: {LANGSMITH_TRACING_V2}")

# ============================================================================
# 🎯 WHAT IS LANGSMITH?
# ============================================================================

print("\n" + "=" * 70)
print("🎯 WHAT IS LANGSMITH?")
print("=" * 70)

print("""
🔍 LANGSMITH: The Observability Platform for LLM Applications

🎯 ELI5: LangSmith is like a CCTV system + notebook for your AI agents.
It watches every step, records mistakes, and helps you improve.

🔑 KEY FEATURES:

1. **Tracing**: Watch every step of your agent's execution
2. **Evaluation**: Test your agents with real data
3. **Debugging**: Find and fix issues quickly
4. **Analytics**: Understand performance and costs
5. **Collaboration**: Share insights with your team

🔄 HOW IT WORKS:

1. **Instrument** your LLM calls with LangSmith
2. **Run** your agents and see every step
3. **Evaluate** with test datasets
4. **Debug** failed runs and slow tools
5. **Improve** based on insights

💡 BUSINESS VALUE:

- **Faster Debugging**: Find issues in minutes, not hours
- **Better Performance**: Optimize based on real data
- **Cost Control**: Track and optimize LLM usage
- **Quality Assurance**: Ensure consistent results
- **Team Collaboration**: Share insights and improvements
""")

# ============================================================================
# 🧪 DEMONSTRATION: LANGSMITH TRACING
# ============================================================================

print("\n" + "=" * 70)
print("🧪 DEMONSTRATION: LangSmith Tracing")
print("=" * 70)

def demonstrate_langsmith_tracing():
    """Demonstrate how LangSmith tracing works"""
    
    print("🔍 LANGSMITH TRACING EXAMPLE:")
    print("-" * 50)
    
    # Simulate a traced agent execution
    execution_steps = [
        {
            "step": "User Input",
            "data": "I need a laptop for video editing under $1000",
            "timestamp": "2024-09-02T18:00:00Z"
        },
        {
            "step": "Tool Selection",
            "data": "Selected: ProductSearchTool, PriceTool, RecommendationTool",
            "timestamp": "2024-09-02T18:00:01Z"
        },
        {
            "step": "Product Search",
            "data": "Found 15 laptops matching criteria",
            "timestamp": "2024-09-02T18:00:02Z"
        },
        {
            "step": "Price Filtering",
            "data": "Filtered to 8 laptops under $1000",
            "timestamp": "2024-09-02T18:00:03Z"
        },
        {
            "step": "Recommendation",
            "data": "Ranked top 3 laptops for video editing",
            "timestamp": "2024-09-02T18:00:04Z"
        },
        {
            "step": "Response Generation",
            "data": "Generated personalized recommendations",
            "timestamp": "2024-09-02T18:00:05Z"
        }
    ]
    
    print("📊 TRACED EXECUTION:")
    for i, step in enumerate(execution_steps, 1):
        print(f"  {i}. {step['step']}")
        print(f"     Data: {step['data']}")
        print(f"     Time: {step['timestamp']}")
        print()
    
    print("🎯 WHAT LANGSMITH SHOWS:")
    print("  ✅ Every step with timing")
    print("  ✅ Input/output data")
    print("  ✅ Tool usage and costs")
    print("  ✅ Error details and stack traces")
    print("  ✅ Performance metrics")

demonstrate_langsmith_tracing()

# ============================================================================
# 📊 LANGSMITH EVALUATION
# ============================================================================

print("\n" + "=" * 70)
print("📊 LANGSMITH EVALUATION")
print("=" * 70)

print("""
🎯 EVALUATION IN LANGSMITH:

1. **RAG-Triad Evaluation**
   - Groundedness: Is the answer based on retrieved facts?
   - Context Relevance: Are the retrieved facts relevant?
   - Answer Relevance: Does the answer address the question?

2. **Custom Metrics**
   - Response time
   - Cost per query
   - User satisfaction
   - Business KPIs

3. **A/B Testing**
   - Compare different prompts
   - Test different models
   - Evaluate tool combinations

4. **Regression Testing**
   - Ensure improvements don't break existing functionality
   - Track performance over time
   - Monitor for drift

💡 EVALUATION EXAMPLE:

Question: "I need a laptop for video editing under $1000"

Evaluation Metrics:
- ✅ Groundedness: 0.95 (answer based on product data)
- ✅ Context Relevance: 0.92 (retrieved relevant laptops)
- ✅ Answer Relevance: 0.98 (directly addresses the question)
- ✅ Response Time: 2.3 seconds
- ✅ Cost: $0.05 per query
- ✅ User Rating: 4.8/5.0
""")

# ============================================================================
# 🛠 LANGSMITH SETUP AND USAGE
# ============================================================================

print("\n" + "=" * 70)
print("🛠 LANGSMITH SETUP AND USAGE")
print("=" * 70)

print("""
🔧 SETUP STEPS:

1. **Get LangSmith API Key**
   - Sign up at https://smith.langchain.com/
   - Create a new project
   - Get your API key

2. **Configure Environment**
   ```bash
   # Add to .env file
   LANGSMITH_API_KEY=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
   LANGSMITH_PROJECT=pr-candid-passing-65
   LANGSMITH_TRACING_V2=true
   ```

3. **Install Dependencies**
   ```bash
   pip install langsmith
   ```

4. **Instrument Your Code**
   ```python
   from langsmith import Client
   from langchain.callbacks import LangChainTracer
   
   # Initialize client
   client = Client(api_key=LANGSMITH_API_KEY)
   
   # Add tracer to your chain
   tracer = LangChainTracer(project_name=LANGSMITH_PROJECT)
   ```

5. **Run and Monitor**
   - Execute your agents
   - View traces in LangSmith dashboard
   - Analyze performance and costs

📊 DASHBOARD FEATURES:

- **Traces**: See every execution step
- **Evaluations**: Test with real data
- **Analytics**: Performance and cost insights
- **Datasets**: Manage test data
- **Prompts**: Version and compare prompts
- **Feedback**: Collect user ratings
""")

# ============================================================================
# 🎯 LANGSMITH USE CASES
# ============================================================================

print("\n" + "=" * 70)
print("🎯 LANGSMITH USE CASES")
print("=" * 70)

print("""
🌍 REAL-WORLD APPLICATIONS:

1. **Customer Service Chatbots**
   - Monitor response quality
   - Track resolution rates
   - Optimize for customer satisfaction
   - A/B test different approaches

2. **E-commerce Recommendation Systems**
   - Evaluate recommendation relevance
   - Track conversion rates
   - Monitor for bias and fairness
   - Optimize for business metrics

3. **Healthcare AI Systems**
   - Ensure medical accuracy
   - Track compliance with guidelines
   - Monitor for safety issues
   - Audit for regulatory requirements

4. **Financial AI Applications**
   - Validate investment advice
   - Track risk assessment accuracy
   - Monitor for regulatory compliance
   - Ensure consistent decision-making

5. **Content Generation Systems**
   - Evaluate content quality
   - Track brand consistency
   - Monitor for inappropriate content
   - Optimize for engagement metrics

💡 BUSINESS BENEFITS:

- **Quality Assurance**: Ensure consistent, high-quality outputs
- **Cost Optimization**: Track and reduce LLM usage costs
- **Risk Management**: Identify and mitigate issues early
- **Performance Improvement**: Data-driven optimization
- **Compliance**: Meet regulatory and audit requirements
""")

# ============================================================================
# 🧪 HANDS-ON EXERCISE
# ============================================================================

print("\n" + "=" * 70)
print("🧪 HANDS-ON EXERCISE")
print("=" * 70)

print("""
🎯 YOUR TASK: Design a LangSmith evaluation strategy for your agentic system.

Think about:
1. **What metrics** would you track?
2. **What test data** would you use?
3. **What evaluations** would you run?
4. **What alerts** would you set up?

Example Framework:

🏥 HEALTHCARE USE CASE:
Metrics: Medical accuracy, response time, compliance rate
Test Data: 1000 patient scenarios with expert annotations
Evaluations: RAG-triad, medical knowledge validation, safety checks
Alerts: Accuracy below 95%, response time above 5s, safety violations

💻 YOUR USE CASE: Fill in the framework below:
""")

# Interactive input for participants
print("📝 Your LangSmith Evaluation Strategy:")
print("Metrics: _________________________________________________")
print("Test Data: _________________________________________________")
print("Evaluations: _________________________________________________")
print("Alerts: _________________________________________________")

# ============================================================================
# 📝 LANGSMITH SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("📝 LANGSMITH SUMMARY")
print("=" * 70)

print("""
✅ WHAT WE COVERED:

1. **LangSmith Overview**
   - Observability platform for LLM applications
   - Tracing, evaluation, debugging, analytics

2. **Key Features**
   - Step-by-step execution tracking
   - RAG-triad and custom evaluations
   - Performance and cost analytics
   - Team collaboration tools

3. **Setup and Usage**
   - API key configuration
   - Code instrumentation
   - Dashboard monitoring

4. **Business Applications**
   - Quality assurance and compliance
   - Cost optimization and performance
   - Risk management and debugging

🎯 KEY INSIGHTS:

- **LangSmith is essential** for production LLM applications
- **Tracing helps debug** complex agent workflows
- **Evaluation ensures quality** and consistency
- **Analytics optimize** performance and costs
- **Collaboration improves** team productivity

🚀 NEXT UP: LangServe for Production Deployment!

In the next demo, you'll learn:
- How to deploy agents as web services
- Multi-channel session handling
- Production scaling and monitoring
- API management and security
""")

print("\n🎉 LangSmith Demo Complete! Ready for LangServe?")

# ============================================================================
# 🎯 NEXT STEPS
# ============================================================================

print("\n" + "=" * 70)
print("🎯 NEXT STEPS")
print("=" * 70)

print("""
💡 TO GET STARTED WITH LANGSMITH:

1. **Sign up** at https://smith.langchain.com/
2. **Create a project** for your use case
3. **Get your API key** and add to .env
4. **Install langsmith**: `pip install langsmith`
5. **Instrument your code** with tracing
6. **Run evaluations** with test data

📚 RESOURCES:
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [LangSmith Tutorials](https://docs.smith.langchain.com/tutorials)
- [Evaluation Guide](https://docs.smith.langchain.com/evaluation)
- [Best Practices](https://docs.smith.langchain.com/best-practices)

🚀 See you in the LangServe demo! 🎯
""")
