from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents.initialize import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type,pet_color):
    llm = OpenAI(temperature=0.7)  # temperature: 0 --> very safe answer, 1 --> creative but risky answer 
    prompt_template = PromptTemplate(
        input_variables=['animal_type','pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five names for my pet."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template,output_key="pet_name")
    response=name_chain({'animal_type':animal_type, 'pet_color': pet_color})
    return response

def langchain_agents():
    llm = OpenAI(temperature=0.5)
    tools = load_tools(["wikipedia", "llm-math"],llm=llm)
    agent = initialize_agent(
        tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    result = agent.run("What is the average age of a dog? Multipy the age by 3")
    print(result)
    
if __name__ == '__main__':
    langchain_agents()
    # print(generate_pet_name("cow","red"))
    