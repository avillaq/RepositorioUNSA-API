from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Conexión a la base de datos
db = SQLAlchemy()

# Configuracion para limitar el número de peticiones
limiter = Limiter(
    get_remote_address,
    default_limits=["200/day", "50/hour"],
)