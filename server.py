try:
    # try to import flask, or return error if has not been installed
    from flask import Flask
    from flask import jsonify
    from flask import send_from_directory
except ImportError:
    print("You don't have Flask installed, run `$ pip3 install flask` and try again")
    exit(1)

import os, subprocess

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), './')
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 #disable cache


def get_latest_project_mtime():
    """Return the newest file mtime for tracked project assets."""
    latest_mtime = 0.0
    extensions = {'.html', '.css', '.js', '.json', '.py'}
    ignored_dirs = {'.git', '.venv', '__pycache__', 'node_modules'}

    for root, dirs, files in os.walk(static_file_dir):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for name in files:
            _, ext = os.path.splitext(name)
            if ext.lower() not in extensions:
                continue
            full_path = os.path.join(root, name)
            try:
                file_mtime = os.path.getmtime(full_path)
            except OSError:
                continue
            if file_mtime > latest_mtime:
                latest_mtime = file_mtime

    return latest_mtime

# Serving the index file
@app.route('/', methods=['GET'])
def serve_dir_directory_index():
    if os.path.exists("app.py"):
        # if app.py exists we use the render function
        out = subprocess.Popen(['python3','app.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        return stdout if out.returncode == 0 else f"<pre style='color: red;'>{stdout.decode('utf-8')}</pre>"
    if os.path.exists("index.html"):
        return send_from_directory(static_file_dir, 'index.html')
    else:
        return "<h1 align='center'>404</h1><h2 align='center'>Missing index.html file</h2><p align='center'><img src='https://github.com/4GeeksAcademy/html-hello/blob/main/.vscode/rigo-baby.jpeg?raw=true' /></p>"


@app.route('/__hot-reload', methods=['GET'])
def hot_reload_version():
    return jsonify({"version": get_latest_project_mtime()})

# Serving any other image
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0 # avoid cache memory
    return response

app.run(host='0.0.0.0',port=3000, debug=True, extra_files=['./',])
