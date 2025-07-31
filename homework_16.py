### Task 1 ###

class Person():

    def __init__(self, first_name: str, last_name: str, birth_date: str, contact_phone: str):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.birth_date = birth_date.split("-")[0]
        self.contact_phone = contact_phone

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_phone(self):
        return f"{self.contact_phone}"

    def update_phone(self, new_phone: str):
        self.contact_phone = new_phone

    def get_birth_date(self):
        return f"{self.birth_date}"

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Birth date: {self.birth_date}, Contact phone: {self.contact_phone}"


class Student(Person):

    def __init__(self, first_name: str, last_name: str, birth_date: str, contact_phone: str, group: str, scholarship: str):
        super().__init__(first_name, last_name, birth_date, contact_phone)
        self.group = group
        self.scholarship = scholarship

    def get_group(self):
        return f"{self.group}"

    def get_scholarship(self):
        return f"{self.scholarship}"

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Birth date: {self.birth_date}, \
        Contact phone: {self.contact_phone}, Group: {self.group}, Scholarship: {self.scholarship}"


class Teacher(Person):

    def __init__(self, first_name: str, last_name: str, birth_date: str, contact_phone: str, salary: str, subjects: list):
        super().__init__(first_name, last_name, birth_date, contact_phone)
        self.salary = salary
        self.subjects = subjects

    def get_salary(self):
        return f"{self.salary}"

    def get_subjects(self):
        print(self.get_full_name() + " teaches:")
        for value in self.subjects:
            print("- " + value)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Birth date: {self.birth_date}, \
        Contact phone: {self.contact_phone}, Salary: {self.salary}, Subjects: {self.subjects}"

student1 = Student("Mike", "Lost", "1987-12-12", "+30687654321", "4", "6200" )
teacher1 = Teacher("John", "Abrams", "1977-09-09", "+30999876543", "32000", ["Mathematics", "Geometry", "Physics"])

print(student1)
print(teacher1)


### Task 2 ###

class Mathematician:

    @staticmethod
    def square_nums(nums_list: list):
        if not isinstance(nums_list, list):
            raise TypeError("nums_list must be a list")

        return [i**2 for i in nums_list]

    @staticmethod
    def remove_positives(nums_list: list):
        if not isinstance(nums_list, list):
            raise TypeError("nums_list must be a list")

        return [x for x in nums_list if x < 0]

    @staticmethod
    def filter_leaps(nums_list: list):
        if not isinstance(nums_list, list):
            raise TypeError("nums_list must be a list")

        return [year for year in nums_list if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


### Task 3 ###

class Product:
    def __init__(self, type_prod: str, name: str, price: int):
        self.type_prod = type_prod
        self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price

class ProductStore:

    def __init__(self):
        self._products = {}
        self._profit = 0

    def add(self, product: Product, quantity: int):
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product instance")
        if quantity <= 0:
            raise ValueError("The quantity must be positive")

        store_price = product.price * 1.3

        self._products[product.name] = {
            'product': product,
            'quantity': quantity,
            'price': store_price,
            'discount': 0.0
        }

    def get_product_info(self, product_name: str):
        if product_name not in self._products:
            raise ValueError(f"The product '{product_name}' was not found in the store")
        return product_name, self._products[product_name]['quantity']

    def get_all_products(self):
        return {
            name: {
                'type': info['product'].type_prod,
                'price': info['price'],
                'quantity': info['quantity'],
                'discount': info['discount']
            } for name, info in self._products.items()
        }

    def set_discount(self, identifier: str, percent: float, identifier_type: str = 'name'):
        if percent < 0 or percent > 100:
            raise ValueError("The discount percentage must be from 0 to 100")
        if identifier_type not in ['name', 'type']:
            raise ValueError("The identifier type must be 'name' or 'type'")

        result_search = False
        for product_info in self._products.values():
            if (identifier_type == 'name' and product_info['product'].name == identifier) or \
(identifier_type == 'type' and product_info['product'].type == identifier):
                product_info['discount'] = percent / 100
                result_search = True
                break

        if not result_search:
            raise ValueError(f"Products with {identifier_type} '{identifier}' not found")

    def sell_product(self, product_name: str, amount: int):
        if product_name not in self._products:
            raise ValueError(f"The product '{product_name}' was not found in the store")
        if amount <= 0:
            raise ValueError("The quantity must be positive")
        if self._products[product_name]['quantity'] < amount:
            raise ValueError(f"Not enough '{product_name}' in the store")

        product_info = self._products[product_name]
        product_info['quantity'] -= amount

        sale_price = product_info['price'] * (1 - product_info['discount'])
        self._profit += sale_price * amount

        if product_info['quantity'] == 0:
            del self._products[product_name]

    def get_income(self) -> float:
        return self._profit

    def __str__(self):
        return f"{self._products}"

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 30)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)


### Task 4 ###

import datetime

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_error(msg)

    def log_error(self, msg):
        try:
            with open('logs.txt', 'a') as file:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"[{timestamp}] Error: {msg}\n")
        except IOError as e:
            print(f"Error when writing to the log: {e}")