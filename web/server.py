from flask import Flask, render_template, url_for
app = Flask(__name__)

# have to have /username
@app.route('/<username>')
def home(username = None):
    return render_template('index.html', name=username)

@app.route('/<username>/<int:post_id>')
def home_with_id(username = None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)