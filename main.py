print"hello world"
print"let's get started"
print "what's up"
#basic introduction of a spy
spy_name = raw_input("whats your name?")
print " welcome " + spy_name + " nice to meet you "
spy_salutation = raw_input ("what should we call you (mr. or ms.)?")
print "welcome" + " " + spy_salutation +  spy_name
print "alright " +  spy_name + " " "i would like to know something more about you........"
#length of the name of the spy
if len(spy_name) > 0:
    print 'Welcome ' + spy_name + '. Glad to have you back with us.'
else:
    print "A spy needs to have a valid name. Try again please."
#enter the age of spy
spy_age = input("what's ur age")
if spy_age > 12 and spy_age < 50:
    print "you are eligible for a spy"
else:
    print "you are not eligible"
#spy rating
spy_rating= input("what's ur ratiing")
if spy_rating > 4.5:
    print 'Great ace!'
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print 'You are one of the good ones.'
elif spy_rating >= 2.5 and spy_rating <= 3.5:
    print 'You can always do better'
else:
    print 'We can always use somebody to help in the office.'
#spy status
spy_is_online = True
print "Authentication complete. Welcome " + spy_name + " age: " +str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you on board"








