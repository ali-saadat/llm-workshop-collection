#!/usr/bin/env python3
"""
🚀 LLM Workshop Setup Script
This script sets up your virtual environment and installs all dependencies
"""

import os
import sys
import subprocess
import platform

def print_header():
    """Print workshop header"""
    print("🚀 LLM WORKSHOP SETUP")
    print("=" * 50)
    print("Setting up your development environment...")
    print()

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def create_virtual_environment():
    """Create and activate virtual environment"""
    venv_name = "llm_workshop_env"
    
    if os.path.exists(venv_name):
        print(f"✅ Virtual environment '{venv_name}' already exists")
        return venv_name
    
    print(f"🔧 Creating virtual environment: {venv_name}")
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
        print(f"✅ Virtual environment created successfully")
        return venv_name
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return None

def get_activation_command(venv_name):
    """Get the activation command for the virtual environment"""
    system = platform.system().lower()
    
    if system == "windows":
        return f"{venv_name}\\Scripts\\activate"
    else:  # macOS/Linux
        return f"source {venv_name}/bin/activate"

def install_requirements(venv_name):
    """Install required packages in the virtual environment"""
    print("\n📦 Installing required packages...")
    
    # Get the pip path in the virtual environment
    if platform.system().lower() == "windows":
        pip_path = os.path.join(venv_name, "Scripts", "pip")
    else:
        pip_path = os.path.join(venv_name, "bin", "pip")
    
    # Install packages one by one to handle errors gracefully
    packages = [
        "requests>=2.31.0",
        "openai>=1.0.0", 
        "langchain>=0.1.0",
        "langchain-openai>=0.0.5",
        "python-dotenv>=1.0.0"
    ]
    
    failed_packages = []
    
    for package in packages:
        try:
            print(f"   Installing {package}...")
            subprocess.run([pip_path, "install", package], check=True, capture_output=True)
            print(f"   ✅ {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Failed to install {package}")
            failed_packages.append(package)
    
    # Try to install MCP packages (these might fail on some systems)
    mcp_packages = [
        "mcp>=1.0.0",
        "mcp-server-stdio>=1.0.0", 
        "mcp-client-stdio>=1.0.0"
    ]
    
    print("\n🔌 Installing MCP packages (optional for basic workshop)...")
    for package in mcp_packages:
        try:
            print(f"   Installing {package}...")
            subprocess.run([pip_path, "install", package], check=True, capture_output=True)
            print(f"   ✅ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"   ⚠️  {package} failed to install (MCP features will be limited)")
            failed_packages.append(package)
    
    return failed_packages

def print_next_steps(venv_name, failed_packages):
    """Print next steps for the user"""
    activation_cmd = get_activation_command(venv_name)
    
    print("\n" + "=" * 50)
    print("🎉 SETUP COMPLETE!")
    print("=" * 50)
    
    print(f"\n✅ Virtual environment created: {venv_name}")
    
    if failed_packages:
        print(f"\n⚠️  Some packages failed to install: {', '.join(failed_packages)}")
        print("   You can try installing them manually later")
    
    print(f"\n🚀 To start working on the workshop:")
    print(f"   1. Activate your virtual environment:")
    print(f"      {activation_cmd}")
    print(f"   2. Run the workshop parts:")
    print(f"      python workshop_part1_setup.py")
    print(f"      python workshop_part2_agents.py") 
    print(f"      python workshop_part3_mcp_server.py")
    
    print(f"\n💡 If you're using VS Code/Cursor:")
    print(f"   1. Open the command palette (Cmd+Shift+P)")
    print(f"   2. Type 'Python: Select Interpreter'")
    print(f"   3. Choose the interpreter from: {venv_name}/bin/python")
    
    print(f"\n📚 Check README.md for detailed workshop instructions!")
    print(f"\n🎯 Happy coding! 🚀")

def main():
    """Main setup function"""
    print_header()
    
    # Check Python version
    if not check_python_version():
        return
    
    # Create virtual environment
    venv_name = create_virtual_environment()
    if not venv_name:
        return
    
    # Install requirements
    failed_packages = install_requirements(venv_name)
    
    # Print next steps
    print_next_steps(venv_name, failed_packages)

if __name__ == "__main__":
    main()
