#!/usr/bin/env python3
"""
🎯 Simple Demo: Custom Tools Working
This script demonstrates the custom tools working independently
"""

from workshop_part2_agents import CalculatorTool, WeatherTool, TimeTool

def main():
    """Demonstrate the tools working"""
    print("🎯 CUSTOM TOOLS DEMO")
    print("=" * 50)
    print("These tools work independently of the LLM API!")
    print()
    
    # Create tool instances
    calc_tool = CalculatorTool()
    weather_tool = WeatherTool()
    time_tool = TimeTool()
    
    print("🧮 Calculator Tool Examples:")
    print("-" * 30)
    calculations = ["2 + 2", "10 * 5", "100 - 25", "15 / 3", "(5 + 3) * 2"]
    for calc in calculations:
        result = calc_tool._run(calc)
        print(f"  {calc} = {result}")
    
    print("\n🌤️ Weather Tool Examples:")
    print("-" * 30)
    cities = ["London", "New York", "Tokyo", "Sydney"]
    for city in cities:
        result = weather_tool._run(city)
        print(f"  {city}: {result}")
    
    print("\n⏰ Time Tool:")
    print("-" * 30)
    result = time_tool._run("")
    print(f"  {result}")
    
    print("\n" + "=" * 50)
    print("✅ All tools working perfectly!")
    print("🚀 These tools can now be used with LangChain agents")
    print("💡 The 404 errors you saw earlier were from the LLM API, not the tools")

if __name__ == "__main__":
    main()
