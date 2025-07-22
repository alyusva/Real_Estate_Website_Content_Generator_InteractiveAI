from .schemas import PropertyInput
from .utils import validate_content_limits
from .config import settings
from typing import Dict, Any

def generate_content(data: PropertyInput) -> str:
    """
    Generate all 7 content sections with HTML tags according to the challenge requirements.
    
    The generation mode is determined by the GENERATION_MODE environment variable:
    - "template": Uses predefined templates (original implementation)
    - "openai": Uses OpenAI API for dynamic content generation
    - "ollama": Uses Ollama local LLM for content generation
    
    Sections generated:
    1. <title> - Page Title (max 60 chars)
    2. <meta name="description"> - Meta Description (max 155 chars)
    3. <h1> - Headline
    4. <section id="description"> - Full Property Description (500-700 chars)
    5. <ul id="key-features"> - Key Features List (3-5 bullet points)
    6. <section id="neighborhood"> - Neighborhood Summary
    7. <p class="call-to-action"> - Call to Action
    """
    
    # Validate configuration first
    settings.validate_configuration()
    
    # Convert Pydantic model to dict for easier processing
    data_dict = data.dict()
    
    # Choose generator based on mode
    if settings.GENERATION_MODE == "openai":
        generator = _get_openai_generator()
    elif settings.GENERATION_MODE == "ollama":
        generator = _get_ollama_generator()
    else:  # Default to template mode
        generator = _get_template_generator(data.language)
    
    # Generate all 7 sections
    sections = []
    
    try:
        # 1. Title
        title = generator.generate_title(data_dict)
        sections.append(title)
        
        # 2. Meta Description
        meta_description = generator.generate_meta_description(data_dict)
        sections.append(meta_description)
        
        # 3. H1 Headline
        h1 = generator.generate_h1(data_dict)
        sections.append(h1)
        
        # 4. Description Section
        description = generator.generate_description(data_dict)
        sections.append(description)
        
        # 5. Key Features List
        key_features = generator.generate_key_features(data_dict)
        sections.append(key_features)
        
        # 6. Neighborhood Section
        neighborhood = generator.generate_neighborhood(data_dict)
        sections.append(neighborhood)
        
        # 7. Call to Action
        call_to_action = generator.generate_call_to_action(data_dict)
        sections.append(call_to_action)
        
    except Exception as e:
        # If LLM generation fails, fallback to template mode
        if settings.GENERATION_MODE in ["openai", "ollama"]:
            print(f"Warning: {settings.GENERATION_MODE} generation failed ({str(e)}), falling back to template mode")
            return _generate_with_template_fallback(data_dict, data.language)
        else:
            raise e
    
    # Join all sections with newlines
    final_content = "\n".join(sections)
    
    # Optional: Validate content limits (for debugging/quality assurance)
    content_dict = {
        'title': title,
        'meta_description': meta_description,
        'description': description
    }
    validation_results = validate_content_limits(content_dict)
    
    # In a production system, I would add a log validation results
    # or retry generation if limits are exceeded
    
    return final_content

def _get_openai_generator():
    """Get OpenAI generator instance."""
    try:
        from .llm.openai_generator import OpenAIGenerator
        return OpenAIGenerator()
    except ImportError as e:
        raise Exception(f"OpenAI dependencies not installed: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to initialize OpenAI generator: {str(e)}")

def _get_ollama_generator():
    """Get Ollama generator instance."""
    try:
        from .llm.ollama_generator import OllamaGenerator
        return OllamaGenerator()
    except ImportError as e:
        raise Exception(f"Ollama dependencies not installed: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to initialize Ollama generator: {str(e)}")

def _get_template_generator(language: str):
    """Get template generator for the specified language."""
    if language == "pt":
        from .templates.pt import content as template
    else:  # Default to English
        from .templates.en import content as template
    return template

def _generate_with_template_fallback(data_dict: Dict[str, Any], language: str) -> str:
    """Fallback to template generation if LLM fails."""
    template = _get_template_generator(language)
    
    sections = []
    sections.append(template.generate_title(data_dict))
    sections.append(template.generate_meta_description(data_dict))
    sections.append(template.generate_h1(data_dict))
    sections.append(template.generate_description(data_dict))
    sections.append(template.generate_key_features(data_dict))
    sections.append(template.generate_neighborhood(data_dict))
    sections.append(template.generate_call_to_action(data_dict))
    
    return "\n".join(sections) 