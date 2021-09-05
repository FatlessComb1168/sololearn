'''
Collatz conjecture.
Copyright (C) 2021 Fedor Egorov <fedoregorov1@yandex.ru>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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
