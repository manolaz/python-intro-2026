# Getting Started Guide

Welcome to Python Introduction 2026! This guide will help you set up your environment and start learning.

## Step 1: Install Python

### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important:** Check "Add Python to PATH" during installation
4. Click "Install Now"

### macOS
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer package
3. Follow the installation wizard

**Alternative:** Use Homebrew
```bash
brew install python3
```

### Linux
Most Linux distributions come with Python pre-installed. To install or update:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip
```

## Step 2: Verify Installation

Open a terminal or command prompt and run:
```bash
python --version
```
or
```bash
python3 --version
```

You should see something like: `Python 3.x.x`

## Step 3: Choose a Text Editor or IDE

### Recommended Options:

1. **VS Code** (Most Popular)
   - Download: https://code.visualstudio.com/
   - Install Python extension
   - Great for beginners and professionals

2. **PyCharm Community Edition** (Full-featured IDE)
   - Download: https://www.jetbrains.com/pycharm/download/
   - Excellent for Python development
   - Free community edition available

3. **IDLE** (Comes with Python)
   - Already installed with Python
   - Simple and easy for beginners
   - Good for running quick tests

4. **Sublime Text** or **Atom**
   - Lightweight alternatives
   - Good for quick editing

## Step 4: Test Your Setup

1. Create a new file called `test.py`
2. Add this code:
   ```python
   print("Hello, Python!")
   print("Setup is complete!")
   ```
3. Run the file:
   ```bash
   python test.py
   ```
   or
   ```bash
   python3 test.py
   ```

If you see the messages printed, you're all set!

## Step 5: Start Learning

1. Open `lessons/01_introduction.md`
2. Read through the lesson
3. Try the code examples
4. Complete the exercises in `exercises/exercise_01.py`

## Running Python Code

### Method 1: Python Files (.py)
```bash
python filename.py
```

### Method 2: Interactive Python Shell
```bash
python
>>> print("Hello!")
>>> exit()
```

### Method 3: IPython (Enhanced Interactive Shell)
Install IPython:
```bash
pip install ipython
```
Then run:
```bash
ipython
```

## Common Issues and Solutions

### Issue: "Python not found" or "Command not recognized"
**Solution:** Make sure Python is added to your PATH. Reinstall Python and check the "Add to PATH" option.

### Issue: Can't install packages with pip
**Solution:** Use:
```bash
python -m pip install package_name
```
or on some systems:
```bash
python3 -m pip install package_name
```

### Issue: Different Python versions
**Solution:** Use specific version:
```bash
python3 filename.py  # For Python 3
```

## Tips for Success

1. **Practice Daily:** Even 30 minutes a day is better than marathon sessions
2. **Type Code Yourself:** Don't copy-paste; typing helps learning
3. **Read Error Messages:** They tell you what's wrong
4. **Google is Your Friend:** Search for errors and concepts
5. **Join Communities:**
   - [r/learnpython](https://reddit.com/r/learnpython)
   - [Python Discord](https://pythondiscord.com)
   - [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

## Next Steps

1. ✅ Install Python
2. ✅ Choose and setup your editor
3. ✅ Test your installation
4. 📚 Start with Lesson 1: [Introduction to Python](lessons/01_introduction.md)

## Need Help?

- Check the [Python Documentation](https://docs.python.org/3/)
- Visit [Python's Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
- Search on [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

Happy coding! 🐍
