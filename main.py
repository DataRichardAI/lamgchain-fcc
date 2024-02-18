from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type,pet_color):
    llm = OpenAI(temperature=0.7)  # temperature: 0 --> very safe answer, 1 --> creative but risky answer 
    prompt_template = PromptTemplate(
        input_variables=['animal_type','pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five names for my pet."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template)
    response=name_chain({'animal_type':animal_type, 'pet_color': pet_color})
    return response
if __name__ == '__main__':
    print(generate_pet_name("cow","red"))
    