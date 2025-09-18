### Task 1 ###

import re

class User:
    def __init__(self, email):
        self.email = User.validate(email)

    @classmethod
    def validate(cls, email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email")
        return email


### Task 2 ###

import random as rnd

class Boss:

    def __init__(self, name: str, company: str, id_=None):
        if id_ is not None:
            self._id = id_
        else:
            self._id = rnd.randint(1000, 9999)
        self._name = name
        self._company = company
        self._workers = []

    def __str__(self):
        return f"Boss({self.name}, {self.company}, {self.id})"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def company(self):
        return self._company

    @property
    def workers(self):
        return self._workers

    @id.setter
    def id(self, value: int):
        self._id = value

    @name.setter
    def name(self, value: str):
        self._name = value

    @company.setter
    def company(self, value: str):
        self._company = value

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise ValueError("Only instances of the Worker class can be added")
        if worker not in self._workers:
            self._workers.append(worker)
            worker.boss = self

class Worker:

    def __init__(self, name: str, company: str, boss: Boss, id_=None):
        if id_ is not None:
            self._id = id_
        else:
            self._id = rnd.randint(1000, 9999)
        self._name = name
        self._company = company
        self._boss = boss

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def company(self):
        return self._company

    @property
    def boss(self):
        return self._boss

    @id.setter
    def id(self, value: int):
        self._id = value

    @name.setter
    def name(self, value: str):
        self._name = value

    @company.setter
    def company(self, value: str):
        self._company = value

    @boss.setter
    def boss(self, value: Boss):
        if not isinstance(value, Boss):
            raise ValueError("The boss must be an instance of the Boss class")
        self._boss = value

### Task 3 ###

from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return str(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                if isinstance(result, str):
                    if result.lower() == 'true':
                        return True
                    if result.lower() == 'false':
                        return False
                return bool(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                return result
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True