# use pip install
# if using pycharm you can go to settings and add it
# pip is just like npm
import pyjokes

joke = pyjokes.get_joke('en', 'chuck')

print(joke)