import random

#random quiz generator
capitals = {'Alabama' : 'Montgomery', 'Alaska' : 'Juneau', 'Arizona' : 'Phoenix', 'Arkansas' : 'Little Rock',
            'California' : 'Sacramento', 'Colorado' : 'Denver', 'Connecticut' : 'Hartford', 'Delawear' : 'Dover',
           'Florida' : 'Tallahassee', 'Georgia' : 'Atlanta', 'Hawaii' : 'Honolulu', 'Idaho' : 'Boise', 'Illinois' : 'Springfield'
           , 'Indiana' : 'Indianapolis', 'Iowa' : 'Des Moines', 'Kansas' : 'Topeka', 'Kentucky' : 'Frankfurt',
            'Louisiana' : 'Baton Rouge' , 'Maine' : 'Augusta', 'Maryland' : 'Annapolis'}

for quiznum in range(10):
    #create the quiz and answer key files
    quizfile = open('capitalsquiz%s.txt' % (quiznum + 1), 'w')
    answerkey = open('capitalsquiz_answer%s.txt' % (quiznum + 1), 'w')

    #write out the header for the quiz
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write(('' * 20)+ 'State Capitals Quiz (Form %s)' % (quiznum + 1))
    quizfile.write('\n\n')

    #Shuffle the orders of the states
    states = list(capitals.keys())
    random.shuffle(states)

    for questionnum in range(19):
        correctans = capitals[states[questionnum]]
        wrongans = list(capitals.values())
        del wrongans[wrongans.index(correctans)]
        wrongans = random.sample(wrongans, 3)
        answeropts = wrongans + [correctans]
        random.shuffle(answeropts)

    quizfile.write('%s. What is the Capital of %s?\n'%(questionnum + 1, states[questionnum]))
    for i in range(4):
        quizfile.write('%s.%s\n' % ('ABCD'[i], answeropts[i]))
        quizfile.write('\n')

        answerkey.write('%s. %s\n' % (questionnum + 1, 'ABCD'[answeropts.index(correctans)]))

quizfile.close()
answerkey.close()
