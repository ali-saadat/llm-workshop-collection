# ⚡ Quick Start Guide

**Get up and running in 5 minutes!**

## 🚀 Fast Setup

1. **Run the setup script:**
   ```bash
   cd basic_workshop/scripts
   python3 workshop_setup.py
   ```

2. **Start the workshop:**
   ```bash
   # Make sure virtual environment is activated
   source llm_workshop_env/bin/activate
   
   # Open the master notebook
   cd basic_workshop/notebooks
   # Open workshop_master.ipynb in VS Code/Cursor
   ```

## 🔧 What the Setup Script Does

- ✅ Creates a virtual environment (`llm_workshop_env`)
- ✅ Installs all required packages
- ✅ Handles macOS "externally-managed-environment" errors
- ✅ Tests your API connection
- ✅ Provides clear next steps

## 🎯 Workshop Parts

- **Part 1** (45 min): LLM Hello World - Connect to your endpoint
- **Part 2** (45 min): LLM Agents - Build agents with tools  
- **Part 3** (45 min): MCP Server - Create your own server

## 🚨 If You Get Errors

**"externally-managed-environment" error:**
- ✅ **Solution**: Use the setup script: `python3 workshop_setup.py`

**Import errors:**
- ✅ **Solution**: Make sure virtual environment is activated
- ✅ **Check**: `which python` should show `llm_workshop_env/bin/python`

**API connection issues:**
- ✅ **Check**: Your endpoint and API key in the workshop files
- ✅ **Test**: Run `python workshop_part1_setup.py`

## 💡 Pro Tips

- Always activate your virtual environment first
- Use the setup script for automatic environment setup
- Check the README.md for detailed instructions
- Each part builds on the previous one

## 🆘 Need Help?

1. Check the troubleshooting section in README.md
2. Make sure your virtual environment is activated
3. Verify your API configuration
4. Run the setup script again if needed

**Happy coding! 🚀**
