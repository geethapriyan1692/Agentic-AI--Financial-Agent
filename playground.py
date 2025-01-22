from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
from phi.model.groq import Groq

import os
import phi
from phi.playground import Playground ,serve_playground_app

#Load environment variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.2-11b-vision-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)


#Building a Financial agent 
financial_agent=Agent(
    name="Financial Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.2-11b-vision-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["use Tables to display the data"],
    show_tool_calls=True,
    markdown=True,
    

)

app=Playground(agents=[financial_agent,web_search_agent]).get_app()

if __name__ == "__main__":    # Fixed the syntax error here
    serve_playground_app("playground:app", reload=True)
     


