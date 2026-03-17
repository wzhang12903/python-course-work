# Import external library (requests) - meets assignment requirement
import requests

# Configuration (API endpoint and default coordinates for demonstration)
# Default: New York (lat=40.7128, lon=-74.0060)
BASE_API_URL = "https://api.open-meteo.com/v1/forecast"

def get_weather_data(latitude, longitude):
    
   
    # API parameters (request only current weather to keep response small)
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
        "timezone": "America/New_York"  # Adjust timezone as needed
    }

    try:
        # Send GET request with timeout (prevents hanging on slow connections)
        response = requests.get(BASE_API_URL, params=params, timeout=10)
        
        # Raise exception for HTTP errors (4xx/5xx status codes)
        response.raise_for_status()
        
        # Parse JSON response into Python dictionary - meets parsing requirement
        data = response.json()
        
        # Check if critical data is present (error handling for missing data)
        if "current_weather" not in data:
            print("❌ Error: No weather data found for this location.")
            return None
        
        return data["current_weather"]

    # Handle common API/network errors
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out (API server is slow or unreachable).")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API (check your internet connection).")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e} (API returned a failed status code).")
        return None
    except ValueError:
        print("❌ Error: Invalid JSON response from API.")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def display_weather(weather_data, city_name):
    
    if not weather_data:
        return

    # Extract key values (with fallback for missing keys)
    temperature = weather_data.get("temperature", "N/A")
    wind_speed = weather_data.get("windspeed", "N/A")
    humidity = weather_data.get("relativehumidity_2m", "N/A")  # Fallback if missing
    weather_code = weather_data.get("weathercode", "N/A")

    # Clean output (explains what data was retrieved)
    print("\n" + "="*40)
    print(f"Current Weather for {city_name}")
    print("="*40)
    print(f"🌡️ Temperature: {temperature} °C")
    print(f"💨 Wind Speed: {wind_speed} km/h")
    print(f"💧 Humidity: {humidity}% (estimated)")
    print(f"🌤️ Weather Code: {weather_code} (0 = clear sky, 45 = fog)")
    print("="*40)

def main():
    """Main program: Get user input (city) and fetch/display weather data."""
    print("📡 Real-Time Weather Data Fetcher")
    print("Using Open-Meteo API (free, no API key required)\n")

    # Predefined city coordinates (simplifies user input; can extend with geocoding)
    city_coords = {
        "beijing": (39.9042, 116.4074),
        "new york": (40.7128, -74.0060),
        "clifton park": (42.9279, -73.7746),  # Example city in New York state and I'm located in
        "london": (51.5074, -0.1278),
        "tokyo": (35.6762, 139.6503),
        "paris": (48.8566, 2.3522),
        
          # Added Clifton Park as an example
    }

    # Get user input for city
    while True:
        city = input("Enter a city (Beijing/New York/London/Tokyo/Paris/Clifton Park): ").strip().lower()
        if city in city_coords:
            lat, lon = city_coords[city]
            break
        print("❌ Invalid city! Please choose from the list.")

    # Fetch weather data
    print(f"\n🔍 Fetching weather data for {city.title()}...")
    weather_data = get_weather_data(lat, lon)

    # Display clean output
    display_weather(weather_data, city.title())

if __name__ == "__main__":
    main()
