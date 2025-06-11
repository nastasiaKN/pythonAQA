import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

response = requests.get(url, params=params)
data = response.json()

photos = data['photos']

if not photos:
    print("No pictures by set parameters")
else:
    for i in range(min(5, len(photos))):
        img_url = photos[i]['img_src']
        img = requests.get(img_url).content

        with open(f'mars_photo{i+1}.jpg', 'wb') as f:
            f.write(img)

        print(f'Saved: mars_photo{i+1}.jpg')
