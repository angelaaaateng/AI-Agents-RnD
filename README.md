# AI-Agents-RnD
A repository of AI agent experiments and builds using LangChain, LangGraph, and modern AI technologies.

## Pet Gift Finder Agent

An intelligent AI agent that helps users find perfect Christmas gifts for their pets with real-time web search capabilities and location-aware shopping recommendations.

### Key Features

🤖 **Intelligent Agent**: Uses LangChain/LangGraph for sophisticated reasoning and tool usage  
🌐 **Real-time Web Search**: Finds current prices, availability, and reviews  
📍 **Location-aware**: Adapts recommendations for different countries and regions  
⚡ **Streaming Responses**: Real-time response generation for better user experience  
📸 **Multimodal**: Can analyze pet photos to provide personalized recommendations  

### Project Structure

- `pet_gift_agent.py` - Main agent implementation with web search tools
- `pet_gift_agent_tutorial.ipynb` - Interactive tutorial showing agent capabilities
- `langgraph_pet_gift.json` - LangGraph deployment configuration
- `pyproject.toml` - Project dependencies and configuration
- `example.env` - Environment variables template

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/angelaaaateng/AI-Agents-RnD.git
   cd AI-Agents-RnD
   ```

2. **Install UV (if not already installed):**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies:**
   ```bash
   uv sync
   ```

4. **Set up environment variables:**
   ```bash
   cp example.env .env
   # Edit .env with your actual API keys
   ```

5. **Run the agent:**
   ```bash
   uv run python pet_gift_agent.py
   ```

6. **Try the interactive tutorial:**
   ```bash
   uv run jupyter lab pet_gift_agent_tutorial.ipynb
   ```

## Required API Keys

- **OpenAI API Key**: For the language model
- **Tavily API Key**: For web search capabilities
- **LangSmith API Key** (optional): For monitoring and debugging

## Deployment

Deploy to LangSmith for interactive web interface:

```bash
uv run langgraph deploy --config langgraph_pet_gift.json
```

## Technologies Used

- **LangChain/LangGraph**: Agent orchestration and tool management
- **OpenAI GPT**: Natural language processing
- **Tavily**: Real-time web search
- **UV**: Modern Python dependency management
- **Jupyter**: Interactive development and tutorials

## License

MIT License - feel free to use this code for your own AI agent experiments!