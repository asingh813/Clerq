from openai import OpenAI

client = OpenAI(api_key="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")

def analyze_contract_text(text):
    prompt = f"""
    You are a legal AI assistant. Read the following contract and:
    1. Summarize key terms in plain English.
    2. Flag any clauses that could pose legal risk to a small business.
    3. Suggest edits.

    CONTRACT:
    {text}
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content
