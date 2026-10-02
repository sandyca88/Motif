---
name: ai-product-ux
description: Design the UX of AI features and agentic products: chat and copilot interfaces, prompt input and suggestions, streaming and progress, tool-use and agent step visibility, citations and confidence, human-in-the-loop approvals, error and refusal states, feedback loops, onboarding and expectation-setting, and trust and safety patterns. Use when the user is designing or building an AI assistant, chatbot, copilot, AI search, AI writing tool, agent workflow, or any feature powered by an LLM.
license: Commercial. See LICENSE.txt
---

# AI Product UX

AI features fail on UX, not just model quality: unclear capability, invisible progress, unverifiable answers, and no way to correct mistakes. Design for **expectation → control → trust → recovery**.

## 1. Frame the feature

State in a short brief: user and job-to-be-done; interaction model (chat, inline copilot, one-click action, background agent, AI search); autonomy level (suggest → draft → act with approval → act autonomously); and cost of an error (low: rewrite a sentence; high: send money, email customers, delete data). **The higher the cost of error, the more confirmation, preview and undo you need.**

## 2. Pattern checklist by stage

**Before input: set expectations**
- Say what it can and can't do in one line near the input; show 3–4 example prompts or suggestion chips tailored to context.
- Show which data/sources it will use (and let users choose/limit them).

**Input**
- Auto-growing composer, attachments with visible chips, mode/model selector only if it changes outcomes meaningfully.
- Structured inputs (pickers, sliders) instead of free text when the options are known.

**While working: make progress visible**
- Stream output; for multi-step agents show a step list (planned → running → done/failed) with tool names in plain language.
- Offer "Stop" at all times; long tasks run in background with notification on completion.

**Output: make it verifiable**
- Citations/sources inline and openable; distinguish quoted facts from generated text.
- Show uncertainty honestly ("I couldn't find X in your files"); never fake confidence.
- Output is editable and actionable: copy, insert, apply, regenerate, and "try another approach".

**Acting on the world: human in the loop**
- Preview diffs before applying (text, code, data changes); approve/reject per item for batches.
- Confirm consequential actions with a specific summary ("Send 42 emails to Customers segment?").
- Provide undo or a clear revert path; log what the agent did (activity history).

**Errors & refusals**
- Explain what went wrong in plain language + next step (rephrase, add context, retry, contact).
- Refusals are brief, non-judgmental and suggest what is possible.

**Feedback & learning**
- Thumbs up/down with optional reason chips; "remember this preference" when the product supports memory, with a visible place to review and delete memories.

**Onboarding**
- First-run: one guided example with the user's own data if possible; progressive disclosure of advanced controls.

## 3. Deliverables

1. Feature brief (above) + autonomy/risk matrix.
2. Flow diagram (Mermaid) including error, refusal, stop and approval branches.
3. Screen specs or built UI in the user's stack for: empty state, composing, streaming/working, result with sources, approval dialog, error.
4. Microcopy set for all states (capability line, suggestions, progress labels, errors, confirmations).
5. Metrics: task success, acceptance/edit rate of AI outputs, regenerate rate, thumbs-down reasons, time saved, and escalation/undo rate.

## Anti-patterns to flag

Anthropomorphic over-promising ("I understand you perfectly"), hidden data use, irreversible actions without preview, endless spinners with no step info, chat as the only interface for tasks that need structure.
