import logging
import xml.etree.ElementTree as ET

# Налаштування логера

logging.basicConfig(
    filename='xml_hubernatorova.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)
logger = logging.getLogger(__name__)

# Парсинг XML-файлу
xml_file_path = "groups.xml"

def find_timing_exbytes():
    """Функція виконує пошук значення timingExbytes/incoming для заданого group/number і повертає
    значення timingExbytes/incoming або повідомлення про відсутність.
    """
    try:
        tree = ET.parse(xml_file_path)  # Парсинг XML-файлу
        root = tree.getroot()  # Кореневий елемент

        found_any = False  # Прапорець для перевірки, чи знайдено хоч одне значення

        for group in root.findall("group"):
            number = group.find("number")
            if number is not None:
                timing = group.find("timingExbytes/incoming")
                if timing is not None:
                    logger.info(f"Для group/number={number.text} знайдено incoming: {timing.text}")
                    print(f"Значення incoming для group/number={number.text}: {timing.text}")
                    found_any = True

        if not found_any:
            logger.info("Значення incoming не знайдено.")
            print("Значення incoming не знайдено.")

    except ET.ParseError as e:
        logger.error(f"Помилка парсингу XML файлу {xml_file_path}: {e}")
        print(f"Помилка парсингу XML файлу {xml_file_path}: {e}")
    except Exception as e:
        logger.error(f"Помилка під час обробки файлу {xml_file_path}: {e}")
        print(f"Помилка під час обробки файлу {xml_file_path}: {e}")

find_timing_exbytes()


