#!/usr/bin/env python3
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
