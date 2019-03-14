from app.services import CRUD
from app.models.post import Post as PostModel, PostSchema


class Post(CRUD):
    def __init__(self, **kw):
        self.model = PostModel
        self.schema = PostSchema
        self.db = kw.get('db')
