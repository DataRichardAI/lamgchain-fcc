from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = OpenAI(temperature=0.6)  # temperature: 0 --> very safe answer, 1 --> creative but risky answer 
    name = llm("I have a cat pet and I want a cool name for it. Suggest me five names for my pet. I is white in color.")
    return name
if __name__ == '__main__':
    print(generate_pet_name())
    