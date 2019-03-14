from app.models import Base as BaseModel
from sqlalchemy import Column, Text, String
from marshmallow_sqlalchemy import ModelSchema


class Post(BaseModel):
    __tablename__ = 'posts'

    title = Column(String(50))
    content = Column(Text())


class PostSchema(ModelSchema):
    class Meta:
        model = Post

    def to_json(self, raw, many=False):
        return self.dump(raw, many=many).data
