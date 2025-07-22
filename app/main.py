from fastapi import FastAPI
from .routes import router
from .config import settings

app = FastAPI(
    title="Real Estate Content Generator",
    description=f"AI-powered content generation for real estate listings. Current mode: {settings.GENERATION_MODE}",
    version="2.0.0"
)

# Validate configuration on startup
@app.on_event("startup")
async def startup_event():
    """Validate configuration on startup."""
    try:
        settings.validate_configuration()
        print(f"✅ Server starting in {settings.GENERATION_MODE.upper()} mode")
        if settings.GENERATION_MODE == "openai":
            print(f"   Using OpenAI model: {settings.OPENAI_MODEL}")
        elif settings.GENERATION_MODE == "ollama":
            print(f"   Using Ollama model: {settings.OLLAMA_MODEL} at {settings.OLLAMA_BASE_URL}")
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        raise e

app.include_router(router) 