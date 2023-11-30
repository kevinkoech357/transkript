from flask import Blueprint, render_template, current_app

user = Blueprint('user', __name__)

ALLOWED_EXTENSIONS = {'mpeg', 'mp3', 'mpeg3', 'mpga', 'mp4', 'm4a', 'wav', 'webm', 'mp4'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@user.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Use secure_filename to ensure a safe filename
        filename = secure_filename(file.filename)

        # Save the file to the upload folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # TO BE CONTINUED

        return 'File uploaded successfully'

    return 'Invalid file type'
