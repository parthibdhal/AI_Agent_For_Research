from crewai import Crew,Process
from tasks import research_task,write_task
from agents import researcher,news_writer
import streamlit as st
## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback


st.title('Your Research Assistant')
with st.sidebar:
    st.header('Enter Research Details')
    topic = st.text_input("Main topic of your research:")
    #detailed_questions = st.text_area("Specific questions or subtopics you are interested in exploring:")

if st.button('Run Research'):
    if not topic :
        st.error("Please fill all the fields.")
    else:
        #inputs = f"Research Topic: {topic}\nDetailed Questions: {detailed_questions}"
        result=crew.kickoff(inputs={'topic':topic})
        # result=crew.kickoff(inputs=inputs)
        st.header("Results of your research project:")
        st.markdown(result)


#F:/anaconda_installed/Scripts/activate
#conda activate C:\Users\parth\OneDrive\Desktop\llmProjects\YT_Agents\agentenv

