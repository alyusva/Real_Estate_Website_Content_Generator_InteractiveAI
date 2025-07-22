import os
from dotenv import load_dotenv
from typing import Literal

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application settings loaded from environment variables."""
    
    # Generation Mode
    GENERATION_MODE: Literal["template", "openai", "ollama"] = os.getenv("GENERATION_MODE", "template")
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    
    # Ollama Configuration
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2")
    
    # API Configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    
    def validate_configuration(self) -> bool:
        """Validate that required configuration is present for the selected mode."""
        if self.GENERATION_MODE == "openai":
            if not self.OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY is required when GENERATION_MODE is 'openai'")
        elif self.GENERATION_MODE == "ollama":
            if not self.OLLAMA_BASE_URL or not self.OLLAMA_MODEL:
                raise ValueError("OLLAMA_BASE_URL and OLLAMA_MODEL are required when GENERATION_MODE is 'ollama'")
        return True

# Global settings instance
settings = Settings() 