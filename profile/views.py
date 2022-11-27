from flask import Blueprint

# СОздаем и именуем блпринт
profile_blueprint = Blueprint('profile_blueprint', __name__)

# Создаем вьюшку, уже без app
@profile_blueprint.route('/profile/<int:user_id>')
def profile_page(user_id):
    return f"Старица профиля пользователя {user_id}"