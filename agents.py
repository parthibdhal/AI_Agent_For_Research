from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os




llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key = os.getenv("GOOGLE_API_KEY"),
    )

researcher = Agent(
    role="senior expert researcher",
    goal="To break down broad visionary ideas into specific, actionable research topics about {topic}, identify key areas requiring in-depth investigation, and prepare report that serves as a roadmap for future goals.: {topic}",
    verbose=True,
    memory=True,
    backstory=("you are a ecperienced researcher in a very prestigious research facility of the world. You have experience of over 30 years. You always have a lot of knowledge about the recent inventions and developments of various cutting edge technologies."),
    max_iter=10,
    tools=[tool],
    llm=llm,
    allow_delegation = False,
)

news_writer = Agent(
    role='senior writer',
    goal = "narrate compelling tech stories about {topic}. Organise the results neatly and give bullet point when possible.",
    verbose=True,
    memory=True,
    backstory=("With a flair of simplifying complex topics you craft engaging narratives that captivate and educate, bringing new new discoveries and inventions to the light in an accessible manner"),
    tools=[tool],
    llm=llm,
    allow_delegation = False,
)










