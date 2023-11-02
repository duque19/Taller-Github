from operations import add, resta, multiplicacion
def game():
    score = 0
    while True:
        print('======== Menu ========'
                '\n1. Add'
                '\n2. Minus'
                '\n3. Multiplication'
                '\n0. Exit')
        option = int(input('\nChoice an option: '))
        if option == 0:
            break
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter you answer: '))
        if option == 1:
            result = add(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
        if option == 2:
            result = resta(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
        if option == 3:
            result = multiplicacion(num_1, num_2)
            if result == answer:
                score += 2
                print('Correct!!')
        else:
            print('Incorrect')
    print(f'======== Game Over ========'
        f'\nYou score is {score}'
        '\nKeep going!')
game()