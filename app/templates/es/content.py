from typing import Dict, Any, List
from ...utils import format_price, get_seo_keywords, truncate_text

def generate_title(data: Dict[str, Any]) -> str:
    location = data['location']
    features = data['features']
    listing_type = data['listing_type']

    bedrooms = features.get('bedrooms', 0)
    property_type = f"{bedrooms} habitaciones" if bedrooms > 0 else "Apartamento"
    action = "en Venta" if listing_type == "sale" else "en Alquiler"

    title = f"{property_type} {action} en {location['neighborhood']}, {location['city']}"
    return f"<title>{truncate_text(title, 60)}</title>"

def generate_meta_description(data: Dict[str, Any]) -> str:
    location = data['location']
    features = data['features']

    bedrooms = features.get('bedrooms', 0)
    area = features.get('area_sqm', 0)

    highlights = []
    if features.get('balcony'):
        highlights.append("balcón")
    if features.get('elevator'):
        highlights.append("ascensor")
    if features.get('parking'):
        highlights.append("aparcamiento")

    highlight_text = f" con {' y '.join(highlights[:2])}" if highlights else ""

    description = f"Amplio apartamento de {bedrooms} habitaciones en {location['city']}{highlight_text}, ubicado en {location['neighborhood']}. Ideal para familias."
    return f'<meta name="description" content="{truncate_text(description, 155)}">'

def generate_h1(data: Dict[str, Any]) -> str:
    location = data['location']
    features = data['features']

    bedrooms = features.get('bedrooms', 0)

    highlights = []
    if features.get('balcony'):
        highlights.append("Balcón")
    if features.get('elevator'):
        highlights.append("Ascensor")

    highlight_text = f" con {highlights[0]}" if highlights else ""

    headline = f"Apartamento de {bedrooms} habitaciones moderno{highlight_text} en {location['neighborhood']}, {location['city']}"
    return f"<h1>{headline}</h1>"

def generate_description(data: Dict[str, Any]) -> str:
    location = data['location']
    features = data['features']
    price = data['price']
    listing_type = data['listing_type']

    bedrooms = features.get('bedrooms', 0)
    bathrooms = features.get('bathrooms', 0)
    area = features.get('area_sqm', 0)
    floor = features.get('floor')
    year_built = features.get('year_built')

    location_desc = f"Situado en el encantador barrio de {location['neighborhood']}"
    property_desc = f"este elegante apartamento de {bedrooms} habitaciones ofrece {area:.0f} m² de espacio luminoso y amplio"

    floor_text = f" en la planta {floor}" if floor else ""
    building_features = []
    if features.get('elevator'):
        building_features.append("acceso por ascensor")
    building_text = f" de un edificio bien conservado con {', '.join(building_features)}" if building_features else ""

    room_desc = f"El apartamento cuenta con {bedrooms} habitaciones, {bathrooms} baños"

    amenities = []
    if features.get('balcony'):
        amenities.append("un balcón privado perfecto para relajarse")
    if features.get('parking'):
        amenities.append("plaza de aparcamiento")

    amenity_text = f", y {', '.join(amenities)}" if amenities else ""

    year_text = f" Construido en {year_built}," if year_built else ""
    price_text = format_price(price, "EUR", "es")
    action = "venta" if listing_type == "sale" else "alquiler"

    description = f"{location_desc}, {property_desc}.{floor_text}{building_text}, {room_desc}{amenity_text}.{year_text} combina comodidades modernas con confort. Con un precio de {action} de {price_text}, esta propiedad en {location['city']} es ideal para familias o profesionales que buscan un hogar bien ubicado."

    if len(description) > 700:
        description = truncate_text(description, 700)
    elif len(description) < 500:
        description += f" No pierdas esta oportunidad de vivir en uno de los barrios más solicitados de {location['city']}."

    return f'<section id="description"><p>{description}</p></section>'

def generate_key_features(data: Dict[str, Any]) -> str:
    location = data['location']
    features = data['features']

    feature_list = []
    if features.get('area_sqm'):
        feature_list.append(f"{features['area_sqm']:.0f} m² de superficie habitable")

    bedrooms = features.get('bedrooms', 0)
    bathrooms = features.get('bathrooms', 0)
    if bedrooms and bathrooms:
        feature_list.append(f"{bedrooms} habitaciones y {bathrooms} baños")

    if features.get('balcony'):
        feature_list.append("Balcón privado")
    if features.get('elevator'):
        feature_list.append("Acceso por ascensor")
    if features.get('parking'):
        feature_list.append("Plaza de aparcamiento")

    feature_list.append(f"Ubicado en {location['neighborhood']}, {location['city']}")

    feature_list = feature_list[:5]

    features_html = '\n'.join([f'  <li>{feature}</li>' for feature in feature_list])
    return f'<ul id="key-features">\n{features_html}\n</ul>'

def generate_neighborhood(data: Dict[str, Any]) -> str:
    location = data['location']

    neighborhood_descriptions = {
        "Salamanca": "Salamanca es uno de los barrios más exclusivos de Madrid, conocido por sus boutiques de lujo, restaurantes gourmet y arquitectura señorial.",
        "Malasaña": "Malasaña destaca por su ambiente alternativo, vida nocturna vibrante y una amplia oferta cultural en el corazón de Madrid.",
        "Chamberí": "Chamberí combina tradición y modernidad con sus calles tranquilas, plazas acogedoras y una gran oferta gastronómica."
    }

    neighborhood = location.get('neighborhood', '')
    city = location.get('city', '')

    description = neighborhood_descriptions.get(
        neighborhood,
        f"{neighborhood} es una zona excelente de {city}, que ofrece una alta calidad de vida con buenas conexiones, servicios cercanos y un ambiente acogedor."
    )

    return f'<section id="neighborhood"><p>{description}</p></section>'

def generate_call_to_action(data: Dict[str, Any]) -> str:
    location = data['location']
    listing_type = data['listing_type']

    if listing_type == "sale":
        cta = f"No dejes pasar esta oportunidad—agenda tu visita y descubre tu nuevo hogar en {location['city']}."
    else:
        cta = f"Contáctanos hoy para concertar una visita y asegurar tu nuevo hogar en alquiler en {location['city']}."

    return f'<p class="call-to-action">{cta}</p>'