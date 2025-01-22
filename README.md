# Agentic-AI--Financial-Agent

## Financial Agent AI Application

A sophisticated AI-powered financial analysis tool built with phidata that combines web search capabilities with detailed financial data analysis. The application uses multiple AI agents to provide comprehensive financial insights and market research.
 
## Features

Multi-agent system combining web search and financial analysis
Real-time stock data analysis using YFinance
Web search capabilities using DuckDuckGo
Interactive playground interface
Analyst recommendations and stock fundamentals
Company news aggregation
Stock price analysis

## Prerequisites

Python 3.8+

## Valid API keys for:

Groq
OpenAI
phidata



## Installation

Clone the repository:

git clone [your-repository-url]
cd financial-agent-ai

## Install required packages:

pip install phidata yfinance packaging duckduckgo-search fastapi uvicorn groq openai python-dotenv

Create a .env file in the root directory with your API keys:

OPENAI_API_KEY=your_openai_api_key
PHIDATA_API_KEY=your_phidata_api_key

## Project Structure
Copyfinancial-agent-ai/
├── main.py           # Main agent implementation
├── playground.py     # Playground app implementation
├── requirements.txt  # Project dependencies
└── .env             # Environment variables (not tracked in git)

## Usage
Running the Multi-Agent System
pythonCopyfrom main import multi_agent

# Example: Get analysis for NVIDIA stock
multi_agent.print_response("summarize the analyst recommendation and share the latest news for NVDA", stream=True)
Starting the Playground App
bashCopypython playground.py
The playground will be available at http://localhost:8000

## Agent Components
## Web Search Agent

Uses DuckDuckGo for web searches
Powered by Groq's LLaMA 3.2 11B Vision Preview model
Includes source citations in responses

## Financial Agent

Utilizes YFinance for financial data

## Provides:

Real-time stock prices
Analyst recommendations
Stock fundamentals
Company news


Displays data in formatted tables

## API Reference
## Main Components
pythonCopyweb_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.2-11b-vision-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name="Financial Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.2-11b-vision-preview"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["use Tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

## Contributing

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request


## Security
Note: Keep your API keys secure and never commit them to the repository. Always use environment variables for sensitive information.

## Acknowledgments

phidata for the AI agent framework
YFinance for financial data access
Groq for the LLM model
