original code from [Ayoisio](https://github.com/ayoisio/adk-code-review-assistant/tree/codelab)

# 🎓 Code Review Assistant - Codelab Edition

**Learn to build production AI agents with Google ADK**

This is the educational codelab branch designed for the "Building a Production AI Code Review Assistant with Google ADK" workshop. You'll progressively build a complete multi-agent system from scratch, learning production patterns along the way.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![ADK](https://img.shields.io/badge/Google%20ADK-1.15%2B-green)
![Gemini](https://img.shields.io/badge/Gemini-2.5-red)

## 🎯 What You'll Build

Starting from a 7-line agent, you'll progressively create:

- **Review Pipeline**: 4 specialized agents (Analyzer → Style Checker → Test Runner → Synthesizer)
- **Fix Pipeline**: Automated code fixing with iterative refinement (Loop architecture)
- **Production Tools**: AST parsing, style checking, test generation, progress tracking
- **State Management**: Multi-tier state with type-safe constants pattern
- **Cloud Deployment**: Deploy to Agent Engine or Cloud Run with observability

## 📚 Codelab Structure

This branch contains **strategic placeholders** marked with comments like:
```python
# MODULE_4_STEP_2_ADD_STATE_STORAGE
# MODULE_5_STEP_1_STYLE_CHECKER_TOOL
# MODULE_6_STEP_5_CREATE_FIX_LOOP
```

You'll replace these placeholders as you progress through the modules, building the system incrementally.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Google Cloud account with billing enabled
- `gcloud` CLI installed and authenticated
- Git

### Setup Instructions

**1. Clone and checkout the codelab branch:**
```bash
git clone https://github.com/ayoisio/code-review-assistant.git
cd code-review-assistant
git checkout codelab
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

**5. Start the codelab:**

Follow the workshop at: [Codelab Link](https://your-codelab-url.com)

## 📂 Codelab Branch Structure

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

## 🧩 Module Overview

### Module 3: Your First Agent (15 min)
- Set up Google Cloud environment
- Create basic agent with `adk create`
- Understand limitations of LLM-only approaches

### Module 4: Building Your First Agent (15 min)
- Create `analyze_code_structure()` tool with AST parsing
- Add state management with StateKeys constants
- Use async + thread pools for performance
- Connect tool to Code Analyzer agent

**Placeholders you'll fill:**
- `MODULE_4_STEP_2_ADD_STATE_STORAGE`
- `MODULE_4_STEP_3_ADD_ASYNC`
- `MODULE_4_STEP_4_EXTRACT_DETAILS`
- `MODULE_4_STEP_4_HELPER_FUNCTION`
- `MODULE_4_STEP_5_CREATE_AGENT`

### Module 5: Building a Pipeline (28 min)
- Add Style Checker with `check_code_style()` tool
- Add Test Runner with built-in code executor
- Add Feedback Synthesizer with memory search
- Wire 4 agents into Sequential pipeline
- Create root agent

**Placeholders you'll fill:**
- `MODULE_5_STEP_1_STYLE_CHECKER_TOOL`
- `MODULE_5_STEP_1_STYLE_HELPERS`
- `MODULE_5_STEP_1_INSTRUCTION_PROVIDER`
- `MODULE_5_STEP_1_STYLE_CHECKER_AGENT`
- `MODULE_5_STEP_2_INSTRUCTION_PROVIDER`
- `MODULE_5_STEP_2_TEST_RUNNER_AGENT`
- `MODULE_5_STEP_4_SEARCH_PAST_FEEDBACK`
- `MODULE_5_STEP_4_UPDATE_GRADING_PROGRESS`
- `MODULE_5_STEP_4_SAVE_GRADING_REPORT`
- `MODULE_5_STEP_4_INSTRUCTION_PROVIDER`
- `MODULE_5_STEP_4_SYNTHESIZER_AGENT`
- `MODULE_5_STEP_5_CREATE_PIPELINE`

### Module 6: Adding the Fix Pipeline (35 min)
- Add Code Fixer agent
- Add Fix Test Runner agent
- Add Fix Validator with loop exit logic
- Create LoopAgent with max 3 iterations
- Add Fix Synthesizer
- Wire fix pipeline with review pipeline

**Placeholders you'll fill:**
- `MODULE_6_STEP_1_CODE_FIXER_INSTRUCTION_PROVIDER`
- `MODULE_6_STEP_1_CODE_FIXER_AGENT`
- `MODULE_6_STEP_2_FIX_TEST_RUNNER_INSTRUCTION_PROVIDER`
- `MODULE_6_STEP_2_FIX_TEST_RUNNER_AGENT`
- `MODULE_6_STEP_3_VALIDATE_FIXED_STYLE`
- `MODULE_6_STEP_3_COMPILE_FIX_REPORT`
- `MODULE_6_STEP_3_EXIT_FIX_LOOP`
- `MODULE_6_STEP_3_FIX_VALIDATOR_INSTRUCTION_PROVIDER`
- `MODULE_6_STEP_3_FIX_VALIDATOR_AGENT`
- `MODULE_6_STEP_5_CREATE_FIX_LOOP`
- `MODULE_6_STEP_5_UPDATE_ROOT_AGENT`
- `MODULE_6_STEP_6_FIX_SYNTHESIZER_INSTRUCTION_PROVIDER`
- `MODULE_6_STEP_6_FIX_SYNTHESIZER_AGENT`
- `MODULE_6_STEP_6_SAVE_FIX_REPORT`

### Module 7: Deploying to Production (30 min)
- Deploy to Agent Engine with `./deploy.sh agent-engine`
- Test deployed agent
- Monitor with Cloud Trace

### Module 8: Production Observability (20 min)
- Access Cloud Trace Explorer
- Read waterfall charts
- Understand performance characteristics
- Identify bottlenecks

## 🧪 Testing Your Progress

After each module, test your agent:

```bash
# Module 4 - Test analyzer only
adk run code_review_assistant --agent=code_analyzer

# Module 5 - Test complete review pipeline
adk run code_review_assistant

# Module 6 - Test with fix pipeline
adk run code_review_assistant
# Submit buggy code, accept fix offer

# Module 7 - Test deployed agent
python tests/test_agent_engine.py
```

## 🔍 Key Learning Objectives

By completing this codelab, you'll master:

- **Tool Integration**: Building deterministic tools (AST, linters) vs LLM-only approaches
- **Sequential Pipelines**: Orchestrating multiple agents with state flow
- **Loop Architecture**: Iterative refinement with exit conditions (`escalate`)
- **State Management**: Three-tier state (temp/session/user) with type-safe constants
- **Dynamic Instructions**: Context providers that inject state into prompts
- **Production Deployment**: Using `deploy.sh` for Agent Engine and Cloud Run
- **Observability**: Reading Cloud Trace to understand agent behavior

## 🎓 Comparing Branches

| Aspect | Codelab Branch | Main Branch |
|--------|----------------|-------------|
| Purpose | Educational, step-by-step | Production-ready reference |
| Code | Placeholders with comments | Complete implementations |
| Use Case | Learning by building | Reference or deployment |
| Documentation | Inline guidance | API-style docs |

## 💡 Tips for Success

**Follow the placeholders in order:**
- Module 4 → Module 5 → Module 6 → Module 7 → Module 8
- Each module builds on the previous one

**Test frequently:**
- After completing each step, run your agent
- Verify tools work before adding agents
- Check state flows correctly between agents

**Use the constants:**
- Always use `StateKeys.CODE_TO_REVIEW` instead of `"code_to_review"`
- This prevents typos that break multi-agent pipelines

**Read the aside boxes:**
- They explain WHY certain patterns are used
- They highlight common mistakes to avoid

**Compare with main branch if stuck:**
- The main branch has complete implementations
- Use it as a reference, not copy-paste

## 🆘 Troubleshooting

**"Module placeholder not found":**
- Ensure you're on the `codelab` branch: `git branch`
- Pull latest changes: `git pull origin codelab`

**"Import errors after adding code":**
- Check you replaced the ENTIRE placeholder, not just part of it
- Verify indentation matches surrounding code

**"Agent doesn't call my tool":**
- Check tool is in the agent's `tools=[...]` list
- Verify function name matches exactly
- Look at agent instruction - does it tell LLM to use the tool?

**"State key returns None":**
- Check spelling matches `StateKeys` constant exactly
- Verify previous agent actually wrote to that key
- Use `print(tool_context.state)` to debug

**"Loop never exits":**
- Ensure `exit_fix_loop()` tool sets `tool_context.actions.escalate = True`
- Check validator's instruction tells it to call this tool when successful
- Verify `max_iterations=3` is set on LoopAgent

## ✅ Completion Checklist

After finishing the codelab, you should have:

- [ ] Complete review pipeline (4 agents working sequentially)
- [ ] Complete fix pipeline (loop + synthesizer)
- [ ] All tools implemented and tested
- [ ] Deployed to Agent Engine or Cloud Run
- [ ] Verified with `tests/test_agent_engine.py`
- [ ] Reviewed traces in Cloud Trace Explorer
- [ ] Understanding of all production patterns

## 🎉 Next Steps

Once you complete the codelab:

1. **Switch to main branch** to see the complete production code
2. **Customize the assistant** for your specific use case
3. **Add new languages** beyond Python
4. **Integrate with GitHub** for automated PR reviews
5. **Build your own agent** using these patterns

---

Built with ❤️ using Google ADK and Gemini
