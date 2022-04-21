from tkinter import *
import numpy as np

words_data = np.genfromtxt('listadepalavras.txt', dtype=None,
                           names=['tupi_word', 'portuguese_meaning1', 'portuguese_meaning2', 'portuguese_meaning3',
                                  'grammar_type'], delimiter="; ", encoding=('utf-8'))


app = Tk()
word = Entry(app)
word.place(x=10, y=30)


def store_input():
    user_input = word.get()
    data_bank = words_data
    mtrxrows = len(data_bank)
    mtrxcols = len(data_bank[0])

    if user_input in words_data['portuguese_meaning1']:
        for rows in range(mtrxrows):
            if(data_bank[rows][1] == user_input):
                print('The given element {', user_input, '} is present at row {' +
                      str(rows + 1)+'} and column {' + str(1) + '}')
                print(data_bank[rows][0])
                print(data_bank[rows][4])

    else:
        pass

    if user_input in words_data['portuguese_meaning2']:
        for rows in range(mtrxrows):
            if(data_bank[rows][2] == user_input):
                print('The given element {', user_input, '} is present at row {' +
                      str(rows+1)+'} and column {'+str(2)+'}')
                print(data_bank[rows][0])
                print(data_bank[rows][4])

    else:
        pass

    if user_input in words_data['portuguese_meaning3']:
        for rows in range(mtrxrows):
            if(data_bank[rows][3] == user_input):
                print('The given element {', user_input, '} is present at row {' +
                      str(rows+1)+'} and column {'+str(3)+'}')
                print(data_bank[rows][0])
                print(data_bank[rows][4])

    else:
        pass

    if user_input in words_data['portuguese_meaning1'] \
            or user_input in words_data['portuguese_meaning2'] or user_input in words_data['portuguese_meaning3']:
        pass

    else:
        print('palavra não encontrada')


b = Button(app, text="OK", width=10, command=store_input)
b.place(x=10, y=60)

app.mainloop()
