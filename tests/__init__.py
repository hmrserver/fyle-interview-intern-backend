from core.server import app
app.testing = True
from core import db
from core.models.users import User