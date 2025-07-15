import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open your sheet
sheet = client.open("YourSheetName").sheet1

# Google Places API key
API_KEY = 'AIzaSyDpo2demSgUbDPIBCr6kw-JZ1LmmBXWQmk'

# 1. Search nearby places
location = "37.7749,-122.4194"  # Example: San Francisco
radius = 1000
type = "restaurant"

nearby_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&key={API_KEY}"

nearby_resp = requests.get(nearby_url).json()

# 2. Loop through places and get full details
for place in nearby_resp["results"]:
    place_id = place["place_id"]
    details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,formatted_address,website,rating,user_ratings_total,reviews&key={API_KEY}"
    details_resp = requests.get(details_url).json()
    result = details_resp["result"]

    name = result.get("name")
    address = result.get("formatted_address")
    website = result.get("website")
    rating = result.get("rating")
    total_reviews = result.get("user_ratings_total")
    reviews = result.get("reviews", [])

    # Example: take the first review text
    review_text = reviews[0]["text"] if reviews else ""

    # Save to Google Sheets
    sheet.append_row([name, address, website, rating, total_reviews, review_text])
