from app.common.api import AppResource
from app.services.post import Post as PostService
from flask import request


class Posts(AppResource):
    service = None

    def __init__(self):
        self.service = PostService(db=self.session)

    def get(self):
        return self.service.all()

    def post(self):
        data = request.get_json()
        new = self.service.create(title=data["title"], content=data["content"])
        return self.service.to_json(new)
