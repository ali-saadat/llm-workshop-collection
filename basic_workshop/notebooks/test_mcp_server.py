#!/usr/bin/env python3
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
        process.stdin.write(json.dumps(init_request) + "\n")
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
        process.stdin.write(json.dumps(list_tools_request) + "\n")
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
        
        print("\n📤 Testing hello_world tool...")
        process.stdin.write(json.dumps(hello_request) + "\n")
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
        
        print("\n📤 Testing calculate tool...")
        process.stdin.write(json.dumps(calc_request) + "\n")
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
        
        print("\n📤 Testing get_current_time tool...")
        process.stdin.write(json.dumps(time_request) + "\n")
        process.stdin.flush()
        
        # Read time response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response.get('result', {}).get('content', [])
            if result:
                print(f"📥 Result: {result[0].get('text', 'No text')}")
        
        print("\n🎉 All MCP server tests passed!")
        
        # Clean up
        process.terminate()
        process.wait()
        
    except Exception as e:
        print(f"❌ Error testing MCP server: {e}")
        return False
    
    return True

if __name__ == "__main__":
    asyncio.run(test_mcp_server())
