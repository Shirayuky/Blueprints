from flask import Blueprint, render_template

# Добавим импорт шаблонизатора
catalog_blueprint = Blueprint('catalog_blueprint',
                              __name__,
                              template_folder='templates')


@catalog_blueprint.route('/catalog')
def catalog_page():
    return render_template('main.html')


@catalog_blueprint.route('/catalog/<category>')
def category_page(category):
    return render_template('category.html')


@catalog_blueprint.route('/catalog/category/<int:item>')
def item_page(item):
    return render_template('item.html')
