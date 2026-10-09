def build_prompt(user_prompt, technique):
    templates = {
        "Zero-shot": f"Answer the following question directly:\n{user_prompt}",
        "Few-shot": f"Understand the question and provide a clear answer:\n{user_prompt}",
        "Chain-of-Thought": f"Analyze the problem carefully and provide the answer with a brief explanation:\n{user_prompt}",
        "Role-based": f"You are an expert assistant. Answer this question clearly:\n{user_prompt}"
    }

    return templates.get(
        technique,
        f"Answer clearly and accurately:\n{user_prompt}"
    )
def zero_shot_prompt(user_input):
    return f"""
Answer the following question clearly and accurately.

Question: {user_input}
"""


def one_shot_prompt(user_input):
    return f"""
Follow the example below to understand the expected answer style.

Example:
Question: What is AI?
Answer: Artificial Intelligence enables machines to perform tasks
that normally require human intelligence.

Now answer this question:
Question: {user_input}
Answer:
"""


def few_shot_prompt(user_input):
    return f"""
Follow the examples below.

Example 1:
Question: What is Python?
Answer: Python is a high-level programming language.

Example 2:
Question: What is SQL?
Answer: SQL is used to manage and query relational databases.

Example 3:
Question: What is an LLM?
Answer: An LLM is a language model trained on large amounts of text.

Now answer this question in a similar style:
Question: {user_input}
Answer:
"""


def cot_prompt(user_input):
    return f"""
Analyze the question carefully before answering.
Provide a clear explanation of the main steps and a concise conclusion.

Question: {user_input}
"""
