#!/usr/bin/env python3
"""
Example script demonstrating the Real Estate Content Generator API.
Also, this script shows how to use the API with sample data from the challenge.
"""

import json
import requests
from app.schemas import PropertyInput
from app.generator import generate_content

def test_local_generation():
    """Test content generation without API server."""
    print("=== LOCAL CONTENT GENERATION TEST ===\n")
    
    # Example data
    sample_data = {
        "title": "T3 apartment in Lisbon",
        "location": {
            "city": "Lisbon",
            "neighborhood": "Campo de Ourique"
        },
        "features": {
            "bedrooms": 3,
            "bathrooms": 2,
            "area_sqm": 120,
            "balcony": True,
            "parking": False,
            "elevator": True,
            "floor": 2,
            "year_built": 2005
        },
        "price": 650000,
        "listing_type": "sale",
        "language": "en"
    }
    
    # Test English generation
    print("ENGLISH CONTENT:")
    print("=" * 60)
    property_input = PropertyInput(**sample_data)
    english_content = generate_content(property_input)
    print(english_content)
    print("\n" + "=" * 60)

    # Test Portuguese generation
    print("\nPORTUGUESE CONTENT:")
    print("=" * 60)
    sample_data["language"] = "pt"
    property_input_pt = PropertyInput(**sample_data)
    portuguese_content = generate_content(property_input_pt)
    print(portuguese_content)
    print("\n" + "=" * 60)

    # Test Spanish generation
    print("\nSPANISH CONTENT:")
    print("=" * 60)
    sample_data["language"] = "es"
    property_input_es = PropertyInput(**sample_data)
    spanish_content = generate_content(property_input_es)
    print(spanish_content)
    print("\n" + "=" * 60)

def test_api_endpoint():
    """Test the API endpoint (requires server to be running)."""
    print("\n=== API ENDPOINT TEST ===\n")
    
    sample_data = {
        "title": "T3 apartment in Lisbon",
        "location": {
            "city": "Lisbon",
            "neighborhood": "Campo de Ourique"
        },
        "features": {
            "bedrooms": 3,
            "bathrooms": 2,
            "area_sqm": 120,
            "balcony": True,
            "parking": False,
            "elevator": True,
            "floor": 2,
            "year_built": 2005
        },
        "price": 650000,
        "listing_type": "sale",
        "language": "en"
    }
    
    try:
        # Test API call
        response = requests.post(
            "http://localhost:8000/generate",
            json=sample_data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API Response successful!")
            print("Generated content:")
            print("-" * 40)
            print(result["content"])
        else:
            print(f"❌ API Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to API server.")
        print("Start the server with: uvicorn app.main:app --reload")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_edge_cases():
    """Test edge cases and missing data handling."""
    print("\n=== EDGE CASES TEST ===\n")
    
    # Test with minimal data
    minimal_data = {
        "title": "Studio apartment",
        "location": {
            "city": "Porto",
            "neighborhood": "Cedofeita"
        },
        "features": {
            "bedrooms": 1,
            "bathrooms": 1,
            "area_sqm": 45
            # Missing: balcony, parking, elevator, floor, year_built
        },
        "price": 200000,
        "listing_type": "sale",
        "language": "en"
    }
    
    print("MINIMAL DATA TEST (missing optional fields):")
    print("-" * 50)
    property_input = PropertyInput(**minimal_data)
    minimal_content = generate_content(property_input)
    print(minimal_content)
    print("\n" + "-" * 50)

if __name__ == "__main__":
    # Run all tests
    test_local_generation()
    test_edge_cases()
    test_api_endpoint()
    
    print("\nExample completed!!!!")
    print("To start the API server, run:")
    print("  uvicorn app.main:app --reload")
    print("\nThen test with:")
    print("  curl -X POST http://localhost:8000/generate \\")
    print("    -H 'Content-Type: application/json' \\")
    print("    -d @example_data.json") 