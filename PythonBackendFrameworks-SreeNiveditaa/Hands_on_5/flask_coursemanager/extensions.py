from flask_sqlalchemy import SQLAlchemy # pyright: ignore[reportMissingImports]
from flask_migrate import Migrate # pyright: ignore[reportMissingModuleSource]

db = SQLAlchemy()
migrate = Migrate()