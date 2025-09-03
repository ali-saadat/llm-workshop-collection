#!/usr/bin/env python3
"""
🎯 MCP Server Demo - Practical Usage Examples
"""

import asyncio
import subprocess
import json
import sys

class MCPDemo:
    """MCP Server Demo Class"""
    
    def __init__(self):
        self.process = None
    
    async def start_server(self):
        """Start the MCP server"""
        print("🚀 Starting MCP Server...")
        self.process = subprocess.Popen(
            ['python3', 'working_mcp_server.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        await asyncio.sleep(1)  # Wait for server to start
        print("✅ MCP Server started successfully!")
    
    async def send_request(self, request):
        """Send a request to the MCP server"""
        self.process.stdin.write(json.dumps(request) + "\n")
        self.process.stdin.flush()
        
        response_line = self.process.stdout.readline()
        if response_line:
            return json.loads(response_line.strip())
        return None
    
    async def initialize(self):
        """Initialize the MCP connection"""
        print("\n📡 Initializing MCP connection...")
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "demo-client",
                    "version": "1.0.0"
                }
            }
        }
        
        response = await self.send_request(init_request)
        if response:
            server_name = response.get('result', {}).get('serverInfo', {}).get('name', 'Unknown')
            print(f"✅ Connected to: {server_name}")
    
    async def list_tools(self):
        """List available tools"""
        print("\n📋 Listing available tools...")
        list_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list"
        }
        
        response = await self.send_request(list_request)
        if response:
            tools = response.get('result', {}).get('tools', [])
            print(f"✅ Found {len(tools)} tools:")
            for tool in tools:
                print(f"   - {tool.get('name', 'Unknown')}: {tool.get('description', 'No description')}")
    
    async def demo_hello_world(self):
        """Demo the hello_world tool"""
        print("\n👋 Demo: Hello World Tool")
        print("-" * 30)
        
        # Test with different names
        names = ["Alice", "Bob", "Workshop Participant", "MCP User"]
        
        for name in names:
            request = {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "hello_world",
                    "arguments": {"name": name}
                }
            }
            
            response = await self.send_request(request)
            if response:
                result = response.get('result', {}).get('content', [])
                if result:
                    print(f"   Input: {name}")
                    print(f"   Output: {result[0].get('text', 'No text')}")
                    print()
    
    async def demo_calculator(self):
        """Demo the calculate tool"""
        print("\n🧮 Demo: Calculator Tool")
        print("-" * 30)
        
        # Test various calculations
        expressions = [
            "2 + 2",
            "10 * 5",
            "100 / 4",
            "15 * 8 + 3",
            "(10 + 5) * 2",
            "2^3",  # This should fail
            "sqrt(16)"  # This should fail
        ]
        
        for expr in expressions:
            request = {
                "jsonrpc": "2.0",
                "id": 4,
                "method": "tools/call",
                "params": {
                    "name": "calculate",
                    "arguments": {"expression": expr}
                }
            }
            
            response = await self.send_request(request)
            if response:
                result = response.get('result', {}).get('content', [])
                if result:
                    print(f"   Expression: {expr}")
                    print(f"   Result: {result[0].get('text', 'No text')}")
                    print()
    
    async def demo_time_tool(self):
        """Demo the get_current_time tool"""
        print("\n🕐 Demo: Current Time Tool")
        print("-" * 30)
        
        # Get time multiple times to show it's dynamic
        for i in range(3):
            request = {
                "jsonrpc": "2.0",
                "id": 5,
                "method": "tools/call",
                "params": {
                    "name": "get_current_time",
                    "arguments": {}
                }
            }
            
            response = await self.send_request(request)
            if response:
                result = response.get('result', {}).get('content', [])
                if result:
                    print(f"   Call {i+1}: {result[0].get('text', 'No text')}")
            
            await asyncio.sleep(1)  # Wait 1 second between calls
    
    async def demo_error_handling(self):
        """Demo error handling"""
        print("\n❌ Demo: Error Handling")
        print("-" * 30)
        
        # Test unknown tool
        request = {
            "jsonrpc": "2.0",
            "id": 6,
            "method": "tools/call",
            "params": {
                "name": "unknown_tool",
                "arguments": {}
            }
        }
        
        response = await self.send_request(request)
        if response:
            result = response.get('result', {}).get('content', [])
            if result:
                print(f"   Unknown tool result: {result[0].get('text', 'No text')}")
        
        # Test invalid calculation
        request = {
            "jsonrpc": "2.0",
            "id": 7,
            "method": "tools/call",
            "params": {
                "name": "calculate",
                "arguments": {"expression": "import os; os.system('ls')"}
            }
        }
        
        response = await self.send_request(request)
        if response:
            result = response.get('result', {}).get('content', [])
            if result:
                print(f"   Invalid expression result: {result[0].get('text', 'No text')}")
    
    async def stop_server(self):
        """Stop the MCP server"""
        if self.process:
            print("\n🛑 Stopping MCP Server...")
            self.process.terminate()
            self.process.wait()
            print("✅ MCP Server stopped")
    
    async def run_demo(self):
        """Run the complete demo"""
        print("🎯 MCP SERVER DEMO")
        print("=" * 50)
        
        try:
            # Start server
            await self.start_server()
            
            # Initialize connection
            await self.initialize()
            
            # List tools
            await self.list_tools()
            
            # Demo each tool
            await self.demo_hello_world()
            await self.demo_calculator()
            await self.demo_time_tool()
            await self.demo_error_handling()
            
            print("\n🎉 MCP Server Demo Completed Successfully!")
            print("\n📚 Next Steps:")
            print("   1. Integrate with VS Code/Cursor using MCP extension")
            print("   2. Add custom tools to the server")
            print("   3. Create your own MCP clients")
            print("   4. Deploy as a service for team use")
            
        except Exception as e:
            print(f"❌ Demo error: {e}")
        finally:
            await self.stop_server()

async def main():
    """Main entry point"""
    demo = MCPDemo()
    await demo.run_demo()

if __name__ == "__main__":
    asyncio.run(main())
