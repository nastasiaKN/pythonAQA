import requests
import allure

@allure.feature("Mars Rover Photos")
@allure.story("Download photos")
@allure.title("Download first 3 Curiosity photos from NASA API")
@allure.description("Запитуємо фото з камери 'fhaz' і зберігаємо перші 3.")
def test_download_mars_photos():
    with allure.step("Send GET request to NASA API"):
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
        params = {
            'sol': 1000,
            'camera': 'fhaz',
            'api_key': 'DEMO_KEY'
        }
        response = requests.get(url, params=params)
        assert response.status_code == 200, "Expected status code 200"
        data = response.json()
        photos = data.get('photos', [])
        assert photos, "No photos found"

    with allure.step("Download and save first 3 photos"):
        for i, photo in enumerate(photos[:3]):
            image_url = photo['img_src']
            image_data = requests.get(image_url).content
            filename = f"mars_photo_{i}.jpg"
            with open(filename, 'wb') as f:
                f.write(image_data)