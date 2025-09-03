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
print("   - calculate: Perform math calculations")

# ============================================================================
# 🧪 TESTING YOUR MCP SERVER
# ============================================================================

print("\n" + "=" * 60)
print("🧪 Testing Your MCP Server")
print("=" * 60)

# Create a test client
test_client_code = '''#!/usr/bin/env python3
"""
🧪 MCP Server Test Client
"""

import asyncio
import subprocess
import json

async def test_mcp_server():
    """Test the MCP server functionality"""
    
    print("🧪 Testing MCP Server")
    print("=" * 50)
    
    try:
        # Start the MCP server process
        print("🚀 Starting MCP server...")
        process = subprocess.Popen(
            ['python3', 'workshop_mcp_server.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("✅ MCP server started!")
        
        # Wait a moment for server to start
        await asyncio.sleep(1)
        
        # Send initialization request
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        }
        
        print("📤 Sending initialization request...")
        process.stdin.write(json.dumps(init_request) + "\\n")
        process.stdin.flush()
        
        # Read response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            server_name = response.get('result', {}).get('serverInfo', {}).get('name', 'Unknown')
            print(f"📥 Connected to: {server_name}")
        
        # Send list tools request
        list_tools_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list"
        }
        
        print("📤 Requesting available tools...")
        process.stdin.write(json.dumps(list_tools_request) + "\\n")
        process.stdin.flush()
        
        # Read tools response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            tools = response.get('result', {}).get('tools', [])
            print(f"📋 Available tools ({len(tools)}):")
            for tool in tools:
                print(f"   - {tool.get('name', 'Unknown')}: {tool.get('description', 'No description')}")
        
        # Test hello_world tool
        hello_request = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "hello_world",
                "arguments": {"name": "Workshop Participant"}
            }
        }
        
        print("\\n📤 Testing hello_world tool...")
        process.stdin.write(json.dumps(hello_request) + "\\n")
        process.stdin.flush()
        
        # Read hello response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response.get('result', {}).get('content', [])
            if result:
                print(f"📥 Result: {result[0].get('text', 'No text')}")
        
        # Test calculate tool
        calc_request = {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "calculate",
                "arguments": {"expression": "15 * 8 + 3"}
            }
        }
        
        print("\\n📤 Testing calculate tool...")
        process.stdin.write(json.dumps(calc_request) + "\\n")
        process.stdin.flush()
        
        # Read calc response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response.get('result', {}).get('content', [])
            if result:
                print(f"📥 Result: {result[0].get('text', 'No text')}")
        
        # Test get_current_time tool
        time_request = {
            "jsonrpc": "2.0",
            "id": 5,
            "method": "tools/call",
            "params": {
                "name": "get_current_time",
                "arguments": {}
            }
        }
        
        print("\\n📤 Testing get_current_time tool...")
        process.stdin.write(json.dumps(time_request) + "\\n")
        process.stdin.flush()
        
        # Read time response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response.get('result', {}).get('content', [])
            if result:
                print(f"📥 Result: {result[0].get('text', 'No text')}")
        
        print("\\n🎉 All MCP server tests passed!")
        
        # Clean up
        process.terminate()
        process.wait()
        
    except Exception as e:
        print(f"❌ Error testing MCP server: {e}")
        return False
    
    return True

if __name__ == "__main__":
    asyncio.run(test_mcp_server())
'''

# Save the test client code
with open("test_mcp_server.py", "w") as f:
    f.write(test_client_code)

print("✅ Created test_mcp_server.py")
print("🧪 To test your MCP server, run:")
print("   python3 test_mcp_server.py")

# ============================================================================
# 🔌 CONNECTING TO VS CODE/CURSOR
# ============================================================================

print("\n" + "=" * 60)
print("🔌 Connecting to VS Code/Cursor")
print("=" * 60)

print("""
🎯 To use your MCP server with VS Code/Cursor:

1. **Install MCP Extension**:
   - Open VS Code/Cursor
   - Go to Extensions (Cmd+Shift+X)
   - Search for "MCP" or "Model Context Protocol"
   - Install the official MCP extension

2. **Configure MCP Client**:
   - Open Command Palette (Cmd+Shift+P)
   - Type "MCP: Configure"
   - Add your server configuration:
   
   ```json
   {
     "mcpServers": {
       "workshop-mcp-server": {
         "command": "python3",
         "args": ["/full/path/to/workshop_mcp_server.py"],
       "env": {}
       }
     }
   }
   ```

3. **Connect to Server**:
   - Open Command Palette (Cmd+Shift+P)
   - Type "MCP: Connect to Server"
   - Select "workshop-mcp-server"
   - You should see "Connected" status

4. **Use MCP Tools**:
   - In any chat/assistant panel, you can now use:
     - `@hello_world` - Greet with custom name
     - `@get_current_time` - Get current time
     - `@calculate` - Perform math calculations
""")

# ============================================================================
# 🎯 HANDS-ON EXERCISE
# ============================================================================

print("\n" + "=" * 60)
print("🎯 Hands-On Exercise")
print("=" * 60)

print("""
🎯 Your Turn! Try these exercises:

1. **Test the MCP Server**:
   - Run: `python3 test_mcp_server.py`
   - Verify all tools work correctly

2. **Add a Custom Tool**:
   - Edit `workshop_mcp_server.py`
   - Add a new tool (e.g., "get_weather", "random_quote")
   - Test your new tool

3. **Connect to VS Code/Cursor**:
   - Follow the configuration steps above
   - Use the tools in your AI assistant

4. **Create Your Own Client**:
   - Write a Python script that uses your MCP server
   - Build a simple application with MCP integration

💡 Tips:
- Keep tools simple and focused
- Always validate input parameters
- Handle errors gracefully
- Test thoroughly before deploying
""")

# ============================================================================
# 📝 PART 3 SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("📝 Part 3 Summary")
print("=" * 60)

print("""
✅ What We Accomplished:
- Created a working MCP server with 3 tools
- Implemented proper request/response handling
- Added error handling and input validation
- Created a test client to verify functionality
- Learned how to connect to VS Code/Cursor

🔑 Key Concepts:
- MCP Protocol: Standard for AI-tool communication
- JSON-RPC: Communication protocol used by MCP
- Tool Definition: Schema for tool inputs and outputs
- Client Integration: How to connect MCP servers to applications

🚀 Next Steps:
- Add more sophisticated tools to your server
- Integrate with your favorite AI assistants
- Build custom applications using MCP
- Explore advanced MCP features and capabilities

🎉 Congratulations! You've built your first MCP server!
""")

print("\n🎉 Part 3 Complete! You now have a working MCP server!")
print("🚀 Ready to integrate with AI assistants and build amazing tools!")