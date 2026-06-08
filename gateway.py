import requests
import time
import logging

logger = logging.getLogger(__name__)

PROVIDERS = {
    "openai": "https://api.openai.com/v1/chat/completions",
    "anthropic": "https://api.anthropic.com/v1/messages",
}

class LLMGateway:
    def __init__(self, providers: dict, retries: int = 3):
        self.providers = providers
        self.retries = retries

    def call(self, prompt: str, provider: str = "openai") -> str:
        url = PROVIDERS.get(provider)
        token = self.providers.get(provider)
        for attempt in range(self.retries):
            try:
                response = requests.post(url, headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                }, json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]})
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.warning(f"Attempt {attempt+1} failed: {e}")
                time.sleep(2 ** attempt)
        raise Exception("All retries failed")
