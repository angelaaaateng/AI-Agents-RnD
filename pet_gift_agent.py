"""
Pet Gift Finder Agent
A LangChain agent that helps users find perfect Christmas gifts for their pets
with location-aware shopping and real-time web search capabilities.
"""

from dotenv import load_dotenv
import os
from typing import Dict, Any

# Load environment variables
load_dotenv()

# Enable LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "pet-gift-finder-tutorial"

from langchain.tools import tool
from tavily import TavilyClient
from langchain.agents import create_agent

# Initialize the Tavily client for web searching
tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:
    """Search the web for current information about pet gifts, products, and shopping"""
    return tavily_client.search(query)

@tool
def pet_gift_search(pet_type: str, pet_characteristics: str, budget: str = "moderate", location: str = "US") -> Dict[str, Any]:
    """Search for specific pet gifts based on type, characteristics, budget, and location"""
    search_query = f"Christmas gifts for {pet_type} {pet_characteristics} {budget} budget 2024 where to buy {location}"
    return tavily_client.search(search_query)

@tool
def local_store_search(product_name: str, location: str) -> Dict[str, Any]:
    """Find local pet stores and retailers in a specific location that might carry a product"""
    search_query = f"pet stores near {location} {product_name} in stock local retailers"
    return tavily_client.search(search_query)

# System prompt for the agent
system_prompt = """
You are a helpful pet gift advisor with access to real-time web search capabilities.

Your role:
- Help pet owners find appropriate Christmas gifts based on their pet's characteristics
- Use your web search tools to find current products, prices, and availability
- Consider pet safety, size, age, and personality when making recommendations
- Provide specific product suggestions with purchasing information
- Offer options across different budget ranges
- Help users find local stores and retailers in their area

When to use tools:
- Use web_search for general queries about pet products, reviews, or shopping
- Use pet_gift_search when you have specific pet characteristics, budget, and location info
- Use local_store_search to find nearby pet stores that might carry specific products
- Always ask for the user's location if they want local shopping options
- Always search for current information rather than relying on outdated knowledge

Location examples:
- For US users: Search Amazon, Petco, PetSmart, Chewy
- For Philippines users: Search Shopee, Lazada, local pet stores in Manila/Cebu/Davao
- For other countries: Adapt to local e-commerce and pet store chains

When analyzing pets from photos:
- Identify breed characteristics that might influence gift choices
- Estimate size and age if possible
- Note any visible personality traits or energy levels

Always prioritize pet safety and provide real, purchasable products with current pricing and local availability.
"""

# Create the agent
agent = create_agent(
    model="gpt-5-nano",
    tools=[web_search, pet_gift_search, local_store_search],
    system_prompt=system_prompt
    # No checkpointer needed - LangGraph API handles persistence automatically
)

# Export the agent for LangGraph deployment
__all__ = ["agent"]