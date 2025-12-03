# 🎓 Code Reviewer

Production AI agents with Google ADK

## 🎯 In This Project

- **Review Pipeline**: 4 specialized agents (Analyzer → Style Checker → Test Runner → Synthesizer)
- **Fix Pipeline**: Automated code fixing with iterative refinement (Loop architecture)
- **Production Tools**: AST parsing, style checking, test generation, progress tracking
- **State Management**: Multi-tier state with type-safe constants pattern
- **Cloud Deployment**: Deploy to Cloud Run with observability

## 📂 Project Structure

```
code-review-assistant/
├── code_review_assistant/
│   ├── __init__.py
│   ├── agent.py                 # Main orchestration (root agent + pipelines)
│   ├── agent_engine_app.py      # For deployment on Vertex AI Agent engine
│   ├── config.py                # Configuration management
│   ├── constants.py             # StateKeys constants
│   ├── requirements.txt         # Python dependencies
│   ├── services.py
│   ├── setup.py
│   ├── tools.py                 # Tool implementations
│   └── sub_agents/
│       ├── review_pipeline/
│       │   ├── __init__.py
│       │   ├── code_analyzer.py
│       │   ├── style_checker.py
│       │   ├── test_runner.py
│       │   └── feedback_synthesizer.py
│       └── fix_pipeline/
│           ├── __init__.py
│           ├── code_fixer.py
│           ├── fix_test_runner.py
│           ├── fix_validator.py
│           └── fix_synthesizer.py
├── tests/
│   ├── test_code_analyzer.py
│   └── ...
├── .env.example                  # Environment variable template
├── deploy.sh                     # Deployment script
├── main.py
├── pyproject.toml
└── README.md                     # This file
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

### Deployment

```bash
./deploy.sh {local | cloud-run}
```

### Acknowledgement

original codelab from [Ayoisio](https://github.com/ayoisio/adk-code-review-assistant/tree/codelab)
