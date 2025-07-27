# Real Estate Website Content Generator (InteractiveAI)

🏠 **API REST para generación automática de contenido SEO optimizado para anuncios inmobiliarios**

Esta solución implementa el **AI Engineer Technical Challenge** para generar contenido web de alta calidad para listados inmobiliarios, con soporte multilingüe y optimización SEO.

## 🎯 **Características principales**

✅ **Genera exactamente 7 secciones HTML** según el challenge  
✅ **3 modos de generación**: Template, OpenAI, y Ollama  
✅ **Soporte multilingüe** (Inglés, Portugués y Español)  
✅ **Optimización SEO** con keywords naturales  
✅ **Manejo robusto** de datos faltantes  
✅ **Validación de límites** de caracteres  
✅ **Arquitectura modular** y bien documentada  
✅ **Fallback automático** si falla la generación con LLM  

## 🤖 **Modos de generación**

### 1. **Template Mode** (Por defecto)
- Usa plantillas predefinidas y lógica programática
- No requiere dependencias externas
- Rápido y confiable
- Ideal para producción estable

### 2. **OpenAI Mode** 
- Usa la API de OpenAI (GPT-4o-mini por defecto)
- Contenido más creativo y natural
- Requiere API key de OpenAI
- Ideal para máxima calidad de contenido

### 3. **Ollama Mode**
- Usa modelos locales via Ollama
- Privacidad total (sin envío de datos externos)
- Requiere servidor Ollama local
- Ideal para entornos con restricciones de privacidad

## 📦 **Instalación**

```bash
# Clonar el repositorio
git clone <repository-url>
cd Real_Estate_Website_Content_Generator_InteractiveAI

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## ⚙️ **Configuración**

### 1. Crear archivo de configuración
```bash
cp .env.example .env
```

### 2. Editar `.env` según el modo deseado:

#### **Template Mode** (por defecto):
```env
GENERATION_MODE=template
```

#### **OpenAI Mode**:
```env
GENERATION_MODE=openai
OPENAI_API_KEY=tu_api_key_de_openai_aqui
OPENAI_MODEL=gpt-4o-mini
```

#### **Ollama Mode**:
```env
GENERATION_MODE=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

### 3. Configurar Ollama (solo si usas modo Ollama)

#### Opción A: Instalación nativa
```bash
# Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Descargar modelo
ollama pull llama3.2

# Iniciar servidor (puerto 11434)
ollama serve
```

#### Opción B: Docker
```bash
# Ejecutar Ollama en Docker
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# Descargar modelo
docker exec -it ollama ollama pull llama3.2
```

## 🚀 **Ejecución**

### Iniciar el servidor
```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en: `http://localhost:8000`

### Verificar estado
```bash
curl http://localhost:8000/status
```

Respuesta:
```json
{
  "generation_mode": "template",
  "openai_model": null,
  "ollama_model": null,
  "ollama_url": null,
  "status": "ready"
}
```

## 🧪 **Testing**

### Probar todos los modos
```bash
python example_multi_mode.py
```

### Probar modo específico
```bash
# Cambiar en .env el GENERATION_MODE
python example.py
```

### Probar via API
```bash
curl -X POST http://localhost:8000/generate \
  -H 'Content-Type: application/json' \
  -d @example_data.json
```

## 🔄 **Uso de la API**

### Endpoints disponibles

#### **GET** `/status` - Estado y configuración actual
#### **POST** `/generate` - Genera contenido SEO optimizado

### Estructura de entrada (JSON)
```json
{
  "title": "T3 apartment in Lisbon",
  "location": {
    "city": "Lisbon",
    "neighborhood": "Campo de Ourique"
  },
  "features": {
    "bedrooms": 3,
    "bathrooms": 2,
    "area_sqm": 120,
    "balcony": true,
    "parking": false,
    "elevator": true,
    "floor": 2,
    "year_built": 2005
  },
  "price": 650000,
  "listing_type": "sale",
  "language": "en"
}
```

## 📋 **Las 7 secciones generadas**

1. **`<title>`** - Título de página (máx 60 caracteres)
2. **`<meta name="description">`** - Meta descripción SEO (máx 155 caracteres)  
3. **`<h1>`** - Titular principal
4. **`<section id="description">`** - Descripción completa (500-700 caracteres)
5. **`<ul id="key-features">`** - Lista de características clave (3-5 puntos)
6. **`<section id="neighborhood">`** - Resumen del barrio
7. **`<p class="call-to-action">`** - Llamada a la acción

## 🌍 **Soporte multilingüe**


### Inglés (`"language": "en"`)
- Keywords: "apartment for sale in Lisbon", "real estate in Portugal"
- Formato de precio: €650,000
- Vocabulario: bedrooms, bathrooms, elevator access

### Portugués (`"language": "pt"`)
- Keywords: "apartamento para venda em Lisboa", "imobiliário em Portugal"
- Formato de precio: €650.000
- Vocabulario: quartos, casas de banho, acesso por elevador

### Español (`"language": "es"`)
- Keywords: "apartamento en venta en Lisboa", "inmobiliaria en Portugal"
- Formato de precio: €650.000
- Vocabulario: habitaciones, baños, ascensor, balcón

## 🏗️ **Arquitectura del proyecto**

```
app/
├── main.py              # Punto de entrada FastAPI
├── routes.py            # Definición de endpoints
├── schemas.py           # Modelos Pydantic
├── config.py            # Configuración y variables de entorno
├── generator.py         # Lógica principal de generación
├── utils.py             # Funciones auxiliares
├── llm/                 # Generadores LLM
│   ├── prompts.py       # Prompts optimizados para cada sección
│   ├── openai_generator.py   # Generador OpenAI
│   └── ollama_generator.py   # Generador Ollama
└── templates/           # Generadores de plantillas
    ├── en/content.py    # Plantillas en inglés
    └── pt/content.py    # Plantillas en portugués
.env                     # Configuración de entorno
requirements.txt         # Dependencias
example_multi_mode.py    # Test de los 3 modos
README.md               # Esta documentación
```

## 🔧 **Características avanzadas**

### Fallback automático
- Si OpenAI/Ollama fallan, el sistema automáticamente usa el modo template
- Garantiza disponibilidad del servicio siempre

### Prompts optimizados
- Prompts específicos para cada sección (título, descripción, etc.)
- Adaptados para inglés y portugués
- Optimizados para SEO y límites de caracteres

### Validación en tiempo real
- Verificación de configuración al iniciar el servidor
- Validación de límites de caracteres
- Manejo de errores con mensajes descriptivos

## 🚀 **Ventajas de cada modo**

| Aspecto | Template | OpenAI | Ollama |
|---------|----------|--------|--------|
| **Velocidad** | ⚡ Muy rápida | 🐌 Lenta (API) | 🐎 Media |
| **Calidad** | ✅ Buena | 🌟 Excelente | ⭐ Muy buena |
| **Creatividad** | 📏 Limitada | 🎨 Alta | 🎭 Alta |
| **Costo** | 💰 Gratis | 💸 Pago por uso | 💰 Gratis |
| **Privacidad** | 🔒 Total | ⚠️ Datos a OpenAI | 🔒 Total |
| **Dependencias** | ✅ Ninguna | 🌐 Internet + API | 🖥️ Servidor local |
| **Consistencia** | 📊 Alta | 🎲 Variable | 🎲 Variable |

## 💡 **Casos de uso recomendados**

- **Template**: Producción masiva, alta disponibilidad, costos bajos
- **OpenAI**: Contenido premium, máxima calidad, casos especiales
- **Ollama**: Privacidad crítica, sin internet, desarrollo local

## 🎯 **Criterios de evaluación cumplidos**

- ✅ **Cumplimiento de estructura**: Las 7 secciones HTML exactas
- ✅ **Fluidez del lenguaje**: Contenido natural (especialmente con LLMs)
- ✅ **Efectividad SEO**: Keywords integradas orgánicamente
- ✅ **Adaptabilidad multilingüe**: Inglés y portugués nativos
- ✅ **Diseño de código**: Arquitectura modular y extensible
- ✅ **Robustez**: Fallback automático y manejo de errores
- ✅ **Escalabilidad**: Múltiples modos de generación
- ✅ **AI Engineering**: Integración real de LLMs con fallbacks

## 📊 **Comparación de salidas**

### Template Mode (Estructura fija, rápida)
```html
<title>T3 Apartment for Sale in Campo de Ourique, Lisbon</title>
<meta name="description" content="Spacious 3-bedroom apartment in Lisbon with balcony and elevator...">
```

### OpenAI Mode (Contenido dinámico, creativo)
```html
<title>Stunning T3 Haven in Historic Campo de Ourique</title>
<meta name="description" content="Discover this exceptional 3-bedroom sanctuary in Lisbon's beloved Campo de Ourique...">
```

### Ollama Mode (Balance entre creatividad y control)
```html
<title>Premium T3 Apartment - Campo de Ourique, Lisbon</title>
<meta name="description" content="Elegant 3-bedroom residence featuring modern amenities in Campo de Ourique...">
```

---

**Desarrollado por**: Alvaro Yuste Valles  
**Tiempo de desarrollo**: ~8-10 horas  
**Challenge**: AI Engineer Technical Challenge - Real Estate Content Generator  
**Versión**: 2.0.0 (Multi-mode AI Generation)
