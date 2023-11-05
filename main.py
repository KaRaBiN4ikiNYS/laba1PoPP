import json
import xml.etree.ElementTree as ET


class Shop:

    def init(self, name, price):
        if not isinstance(price, (int, float)):
            raise InvalidPriceError("Price must be a number.")
        self.name = name
        self.price = price

    def to_dict(self): # преобразует в словарь
        return {
            'name: ': self.name,
            'price: ': self.price,
        }

    dictr = {'macbook: ': 3000,
             'macbookPro': 4500}

class InvalidPriceError(Exception):
    pass

class Product(Shop):
    def init(self, name, price, weight):
        super().init(name="no name", price=0)
        self.weight = weight

    def to_dict(self):
        product_data = super().to_dict()
        product_data.update({
            'weight': self.weight
        })
        return product_data

class Service(Shop):
    def init(self, name, price, time):
        super().init(price, name)
        self.time = time # время работы услуги (время чистки макбука)

    def to_dict(self):
        service_data = super().to_dict()
        service_data.update({
            'time': self.time
        })
        return service_data

try:
    """Создание объектов класса"""
    product_1 = Product("macbook", 3000, "10 kg")
    product_2 = Product("macbook Pro", 4500, "8 kg")
    service_1 = Service("chistka macbook", 500, "1 h")
    service_2 = Service("chistka macbook Pro", 1500, "1.5 h")

    data = {
        'product': [product_1.to_dict(), product_2.to_dict()],
        'service': [service_1.to_dict(), service_2.to_dict()]
    }

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    root = ET.Element("data")
    for product in [product_1, product_2]:
        product_element = ET.SubElement(root, "product")
        for key, value in product.to_dict().items():
            ET.SubElement(product_element, key).text = str(value)

    for service in [service_1, service_2]:
        service_element = ET.SubElement(root, "service")
        for key, value in service.to_dict().items():
            ET.SubElement(service_element, key).text = str(value)

    tree = ET.ElementTree(root) # считали файл сюда
    tree.write('data.xml') # запись в файл

    with open('data.json', 'r') as json_file: # r - read - чтение файла
        loaded_data = json.load(json_file)
    with open('data_from_json.json', 'w') as json_file: # w - write - запись файла
        json.dump(loaded_data, json_file, indent=4)

except InvalidPriceError as e:
    print("Invalid price:", e)

except Exception as e:
    print("An error occurred:", e)
