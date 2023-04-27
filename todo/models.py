from db_handler import db_get


class BaseModel():
    _fields = {}

    def __validate_fields(self, fields):
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


class Task(BaseModel):
    _fields = {'text': str()}
