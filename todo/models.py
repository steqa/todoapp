from typing import Optional

from db_handler import db_add, db_get


class BaseModel():
    _fields = {}

    def __validate_fields(self, fields: dict) -> bool:
        allowed_fields = self.__class__._fields
        allowed_fields['id'] = int()
        model = self.__class__.__name__
        for field in fields.keys():
            if field not in allowed_fields:
                raise ValueError(f"{model}.filter() got an unexpected "
                                 f"keyword argument '{field}'")
        return True

    def all(self):
        model = self.__class__.__name__
        return db_get(model)

    def filter(self, **kwargs):
        model = self.__class__.__name__
        if not kwargs:
            raise TypeError(f"{model}.filter() must accept "
                            f"at least 1 named argument")

        self.__validate_fields(fields=kwargs)
        records = db_get(model, filter_fields=kwargs)
        return records

    def save(self):
        model = self.__class__.__name__
        return db_add(model, data=self.__dict__)


class Task(BaseModel):
    _fields = {'text': str()}

    def __init__(self, text: Optional[str] = None) -> None:
        if text:
            self.text = text
