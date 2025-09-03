# 🎯 MCP Server - Complete Client Instructions

## 🚀 **MCP Server Successfully Running!**

Your MCP server is working perfectly with the following tools:
- ✅ **hello_world**: Greet users with custom names
- ✅ **get_current_time**: Get current date and time
- ✅ **calculate**: Perform mathematical calculations

---

## 📋 **How to Use MCP Server as Client**

### **Method 1: VS Code/Cursor Integration**

#### **Step 1: Install MCP Extension**
1. Open VS Code or Cursor
2. Go to Extensions (Cmd+Shift+X)
3. Search for "MCP" or "Model Context Protocol"
4. Install the official MCP extension

#### **Step 2: Configure MCP Client**
1. Open Command Palette (Cmd+Shift+P)
2. Type "MCP: Configure"
3. Add your server configuration:

```json
{
  "mcpServers": {
    "workshop-mcp-server": {
      "command": "python3",
      "args": ["/Users/asaadat/Documents/dds workshop/new/working_mcp_server.py"],
      "env": {}
    }
  }
}
```

#### **Step 3: Connect to Server**
1. Open Command Palette (Cmd+Shift+P)
2. Type "MCP: Connect to Server"
3. Select "workshop-mcp-server"
4. You should see "Connected" status

#### **Step 4: Use MCP Tools**
1. In any chat/assistant panel, you can now use:
   - `@hello_world` - Greet with custom name
   - `@get_current_time` - Get current time
   - `@calculate` - Perform math calculations

---

### **Method 2: Direct Command Line Testing**

#### **Test Individual Tools**
```bash
# Test hello_world
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "hello_world", "arguments": {"name": "Your Name"}}}' | python3 working_mcp_server.py

# Test calculate
echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "calculate", "arguments": {"expression": "2 + 2"}}}' | python3 working_mcp_server.py

# Test get_current_time
echo '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "get_current_time", "arguments": {}}}' | python3 working_mcp_server.py
```

#### **Interactive Testing**
```bash
# Start the server
python3 working_mcp_server.py

# In another terminal, send requests:
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}}' | nc localhost 8000
```

---

### **Method 3: Python Client Integration**

#### **Create Your Own MCP Client**
```python
#!/usr/bin/env python3
import asyncio
import subprocess
import json

class MCPClient:
    def __init__(self, server_script):
        self.server_script = server_script
        self.process = None
    
    async def start(self):
        """Start the MCP server"""
        self.process = subprocess.Popen(
            ['python3', self.server_script],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        await asyncio.sleep(1)  # Wait for server to start
    
    async def call_tool(self, tool_name, arguments=None):
        """Call a tool on the MCP server"""
        if arguments is None:
            arguments = {}
        
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            }
        }
        
        self.process.stdin.write(json.dumps(request) + "\n")
        self.process.stdin.flush()
        
        response_line = self.process.stdout.readline()
        response = json.loads(response_line.strip())
        
        return response.get('result', {}).get('content', [{}])[0].get('text', '')
    
    async def stop(self):
        """Stop the MCP server"""
        if self.process:
            self.process.terminate()
            self.process.wait()

# Usage example
async def main():
    client = MCPClient('working_mcp_server.py')
    await client.start()
    
    # Test tools
    result1 = await client.call_tool('hello_world', {'name': 'Python User'})
    print(f"Hello: {result1}")
    
    result2 = await client.call_tool('calculate', {'expression': '10 * 5'})
    print(f"Calculation: {result2}")
    
    result3 = await client.call_tool('get_current_time')
    print(f"Time: {result3}")
    
    await client.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🔧 **Advanced Usage**

### **Custom Tool Development**
To add your own tools to the MCP server:

1. **Edit `working_mcp_server.py`**
2. **Add tool definition** in the `__init__` method:
```python
"my_custom_tool": {
    "description": "My custom tool description",
    "inputSchema": {
        "type": "object",
        "properties": {
            "param1": {
                "type": "string",
                "description": "Parameter description"
            }
        }
    }
}
```

3. **Add tool execution** in the `execute_tool` method:
```python
elif tool_name == "my_custom_tool":
    param1 = arguments.get("param1", "")
    return f"Custom tool result: {param1}"
```

### **Error Handling**
The server includes built-in error handling for:
- Invalid tool names
- Malformed requests
- Calculation errors
- JSON parsing errors

### **Security Considerations**
- The `calculate` tool only allows basic mathematical expressions
- No file system access or system commands
- Input validation for all parameters

---

## 🎯 **Real-World Use Cases**

### **1. Development Assistant**
```python
# Calculate project metrics
result = await client.call_tool('calculate', {'expression': '1000 * 0.15'})
print(f"15% of 1000: {result}")
```

### **2. Time Management**
```python
# Get current time for logging
result = await client.call_tool('get_current_time')
print(f"Operation completed at: {result}")
```

### **3. User Interaction**
```python
# Greet users in applications
result = await client.call_tool('hello_world', {'name': 'John Doe'})
print(f"Welcome message: {result}")
```

---

## 🚀 **Next Steps**

1. **Integrate with VS Code/Cursor** using the MCP extension
2. **Add more tools** to the server for your specific needs
3. **Deploy the server** as a service for team use
4. **Create custom clients** for your applications
5. **Add authentication** for production use

---

## 🎉 **Success!**

Your MCP server is now fully functional and ready for integration with:
- ✅ VS Code/Cursor MCP extensions
- ✅ Custom Python applications
- ✅ Command-line tools
- ✅ Web applications
- ✅ AI assistants

**The MCP server provides a bridge between AI models and your local tools, enabling powerful automation and integration capabilities!** 🚀
