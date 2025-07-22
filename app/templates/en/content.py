from typing import Dict, Any, List
from ...utils import format_price, get_seo_keywords, truncate_text

def generate_title(data: Dict[str, Any]) -> str:
    """Generate SEO-optimized title (max 60 chars)."""
    location = data['location']
    features = data['features']
    listing_type = data['listing_type']
    
    bedrooms = features.get('bedrooms', 0)
    property_type = f"T{bedrooms}" if bedrooms > 0 else "Apartment"
    action = "for Sale" if listing_type == "sale" else "for Rent"
    
    title = f"{property_type} Apartment {action} in {location['neighborhood']}, {location['city']}"
    return f"<title>{truncate_text(title, 60)}</title>"

def generate_meta_description(data: Dict[str, Any]) -> str:
    """Generate meta description (max 155 chars)."""
    location = data['location']
    features = data['features']
    
    bedrooms = features.get('bedrooms', 0)
    area = features.get('area_sqm', 0)
    
    highlights = []
    if features.get('balcony'):
        highlights.append("balcony")
    if features.get('elevator'):
        highlights.append("elevator")
    if features.get('parking'):
        highlights.append("parking")
    
    highlight_text = f" with {' and '.join(highlights[:2])}" if highlights else ""
    
    description = f"Spacious {bedrooms}-bedroom apartment in {location['city']}{highlight_text}, located in {location['neighborhood']}. Ideal for families."
    return f'<meta name="description" content="{truncate_text(description, 155)}">'

def generate_h1(data: Dict[str, Any]) -> str:
    """Generate main headline."""
    location = data['location']
    features = data['features']
    
    bedrooms = features.get('bedrooms', 0)
    
    highlights = []
    if features.get('balcony'):
        highlights.append("Balcony")
    if features.get('elevator'):
        highlights.append("Elevator Access")
    
    highlight_text = f" with {highlights[0]}" if highlights else ""
    
    headline = f"Modern T{bedrooms} Apartment{highlight_text} in {location['neighborhood']}, {location['city']}"
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
    location_desc = f"Located in the charming neighborhood of {location['neighborhood']}"
    property_desc = f"this elegant T{bedrooms} apartment offers {area:.0f} sqm of bright and spacious living"
    
    floor_text = f" on the {floor}{'nd' if floor == 2 else 'rd' if floor == 3 else 'th'} floor" if floor else ""
    building_features = []
    if features.get('elevator'):
        building_features.append("elevator access")
    building_text = f" of a well-maintained building with {', '.join(building_features)}" if building_features else ""
    
    room_desc = f"The apartment features {bedrooms} bedrooms, {bathrooms} bathrooms"
    
    amenities = []
    if features.get('balcony'):
        amenities.append("a private balcony perfect for relaxing")
    if features.get('parking'):
        amenities.append("parking space")
    
    amenity_text = f", and {', '.join(amenities)}" if amenities else ""
    
    year_text = f" Built in {year_built}," if year_built else ""
    price_text = format_price(price, "EUR", "en")
    action = "sale" if listing_type == "sale" else "rental"
    
    description = f"{location_desc}, {property_desc}.{floor_text}{building_text}, {room_desc}{amenity_text}.{year_text} it combines modern amenities with timeless comfort. With a {action} price of {price_text}, this {location['city']} property is ideal for families or professionals looking for a well-located home in the capital."
    
    # Ensure it's between 500-700 characters
    if len(description) > 700:
        description = truncate_text(description, 700)
    elif len(description) < 500:
        description += f" Don't miss this opportunity to live in one of {location['city']}'s most sought-after neighborhoods."
    
    return f'<section id="description"><p>{description}</p></section>'

def generate_key_features(data: Dict[str, Any]) -> str:
    """Generate key features list (3-5 bullet points)."""
    location = data['location']
    features = data['features']
    
    feature_list = []
    
    # Area
    if features.get('area_sqm'):
        feature_list.append(f"{features['area_sqm']:.0f} sqm of living space")
    
    # Bedrooms and bathrooms
    bedrooms = features.get('bedrooms', 0)
    bathrooms = features.get('bathrooms', 0)
    if bedrooms and bathrooms:
        feature_list.append(f"{bedrooms} bedrooms and {bathrooms} bathrooms")
    
    # Special features
    if features.get('balcony'):
        feature_list.append("Private balcony")
    if features.get('elevator'):
        feature_list.append("Elevator access")
    if features.get('parking'):
        feature_list.append("Parking space")
    
    # Location
    feature_list.append(f"Located in {location['neighborhood']}, {location['city']}")
    
    # Limit to 5 features
    feature_list = feature_list[:5]
    
    features_html = '\n'.join([f'  <li>{feature}</li>' for feature in feature_list])
    return f'<ul id="key-features">\n{features_html}\n</ul>'

def generate_neighborhood(data: Dict[str, Any]) -> str:
    """Generate neighborhood summary."""
    location = data['location']
    
    # Generic neighborhood descriptions - in real implementation, this could be enhanced with actual data
    neighborhood_descriptions = {
        "Campo de Ourique": "Campo de Ourique is one of Lisbon's most desirable neighborhoods, known for its vibrant cafés, green parks, and excellent schools. With a strong local community and easy access to the city center, it offers the perfect blend of charm and convenience.",
        "Chiado": "Chiado is the cultural heart of Lisbon, featuring elegant shopping streets, historic theaters, and charming plazas. This sophisticated neighborhood offers easy access to the city's best restaurants and cultural attractions.",
        "Principe Real": "Principe Real is an upscale neighborhood known for its beautiful gardens, antique shops, and trendy boutiques. It's perfect for those who appreciate refined living in the heart of the city.",
    }
    
    neighborhood = location.get('neighborhood', '')
    city = location.get('city', '')
    
    description = neighborhood_descriptions.get(
        neighborhood, 
        f"{neighborhood} is a wonderful area of {city}, offering residents a great quality of life with excellent amenities, good transport connections, and a strong sense of community. The neighborhood provides easy access to schools, shops, and recreational facilities."
    )
    
    return f'<section id="neighborhood"><p>{description}</p></section>'

def generate_call_to_action(data: Dict[str, Any]) -> str:
    """Generate call to action."""
    location = data['location']
    listing_type = data['listing_type']
    
    if listing_type == "sale":
        cta = f"Don't miss this opportunity—schedule your viewing today and discover your new home in {location['city']}."
    else:
        cta = f"Contact us today to arrange a viewing and secure your new rental home in {location['city']}."
    
    return f'<p class="call-to-action">{cta}</p>' 