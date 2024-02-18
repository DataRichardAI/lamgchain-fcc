from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type):
    llm = OpenAI(temperature=0.6)  # temperature: 0 --> very safe answer, 1 --> creative but risky answer 
    prompt_template = PromptTemplate(
        input_variables=['animal_type'],
        template = "I have a {animal_type} pet and I want a cool name for it. Suggest me five names for my pet. I is white in color."        
    )
    name = 
    return name
if __name__ == '__main__':
    print(generate_pet_name())
    