# Example Questions for the AI Financial Advisor

You can ask the system various types of questions. The CrewAI agents are programmed to extract your investment goals, risk tolerance, and time horizon to provide tailored mutual fund recommendations.

Here is a list of sample questions you can use to test the system:

## 🟢 Complete & Specific Queries
These queries provide all the necessary variables (risk profile, horizon, and intent) directly.
- *"I have some savings and I want to invest in low-risk mutual funds for 3 years. What do you recommend?"*
- *"Can you suggest some high-risk mutual funds for aggressive wealth creation over the next 5 years?"*
- *"I am planning for a short-term goal. Which medium-risk funds should I invest in for just 1 year?"*

## 🟡 Partial/Ambiguous Queries
These queries are missing one or more variables. The Intent Agent will make intelligent assumptions (like defaulting to "medium risk" or "unknown" horizon).
- *"What are the best mutual funds to invest in right now?"*
- *"I want to save up for retirement, but I want to keep my money relatively safe. Any suggestions?"*
- *"Which mutual funds gave the highest returns recently?"*
- *"I'm looking for aggressive growth opportunities to build wealth."*

## 🔴 Filtering by Categories
These test how well the tools utilize specific filtering criteria under the hood.
- *"I want high-risk funds that have shown at least 30% CAGR."*
- *"Show me medium risk funds that will give me good returns for a 3-year plan."*
- *"Are there any low-risk funds doing better than 7% a year?"*

## 🚫 Unsupported Intents
These questions test the system's ability to recognize out-of-scope requests and politely decline.
- *"What's the weather like in New York today?"*
- *"Can you help me file my taxes?"*
- *"What are the best stocks to buy instead of mutual funds?"*
- *"Can you write a poem about investing?"*
