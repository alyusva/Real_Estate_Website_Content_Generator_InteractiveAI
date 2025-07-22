from typing import Dict, Any, List
from ...utils import format_price, get_seo_keywords, truncate_text

def generate_title(data: Dict[str, Any]) -> str:
    """Generate SEO-optimized title (max 60 chars)."""
    location = data['location']
    features = data['features']
    listing_type = data['listing_type']
    
    bedrooms = features.get('bedrooms', 0)
    property_type = f"T{bedrooms}" if bedrooms > 0 else "Apartamento"
    action = "para Venda" if listing_type == "sale" else "para Arrendar"
    
    title = f"{property_type} {action} em {location['neighborhood']}, {location['city']}"
    return f"<title>{truncate_text(title, 60)}</title>"

def generate_meta_description(data: Dict[str, Any]) -> str:
    """Generate meta description (max 155 chars)."""
    location = data['location']
    features = data['features']
    
    bedrooms = features.get('bedrooms', 0)
    area = features.get('area_sqm', 0)
    
    highlights = []
    if features.get('balcony'):
        highlights.append("varanda")
    if features.get('elevator'):
        highlights.append("elevador")
    if features.get('parking'):
        highlights.append("estacionamento")
    
    highlight_text = f" com {' e '.join(highlights[:2])}" if highlights else ""
    
    description = f"Apartamento T{bedrooms} espaçoso em {location['city']}{highlight_text}, localizado em {location['neighborhood']}. Ideal para famílias."
    return f'<meta name="description" content="{truncate_text(description, 155)}">'

def generate_h1(data: Dict[str, Any]) -> str:
    """Generate main headline."""
    location = data['location']
    features = data['features']
    
    bedrooms = features.get('bedrooms', 0)
    
    highlights = []
    if features.get('balcony'):
        highlights.append("Varanda")
    if features.get('elevator'):
        highlights.append("Elevador")
    
    highlight_text = f" com {highlights[0]}" if highlights else ""
    
    headline = f"Apartamento T{bedrooms} Moderno{highlight_text} em {location['neighborhood']}, {location['city']}"
    return f"<h1>{headline}</h1>"

def generate_description(data: Dict[str, Any]) -> str:
    """Generate full property description (500-700 chars)."""
    location = data['location']
    features = data['features']
    price = data['price']
    listing_type = data['listing_type']
    
    bedrooms = features.get('bedrooms', 0)
    bathrooms = features.get('bathrooms', 0)
    area = features.get('area_sqm', 0)
    floor = features.get('floor')
    year_built = features.get('year_built')
    
    # Build description parts
    location_desc = f"Localizado no encantador bairro de {location['neighborhood']}"
    property_desc = f"este elegante apartamento T{bedrooms} oferece {area:.0f} m² de espaço luminoso e amplo"
    
    floor_text = f" no {floor}º andar" if floor else ""
    building_features = []
    if features.get('elevator'):
        building_features.append("acesso por elevador")
    building_text = f" de um edifício bem conservado com {', '.join(building_features)}" if building_features else ""
    
    room_desc = f"O apartamento possui {bedrooms} quartos, {bathrooms} casas de banho"
    
    amenities = []
    if features.get('balcony'):
        amenities.append("uma varanda privativa perfeita para relaxar")
    if features.get('parking'):
        amenities.append("lugar de estacionamento")
    
    amenity_text = f", e {', '.join(amenities)}" if amenities else ""
    
    year_text = f" Construído em {year_built}," if year_built else ""
    price_text = format_price(price, "EUR", "pt")
    action = "venda" if listing_type == "sale" else "arrendamento"
    
    description = f"{location_desc}, {property_desc}.{floor_text}{building_text}, {room_desc}{amenity_text}.{year_text} combina comodidades modernas com conforto intemporal. Com um preço de {action} de {price_text}, este imóvel em {location['city']} é ideal para famílias ou profissionais que procuram uma casa bem localizada na capital."
    
    # Ensure it's between 500-700 characters
    if len(description) > 700:
        description = truncate_text(description, 700)
    elif len(description) < 500:
        description += f" Não perca esta oportunidade de viver num dos bairros mais procurados de {location['city']}."
    
    return f'<section id="description"><p>{description}</p></section>'

def generate_key_features(data: Dict[str, Any]) -> str:
    """Generate key features list (3-5 bullet points)."""
    location = data['location']
    features = data['features']
    
    feature_list = []
    
    # Area
    if features.get('area_sqm'):
        feature_list.append(f"{features['area_sqm']:.0f} m² de área habitacional")
    
    # Bedrooms and bathrooms
    bedrooms = features.get('bedrooms', 0)
    bathrooms = features.get('bathrooms', 0)
    if bedrooms and bathrooms:
        feature_list.append(f"{bedrooms} quartos e {bathrooms} casas de banho")
    
    # Special features
    if features.get('balcony'):
        feature_list.append("Varanda privativa")
    if features.get('elevator'):
        feature_list.append("Acesso por elevador")
    if features.get('parking'):
        feature_list.append("Lugar de estacionamento")
    
    # Location
    feature_list.append(f"Localizado em {location['neighborhood']}, {location['city']}")
    
    # Limit to 5 features
    feature_list = feature_list[:5]
    
    features_html = '\n'.join([f'  <li>{feature}</li>' for feature in feature_list])
    return f'<ul id="key-features">\n{features_html}\n</ul>'

def generate_neighborhood(data: Dict[str, Any]) -> str:
    """Generate neighborhood summary."""
    location = data['location']
    
    # Generic neighborhood descriptions - in real implementation, this could be enhanced with actual data
    neighborhood_descriptions = {
        "Campo de Ourique": "Campo de Ourique é um dos bairros mais desejados de Lisboa, conhecido pelos seus cafés vibrantes, parques verdes e excelentes escolas. Com uma forte comunidade local e fácil acesso ao centro da cidade, oferece a combinação perfeita entre charme e conveniência.",
        "Chiado": "O Chiado é o coração cultural de Lisboa, com elegantes ruas comerciais, teatros históricos e praças encantadoras. Este bairro sofisticado oferece fácil acesso aos melhores restaurantes e atrações culturais da cidade.",
        "Príncipe Real": "O Príncipe Real é um bairro sofisticado conhecido pelos seus belos jardins, lojas de antiguidades e boutiques modernas. É perfeito para quem aprecia uma vida refinada no coração da cidade.",
    }
    
    neighborhood = location.get('neighborhood', '')
    city = location.get('city', '')
    
    description = neighborhood_descriptions.get(
        neighborhood, 
        f"{neighborhood} é uma área maravilhosa de {city}, oferecendo aos residentes uma excelente qualidade de vida com ótimas comodidades, boas ligações de transporte e um forte sentido de comunidade. O bairro proporciona fácil acesso a escolas, lojas e instalações recreativas."
    )
    
    return f'<section id="neighborhood"><p>{description}</p></section>'

def generate_call_to_action(data: Dict[str, Any]) -> str:
    """Generate call to action."""
    location = data['location']
    listing_type = data['listing_type']
    
    if listing_type == "sale":
        cta = f"Não perca esta oportunidade—agende já a sua visita e descubra o seu novo lar em {location['city']}."
    else:
        cta = f"Contacte-nos hoje para marcar uma visita e garantir o seu novo lar de arrendamento em {location['city']}."
    
    return f'<p class="call-to-action">{cta}</p>' 