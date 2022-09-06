from flet import app
from core.gui.SQLGUY import SQLGUY

app(target=SQLGUY().loop)

