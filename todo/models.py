class BaseModel():
    _fields = {}
    def __validate_fields(self, fields):
        allowed_fields = self.__class__._fields
        allowed_fields['id'] = int()
        model = self.__class__.__name__
        for field in fields.keys():
            if field not in allowed_fields:
                raise ValueError(f'"{field}" is an invalid field ' \
                                 f'for filtering in the {model} model')
        return True


class Task(BaseModel):
    _fields = {'text': str()}
