## command 

``` 
export OPENAI_API_KEY=...   # any supported model; a cheap one is fine
uv run python -m agentdojo.scripts.benchmark -s workspace -ut user_task_0 --model gpt-4o-mini-2024-07-18


uv run python -m agentdojo.scripts.benchmark -s workspace -ut user_task_0 --model gpt-4o-mini-2024-07-18 --attack important_instructions


python scripts/count.py runs_clean/user_task_2/important_instructions