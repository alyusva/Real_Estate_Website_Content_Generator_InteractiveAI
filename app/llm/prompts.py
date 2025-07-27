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
    elif language == "es":
        return f"""
Genera un título SEO optimizado (máximo 60 caracteres) para un anuncio inmobiliario con los siguientes datos:
- Tipo: apartamento de {features.get('bedrooms', '')} habitaciones
- Ubicación: {location['neighborhood']}, {location['city']}
- Tipo de anuncio: {'venta' if listing_type == 'sale' else 'alquiler'}

El título debe:
- Incluir palabras clave como "{features.get('bedrooms', '')} habitaciones", "{location['city']}", "{location['neighborhood']}"
- Ser atractivo y claro
- Tener máximo 60 caracteres
- Estar en español

Responde solo con el título, sin explicaciones.
"""
    else:
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
        highlights.append("varanda" if language == "pt" else "balcón" if language == "es" else "balcony")
    if features.get('elevator'):
        highlights.append("elevador" if language == "pt" else "ascensor" if language == "es" else "elevator")
    if features.get('parking'):
        highlights.append("estacionamento" if language == "pt" else "aparcamiento" if language == "es" else "parking")

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
    elif language == "es":
        return f"""
Genera una meta descripción SEO (máximo 155 caracteres) para un anuncio inmobiliario:
- Apartamento de {features.get('bedrooms', '')} habitaciones en {location['city']}
- Ubicación: {location['neighborhood']}
- Características: {', '.join(highlights[:3]) if highlights else 'apartamento espacioso'}
- Superficie: {features.get('area_sqm', '')} m²

La descripción debe:
- Ser atractiva para buscadores
- Incluir "apartamento de {features.get('bedrooms', '')} habitaciones", "{location['city']}", "{location['neighborhood']}"
- Tener máximo 155 caracteres
- Terminar con algo como "Ideal para familias"
- Estar en español

Responde solo con la meta descripción, sin explicaciones.
"""
    else:
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
    elif language == "es":
        return f"""
Escribe una descripción completa y atractiva (500-700 caracteres) para un apartamento:

DATOS DE LA PROPIEDAD:
- Tipo: apartamento de {features.get('bedrooms', '')} habitaciones
- Ubicación: {location['neighborhood']}, {location['city']}
- Superficie: {features.get('area_sqm', '')} m²
- Habitaciones: {features.get('bedrooms', '')}
- Baños: {features.get('bathrooms', '')}
- Planta: {features.get('floor', 'N/A')}
- Año de construcción: {features.get('year_built', 'N/A')}
- Balcón: {'Sí' if features.get('balcony') else 'No'}
- Ascensor: {'Sí' if features.get('elevator') else 'No'}
- Aparcamiento: {'Sí' if features.get('parking') else 'No'}
- Precio: €{price:,.0f}
- Tipo: {'Venta' if listing_type == 'sale' else 'Alquiler'}

La descripción debe:
- Ser envolvente y persuasiva
- Incluir palabras clave SEO naturalmente: "apartamento de {features.get('bedrooms', '')} habitaciones", "{location['city']}", "{location['neighborhood']}", "inmobiliaria en España"
- Mencionar las características más atractivas
- Tener entre 500-700 caracteres
- Terminar con una frase sobre la ubicación u oportunidad
- Estar en español

Responde solo con la descripción, sin explicaciones.
"""
    else:
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
    elif language == "es":
        return f"""
Escribe una descripción atractiva del barrio {location['neighborhood']} en {location['city']} (aproximadamente 200-300 caracteres):

La descripción debe:
- Resaltar las características únicas del barrio
- Mencionar servicios, transporte o atracciones cercanas
- Ser atractiva para compradores o inquilinos potenciales
- Incluir "{location['neighborhood']}" y "{location['city']}" naturalmente
- Estar en español

Si no conoces detalles específicos del barrio, crea una descripción genérica pero atractiva sobre la zona.

Responde solo con la descripción, sin explicaciones.
"""
    else:
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
    elif language == "es":
        return f"""
Escribe una llamada a la acción (call-to-action) persuasiva para un anuncio inmobiliario en {location['city']}:

Tipo de anuncio: {'Venta' if listing_type == 'sale' else 'Alquiler'}

La llamada debe:
- Ser urgente y persuasiva
- Invitar a contactar o visitar
- Mencionar "{location['city']}"
- Tener aproximadamente 50-80 caracteres
- Estar en español

Responde solo con la llamada a la acción, sin explicaciones.
"""
    else:
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
