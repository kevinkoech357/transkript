from flask import Blueprint, render_template, current_app

user = Blueprint('user', __name__)

ALLOWED_EXTENSIONS = {'mpeg', 'mp3', 'mpeg3', 'mpga', 'mp4', 'm4a', 'wav', 'webm', 'mp4'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@user.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@user.route('/', methods=['POST'])
def upload_file():
    pass
