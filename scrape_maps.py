import requests

API_KEY = 'AIzaSyDpo2demSgUbDPIBCr6kw-JZ1LmmBXWQmk'
location = '42.9878533,-81.1678841'  # London, Ontario
radius = 1000  # meters
type = 'restaurant'

url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&key={API_KEY}'

response = requests.get(url)
places = response.json()['results']

for place in places:
    print(place['name'], place.get('vicinity'))
