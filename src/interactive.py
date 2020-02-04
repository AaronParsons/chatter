'''
This is a module to talk to AI overlords.
'''

import random

RESPONSES = [
    'Sounds great.',
    'Everyone is stupider for having listened to you.',
    'Brilliant, Holmes.']

def chat():
    while True:
        try:
            from_user = raw_input('Hi?')
            print(random.choice(RESPONSES))
        except(KeyboardInterrupt):
            print('Nice try. Ha ha!')
            return
   
