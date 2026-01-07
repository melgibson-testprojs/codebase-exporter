# LLM Codebase Dumper

**LLM Codebase Dumper** is a lightweight Python utility that exports an entire
codebase — **directory structure + source file contents** — into a single text
file optimized for **Large Language Models (LLMs)** such as **ChatGPT, GPT-4,
Claude, Gemini, and other AI coding assistants**.

It removes the friction of manually copy-pasting files and ensures an LLM gets
**complete, structured project context**.

---

##  Why LLM Codebase Dumper?

LLMs give significantly better answers when they can see:
- The **full directory structure**
- How files relate to each other
- The **actual source code**, not fragments

However, sharing an entire project manually is:
- Slow
- Error-prone
- Easy to miss important files

**LLM Codebase Dumper automates this in one command.**

---

##  Features

-  Recursively scans the entire project folder
-  Prints the complete directory tree structure first
-  Extracts contents of `.py` and `.txt` files
-  Includes full file paths before every file’s content
-  Produces a **single LLM-friendly text file**
-  Safe file reading (handles encoding issues gracefully)
-  Zero dependencies — Python standard library only

---

##  Ideal Use Cases

- Giving **ChatGPT / GPT-4** full project context
- Debugging complex applications with an LLM
- Codebase reviews & refactoring suggestions
- Security and architecture analysis
- Generating documentation with AI
- Preparing datasets for fine-tuned or local LLMs
- Archiving project snapshots in human-readable form

---

##  Installation

### Option 1: Clone from GitHub (recommended)

```bash
git clone https://github.com/yourusername/llm-codebase-dumper.git
cd llm-codebase-dumper
```

### Option 2: Download manually

- Click Code → Download ZIP
- Extract the folder
- Navigate into it via terminal

No additional dependencies required other than python 3.7.

##  Usage
- Run the script in terminal:

```bash
python main.py
```

- When prompted, enter the full path of the project you want to export: eg. D:\my_project
- After execution, an output file will be created: output.txt

###  output.txt
```bash
DIRECTORY STRUCTURE
================================================================================
📁 my_project
│   📄 main.py
│   📄 config.txt
│   📁 services
│   │   📄 api.py
│   │   📄 utils.py
│   📁 models
│   │   📄 user.py

FILE CONTENTS SECTION
================================================================================
FILE PATH: my_project/main.py
================================================================================
from services.api import start_server

if __name__ == "__main__":
    start_server()

================================================================================
FILE PATH: my_project/services/api.py
================================================================================
def start_server():
    print("Server started")
```
