# Agent Prototype(early stages of development)

Hey I'm Angel this is an exploration into building autonomous AI agents from scratch using Python and ReAct (Reasoning and Acting) prompting techniques.
Hope yall get some value out of the completed project. If you're here early follow along as I will be adding to this until completed.

## Project Overview

This repository contains my implementation of autonomous AI agents following a hands-on learning approach. The project focuses on understanding the core concepts of AI agent architecture and ReAct prompting patterns. I also plan on dockerizing this project in the future.

## Repository Structure(so far)

```
agent_prototype/
├── .venv/                 # Python virtual environment
├── .env                   # Environment variables (API keys, etc.)
├── .gitignore            # Git ignore rules
├── openai_module.py      # OpenAI integration module
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd agent_prototype
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # In my case: .venv/bin/activate.fish
                              # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Add your OpenAI API key and other necessary credentials to the `.env` file

## What is ReAct Prompting?

ReAct (Reasoning and Acting) is a prompting technique that combines reasoning traces and task-specific actions in large language models. It allows agents to:
- Reason about problems step-by-step
- Take actions based on that reasoning
- Observe results and adjust their approach

## Progress

- ✅ Initial project setup
- ✅ Virtual environment configuration
- ✅ OpenAI module file created

## Usage

*Instructions will be added as the project develops*

## Learning Goals

- Understand autonomous AI agent architecture
- Implement ReAct prompting patterns
- Build agents that can reason and act independently
- Explore practical applications of AI agents

---

*This is an experimental project for learning purposes.*