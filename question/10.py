import random   

complect = {'DDR' : '4',
            'Motherboard' : 'asus',
            'proc' : 'intel'}


for quizNum in range(35):
    qfile = open('complectq%s.txt' % (quizNum+1), 'w')
    answerKeyFile = open('complects_answer%s.txt' % (quizNum+1), 'w')
    #запись заголовка билета
    qfile.write('Name:\n\nDate: \n\nCourse: \n\n')
    qfile.write((' ' * 3) + 'Checking answer(number%s)' % (quizNum + 1))    
    qfile.write('\n\n')
    complectss = list(complect.keys())

    for question_num in range (3):
        corect_answer = complect[complectss[question_num]]
        wrong_answer = list(complect.values())
        del  wrong_answer[wrong_answer.index(corect_answer)]
        wrong_answer = random.sample(wrong_answer, 2)
        answer_option = wrong_answer +[corect_answer]
        random.shuffle(answer_option)

        qfile.write('%s. chose answer %s\n' %(question_num +1, complect[question_num]) )

        for i in range(2):
            qfile.write( '%s. %s\n' % ('AB'[i], answer_option[i]))
            qfile.write('\n')
            # запись ключа файла в файл
            answerKeyFile.write('%s. %s\n' % (question_num + 1, 'AB'[answer_option.index(corect_answer)]))

            qfile.close()
            answerKeyFile.close()
