#!/usr/bin/env python3
"""
🌐 LangServe Demo: Production Deployment
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
# 🌐 LANGSERVE DEMO: PRODUCTION DEPLOYMENT
# ============================================================================

print("🌐 LANGSERVE DEMO: Production Deployment")
print("=" * 70)
print("Duration: ~20 minutes | Level: Intermediate/Advanced")
print("=" * 70)

# ============================================================================
# 🔑 LANGSERVE CONFIGURATION
# ============================================================================

print("\n🔑 Setting up LangServe configuration...")

# LangServe configuration from environment variables
BASE_URL = os.getenv("BASE_URL", "https://yylh5vmmm0.execute-api.eu-central-1.amazonaws.com/prod")
API_KEY = os.getenv("API_KEY", "ALI-CLASS-2025")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-3.5-turbo")
DEPLOYMENT_PORT = os.getenv("DEPLOYMENT_PORT", "8000")
DEPLOYMENT_HOST = os.getenv("DEPLOYMENT_HOST", "0.0.0.0")

print("✅ LangServe configuration loaded!")
print(f"🌐 Base URL: {BASE_URL}")
print(f"🔑 API Key: {API_KEY[:10]}...")
print(f"🤖 Default Model: {DEFAULT_MODEL}")
print(f"🚀 Deployment Host: {DEPLOYMENT_HOST}")
print(f"🔌 Deployment Port: {DEPLOYMENT_PORT}")

# ============================================================================
# 🎯 WHAT IS LANGSERVE?
# ============================================================================

print("\n" + "=" * 70)
print("🎯 WHAT IS LANGSERVE?")
print("=" * 70)

print("""
🌐 LANGSERVE: Production Deployment for LangChain Applications

🎯 ELI5: LangServe is like turning your Lego creation into a web service
that others can use. It wraps your agent in a FastAPI server with
automatic API documentation, authentication, and scaling.

🔑 KEY FEATURES:

1. **FastAPI Integration**: Automatic REST API generation
2. **Multi-Channel Support**: Web, WhatsApp, mobile, etc.
3. **Session Management**: Handle user conversations
4. **Authentication**: Secure your endpoints
5. **Scaling**: Handle multiple users and requests
6. **Monitoring**: Built-in observability and logging

🔄 HOW IT WORKS:

1. **Wrap** your LangChain agent/graph with LangServe
2. **Deploy** as a FastAPI web service
3. **Handle** multiple user sessions
4. **Scale** with load balancers and containers
5. **Monitor** with built-in observability

💡 BUSINESS VALUE:

- **Rapid Deployment**: Go from prototype to production in minutes
- **Multi-Channel**: Serve web, mobile, and messaging platforms
- **Scalability**: Handle thousands of concurrent users
- **Security**: Built-in authentication and rate limiting
- **Monitoring**: Track usage, performance, and costs
""")

# ============================================================================
# 🧪 DEMONSTRATION: LANGSERVE DEPLOYMENT
# ============================================================================

print("\n" + "=" * 70)
print("🧪 DEMONSTRATION: LangServe Deployment")
print("=" * 70)

def demonstrate_langserve_deployment():
    """Demonstrate how LangServe deployment works"""
    
    print("🌐 LANGSERVE DEPLOYMENT EXAMPLE:")
    print("-" * 50)
    
    # Simulate deployment steps
    deployment_steps = [
        {
            "step": "1. Create Agent",
            "description": "Build your LangChain agent with tools and memory",
            "code": "agent = create_agent_with_tools()"
        },
        {
            "step": "2. Wrap with LangServe",
            "description": "Convert agent to FastAPI service",
            "code": "app = FastAPI()\nadd_routes(app, agent)"
        },
        {
            "step": "3. Add Authentication",
            "description": "Secure your endpoints",
            "code": "app.add_middleware(AuthMiddleware)"
        },
        {
            "step": "4. Deploy",
            "description": "Launch as web service",
            "code": f"uvicorn app:app --host {DEPLOYMENT_HOST} --port {DEPLOYMENT_PORT}"
        },
        {
            "step": "5. Test API",
            "description": "Verify endpoints work",
            "code": f"curl -X POST http://localhost:{DEPLOYMENT_PORT}/invoke -d '{{\"input\": \"Hello\"}}'"
        }
    ]
    
    print("📊 DEPLOYMENT STEPS:")
    for step in deployment_steps:
        print(f"\n{step['step']}")
        print(f"   Description: {step['description']}")
        print(f"   Code: {step['code']}")
    
    print("\n🎯 WHAT YOU GET:")
    print("  ✅ REST API with automatic documentation")
    print("  ✅ Session management for conversations")
    print("  ✅ Authentication and rate limiting")
    print("  ✅ Health checks and monitoring")
    print("  ✅ Easy scaling with containers")

demonstrate_langserve_deployment()

# ============================================================================
# 🔧 LANGSERVE SETUP AND USAGE
# ============================================================================

print("\n" + "=" * 70)
print("🔧 LANGSERVE SETUP AND USAGE")
print("=" * 70)

print("""
🛠 SETUP STEPS:

1. **Install Dependencies**
   ```bash
   pip install langserve fastapi uvicorn
   ```

2. **Create Your Agent**
   ```python
   from langchain.agents import create_agent
   from langchain.tools import Tool
   
   # Create your agent with tools
   agent = create_agent(llm, tools, memory)
   ```

3. **Wrap with LangServe**
   ```python
   from fastapi import FastAPI
   from langserve import add_routes
   
   app = FastAPI(title="My Agent API")
   add_routes(app, agent, path="/agent")
   ```

4. **Add Middleware (Optional)**
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

5. **Deploy**
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

📊 AUTOMATIC API FEATURES:

- **OpenAPI Documentation**: Available at `/docs`
- **Health Checks**: Available at `/health`
- **Session Management**: Automatic conversation tracking
- **Error Handling**: Graceful error responses
- **Request Validation**: Automatic input validation
- **Response Serialization**: JSON responses
""")

# ============================================================================
# 🌍 MULTI-CHANNEL DEPLOYMENT
# ============================================================================

print("\n" + "=" * 70)
print("🌍 MULTI-CHANNEL DEPLOYMENT")
print("=" * 70)

print("""
🎯 MULTI-CHANNEL SUPPORT:

LangServe makes it easy to deploy your agent across multiple channels:

1. **Web Application**
   ```python
   # Frontend calls your API
   fetch('/agent/invoke', {
     method: 'POST',
     body: JSON.stringify({input: userMessage})
   })
   ```

2. **Mobile App**
   ```python
   # Mobile app calls same API
   requests.post('/agent/invoke', json={'input': userMessage})
   ```

3. **WhatsApp Integration**
   ```python
   # WhatsApp webhook calls your API
   @app.post("/whatsapp/webhook")
   def whatsapp_webhook(message):
       response = agent.invoke({"input": message.text})
       send_whatsapp_message(message.from_user, response)
   ```

4. **Slack Bot**
   ```python
   # Slack app calls your API
   @app.post("/slack/command")
   def slack_command(command):
       response = agent.invoke({"input": command.text})
       return {"text": response}
   ```

5. **Voice Assistant**
   ```python
   # Voice app calls your API
   @app.post("/voice/process")
   def voice_process(audio):
       text = speech_to_text(audio)
       response = agent.invoke({"input": text})
       return text_to_speech(response)
   ```

💡 BENEFITS:

- **Single Codebase**: One agent serves all channels
- **Consistent Experience**: Same logic across platforms
- **Easy Maintenance**: Update once, deploy everywhere
- **Cost Effective**: Shared infrastructure and resources
""")

# ============================================================================
# 🔒 PRODUCTION CONSIDERATIONS
# ============================================================================

print("\n" + "=" * 70)
print("🔒 PRODUCTION CONSIDERATIONS")
print("=" * 70)

print("""
🛡️ PRODUCTION READINESS:

1. **Authentication & Authorization**
   ```python
   from fastapi import Depends, HTTPException
   from fastapi.security import HTTPBearer
   
   security = HTTPBearer()
   
   def verify_token(token: str = Depends(security)):
       if not validate_token(token.credentials):
           raise HTTPException(status_code=401)
       return token.credentials
   
   @app.post("/agent/invoke")
   def invoke_agent(input_data: dict, token: str = Depends(verify_token)):
       return agent.invoke(input_data)
   ```

2. **Rate Limiting**
   ```python
   from slowapi import Limiter, _rate_limit_exceeded_handler
   from slowapi.util import get_remote_address
   
   limiter = Limiter(key_func=get_remote_address)
   app.state.limiter = limiter
   
   @app.post("/agent/invoke")
   @limiter.limit("10/minute")
   def invoke_agent(request: Request, input_data: dict):
       return agent.invoke(input_data)
   ```

3. **Error Handling**
   ```python
   from fastapi import HTTPException
   
   @app.exception_handler(Exception)
   async def global_exception_handler(request: Request, exc: Exception):
       logger.error(f"Global exception: {exc}")
       return JSONResponse(
           status_code=500,
           content={"error": "Internal server error"}
       )
   ```

4. **Monitoring & Logging**
   ```python
   import logging
   from fastapi import Request
   
   @app.middleware("http")
   async def log_requests(request: Request, call_next):
       start_time = time.time()
       response = await call_next(request)
       process_time = time.time() - start_time
       
       logger.info(f"{request.method} {request.url} - {response.status_code} - {process_time:.3f}s")
       return response
   ```

5. **Health Checks**
   ```python
   @app.get("/health")
   def health_check():
       return {"status": "healthy", "timestamp": datetime.now()}
   
   @app.get("/health/ready")
   def readiness_check():
       # Check database, external services, etc.
       return {"status": "ready"}
   ```

6. **Scaling with Docker**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   EXPOSE 8000
   
   CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
   ```
""")

# ============================================================================
# 🎯 LANGSERVE USE CASES
# ============================================================================

print("\n" + "=" * 70)
print("🎯 LANGSERVE USE CASES")
print("=" * 70)

print("""
🌍 REAL-WORLD APPLICATIONS:

1. **Customer Service Platform**
   - Web chat widget
   - Mobile app integration
   - WhatsApp Business API
   - Slack workspace bot
   - Voice assistant integration

2. **E-commerce Assistant**
   - Product recommendation API
   - Shopping cart assistance
   - Order tracking bot
   - Customer support chatbot
   - Voice shopping assistant

3. **Healthcare Portal**
   - Patient symptom checker
   - Appointment scheduling
   - Medication reminders
   - Health education bot
   - Telemedicine assistant

4. **Financial Services**
   - Investment advisor API
   - Budget planning assistant
   - Fraud detection system
   - Customer onboarding bot
   - Voice banking assistant

5. **Educational Platform**
   - Tutoring assistant API
   - Homework help bot
   - Course recommendation system
   - Student support chatbot
   - Voice learning assistant

💡 BUSINESS BENEFITS:

- **Rapid Deployment**: From prototype to production in hours
- **Multi-Channel Reach**: Serve customers wherever they are
- **Scalable Infrastructure**: Handle growth automatically
- **Cost Effective**: Shared resources across channels
- **Easy Maintenance**: Single codebase for all platforms
""")

# ============================================================================
# 🧪 HANDS-ON EXERCISE
# ============================================================================

print("\n" + "=" * 70)
print("🧪 HANDS-ON EXERCISE")
print("=" * 70)

print("""
🎯 YOUR TASK: Design a LangServe deployment strategy for your agentic system.

Think about:
1. **What channels** would you support?
2. **What authentication** would you need?
3. **What scaling** requirements do you have?
4. **What monitoring** would you implement?

Example Framework:

🏥 HEALTHCARE USE CASE:
Channels: Web portal, mobile app, WhatsApp, voice assistant
Authentication: OAuth2 with patient data access controls
Scaling: Auto-scaling based on patient volume
Monitoring: Response time, accuracy, compliance tracking

💻 YOUR USE CASE: Fill in the framework below:
""")

# Interactive input for participants
print("📝 Your LangServe Deployment Strategy:")
print("Channels: _________________________________________________")
print("Authentication: _________________________________________________")
print("Scaling: _________________________________________________")
print("Monitoring: _________________________________________________")

# ============================================================================
# 📝 LANGSERVE SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("📝 LANGSERVE SUMMARY")
print("=" * 70)

print("""
✅ WHAT WE COVERED:

1. **LangServe Overview**
   - Production deployment for LangChain applications
   - FastAPI integration with automatic API generation

2. **Key Features**
   - Multi-channel support (web, mobile, messaging)
   - Session management and authentication
   - Automatic scaling and monitoring

3. **Setup and Usage**
   - Simple agent wrapping with LangServe
   - FastAPI deployment and configuration
   - Production-ready middleware and security

4. **Business Applications**
   - Customer service platforms
   - E-commerce assistants
   - Healthcare and financial services
   - Educational and enterprise applications

🎯 KEY INSIGHTS:

- **LangServe simplifies** production deployment
- **Multi-channel support** maximizes reach
- **Built-in features** handle common production needs
- **Easy scaling** supports business growth
- **Security and monitoring** ensure reliability

🚀 READY FOR PRODUCTION!

You now have the complete LangChain ecosystem:
- **LangChain**: Build agents and tools
- **LangGraph**: Create complex workflows
- **LangSmith**: Monitor and evaluate
- **LangServe**: Deploy to production
""")

print("\n🎉 LangServe Demo Complete! Ready for Production!")

# ============================================================================
# 🎯 NEXT STEPS
# ============================================================================

print("\n" + "=" * 70)
print("🎯 NEXT STEPS")
print("=" * 70)

print("""
💡 TO GET STARTED WITH LANGSERVE:

1. **Install dependencies**: `pip install langserve fastapi uvicorn`
2. **Create your agent** with LangChain/LangGraph
3. **Wrap with LangServe** and add routes
4. **Add middleware** for authentication and monitoring
5. **Deploy locally** with `uvicorn app:app --host 0.0.0.0 --port 8000`
6. **Test your API** at `http://localhost:8000/docs`
7. **Deploy to production** with Docker/cloud services

📚 RESOURCES:
- [LangServe Documentation](https://python.langchain.com/docs/langserve/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Deployment Guide](https://python.langchain.com/docs/langserve/deploy/)
- [Best Practices](https://python.langchain.com/docs/langserve/best-practices/)

🚀 You're ready to build and deploy production AI systems! 🎯
""")
