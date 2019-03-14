from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import Column, Integer, DateTime, func, MetaData

meta = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})


@as_declarative(metadata=meta)
class Base(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()),
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now())
