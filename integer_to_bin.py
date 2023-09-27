'''
Integer to binary number converter.
Copyright (C) 2021 Fedor Egorov
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

b = True;
while b:
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
            b = False;
        else:
            continue;
