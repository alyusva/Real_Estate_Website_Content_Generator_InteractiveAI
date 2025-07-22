from typing import Dict, Any

def get_title_prompt(data: Dict[str, Any], language: str) -> str:
    """Generate prompt for title generation."""
    location = data['location']
    features = data['features']
    listing_type = data['listing_type']
    
    if language == "pt":
        return f"""
Gera um título SEO optimizado (máximo 60 caracteres) para um anúncio imobiliário com os seguintes dados:
- Tipo: T{features.get('bedrooms', '')} apartamento
- Localização: {location['neighborhood']}, {location['city']}
- Tipo de anúncio: {'venda' if listing_type == 'sale' else 'arrendamento'}

O título deve:
- Incluir keywords como "T{features.get('bedrooms', '')}", "{location['city']}", "{location['neighborhood']}"
- Ser atrativo e claro
- Ter máximo 60 caracteres
- Ser em português de Portugal

Responde apenas com o título, sem explicações.
"""
    else:  # English
        return f"""
Generate an SEO-optimized title (maximum 60 characters) for a real estate listing with the following data:
- Type: {features.get('bedrooms', '')}-bedroom apartment
- Location: {location['neighborhood']}, {location['city']}
- Listing type: {'sale' if listing_type == 'sale' else 'rent'}

The title should:
- Include keywords like "apartment", "{location['city']}", "{location['neighborhood']}"
- Be attractive and clear
- Have maximum 60 characters
- Be in English

Respond only with the title, no explanations.
"""

def get_meta_description_prompt(data: Dict[str, Any], language: str) -> str:
    """Generate prompt for meta description generation."""
    location = data['location']
    features = data['features']
    listing_type = data['listing_type']
    
    highlights = []
    if features.get('balcony'):
        highlights.append("varanda" if language == "pt" else "balcony")
    if features.get('elevator'):
        highlights.append("elevador" if language == "pt" else "elevator")
    if features.get('parking'):
        highlights.append("estacionamento" if language == "pt" else "parking")
    
    if language == "pt":
        return f"""
Gera uma meta descrição SEO (máximo 155 caracteres) para um anúncio imobiliário:
- Apartamento T{features.get('bedrooms', '')} em {location['city']}
- Localização: {location['neighborhood']}
- Características: {', '.join(highlights[:3]) if highlights else 'apartamento espaçoso'}
- Área: {features.get('area_sqm', '')} m²

A descrição deve:
- Ser atrativa para motores de busca
- Incluir "apartamento T{features.get('bedrooms', '')}", "{location['city']}", "{location['neighborhood']}"
- Ter máximo 155 caracteres
- Terminar com algo como "Ideal para famílias"
- Ser em português de Portugal

Responde apenas com a meta descrição, sem explicações.
"""
    else:  # English
        return f"""
Generate an SEO meta description (maximum 155 characters) for a real estate listing:
- {features.get('bedrooms', '')}-bedroom apartment in {location['city']}
- Location: {location['neighborhood']}
- Features: {', '.join(highlights[:3]) if highlights else 'spacious apartment'}
- Area: {features.get('area_sqm', '')} sqm

The description should:
- Be attractive for search engines
- Include "{features.get('bedrooms', '')}-bedroom apartment", "{location['city']}", "{location['neighborhood']}"
- Have maximum 155 characters
- End with something like "Ideal for families"
- Be in English

Respond only with the meta description, no explanations.
"""

def get_description_prompt(data: Dict[str, Any], language: str) -> str:
    """Generate prompt for full property description."""
    location = data['location']
    features = data['features']
    price = data['price']
    listing_type = data['listing_type']
    
    if language == "pt":
        return f"""
Escreve uma descrição completa e atrativa (500-700 caracteres) para um apartamento:

DADOS DO IMÓVEL:
- Tipo: T{features.get('bedrooms', '')} apartamento
- Localização: {location['neighborhood']}, {location['city']}
- Área: {features.get('area_sqm', '')} m²
- Quartos: {features.get('bedrooms', '')}
- Casas de banho: {features.get('bathrooms', '')}
- Andar: {features.get('floor', 'N/A')}
- Ano de construção: {features.get('year_built', 'N/A')}
- Varanda: {'Sim' if features.get('balcony') else 'Não'}
- Elevador: {'Sim' if features.get('elevator') else 'Não'}
- Estacionamento: {'Sim' if features.get('parking') else 'Não'}
- Preço: €{price:,.0f}
- Tipo: {'Venda' if listing_type == 'sale' else 'Arrendamento'}

A descrição deve:
- Ser envolvente e persuasiva
- Incluir keywords SEO naturalmente: "apartamento T{features.get('bedrooms', '')}", "{location['city']}", "{location['neighborhood']}", "imobiliário em Portugal"
- Mencionar as características mais atrativas
- Ter entre 500-700 caracteres
- Terminar com uma frase sobre a localização ou oportunidade
- Ser em português de Portugal

Responde apenas com a descrição, sem explicações.
"""
    else:  # English
        return f"""
Write a complete and attractive description (500-700 characters) for an apartment:

PROPERTY DATA:
- Type: {features.get('bedrooms', '')}-bedroom apartment
- Location: {location['neighborhood']}, {location['city']}
- Area: {features.get('area_sqm', '')} sqm
- Bedrooms: {features.get('bedrooms', '')}
- Bathrooms: {features.get('bathrooms', '')}
- Floor: {features.get('floor', 'N/A')}
- Year built: {features.get('year_built', 'N/A')}
- Balcony: {'Yes' if features.get('balcony') else 'No'}
- Elevator: {'Yes' if features.get('elevator') else 'No'}
- Parking: {'Yes' if features.get('parking') else 'No'}
- Price: €{price:,.0f}
- Type: {'Sale' if listing_type == 'sale' else 'Rent'}

The description should:
- Be engaging and persuasive
- Include SEO keywords naturally: "{features.get('bedrooms', '')}-bedroom apartment", "{location['city']}", "{location['neighborhood']}", "real estate in Portugal"
- Mention the most attractive features
- Be between 500-700 characters
- End with a sentence about the location or opportunity
- Be in English

Respond only with the description, no explanations.
"""

def get_neighborhood_prompt(data: Dict[str, Any], language: str) -> str:
    """Generate prompt for neighborhood description."""
    location = data['location']
    
    if language == "pt":
        return f"""
Escreve uma descrição atrativa do bairro {location['neighborhood']} em {location['city']} (aproximadamente 200-300 caracteres):

A descrição deve:
- Destacar as características únicas do bairro
- Mencionar comodidades, transporte, ou atrações próximas
- Ser atrativa para potenciais compradores/inquilinos
- Incluir "{location['neighborhood']}" e "{location['city']}" naturalmente
- Ser em português de Portugal

Se não conheceres detalhes específicos do bairro, cria uma descrição genérica mas atrativa sobre a zona.

Responde apenas com a descrição, sem explicações.
"""
    else:  # English
        return f"""
Write an attractive description of the {location['neighborhood']} neighborhood in {location['city']} (approximately 200-300 characters):

The description should:
- Highlight unique characteristics of the neighborhood
- Mention amenities, transport, or nearby attractions
- Be attractive to potential buyers/renters
- Include "{location['neighborhood']}" and "{location['city']}" naturally
- Be in English

If you don't know specific details about the neighborhood, create a generic but attractive description of the area.

Respond only with the description, no explanations.
"""

def get_cta_prompt(data: Dict[str, Any], language: str) -> str:
    """Generate prompt for call-to-action."""
    location = data['location']
    listing_type = data['listing_type']
    
    if language == "pt":
        return f"""
Escreve uma chamada para ação (call-to-action) persuasiva para um anúncio imobiliário em {location['city']}:

Tipo de anúncio: {'Venda' if listing_type == 'sale' else 'Arrendamento'}

A chamada deve:
- Ser urgente e persuasiva
- Incentivar o contacto ou visita
- Mencionar "{location['city']}"
- Ter aproximadamente 50-80 caracteres
- Ser em português de Portugal

Responde apenas com a chamada para ação, sem explicações.
"""
    else:  # English
        return f"""
Write a persuasive call-to-action for a real estate listing in {location['city']}:

Listing type: {'Sale' if listing_type == 'sale' else 'Rent'}

The call-to-action should:
- Be urgent and persuasive
- Encourage contact or viewing
- Mention "{location['city']}"
- Be approximately 50-80 characters
- Be in English

Respond only with the call-to-action, no explanations.
""" 