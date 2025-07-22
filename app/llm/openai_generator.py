import openai
from typing import Dict, Any
from ..config import settings
from .prompts import (
    get_title_prompt, 
    get_meta_description_prompt, 
    get_description_prompt,
    get_neighborhood_prompt,
    get_cta_prompt
)
from ..utils import format_price

class OpenAIGenerator:
    """Content generator using OpenAI API."""
    
    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise ValueError("OpenAI API key is required")
        
        self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL
    
    def _call_openai(self, prompt: str, max_tokens: int = 150) -> str:
        """Make a call to OpenAI API."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert real estate copywriter and SEO specialist."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.7,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
    
    def generate_title(self, data: Dict[str, Any]) -> str:
        """Generate title using OpenAI."""
        prompt = get_title_prompt(data, data.get('language', 'en'))
        title_text = self._call_openai(prompt, max_tokens=50)
        return f"<title>{title_text}</title>"
    
    def generate_meta_description(self, data: Dict[str, Any]) -> str:
        """Generate meta description using OpenAI."""
        prompt = get_meta_description_prompt(data, data.get('language', 'en'))
        meta_text = self._call_openai(prompt, max_tokens=100)
        return f'<meta name="description" content="{meta_text}">'
    
    def generate_h1(self, data: Dict[str, Any]) -> str:
        """Generate H1 headline using OpenAI (similar to title but for display)."""
        # For H1, we can use a slightly modified title prompt
        location = data['location']
        features = data['features']
        language = data.get('language', 'en')
        
        if language == "pt":
            prompt = f"Cria um título H1 atrativo (diferente do título SEO) para um apartamento T{features.get('bedrooms', '')} em {location['neighborhood']}, {location['city']}. Deve ser cativante e incluir uma característica especial se disponível. Máximo 80 caracteres."
        else:
            prompt = f"Create an attractive H1 headline (different from SEO title) for a {features.get('bedrooms', '')}-bedroom apartment in {location['neighborhood']}, {location['city']}. Should be catchy and include a special feature if available. Maximum 80 characters."
        
        h1_text = self._call_openai(prompt, max_tokens=60)
        return f"<h1>{h1_text}</h1>"
    
    def generate_description(self, data: Dict[str, Any]) -> str:
        """Generate full property description using OpenAI."""
        prompt = get_description_prompt(data, data.get('language', 'en'))
        description_text = self._call_openai(prompt, max_tokens=300)
        return f'<section id="description"><p>{description_text}</p></section>'
    
    def generate_key_features(self, data: Dict[str, Any]) -> str:
        """Generate key features list using OpenAI."""
        location = data['location']
        features = data['features']
        language = data.get('language', 'en')
        
        if language == "pt":
            prompt = f"""
Lista 4-5 características principais em formato de bullet points para:
- Apartamento T{features.get('bedrooms', '')} em {location['neighborhood']}
- Área: {features.get('area_sqm', '')} m²
- Características: varanda={'sim' if features.get('balcony') else 'não'}, elevador={'sim' if features.get('elevator') else 'não'}, estacionamento={'sim' if features.get('parking') else 'não'}

Formato: cada linha deve começar com "•" e ser concisa.
"""
        else:
            prompt = f"""
List 4-5 key features in bullet point format for:
- {features.get('bedrooms', '')}-bedroom apartment in {location['neighborhood']}
- Area: {features.get('area_sqm', '')} sqm
- Features: balcony={'yes' if features.get('balcony') else 'no'}, elevator={'yes' if features.get('elevator') else 'no'}, parking={'yes' if features.get('parking') else 'no'}

Format: each line should start with "•" and be concise.
"""
        
        features_text = self._call_openai(prompt, max_tokens=150)
        
        # Convert to HTML format
        lines = [line.strip() for line in features_text.split('\n') if line.strip()]
        features_html = '\n'.join([f'  <li>{line.lstrip("• ")}</li>' for line in lines if line])
        
        return f'<ul id="key-features">\n{features_html}\n</ul>'
    
    def generate_neighborhood(self, data: Dict[str, Any]) -> str:
        """Generate neighborhood description using OpenAI."""
        prompt = get_neighborhood_prompt(data, data.get('language', 'en'))
        neighborhood_text = self._call_openai(prompt, max_tokens=200)
        return f'<section id="neighborhood"><p>{neighborhood_text}</p></section>'
    
    def generate_call_to_action(self, data: Dict[str, Any]) -> str:
        """Generate call to action using OpenAI."""
        prompt = get_cta_prompt(data, data.get('language', 'en'))
        cta_text = self._call_openai(prompt, max_tokens=50)
        return f'<p class="call-to-action">{cta_text}</p>' 