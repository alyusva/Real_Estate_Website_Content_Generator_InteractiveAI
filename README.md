# Real Estate Website Content Generator (InteractiveAI)

🏠 **REST API for automatic generation of SEO-optimized content for real estate listings**

This solution implements the **AI Engineer Technical Challenge** to generate high-quality web content for real estate listings, with multilingual support and SEO optimization.

## 🎯 **Main Features**

✅ **Generates exactly 7 HTML sections** as required by the challenge  
✅ **3 generation modes**: Template, OpenAI, and Ollama  
✅ **Multilingual support** (English, Portuguese, and Spanish)  
✅ **SEO optimization** with natural keywords  
✅ **Robust handling** of missing data  
✅ **Character limit validation**  
✅ **Modular and well-documented architecture**  
✅ **Automatic fallback** if LLM generation fails  

## 🤖 **Generation Modes**

### 1. **Template Mode** (Default)
- Uses predefined templates and programmatic logic
- No external dependencies required
- Fast and reliable
- Ideal for stable production

### 2. **OpenAI Mode**
- Uses the OpenAI API (GPT-4o-mini by default)
- More creative and natural content
- Requires OpenAI API key
- Ideal for highest content quality

### 3. **Ollama Mode**
- Uses local models via Ollama
- Full privacy (no external data sent)
- Requires local Ollama server
- Ideal for privacy-restricted environments

## 📦 **Installation**

```bash
# Clone the repository
git clone <repository-url>
cd Real_Estate_Website_Content_Generator_InteractiveAI

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## ⚙️ **Configuration**

### 1. Create configuration file
```bash
cp .env.example .env
```

### 2. Edit `.env` according to the desired mode:

#### **Template Mode** (default):
```env
GENERATION_MODE=template
```

#### **OpenAI Mode**:
```env
GENERATION_MODE=openai
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

#### **Ollama Mode**:
```env
GENERATION_MODE=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

### 3. Configure Ollama (only if using Ollama mode)

#### Option A: Native installation
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Download model
ollama pull llama3.2

# Start server (port 11434)
ollama serve
```

#### Option B: Docker
```bash
# Run Ollama in Docker
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# Download model
docker exec -it ollama ollama pull llama3.2
```

## 🚀 **Running**

### Start the server
```bash
uvicorn app.main:app --reload
```

The server will be available at: `http://localhost:8000`

### Check status
```bash
curl http://localhost:8000/status
```

Response:
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

### Test all modes
```bash
python example_multi_mode.py
```

### Test specific mode
```bash
# Change GENERATION_MODE in .env
python example.py
```

### Test via API
```bash
curl -X POST http://localhost:8000/generate \
  -H 'Content-Type: application/json' \
  -d @example_data.json
```

## 🔄 **API Usage**

### Available endpoints

#### **GET** `/status` - Current status and configuration
#### **POST** `/generate` - Generates SEO-optimized content

### Input structure (JSON)
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

## 📋 **The 7 generated sections**

1. **`<title>`** - Page title (max 60 characters)
2. **`<meta name="description">`** - SEO meta description (max 155 characters)
3. **`<h1>`** - Main headline
4. **`<section id="description">`** - Full description (500-700 characters)
5. **`<ul id="key-features">`** - Key features list (3-5 bullet points)
6. **`<section id="neighborhood">`** - Neighborhood summary
7. **`<p class="call-to-action">`** - Call to action

## 🌍 **Multilingual support**

### English (`"language": "en"`)
- Keywords: "apartment for sale in Lisbon", "real estate in Portugal"
- Price format: €650,000
- Vocabulary: bedrooms, bathrooms, elevator access

### Portuguese (`"language": "pt"`)
- Keywords: "apartamento para venda em Lisboa", "imobiliário em Portugal"
- Price format: €650.000
- Vocabulary: quartos, casas de banho, acesso por elevador

### Spanish (`"language": "es"`)
- Keywords: "apartamento en venta en Lisboa", "inmobiliaria en Portugal"
- Price format: €650.000
- Vocabulary: habitaciones, baños, ascensor, balcón

## 🏗️ **Project architecture**

```
app/
├── main.py              # FastAPI entry point
├── routes.py            # Endpoint definitions
├── schemas.py           # Pydantic models
├── config.py            # Configuration and environment variables
├── generator.py         # Main generation logic
├── utils.py             # Helper functions
├── llm/                 # LLM generators
│   ├── prompts.py       # Optimized prompts for each section
│   ├── openai_generator.py   # OpenAI generator
│   └── ollama_generator.py   # Ollama generator
└── templates/           # Template generators
    ├── en/content.py    # English templates
    └── pt/content.py    # Portuguese templates
.env                     # Environment configuration
requirements.txt         # Dependencies
example_multi_mode.py    # Test for all 3 modes
README.md               # This documentation
```

## 🔧 **Advanced features**

### Automatic fallback
- If OpenAI/Ollama fail, the system automatically uses template mode
- Ensures service availability at all times

### Optimized prompts
- Section-specific prompts (title, description, etc.)
- Adapted for English and Portuguese
- SEO and character limit optimized

### Real-time validation
- Configuration check at server startup
- Character limit validation
- Error handling with descriptive messages

## 🚀 **Mode advantages**

| Aspect      | Template      | OpenAI         | Ollama        |
|-------------|--------------|----------------|---------------|
| **Speed**   | ⚡ Very fast  | 🐌 Slow (API)  | 🐎 Medium     |
| **Quality** | ✅ Good       | 🌟 Excellent   | ⭐ Very good   |
| **Creativity** | 📏 Limited | 🎨 High        | 🎭 High       |
| **Cost**    | 💰 Free       | 💸 Pay per use | 💰 Free       |
| **Privacy** | 🔒 Full       | ⚠️ Data to OpenAI | 🔒 Full   |
| **Dependencies** | ✅ None  | 🌐 Internet + API | 🖥️ Local server |
| **Consistency** | 📊 High   | 🎲 Variable    | 🎲 Variable   |

## 💡 **Recommended use cases**

- **Template**: Mass production, high availability, low cost
- **OpenAI**: Premium content, highest quality, special cases
- **Ollama**: Critical privacy, offline, local development

## 🎯 **Evaluation criteria met**

- ✅ **Structure compliance**: Exactly 7 HTML sections
- ✅ **Language fluency**: Natural content (especially with LLMs)
- ✅ **SEO effectiveness**: Keywords integrated organically
- ✅ **Multilingual adaptability**: Native English, Portuguese, and Spanish
- ✅ **Code design**: Modular and extensible architecture
- ✅ **Robustness**: Automatic fallback and error handling
- ✅ **Scalability**: Multiple generation modes
- ✅ **AI Engineering**: Real LLM integration with fallbacks

## 📊 **Output comparison**

### Template Mode (Fixed structure, fast)
```html
<title>T3 Apartment for Sale in Campo de Ourique, Lisbon</title>
<meta name="description" content="Spacious 3-bedroom apartment in Lisbon with balcony and elevator...">
```

### OpenAI Mode (Dynamic, creative content)
```html
<title>Stunning T3 Haven in Historic Campo de Ourique</title>
<meta name="description" content="Discover this exceptional 3-bedroom sanctuary in Lisbon's beloved Campo de Ourique...">
```

### Ollama Mode (Balance between creativity and control)
```html
<title>Premium T3 Apartment - Campo de Ourique, Lisbon</title>
<meta name="description" content="Elegant 3-bedroom residence featuring modern amenities in Campo de Ourique...">
```


## 🧩 **Examples and interactive tests**

The repository includes several files to facilitate testing and demonstration:

### `example.py`
- Allows you to test content generation locally and against the REST API.
- Generates content in English, Portuguese, and Spanish using sample data.
- Includes edge case tests (minimal or incomplete data).
- Useful for quickly checking generation and system robustness.

**Usage:**
```bash
python example.py
```

### `example_multi_mode.py`
- Demonstrates and tests all three generation modes: Template, OpenAI, and Ollama.
- Runs examples in all three languages and shows a configuration guide.
- Automatically changes the generation mode before each test.
- Useful for validating integration and results of each mode.

**Usage:**
```bash
python example_multi_mode.py
```

### `RealEstateContentInteractiveDemo.ipynb`
- Interactive notebook to visually test content generation.
- Lets you choose generation mode and language with dropdowns.
- Allows uploading a JSON file or filling out a visual form.
- Shows the generated HTML as text and as rendered HTML.
- Ideal for demos, quick tests, and result exploration.

**Usage:**
Open the notebook in VS Code or JupyterLab and run the cells.
---

**Developed by**: Alvaro Yuste Valles  
**Development time**: ~8-10 hours  
**Challenge**: AI Engineer Technical Challenge - Real Estate Content Generator  
**Version**: 2.0.0 (Multi-mode AI Generation)
