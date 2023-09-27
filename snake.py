'''
Snake.
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

from random import choice;
from time import sleep;
from os import system;

input('Старт');
system('cls');
indent = '';

a = ['\\', '/'];
c = '';

indent = indent.replace(' ', '', 1);
while len(indent) < 165:
    if len(indent) != 0:
        b = choice(a);
        if b == '/' and c == '\\':
            print(indent + b);
        elif b == '/':
            indent = indent.replace(' ', '', 1);
            print(indent + b);
        elif b == '\\' and c == '/':
            print(indent + b);
        else:
            indent += ' ';
            print(indent + b);
        c = b;
        sleep(0.1);
    else:
        for i in range(2):
            print(indent + '\\');
            indent += ' ';
            sleep(0.1);

input();
