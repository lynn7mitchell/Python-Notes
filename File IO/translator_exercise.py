from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('File IO/test.txt', mode='r+') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO Error')
    raise err