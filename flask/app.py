from flask import Flask, render_template, request
import os

template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')
app = Flask(__name__, template_folder = template_dir, static_url_path = '', static_folder = static_dir)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/post/', defaults = {'post_id':1})
@app.route('/post/<int:post_id>')
def post_show(post_id):
    return render_template('post.html', PostId = post_id)


if __name__ == '__main__':
    app.run(port = 8000, debug = True)