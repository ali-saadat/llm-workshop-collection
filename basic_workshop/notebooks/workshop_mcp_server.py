#!/usr/bin/env python3
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

