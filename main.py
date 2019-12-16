from flask import Flask
from Views.User import User
from Views.Category import Category
from Views.Test import Test
from Views.Item import Item


app = Flask(__name__)

app.add_url_rule('/app/test', view_func=Test.as_view('test'))
app.add_url_rule('/app/users', view_func=User.as_view('user'))
app.add_url_rule('/app/categories', view_func=Category.as_view('category'))
app.add_url_rule('/app/items', view_func=Item.as_view('item'))

app.run()
