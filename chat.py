from openai import OpenAI

# Example: reuse your existing OpenAI setup

def ask_ai(prompt, system_prompt="Always answer in rhymes.", temperature=1):
  # Point to the local server
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

  # Create a chat completion request
  completion = client.chat.completions.create(
    model="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",  # Specify the model to use
    messages=[
      {"role": "system", "content": system_prompt},  # System message
      {"role": "user", "content": prompt}  # User message
    ],
    temperature=temperature,  # Set the temperature for randomness in the response
  )

  # Print the generated completion message
  return completion.choices[0].message.content

print(ask_ai("What is the meaning of life?"))
