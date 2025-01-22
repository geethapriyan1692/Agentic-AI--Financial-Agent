from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()


openai.api_key=os.getenv("OPENAI_API_KEY")

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


## Building multi Ai Agent 
multi_agent=Agent(
    team=[web_search_agent,financial_agent],
    instructions=["Always include sources","Search the web for information"],
    show_tool_calls=True,
    markdown=True,
)
multi_agent.print_response("summarize the analyst recommendation and share the latest news for NVDA",stream=True)
