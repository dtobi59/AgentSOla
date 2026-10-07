## command 

``` 
export OPENAI_API_KEY=...   # any supported model; a cheap one is fine
uv run python -m agentdojo.scripts.benchmark -s workspace -ut user_task_0 --model GPT_4O_MINI_2024_07_18


uv run python -m agentdojo.scripts.benchmark -s workspace -ut user_task_0 --model GPT_4O_MINI_2024_07_18 --attack important_instructions


python scripts/count.py runs\gpt-4o-mini-2024-07-18\workspace\user_task_0\important_instructions