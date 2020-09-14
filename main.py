from twill.commands import go,fv,submit,showforms
import config

#fill the login page
go(config.login_page)
fv("1", "username", config.username)
fv("1", "password", config.password)
submit('0')

def is_checked(item):
    value=showforms()[int(item)][0][3].value
    title=showforms()[int(item)][0][2].value
    print(value)
    if value=="0":
        return(title,True)
    elif value=="1":
        return(title,False)

def find_status(course):
    go(config.courses[course])
    completionstate={}
    for i in range(1,len(showforms())):
        #print(is_checked(i))
        completionstate[is_checked(i)[0]]=is_checked(i)[1]
    return(completionstate)

def find_all_status():
    global all_homeworks
    all_homeworks={}
    for course in config.courses:
        all_homeworks[course]=find_status(course)
    return(all_homeworks)

def warn_unchecked():
    find_all_status()
    unchecked={}
    for course in all_homeworks:
        unchecked[course]=[]
        for subject in all_homeworks[course]:
            if all_homeworks[course][subject]==False:
                unchecked[course].append(subject)
    return(unchecked)

print(warn_unchecked())