import logging
import xml.etree.ElementTree as ET


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


file_path = r'C:\Users\Anastasia\course\pythonAQA\lesson_13.1\task_3\groups.xml'


def find_incoming_by_group_number(xml_file, search_number):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == str(search_number):
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    return incoming.text
    return None


search_number = 4

result = find_incoming_by_group_number(file_path, search_number)

if result:
    logging.info(f'incoming for group {search_number}: {result}')
else:
    logging.info(f"Group with number {search_number} isn't found or incoming is missing.")