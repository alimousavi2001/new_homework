from twill.commands import *
import config

#fill the login page
go(config.login_page)
fv("1", "username", config.username)
fv("1", "password", config.password)
submit('0')

def is_checked(item):
    value=showforms()[int(item)][0][3].value
    print(value)
    if value=="0":
        return(True)
    elif value=="1":
        return(False)


def find_unchecked(course):
    go(config.courses[course])
    completionstate=[]
    for i in range(1,len(showforms())):
        print(is_checked(i))
        completionstate.append(is_checked(i))
    print(completionstate)


def check_choosen():
    pass
def find_all_unchecked():
    for course in courses:
        find_unchecked()
