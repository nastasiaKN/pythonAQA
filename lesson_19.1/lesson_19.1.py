import requests

def save_mars_photos():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {
        'sol': 1000,
        'camera': 'fhaz',
        'api_key': 'DEMO_KEY'
    }

    response = requests.get(url, params=params)
    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        print("No pictures by set parameters")
    else:
        for i in photos[:5]:
            img_url = i['img_src']
            camera_name = i['camera']['name']
            img = requests.get(img_url).content

            with open(f"mars_photo{camera_name}.jpg", 'wb') as f:
                f.write(img)

            print(f"Saved: mars_photo{camera_name}.jpg")

save_mars_photos()