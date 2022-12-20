from orders.models import shared


class Category(shared.SlugBaseModel):
    pass


class Book(shared.SlugBaseModel, shared.BaseModel):
    pass
