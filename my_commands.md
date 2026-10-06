##  Securing LLM Agents Against Prompt Injection Through Least-Privilege Tool Permissions

### Overview
I propose designing and evaluating a least-privilege security layer for LLM-based agents. Agents built with frameworks like LangGraph call tools (files, APIs, code execution) with broad permissions and are vulnerable to prompt injection through tool outputs. The project will threat-model agent tool use, implement a permission-scoping, sandboxing and audit-logging layer for LangGraph agents, and evaluate it against a corpus of injection and privilege-escalation attacks, measuring attack success rate, false blocks and latency overhead. Output: an open-source library and an empirical assessment.

### Problem statement 
LLM-based agents call tools (email, files, APIs, code execution) with broad, session-wide permissions. Because they cannot reliably separate instructions from data, a prompt injection hidden in a tool output can redirect the agent to misuse those permissions — leaking data or executing unintended actions. Detection-based defences are imperfect, and existing architectural defences (e.g. CaMeL) require rebuilding the agent, which practitioners rarely do.

### Background of study 
Prompt injection against tool-using agents is documented in benchmarks such as AgentDojo and InjecAgent and listed in the OWASP Top 10 for Agentic Applications. Least-privilege access control is a long-established security principle (Saltzer & Schroeder, 1975) but has not been systematically evaluated as a drop-in containment layer for agent frameworks such as LangGraph.

### Aim 
To determine whether the consequences of prompt injection in tool-using LLM agents can be contained by a drop-in least-privilege permission and audit layer, without modifying the underlying agent.

### Objectives

1. Threat-model tool use in LLM agents and define a per-task permission policy.
2. Implement a permission-scoping and audit-logging layer for LangGraph agents.
3. Evaluate it on AgentDojo against baseline agents, measuring attack success rate, task utility and overhead.
4. Assess auditability: whether an attack can be reconstructed from the log.

## command 

``` 
export OPENAI_API_KEY=...   # any supported model; a cheap one is fine
uv run python -m agentdojo.scripts.benchmark -s workspace -ut user_task_0 --model gpt-4o-mini-2024-07-18


uv run python -m agentdojo.scripts.benchmark -s workspace -ut user_task_0 --model gpt-4o-mini-2024-07-18 --attack important_instructions

