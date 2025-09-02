#!/usr/bin/env python3
"""
🚀 LLM Workshop: Part 3 - MCP Server Development
Duration: ~45 minutes
Level: Beginner

IMPORTANT: Make sure your virtual environment is activated!
If you haven't set up the environment yet, run: python3 workshop_setup.py
"""

import json
import asyncio
import subprocess
import sys
from typing import Any, Dict, List, Optional
from datetime import datetime

# ============================================================================
# 🔧 SECTION 3: MCP SERVER DEVELOPMENT
# ============================================================================

print("🎯 LLM WORKSHOP - PART 3: MCP Server Development")
print("=" * 60)

# ============================================================================
# 📚 WHAT IS MCP?
# ============================================================================

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
# 🛠️ INSTALLING MCP REQUIREMENTS
# ============================================================================

print("\n" + "=" * 60)
print("🛠️ Installing MCP Requirements")
print("=" * 60)

def install_mcp_requirements():
    """Install required packages for MCP development"""
    packages = [
        "mcp",
        "mcp-server-stdio",
        "mcp-client-stdio"
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
print("   pip install mcp mcp-server-stdio mcp-client-stdio")

# ============================================================================
# 🚀 CREATING YOUR FIRST MCP SERVER
# ============================================================================

print("\n" + "=" * 60)
print("🚀 Creating Your First MCP Server")
print("=" * 60)

# Create a simple MCP server
mcp_server_code = '''#!/usr/bin/env python3
"""
🎯 Simple MCP Server - Hello World
This server provides basic tools for demonstration
"""

import asyncio
import json
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource, TextContent, ImageContent, EmbeddedResource,
    LoggingLevel, Prompt, PromptSegment, Tool, TextContent
)

# Create our MCP server
server = Server("workshop-mcp-server")

# ============================================================================
# 🛠️ TOOL 1: Hello World Tool
# ============================================================================

@server.list_tools()
async def list_tools() -> List[Tool]:
    """List all available tools"""
    return [
        Tool(
            name="hello_world",
            description="A simple hello world tool that greets the user",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Your name (optional)"
                    }
                }
            }
        ),
        Tool(
            name="get_current_time",
            description="Get the current date and time",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="calculate_simple",
            description="Perform simple math calculations",
            inputSchema={
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression like '2 + 2' or '10 * 5'"
                    }
                },
                "required": ["expression"]
            }
        )
    ]

# ============================================================================
# 🎯 TOOL IMPLEMENTATIONS
# ============================================================================

@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Execute the requested tool"""
    
    if name == "hello_world":
        name = arguments.get("name", "there")
        message = f"Hello {name}! 👋 Welcome to your first MCP server!"
        return [TextContent(type="text", text=message)]
    
    elif name == "get_current_time":
        from datetime import datetime
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"🕐 Current time: {current_time}"
        return [TextContent(type="text", text=message)]
    
    elif name == "calculate_simple":
        expression = arguments.get("expression", "")
        try:
            # Simple and safe evaluation
            allowed_chars = set('0123456789+-*/.() ')
            if not all(c in allowed_chars for c in expression):
                return [TextContent(type="text", text="❌ Error: Only basic math operations allowed")]
            
            result = eval(expression)
            message = f"🧮 {expression} = {result}"
            return [TextContent(type="text", text=message)]
        except Exception as e:
            return [TextContent(type="text", text=f"❌ Error calculating {expression}: {str(e)}")]
    
    else:
        return [TextContent(type="text", text=f"❌ Unknown tool: {name}")]

# ============================================================================
# 🚀 SERVER STARTUP
# ============================================================================

async def main():
    """Start the MCP server"""
    print("🚀 Starting MCP Server...", file=sys.stderr)
    print("📋 Available tools:", file=sys.stderr)
    print("   - hello_world: Greet the user", file=sys.stderr)
    print("   - get_current_time: Get current time", file=sys.stderr)
    print("   - calculate_simple: Do math calculations", file=sys.stderr)
    print("🔌 Server ready for connections!", file=sys.stderr)
    
    # Start the server
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="workshop-mcp-server",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=None,
                    experimental_capabilities={}
                )
            )
        )

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
# 🧪 TESTING YOUR MCP SERVER
# ============================================================================

print("\n" + "=" * 60)
print("🧪 Testing Your MCP Server")
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
# 🔌 CONNECTING FROM VS CODE/CURSOR
# ============================================================================

print("\n" + "=" * 60)
print("🔌 Connecting from VS Code/Cursor")
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
# 🎯 HANDS-ON EXERCISE
# ============================================================================

print("\n" + "=" * 60)
print("🎯 HANDS-ON EXERCISE")
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
# 🔍 ADVANCED MCP FEATURES
# ============================================================================

print("\n" + "=" * 60)
print("🔍 Advanced MCP Features")
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
# 📝 SUMMARY
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
print("\n🌟 **WORKSHOP COMPLETE!** 🌟")
print("You've learned LLM basics, agents, and MCP servers!")
print("Time to build something amazing! 🚀")
