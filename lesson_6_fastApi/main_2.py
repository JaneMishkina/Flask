from pydantic import BaseModel, Field
class Item(BaseModel):
    name: str = Field(max_length=10)

class User(BaseModel):
    age: int = Field(default=0)

# В этом примере мы определили класс Item, который содержит поле name, тип
# которого str. Мы также использовали функцию Field для задания ограничения на
# максимальную длину строки в 10 символов.
# Также определен класс User, кот. содержит поле age, типа int. Мы также использовали функцию
# Field для задания значения по умолчанию для поля =0.
