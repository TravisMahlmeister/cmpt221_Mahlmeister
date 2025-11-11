# import all tables (models) so they get registered with Base.metadata
from .user import Users
# make tables (models) available when importing from schema package
__all__ = ['Users']