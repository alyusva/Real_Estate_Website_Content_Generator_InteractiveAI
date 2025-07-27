import re
from typing import Dict, Any

def format_price(price: float, currency: str = "EUR", language: str = "en") -> str:
    """Format price according to language and currency."""
    if language == "pt":
        if currency == "EUR":
            return f"€{price:,.0f}".replace(",", ".")
        else:
            return f"{price:,.0f} {currency}".replace(",", ".")
    else:  # English
        if currency == "EUR":
            return f"€{price:,.0f}"
        elif currency == "USD":
            return f"${price:,.0f}"
        else:
            return f"{price:,.0f} {currency}"

def truncate_text(text: str, max_chars: int) -> str:
    """Truncate text to max characters without breaking words."""
    if len(text) <= max_chars:
        return text
    
    truncated = text[:max_chars]
    last_space = truncated.rfind(' ')
    if last_space > max_chars * 0.8:  # Only truncate at word boundary if close to limit
        return truncated[:last_space] + "..."
    return truncated + "..."

def get_seo_keywords(data: Dict[str, Any], language: str) -> Dict[str, str]:
    """Generate SEO keywords based on property data and language."""
    location = data.get('location', {})
    features = data.get('features', {})
    listing_type = data.get('listing_type', 'sale')
    
    city = location.get('city', '')
    neighborhood = location.get('neighborhood', '')
    bedrooms = features.get('bedrooms', 0)
    
    if language == "pt":
        keywords = {
            'property_type': f"T{bedrooms}" if bedrooms > 0 else "apartamento",
            'action': "para venda" if listing_type == "sale" else "para arrendar",
            'location_phrase': f"em {neighborhood}, {city}" if neighborhood else f"em {city}",
            'real_estate': "imobiliário em Portugal",
            'apartment_type': f"apartamento T{bedrooms}" if bedrooms > 0 else "apartamento"
        }
    elif language == "es":
        keywords = {
            'property_type': f"{bedrooms} habitaciones" if bedrooms > 0 else "apartamento",
            'action': "en venta" if listing_type == "sale" else "en alquiler",
            'location_phrase': f"en {neighborhood}, {city}" if neighborhood else f"en {city}",
            'real_estate': "inmobiliaria en España",
            'apartment_type': f"apartamento de {bedrooms} habitaciones" if bedrooms > 0 else "apartamento"
        }
    else:  # English
        bedrooms_text = f"{bedrooms}-bedroom" if bedrooms > 0 else ""
        keywords = {
            'property_type': f"{bedrooms_text} apartment" if bedrooms > 0 else "apartment",
            'action': "for sale" if listing_type == "sale" else "for rent",
            'location_phrase': f"in {neighborhood}, {city}" if neighborhood else f"in {city}",
            'real_estate': "real estate in Portugal",
            'apartment_type': f"T{bedrooms} apartment" if bedrooms > 0 else "apartment"
        }
    
    return keywords

def validate_content_limits(content_dict: Dict[str, str]) -> Dict[str, bool]:
    """Validate that content sections meet character limits."""
    limits = {
        'title': 60,
        'meta_description': 155,
        'description': 700  # Max limit, minimum is 500
    }
    
    results = {}
    for section, limit in limits.items():
        if section in content_dict:
            # Extract text content without HTML tags for accurate counting
            text_content = re.sub(r'<[^>]+>', '', content_dict[section])
            results[section] = len(text_content) <= limit
        else:
            results[section] = True
    
    return results 