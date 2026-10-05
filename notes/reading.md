
==================================
Lethal trifecta of LLM Agent by Simon Willison @ 
===================================

Important to introduce Sir Simon Willion has the one who coined the term Prompt injection. 

In this his post he clearing highlighted three ingredient that makes llm agent susceptible to attacks.
1. Access of private data
2. The exposure of untrusted data
3. The ability to communicate externally( Exfiltration of LLM instruction )

Sir simon willison futher proceeded to clear distinguish prompt injection from jailbreaking, stating that they are different problem. 



AGENTDODO Paper
===================================

### Core terminology
1. The environment: This specifies an
application area for an AI agent and a set of available tools (e.g., a workspace environment with
access to email, calendar and cloud storage tools). 
2. The environment state: This keeps track of the data for
all the applications that an agent can interact with.
3. A user task:  Is a natural language instruction that the agent should follow in a given environment (e.g.,
add an event to a calendar
4. An injection task: This specifies the goal of the attacker (e.g., exfiltrate the
user’s credit card)
5. Task suite: Is the collection of user tasks and injection tasks for an environment
6. A utility function: which determines whether the agent has solved the task correctly, by
inspecting the model output and the mutations in the environment state.

### Reporting AgentDojo ResultsWe consider three metrics in AgentDojo:

1. Benign Utility: the fraction of user tasks that the model solves in the absence of any attacks.
2. Utility Under Attack: the fraction of security cases (i.e., a pair of user task and injection task) where
the agent solves the user task correctly, without any adversarial side effects. We sometimes report the
complement of this value as the untargeted attack success rate.
3. Targeted Attack Success Rate (ASR): the fraction of security cases where the attacker’s goal is met
(i.e., the agent executes the malicious actions).