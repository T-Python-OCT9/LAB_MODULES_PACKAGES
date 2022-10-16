def date_time():

    A = '16/10/2022'
    a = ''
    guess = 0
    number_of_gussung = 3

    while A != a:

        a = input('Plase enter the date of the we learnd about Modules: ')
        
        if A != a:
            print('Plase enter the corcet date',f'You have ( {number_of_gussung} ) Chance left')

            number_of_gussung -= 1


        if guess == 3:
            print('You can not guess more')
            break

        guess += 1

    else: print('True')

date_time()









   



    



