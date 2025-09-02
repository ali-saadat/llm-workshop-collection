#!/usr/bin/env python3
"""
🧪 Test Script for Custom Tools
This script tests the custom tools independently to ensure they work correctly
"""

from workshop_part2_agents import CalculatorTool, WeatherTool, TimeTool

def test_calculator_tool():
    """Test the calculator tool"""
    print("🧮 Testing Calculator Tool")
    print("-" * 30)
    
    tool = CalculatorTool()
    
    # Test basic operations
    test_cases = [
        "2 + 2",
        "10 * 5",
        "100 - 25",
        "15 / 3",
        "(5 + 3) * 2"
    ]
    
    for test_case in test_cases:
        try:
            result = tool._run(test_case)
            print(f"✅ {test_case} = {result}")
        except Exception as e:
            print(f"❌ {test_case}: {e}")
    
    print()

def test_weather_tool():
    """Test the weather tool"""
    print("🌤️ Testing Weather Tool")
    print("-" * 30)
    
    tool = WeatherTool()
    
    # Test cities
    test_cities = ["London", "New York", "Tokyo", "Sydney", "Paris"]
    
    for city in test_cities:
        try:
            result = tool._run(city)
            print(f"✅ {city}: {result}")
        except Exception as e:
            print(f"❌ {city}: {e}")
    
    print()

def test_time_tool():
    """Test the time tool"""
    print("⏰ Testing Time Tool")
    print("-" * 30)
    
    tool = TimeTool()
    
    try:
        result = tool._run("")
        print(f"✅ {result}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print()

def main():
    """Run all tests"""
    print("🚀 Testing Custom Tools")
    print("=" * 50)
    print()
    
    test_calculator_tool()
    test_weather_tool()
    test_time_tool()
    
    print("🎉 All tool tests completed!")
    print("\n💡 If all tests passed, your tools are working correctly!")
    print("🚀 You can now use them with LangChain agents!")

if __name__ == "__main__":
    main()
