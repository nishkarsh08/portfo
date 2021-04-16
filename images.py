


from flask import Flask, render_template, url_for, request, \
    redirect  # render template allows us to send the HTML file etc
import csv

app = Flask(__name__)  # print(app) --> __main__ i.e main file that is running


@app.route('/')  # this is a decorator ----> / means root
def my_home():
    # print(url_for('static', filename='action_avengers_book_comic_marvel_movie_icon_183140.ico'))
    # return 'Hello, World!'  # we just sent a string. Flask will convert this into HTML automatically
    return render_template('index.html')


@app.route('/<string:page_name>')  # this is a decorator ----> / means root
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n email: {email}, subject: {subject}, message: {message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Did not save to database"
    else:
        return "Something went wrong. Try again!"
# @app.route('/<username>/<int:post_id>')  # See this URL parameters, we have mentioned these in our HTML too
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/works.html')  # this is a decorator ----> / means root
# def work():
#     return render_template('works.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
