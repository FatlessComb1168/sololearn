from os import system;
while True:
    try:
        system('cls');
        x = int(input("Enter any natural number: "));
        i = n = 0;
        array = [];

        while True:
            array.append(n);
            n = x + n;
            
            if x % 2 == 0:
                x = x / 2;
                i = i + 1;
                
            elif x != 1 and x % 2 != 0:
                x = 3 * x + 1;
                i = i + 1;
                
            if x == 1:
                break;

        n = str(int(n));
        print("\nNumber of iterations: " + str(i));
        print("Summary of all given numbers: " + n);
        print("Maximum: " + str(int(max(array))));
        input();
    except:
        a = input('Exit? (y/n): ');
        if a == 'y':
            break;
        else:
            continue;