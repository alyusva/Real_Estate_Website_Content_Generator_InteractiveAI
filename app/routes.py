from fastapi import APIRouter, HTTPException
from .schemas import PropertyInput, ContentOutput
from .generator import generate_content
from .config import settings

router = APIRouter()

@router.get("/status")
def get_status():
    """Get current configuration status."""
    return {
        "generation_mode": settings.GENERATION_MODE,
        "openai_model": settings.OPENAI_MODEL if settings.GENERATION_MODE == "openai" else None,
        "ollama_model": settings.OLLAMA_MODEL if settings.GENERATION_MODE == "ollama" else None,
        "ollama_url": settings.OLLAMA_BASE_URL if settings.GENERATION_MODE == "ollama" else None,
        "status": "ready"
    }

@router.post("/generate", response_model=ContentOutput)
def generate(property_input: PropertyInput):
    """Generate SEO-optimized real estate content."""
    try:
        content = generate_content(property_input)
        return ContentOutput(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 