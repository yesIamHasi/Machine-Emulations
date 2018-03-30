# -*- coding: cp1252 -*-
import os, random

ball = '''
                   ........
                 ..@@@@@@@@@.
                ...@.......@...
               ....@.......@....
              .....@@@@@@@@@.....
              .....@@@@@@@@@.....  BBBBB     AAAA   L       L
               ....@.......@....   B    B   A    A  L       L
                ...@.......@...    BBBBB    AAAAAA  L       L
                 ..@@@@@@@@@..     B    B   A    A  L       L
                  ...........      BBBBB    A    A  LLLLLL  LLLLLL

'''

when_replies = ['Soon', 'Never', 'At the end of this year']
helping_verbs = ['is', 'are', 'am', 'will', 'shall', 'should', 'would', 'can', 'was', 'were']
replies = ['Ask with concentration', 'Let me concentrate', 'You have a bright future']
where_replies = ['Somewhere safe', 'On earth']
advice = ['Remember only enemies speak the truth. Friends and lovers lie endlessly, caught in the web of duty', 'Make good friends', 'Have the courage to live a life true to yourself, not the life others expect of you',
          'Never argue with a stupid person, they’ll drag you down to their level and beat you with experience',
          'Only pack what you can carry yourself', 'ou can be the ripest, juiciest peach in the world, but there will always be someone who hates peaches',
          'Never let your sense of morals prevent you from doing what is right'
          ]

REPLY_STATE = 0

while True:
        REPLY_STATE = 0
        os.system('cls')
        print ball
        
        question = raw_input('Ask <<< ').lower()
	
        for helping_verb in helping_verbs:
                if question.startswith(helping_verb):
                        print random.choice(['Yes, definitely', 'no', 'may be', 'Without any doubt','My reply is no',
                                             'My sources say no', 'Ofcourse'])+'.'
                        REPLY_STATE = 1
                        
        if question.startswith('when') :
                print random.choice(when_replies)+'.'
                REPLY_STATE = 1

        if question.startswith('where') :
                print random.choice(where_replies)+'.'
                REPLY_STATE = 1

        if 'give me advice' in question:
                print random.choice(advice)+'.'
                REPLY_STATE = 1

        if REPLY_STATE == 0:
                print random.choice(replies)+'.'

        raw_input('\n\n\nPress Enter to Continue ...')
	
	

