from os import system;
while True:
    try:
        system('cls');
        a = int(input('Enter any natural number: '));
        b = '';

        while a != 0:
            b += str(a % 2);
            a = a // 2;

        b = b[::-1];
        print('Binary number: ' + b);
        input();
    except:
        a = input('Exit? (y/n): ');
        if a == 'y':
            break;
        else:
            continue;