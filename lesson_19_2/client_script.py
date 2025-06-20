import requests

def upload_get_delete_image(image_path):
    filename = image_path.split('/')[-1]
    server_url = 'http://127.0.0.1:8080'

    with open(image_path, 'rb') as img:
        files = {'image': img}
        res = requests.post(f'{server_url}/upload', files=files)
        print('UPLOAD:', res.status_code, res.json())

    headers = {'Content-Type': 'text'}
    res = requests.get(f'{server_url}/image/{filename}', headers=headers)
    print('GET URL:', res.status_code, res.json())

    res = requests.delete(f'{server_url}/delete/{filename}')
    print('DELETE:', res.status_code, res.json())

upload_get_delete_image('example.jpg')