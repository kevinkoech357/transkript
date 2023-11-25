from flask import Blueprint, render_template

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def index():
    return render_template('index.html')
