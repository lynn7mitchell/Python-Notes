from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)

# variable rules
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

# <> is a dynamic parameter example: www.website.com/lynn would mean <username> = lynn then set default = None
# int means it HAS TO be an integer
# @app.route('/<username>/<int:post_id>')
# pass username as a prarameter and set a default
# def hello_world(username=None, post_id=None):
# name = name(lynn)
# now name is a variable that can be used in your templates
    # return render_template('index.html', name=username, post_id=post_id)

@app.route('/test')
def test():
    return 'test!'


@app.route('/')
# @app.route('/index.html')
def home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        error = 'something went wrong'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return 'form submitted'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
    

# @app.route('/components.html')
# def components():
#     return render_template('/components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('/contact.html')

# @app.route('/work.html')
# def work():
#     return render_template('/work.html')

# @app.route('/works.html')
# def works():
#     return render_template('/works.html')