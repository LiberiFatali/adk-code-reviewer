# 🎓 Code Reviewer

Production AI agents with Google ADK

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![ADK](https://img.shields.io/badge/Google%20ADK-1.15%2B-green)
![Gemini](https://img.shields.io/badge/Gemini-2.5-red)

## 🎯 In This Project

- **Review Pipeline**: 4 specialized agents (Analyzer → Style Checker → Test Runner → Synthesizer)
- **Fix Pipeline**: Automated code fixing with iterative refinement (Loop architecture)
- **Production Tools**: AST parsing, style checking, test generation, progress tracking
- **State Management**: Multi-tier state with type-safe constants pattern
- **Cloud Deployment**: Deploy to Agent Engine or Cloud Run with observability

## 📂 Project Structure

```
code-review-assistant/
├── code_review_assistant/
│   ├── agent.py                 # Placeholders for pipelines
│   ├── config.py                # Complete - no changes needed
│   ├── constants.py             # Complete - StateKeys defined
│   ├── tools.py                 # Placeholders for tools (Modules 4-6)
│   └── sub_agents/
│       ├── review_pipeline/     # Placeholders (Module 5)
│       │   ├── code_analyzer.py
│       │   ├── style_checker.py
│       │   ├── test_runner.py
│       │   └── feedback_synthesizer.py
│       └── fix_pipeline/        # Placeholders (Module 6)
│           ├── code_fixer.py
│           ├── fix_test_runner.py
│           ├── fix_validator.py
│           └── fix_synthesizer.py
├── tests/
│   └── test_agent_engine.py    # Complete - test deployment
├── deploy.sh                    # Complete - handles all deployments
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Google Cloud account with billing enabled
- `gcloud` CLI installed and authenticated
- Git

### Setup Instructions

**1. Clone code:**

```bash
git clone https://github.com/LiberiFatali/adk-code-reviewer
cd code-review-assistant
```

**2. Create virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

**3. Install dependencies:**

```bash
pip install -r code_review_assistant/requirements.txt
```

**4. Configure your environment:**

```bash
cp .env.example .env
nano .env  # Add your GOOGLE_CLOUD_PROJECT
```

### Deployment on Cloud

```bash
./deploy.sh cloud-run
```

### Acknowledgement
original code from [Ayoisio](https://github.com/ayoisio/adk-code-review-assistant/tree/codelab)
