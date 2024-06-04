from openai import OpenAI

def translate_finnish_word_into_swedish_and_norwegian(word):
  # Point to the local server
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

  # Create a translation request
  completion = client.chat.completions.create(
    model="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",  # Specify the model to use
    messages=[
      {"role": "system", "content": "Translate the Finnish word into Swedish and Norwegian. Return the answer like this:'In Swedish <swedish word>, in Norwegean <norwegean word>', no other text.'"},  # System message
      {"role": "user", "content": word}  # User message
    ],
    temperature=0.5,  # Set the temperature for randomness in the response
  )
  

  # Print the generated completion message
  return completion.choices[0].message.content

user_input = input("Enter a Finnish word: ")

print(translate_finnish_word_into_swedish_and_norwegian(user_input))