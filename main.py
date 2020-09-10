from twill.commands import *
import config

go(config.login_page)
fv("1", "username", config.username)
fv("1", "password", config.password)
submit('0')
def find_unchecked(course):
    go(courses["course"]) #TODO read form values

def check_choosen():
    pass
def find_all_unchecked():
    for course in courses:
        find_unchecked()
