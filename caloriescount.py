#importing libraries
from groq import Groq
import re

#1.ingredients pass it into llama and get the answer in steps and total calorie count.
#contains the vegetables or materials deletected from cv

#ingredients=['onion','chicken','tomato','cucumber','corn','potato','bread']
#for input from user
ingredients = input("Enter the ingredients  with comma seperated:\n")
#converting the list items into a string to pass it into llama
ingredients_text=", ".join(ingredients)
#print(ingredients_text)
#pass it into llama using groq api
client = Groq(api_key="{your_api_key}")
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": f"Create a healthy diet recipe using the ingredients {ingredients_text} and calculate the calories and print only the total calories in number under calories tag,"
                       f"suggest the size of ingredients for a single serving."
                       f"The output should be in the format of ingredients tag containing the ingredients "
                       f"and steps tag containing the instruction and "
                       f"calories tag containing calories without any extra details ."
        },

    ],
    temperature=1.2,
    max_tokens=1024,
    top_p=0.9,
    stream=True,
    stop=None,
)
ans=""
for chunk in completion:
    if chunk.choices[0].delta.content:
        ans += chunk.choices[0].delta.content
        #print(f"part:\n{chunk.choices[0].delta.content}")
#print(f"final answer :{ans}")

# extracting the tags from the response
ingredients_part = ""
steps_part = ""
calories_part=""
in_ingredients_section = False
in_steps_section = False
in_calories_section=False

for line in ans.split("\n"):
    if "Ingredients" in line:
        in_ingredients_section = True
        in_steps_section = False
        in_calories_section = False
    elif "Steps" in line:
        in_ingredients_section = False
        in_steps_section = True
        in_calories_section = False
    elif "Calories" in line:
        in_ingredients_section = False
        in_steps_section = False
        in_calories_section = True

    # Collect ingredients
    if in_ingredients_section and line.strip() and "Ingredients" not in line:
        #print("ingre line:",line)
        ingredients_part += re.sub(r'[^a-zA-Z0-9\s/]', '', line)+ "\n"

    # Collect steps
    if in_steps_section and line.strip() and "Steps" not in line:
        steps_part += line.strip() + "\n"

    if in_calories_section and line.strip() :
        #print("calories line:",line)
        calories_part = re.sub(r'[^0-9]', '', line)

# Now ingredients_part has the ingredients and steps_part has the steps
ingredients_list = ingredients_part.strip().split("\n")  # List of ingredients
steps = steps_part.strip().split("\n")  # List of steps
calories = calories_part
# Output the results
print(f"\nIngredients:")
for items in ingredients_list:
    print(items.strip())
print(f"\nSteps:")
for step in steps:
    print(step.strip())
print(f"\nCalories: {calories}")