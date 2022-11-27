from flask import Flask, render_template, request
# Импортируем блюпринты из других пакетов
from catalog.views import catalog_blueprint
from profile.views import profile_blueprint

app = Flask(__name__)

# Регистрируем каталог
app.register_blueprint(catalog_blueprint)
# Регистрируем профиль
app.register_blueprint(profile_blueprint)

app.run()
