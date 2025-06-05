import json
import logging


logging.basicConfig(
    filename='json__kiian.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

files = [
    r'C:\Users\Anastasia\course\pythonAQA\lesson_13.1\task_2\login.json',
    r'C:\Users\Anastasia\course\pythonAQA\lesson_13.1\task_2\localizations_ru.json',
    r'C:\Users\Anastasia\course\pythonAQA\lesson_13.1\task_2\localizations_en.json',
    r'C:\Users\Anastasia\course\pythonAQA\lesson_13.1\task_2\swsgger.json'
]

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
    except Exception as e:
        filename = file_path.split('\\')[-1]
        logging.error(f"file {filename} isn't valid: {e}")

print('Completed.')





