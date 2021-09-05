'''
Get random unicode.
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
from random import randint;
from os import system;

# Get random unicode string without invalid characters!

# Input 1: length of random unicode string
# Input 2: maximum number of unicode cover (0-130000)

def get_random_unicode():
    a = '';
    for i in range(l*5):
        a = a + str(chr(randint(1,m)));
    a = str(list(a));
    for i in a:
        for i in range(150):
            a = a.replace(chr(i),'');
    a = a[0:l]
    return a;

while True:
    try:
        system('cls');
        print('Get random unicode string without invalid characters!');
        l = int(input('Enter length of random unicode string: '));
        m = int(input('Enter maximum number of unicode cover (0-130000): '));
        a = get_random_unicode();
        print('Random unicode: ' + a);
        input();
    except:
        a = input('Exit? (y/n): ');
        if a == 'y':
            break;
        else:
            continue;
