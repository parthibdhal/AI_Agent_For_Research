from crewai import Task
from tools import tool
from agents import researcher,news_writer

# Research task
research_task = Task(
  description=(
    "Based on the topic {topic},figure out what it is that the user needs in order to figure out their problem"
    "Make sure not to put exact same input multiple time while searching the internet.Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points, recent advancements or news about {topic}."
    # "its market opportunities, and potential risks."
  ),
  expected_output='A clear explanation of the principles, concepts, disciplines, and skills needed by the visionary in order to accomoplish their goal. Prepare a 2 page long report.',
  tools=[tool],
  agent=researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the world."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='An article on {topic} , 5 principles and concepts reviewed and thoroughly explaiened. At the end provide 5 internet articles titles and their URL',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)