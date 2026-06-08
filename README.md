# llm-api-gateway
Smart LLM API gateway with rate limiting, retry logic, and automatic failover.

## Features
- Multi-provider support (OpenAI, Anthropic)
- Automatic retry with exponential backoff
- Rate limiting per provider

## Usage
from gateway import LLMGateway
gw = LLMGateway({"openai": "your-key"})
gw.call("Hello world")

## License
MIT
