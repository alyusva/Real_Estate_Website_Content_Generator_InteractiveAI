import httpx
import json
from typing import Dict, Any
from ..config import settings
from .prompts import (
    get_title_prompt, 
    get_meta_description_prompt, 
    get_description_prompt,
    get_neighborhood_prompt,
    get_cta_prompt
)

class OllamaGenerator:
    """Content generator using Ollama."""
    
    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.OLLAMA_MODEL
    
    def _call_ollama(self, prompt: str) -> str:
        """Make a call to Ollama API."""
        try:
            with httpx.Client(timeout=60.0) as client:
                response = client.post(
                    f"{self.base_url}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": prompt,
                        "stream": False,
                        "options": {
                            # temperature controls the randomness of generation. 0.7 is a balanced value, producing creative but not chaotic text.
                            "temperature": 0.7, 
                            # top_p limits the cumulative probability of candidate words. 0.9 allows variety while maintaining coherence.
                            "top_p": 0.9,
                            # top_k limits the number of candidate words considered at each step. 40 gives diversity without losing quality.
                            "top_k": 40
                        }
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    return result.get("response", "").strip()
                else:
                    raise Exception(f"Ollama API error: {response.status_code} - {response.text}")
                    
        except httpx.ConnectError:
            raise Exception(f"Could not connect to Ollama at {self.base_url}. Make sure Ollama is running.")
        except Exception as e:
            raise Exception(f"Ollama API error: {str(e)}")
    
    def generate_title(self, data: Dict[str, Any]) -> str:
        """Generate title using Ollama."""
        prompt = get_title_prompt(data, data.get('language', 'en'))
        title_text = self._call_ollama(prompt)
        # Clean up the response (remove quotes if present)
        title_text = title_text.strip('"\'')
        return f"<title>{title_text}</title>"
    
    def generate_meta_description(self, data: Dict[str, Any]) -> str:
        """Generate meta description using Ollama."""
        prompt = get_meta_description_prompt(data, data.get('language', 'en'))
        meta_text = self._call_ollama(prompt)
        meta_text = meta_text.strip('"\'')
        return f'<meta name="description" content="{meta_text}">'
    
    def generate_h1(self, data: Dict[str, Any]) -> str:
        """Generate H1 headline using Ollama."""
        location = data['location']
        features = data['features']
        language = data.get('language', 'en')
        
        if language == "pt":
            prompt = f"Cria um título H1 atrativo (diferente do título SEO) para um apartamento T{features.get('bedrooms', '')} em {location['neighborhood']}, {location['city']}. Deve ser cativante e incluir uma característica especial se disponível. Máximo 80 caracteres. Responde apenas com o título."
        elif language == "es":
            prompt = f"Crear un título H1 atractivo (diferente del título SEO) para un apartamento de{features.get('bedrooms', '')} habitaciones en {location['neighborhood']}, {location['city']}. Debe ser cautivador e incluir una característica especial si está disponible. Máximo 80 caracteres. Responde solo con el título."
        else:
            prompt = f"Create an attractive H1 headline (different from SEO title) for a {features.get('bedrooms', '')}-bedroom apartment in {location['neighborhood']}, {location['city']}. Should be catchy and include a special feature if available. Maximum 80 characters. Respond only with the headline."
        
        h1_text = self._call_ollama(prompt)
        h1_text = h1_text.strip('"\'')
        return f"<h1>{h1_text}</h1>"
    
    def generate_description(self, data: Dict[str, Any]) -> str:
        """Generate full property description using Ollama."""
        prompt = get_description_prompt(data, data.get('language', 'en'))
        description_text = self._call_ollama(prompt)
        description_text = description_text.strip('"\'')
        return f'<section id="description"><p>{description_text}</p></section>'
    
    def generate_key_features(self, data: Dict[str, Any]) -> str:
        """Generate key features list using Ollama."""
        location = data['location']
        features = data['features']
        language = data.get('language', 'en')
        
        if language == "pt":
            prompt = f"""
Lista 4-5 características principais em formato de bullet points para:
- Apartamento T{features.get('bedrooms', '')} em {location['neighborhood']}
- Área: {features.get('area_sqm', '')} m²
- Características: varanda={'sim' if features.get('balcony') else 'não'}, elevador={'sim' if features.get('elevator') else 'não'}, estacionamento={'sim' if features.get('parking') else 'não'}

Formato: cada linha deve começar com "•" e ser concisa. Responde apenas com a lista.
"""
        elif language == "es":
            prompt = f"""
Lista 4-5 características clave en formato de puntos clave para:
- Apartamento de {features.get('bedrooms', '')} habitaciones en {location['neighborhood']}
- Área: {features.get('area_sqm', '')} m²
- Características: balcón={'sí' if features.get('balcony') else 'no'}, ascensor={'sí' if features.get('elevator') else 'no'}, aparcamiento={'sí' if features.get('parking') else 'no'}

Formato: cada línea debe comenzar con "•" y ser concisa. Responde solo con la lista.
"""
        else:
            prompt = f"""
List 4-5 key features in bullet point format for:
- {features.get('bedrooms', '')}-bedroom apartment in {location['neighborhood']}
- Area: {features.get('area_sqm', '')} sqm
- Features: balcony={'yes' if features.get('balcony') else 'no'}, elevator={'yes' if features.get('elevator') else 'no'}, parking={'yes' if features.get('parking') else 'no'}

Format: each line should start with "•" and be concise. Respond only with the list.
"""
        
        features_text = self._call_ollama(prompt)
        
        # Convert to HTML format
        lines = [line.strip() for line in features_text.split('\n') if line.strip()]
        features_html = '\n'.join([f'  <li>{line.lstrip("• -")}</li>' for line in lines if line])
        
        return f'<ul id="key-features">\n{features_html}\n</ul>'
    
    def generate_neighborhood(self, data: Dict[str, Any]) -> str:
        """Generate neighborhood description using Ollama."""
        prompt = get_neighborhood_prompt(data, data.get('language', 'en'))
        neighborhood_text = self._call_ollama(prompt)
        neighborhood_text = neighborhood_text.strip('"\'')
        return f'<section id="neighborhood"><p>{neighborhood_text}</p></section>'
    
    def generate_call_to_action(self, data: Dict[str, Any]) -> str:
        """Generate call to action using Ollama."""
        prompt = get_cta_prompt(data, data.get('language', 'en'))
        cta_text = self._call_ollama(prompt)
        cta_text = cta_text.strip('"\'')
        return f'<p class="call-to-action">{cta_text}</p>' 