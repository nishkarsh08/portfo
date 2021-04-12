# from PIL import Image, ImageFilter
#
# img = Image.open('norbert-toth-_zUAcIvs-ME-unsplash.jpg')  # give us an image object
# filtered_img = img.filter(ImageFilter.BLUR)
# img = Image.open(r'C:\Users\HP\Desktop\Image Processing project\Pokemons\pikachu.jpg')

# L means Grayscale, obviously there are other things.

# crooked = filtered_img.rotate(90)  # rotate image 90 degrees
# crooked.save("Greychu.png", "png")

# resize = filtered_img.resize((300, 300))  # resize takes a tuple as parameters
# resize.save("Greychu.png", "png")

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("EditedRain.png", "png")
# region.show()  # Showing the image

# img.thumbnail((400, 400))
# # if we use resize method then the image will become squished.
# # Thumbnail method maintains the aspect ratio of the given image.
# img.save("EditedRain.jpg")
# img.show()


# Converter JPEG to PNG

# import sys # for taking arguments from the command line
# import os  # for path manipulations
# from PIL import Image # To convert the type of images
#
# image_folder = sys.argv[1]  # Pokemons\
# output_folder = sys.argv[2]     # new\
#
# if not os.path.exists(output_folder):  # os.path.exists gonna return True if path exists else False
#     os.makedirs(output_folder)  # os.makedirs create directory if not present
#
#
# for filename in os.listdir(image_folder):   # os.listdir takes a path of the directory and
#     # returns a list of files contains inside it.['bulbasaur.jpg', 'charmander.jpg', 'pikachu.jpg', 'squirtle.jpg']
#     print(os.listdir(image_folder))
#     # print(filename)
#     img = Image.open(f"{image_folder}{filename}")
#     print(os.path.splitext(filename))   # returns a split text tuple like ('pikachu', '.jpg')
#     clean_name = os.path.splitext(filename)[0]
#     img.save(f"{output_folder}{clean_name}.png", "png")
#     print('All done!!')


# WORKING WITH PDFs:
# import PyPDF2
#
# with open(f'.\PDFs\dummy.pdf', 'rb') as file:  # only 'r' gives us an error:
#     # PdfFileReader stream/file object is not in binary mode.
#     # this will create a binary object. To read it we need 'rb' read binary. Voila!
#     reader = PyPDF2.PdfFileReader(file)
#     # print(reader.numPages)
#     # print(reader.getPage(0))    # returns a page object 0 means 1st page like indexing
#     page = reader.getPage(0)  # page object -> getting the 1st page
#     print(page.rotateCounterClockwise(90))  # rotating 90 degrees
#     writer = PyPDF2.PdfFileWriter()  # Write object like reading object. Allows us to write the object in memory
#     writer.addPage(page)
#     with open(r'.\PDFs\tilt.pdf', 'wb') as new_file:
#         #   original dummy file is intact the new file tilt is rotated 90 degrees.
#         writer.write(new_file)


# PDF Merger
# import sys
# import PyPDF2
#
# inputs = sys.argv[1:]   # able to take unlimited inputs in a list excluding the first that is the filename
# # We are giving the file path. If it is situated in the cd then only name. Otherwise relative path.
#
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()     # Creates a merger object
#     for pdf in pdf_list:
#         print(pdf)  # PDFs\dummy.pdf    PDFs\twopage.pdf    PDFs\tilt.pdf
#         merger.append(pdf)   # append each pdf
#     merger.write('super.pdf')   # writes in a new file
#
# pdf_combiner(inputs)


# WATERMARK

# import PyPDF2
#
# template = PyPDF2.PdfFileReader(open(r'.\PDFs\super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open(r'.\PDFs\wtr.pdf', 'rb'))
# output_file = PyPDF2.PdfFileWriter()
#
# for i in range(template.getNumPages()):
#     current_page = template.getPage(i)
#     current_page.mergePage(watermark.getPage(0))
#     output_file.addPage(current_page)
#
# with open(r'.\PDFs\watermarked.pdf', 'wb') as file:
#     output_file.write(file)


# EMAILS WITH PYTHON

# import smtplib
# from email.message import EmailMessage
#
# email = EmailMessage()
# email['from'] = 'Babloo Tehelka'
# email['to'] = 'nishkarshshakya08@gmail.com'
# email['subject'] = 'Areee areee areeee gazab beti!!!'
#
# email.set_content('Hello! I am babloo tehelka. I loooooooove Ashley Graham.')
#
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('bablootehelka@gmail.com', '34b4847#')
#     smtp.send_message(email)
#     print('All Done!')


# CUSTOMIZED EMAIL

# import smtplib
# from email.message import EmailMessage
# from pathlib import Path
# from string import Template
#
# html = Template(Path('index.html').read_text())
# email = EmailMessage()
# email['from'] = 'Babloo Tehelka'
# email['to'] = 'nishkarshshakya08@gmail.com'
# email['subject'] = 'Areee areee areeee gazab beti!!!'
#
# email.set_content(html.substitute({'name': 'Daniyaaal'}), 'html')
#
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('bablootehelka@gmail.com', '34b4847#')
#     smtp.send_message(email)
#     print('All Done!')


# PASSWORD CHECKER / HOW MANY TIMES ITS BEEN HACKED
#
# import requests
# import hashlib
# import sys
#
#
# def request_api_data(query_char):  # Receives first5_char of Hash Value
#     url = 'https://api.pwnedpasswords.com/range/' + query_char
#     res = requests.get(url)  # requests.get(url) return status: 400, 200
#     if res.status_code != 200:
#         raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
#     return res  # A requests class OBJECT. Returns status. We can apply methods on this object.
#     # After : is the count of redundancy of password
#     # DE99C4EC4195FC237EC569D37237058549B:5
#     # print(type(request_api_data('DE99C'))) -----> <class 'requests.models.Response'>
#
#
# # x = request_api_data('AAF4C')
#
#
# def get_password_leaks_count(hashes, hash_to_check):  # hashes is the requests object contains every hash
#     # starting with the 5 chars given. hash_to_check contains tail - our unique tail.
#     # print(hashes.text)  # class str.
#     # line = hashes.text
#     # print(line.split(':'))
#     # print(line.splitlines())  # ['000AB2DEE342D579F6FE914C85B9CF98EDE:3', '003EC0930A89382B60E0C012A0F916AC33F:1']
#     # The split() method splits a string into a list.
#     # You can specify the separator, default separator is any whitespace.
#     # ['000AB2DEE342D579F6FE914C85B9CF98EDE', '3\r\n003EC0930A89382B60E0C012A0F916AC33F',
#     # '1\r\n0059D41E74575F8580A0687D1791E9B313F'...] \r is like \n
#     # hashes = (line.split(':') for line in hashes.text) --> ValueError:not enough values to unpack(expected 2, got 1)
#     hashes = (line.split(':') for line in hashes.text.splitlines())  # hashes is a generator
#     # for item in hashes:
#     #     print(item)
#     # ^ Above function returns items ['FFC724CBED25A326BBE370D466CF5797737', '7']
#     # ['FFCD66AAB0F73B33D17DEAF787DCFDAFD5F', '1']
#     # ['FFD7087991CE11EC76B58AB18EC0EA7F568', '119']
#     # lines grabs the first value then we are splitting it - REPEAT
#     for h, count in hashes:
#         # print(h)
#         # print(count)
#         if h == hash_to_check:
#             return count
#     return 0
#
#
# # get_password_leaks_count(x, '61DDCC5E8A2DABEDE0F3B482CD9AEA9434D')
# def pwned_api_check(password):  # receives text password
#     sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  # Text password to sha1 Hash password
#     first5_char, tail = sha1password[:5], sha1password[5:]  # We need to send starting 5 characters of Hash in API,
#     # remaining is tail
#     response = request_api_data(first5_char)  # Sends to API - first5_char
#     return get_password_leaks_count(response, tail)
#
#
# def main(args):  # text passwords given in the argument
#     for password in args:  # loop through text passwords
#         count = pwned_api_check(password)
#         if count:
#             print(f'{password} was found {count} times... you should probably change your password!')
#         else:
#             print(f'{password} was NOT found. Carry on!')
#     return 'done!'
#
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))  # starts here. calling main function with text password


# TWITTER BOT
# import tweepy
# import time
#
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
#
# user = api.me()
# print(user.name)  # prints your name.
# print(user.screen_name)
# print(user.followers_count)
#
# search = "zerotomastery"
# numberOfTweets = 2
#
#
# def limit_handle(cursor):
#     while True:
#         try:
#             yield cursor.next()
#         except tweepy.RateLimitError:
#             time.sleep(1000)
#
#
# # Be nice to your followers. Follow everyone!
# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Usernamehere':
#         print(follower.name)
#         follower.follow()
#
# # Be a narcisist and love your own tweets. or retweet anything with a keyword!
# for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
#     try:
#         tweet.favorite()
#         print('Retweeted the tweet')
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break


# Scraping

# import requests
# from bs4 import BeautifulSoup
# import pprint
#
# response = requests.get('https://news.ycombinator.com/')  # Kinda like a browser with no window
#
# # print(response.text)    # response.text gives us the entire html file. Now its time for scraping.
#
# # response.text gives us a long string. BeautifulSoup can parse it and can turn it into an object we can manipulate.
#
# #soup = BeautifulSoup(response.text, 'html.parser')  # BeautifulSoup object! Yay!
# #
# # # print(soup.find(id="score_26710013"))  # soup.body grabs only body ---- soup.body.contents returns contents in a list
# # #   soup.find_all('div') --------returns list of all divs ------ can also 'a' etc etc etc
# # #   soup.title -------- title tag
# # #   soup.a -------- first a tag
# # #   soup.find('a') ---- first a tag
# #
# # links = soup.select('.storylink')  # select uses CSS selectors to grab information. Returning a list
# # subtext = soup.select('.subtext')
#
#
# # print(votes[0])
# # print(votes[0].get('id'))  # gives us the value of the attribute ID of the first element
# def sort_stories_by_votes(hnlist):
#     x = sorted(hnlist, key=lambda x: x['votes'], reverse=True)
#     return x
#
#
# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = links[idx].getText()
#         href = links[idx].get('href', None)
#         vote = subtext[idx].select('.score')
#         if len(vote):
#             points = int(vote[0].getText().replace(' points', ''))
#             if points > 99:
#                 hn.append({'title': title, 'link': href, 'votes': points})
#     return sort_stories_by_votes(hn)
#
#
# for page in range(0, 5):
#     url = 'https://news.ycombinator.com/' + 'news?p=' + str(page)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.select('.storylink')  # select uses CSS selectors to grab information. Returning a list
#     subtext = soup.select('.subtext')
#     pprint.pprint(create_custom_hn(links, subtext))
#
# #pprint.pprint(create_custom_hn(links, subtext))


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
