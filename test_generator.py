"""
Quick test script to verify the affidavit generator works locally
"""

import requests
import json

# Test data
test_data = {
    "name": "Rajesh Kumar Singh",
    "father_name": "Suresh Kumar Singh",
    "mother_name": "Sunita Singh",
    "spouse_name": "Priya Singh",
    "dob": "15/08/1985",
    "address": "Flat No. 301, Ashoka Apartments, MG Road, Mumbai - 400001",
    "residence_from": "2015",
    "place": "Mumbai",
    "date": "29/12/2025"
}

def test_health_check(base_url):
    """Test the health check endpoint"""
    print("🔍 Testing health check...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"✅ Health check: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {str(e)}")
        return False

def test_pdf_generation(base_url):
    """Test PDF generation"""
    print("\n📄 Testing PDF generation...")
    try:
        response = requests.post(
            f"{base_url}/api/generate-affidavit",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            # Save the PDF
            with open("test_affidavit.pdf", "wb") as f:
                f.write(response.content)
            print("✅ PDF generated successfully!")
            print("📥 Saved as: test_affidavit.pdf")
            return True
        else:
            print(f"❌ PDF generation failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ PDF generation error: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 AFFIDAVIT GENERATOR LOCAL TEST")
    print("=" * 60)
    
    # Test with local server
    base_url = "http://localhost:5000"
    
    print(f"\nTesting against: {base_url}")
    print("\n⚠️  Make sure the Flask server is running!")
    print("   Run: python app.py\n")
    
    input("Press Enter when server is ready...")
    
    # Run tests
    health_ok = test_health_check(base_url)
    
    if health_ok:
        pdf_ok = test_pdf_generation(base_url)
        
        if pdf_ok:
            print("\n" + "=" * 60)
            print("🎉 ALL TESTS PASSED!")
            print("=" * 60)
            print("\n✅ Your affidavit generator is working correctly!")
            print("✅ Ready to deploy to Render")
        else:
            print("\n" + "=" * 60)
            print("⚠️  PDF GENERATION FAILED")
            print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ SERVER NOT RESPONDING")
        print("=" * 60)
        print("\nMake sure you:")
        print("1. Installed dependencies: pip install -r requirements.txt")
        print("2. Started the server: python app.py")
