from random import randint;
from os import system;

while True:
    try:
        system('cls');
        length = int(input('Enter length of password: '));
        result = '';

        for i in range(length):
            result += chr(randint(33,122));
        print('Password (copied!): ' + result);
        input();
    except:
        a = input('Exit? (y/n): ');
        if a == 'y':
            break;
        else:
            continue;