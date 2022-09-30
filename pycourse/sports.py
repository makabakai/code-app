"""
Sports
马云飞 Yunfei Ma
2020118092
"""


people = [{'Chinese surname': '恒', 'Chinese given name': '一陟', 'Date of birth': '1999,Apr,3th',
           'List of sports': ['足球', '篮球']},
          {'Chinese surname': '孙', 'Chinese given name': '振荣', 'Date of birth': '1989,Mar,20th',
           'List of sports': ['篮球', '羽毛球', '乒乓球']},
          {'Chinese surname': '徐', 'Chinese given name': '嘉晨', 'Date of birth': '1993,Nov,1st',
           'List of sports': ['羽毛球']}]


# function sports() which takes a list like people as argument and writes out a report
# that contains the name of each person and the number of sports he/she plays
def sports(para_list):
    for person in para_list:
        if len(person['List of sports']) > 1:
            print(person['Chinese surname'] + person['Chinese given name'] + ' plays ' + str(
                len(person['List of sports'])) + ' sports')
        else:
            print(person['Chinese surname'] + person['Chinese given name'] + ' plays ' + str(
                len(person['List of sports'])) + ' sport')


# function plays_sport() which takes the list of people dictionaries people and a string
# containing a sport as arguments and prints the name of people who play the sport
def play_sport(para_list, sport):
    for person in para_list:
        if sport in person['List of sports']:
            print(person['Chinese surname'] + person['Chinese given name'])


"""
>>> print( people ) 
[{'Chinese surname': '恒', 'Chinese given name': '一陟', 'Date of birth': '1999,Apr,3th', \
'List of sports': ['足球', '篮球']}, \
{'Chinese surname': '孙', 'Chinese given name': '振荣', 'Date of birth': '1989,Mar,20th', \
'List of sports': ['篮球', '羽毛球', '乒乓球']}, \
{'Chinese surname': '徐', 'Chinese given name': '嘉晨', 'Date of birth': '1993,Nov,1st', \
'List of sports': ['羽毛球']}]
>>> sports( people ) 
恒一陟 plays 2 sports
孙振荣 plays 3 sports
徐嘉晨 plays 1 sport
>>> plays_sport( people, '羽毛球' ) 
孙振荣
徐嘉晨
>>> plays_sport( people, '篮球' ) 
恒一陟
孙振荣
"""
