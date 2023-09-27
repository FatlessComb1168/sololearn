'''
Random password.
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

from random import randint;
from os import system;
try:
    from pyperclip import copy;
except:
    pass;

a = '';
while a != 'y':
    try:
        system('cls');
        result = ''.join([chr(randint(33, 122))
            for i in range(int(input('Enter length of password: ')))]);
        try:
            copy(result);
            print('Password (copied!): ' + result);
        except:
            print('Password: ' + result);
            
        input();
    except:
        a = input('Exit? (y/n): ');
