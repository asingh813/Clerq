import openai
openai.api_key = "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"  # replace with your actual key

def analyze_contract_text(text):
    prompt = f"""
    You are a legal AI assistant. Read the following contract and:
    1. Summarize key terms in plain English.
    2. Flag risky clauses.
    3. Suggest edits.

    CONTRACT:
    {text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response['choices'][0]['message']['content']
