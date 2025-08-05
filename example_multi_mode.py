#!/usr/bin/env python3
"""
Example script demonstrating all 3 generation modes:
1. Template mode (original) English, Portuguese, and Spanish.
2. OpenAI mode (requires API key)
3. Ollama mode (requires local Ollama server)
- Show the configuration
"""

import os
import json
from app.schemas import PropertyInput
from app.generator import generate_content

def test_template_mode():
    """Test template-based generation."""
    print("🔧 TESTING TEMPLATE MODE")
    print("=" * 60)
    
    # Set environment for template mode
    os.environ["GENERATION_MODE"] = "template"
    
    # Reload settings
    from app.config import settings
    settings.GENERATION_MODE = "template"
    
    for lang, lang_name in [("en", "ENGLISH"), ("pt", "PORTUGUESE"), ("es", "SPANISH")]:
        sample_data = {
            "title": "T3 apartment in Lisbon",
            "location": {
                "city": "Lisbon",
                "neighborhood": "Campo de Ourique"
            },
            "features": {
                "bedrooms": 3,
                "bathrooms": 2,
                "area_sqm": 120,
                "balcony": True,
                "parking": False,
                "elevator": True,
                "floor": 2,
                "year_built": 2005
            },
            "price": 650000,
            "listing_type": "sale",
            "language": lang
        }
        print(f"\n{lang_name} CONTENT:")
        print("=" * 60)
        try:
            property_input = PropertyInput(**sample_data)
            content = generate_content(property_input)
            print(content)
            print("\n✅ Template mode successful!")
        except Exception as e:
            print(f"❌ Template mode failed: {e}")
        print("\n" + "=" * 60)

def test_openai_mode():
    """Test OpenAI-based generation."""
    print("\n🤖 TESTING OPENAI MODE")
    print("=" * 60)
    
    # Check if API key is available
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("⚠️  OPENAI_API_KEY not set. Skipping OpenAI test.")
        print("   To test OpenAI mode, set your API key in .env file.")
        print("=" * 60)
        return
    
    # Set environment for OpenAI mode
    os.environ["GENERATION_MODE"] = "openai"
    
    # Reload settings
    from app.config import settings
    settings.GENERATION_MODE = "openai"
    settings.OPENAI_API_KEY = openai_key
    
    sample_data = {
        "title": "Modern T2 apartment in Porto",
        "location": {
            "city": "Porto",
            "neighborhood": "Cedofeita"
        },
        "features": {
            "bedrooms": 2,
            "bathrooms": 1,
            "area_sqm": 85,
            "balcony": False,
            "parking": True,
            "elevator": False,
            "floor": 1,
            "year_built": 1995
        },
        "price": 320000,
        "listing_type": "sale",
        "language": "pt"
    }
    
    try:
        property_input = PropertyInput(**sample_data)
        print("🔄 Generating content with OpenAI (this may take a moment)...")
        content = generate_content(property_input)
        print(content)
        print("\n✅ OpenAI mode successful!")
    except Exception as e:
        print(f"❌ OpenAI mode failed: {e}")
        print("   Falling back to template mode...")
    
    print("\n" + "=" * 60)

def test_ollama_mode():
    """Test Ollama-based generation."""
    print("\n🦙 TESTING OLLAMA MODE")
    print("=" * 60)
    
    # Set environment for Ollama mode
    os.environ["GENERATION_MODE"] = "ollama"
    
    # Reload settings
    from app.config import settings
    settings.GENERATION_MODE = "ollama"
    
    sample_data = {
        "title": "Luxury T4 apartment in Lisbon",
        "location": {
            "city": "Lisbon",
            "neighborhood": "Chiado"
        },
        "features": {
            "bedrooms": 4,
            "bathrooms": 3,
            "area_sqm": 180,
            "balcony": True,
            "parking": True,
            "elevator": True,
            "floor": 5,
            "year_built": 2020
        },
        "price": 950000,
        "listing_type": "sale",
        "language": "en"
    }
    
    try:
        property_input = PropertyInput(**sample_data)
        print("🔄 Generating content with Ollama (this may take a moment)...")
        print(f"   Using model: {settings.OLLAMA_MODEL} at {settings.OLLAMA_BASE_URL}")
        content = generate_content(property_input)
        print(content)
        print("\n✅ Ollama mode successful!")
    except Exception as e:
        print(f"❌ Ollama mode failed: {e}")
        print("   Make sure Ollama is running with:")
        print("   docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama")
        print("   ollama pull llama3.2")
        print("   Falling back to template mode...")
    
    print("\n" + "=" * 60)

def show_configuration_guide():
    """Show configuration guide for different modes."""
    print("\n📋 CONFIGURATION GUIDE")
    print("=" * 60)
    print("""
To test different modes, create a .env file with:

🔧 TEMPLATE MODE (No external dependencies):
GENERATION_MODE=template

🤖 OPENAI MODE (Requires API key):
GENERATION_MODE=openai
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini

🦙 OLLAMA MODE (Requires local Ollama server):
GENERATION_MODE=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

To start Ollama:
1. Install Ollama: https://ollama.ai/download
2. Pull a model: ollama pull llama3.2
3. Start server: ollama serve (runs on port 11434)
Alternatively with Docker
""")
    print("=" * 60)

if __name__ == "__main__":
    print("🏠 REAL ESTATE CONTENT GENERATOR - MULTI-MODE TEST")
    print("Testing all 3 generation modes...")
    
    # Test all modes
    test_template_mode()
    test_openai_mode()
    test_ollama_mode()
    
    # Show configuration guide
    show_configuration_guide()
    
    print("\n✨ Multi-mode testing completed!")
    print("\nNext steps:")
    print("1. Configure your preferred mode in .env file")
    print("2. Start the API server: uvicorn app.main:app --reload")
    print("3. Check status: curl http://localhost:8000/status")
    print("4. Generate content: curl -X POST http://localhost:8000/generate -d @example_data.json") 