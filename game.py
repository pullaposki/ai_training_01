# create a game in python that does following:
# 1. creates a loop of 10 questions
# 2. each questions asks you to name a capital city of a country
# 3. in the end it tells you how many questions you got right

import random
import ai
from openai import OpenAI

def get_country_info(country): 
  json = f"""{{
  "country": "{country}",
  "capital": "<capital>",
  "population": "<population>",
  "fun_fact": "<fun fact>"
  }}"""
  ai_instructions = f"You're a helpful travel agent. Respond to a country name with some basic information about the country. Your response should include the country's capital, population, and a fun fact. Return the answer in JSON format. Follow this structure: {json}"
  return ai.ask_ai(country, ai_instructions,0.1)

def get_capital_city(country):
  response = get_country_info(country)
  return response.split('"capital": "')[1].split('"')[0]  

def get_country():
  countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq"]
  return random.choice(countries)

def main():
  correct_answers = 0
  for i in range(10):
    country = get_country()
    capital_city = get_capital_city(country)
    user_input = input(f"What is the capital city of {country}? ")
    if user_input == capital_city:
      correct_answers += 1
      print("Correct!")
    else:
      print(f"Wrong! The correct answer is {capital_city}")
  print(f"You got {correct_answers} out of 10 questions right.")

main()