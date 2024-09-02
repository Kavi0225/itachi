from speech import *
from text_to_audio import *
from imagetext import *

res = to_speak()
# print(res)

def tell_me(res):
    if "hinata" in res:
        res1 = "hi how can i help you "
        print(texttospeech(res1))
        res2 = to_speak()
        print(res2)
        if "news" in res2:
            im = 'news.jpg'
            res3 = image_to_string(im)
            print(res3)
            res4  = open(r'textdata.txt')
            # list = []
            for x in res4:
                # list.append(x)
                print(texttospeech(x))
tell_me(res)



