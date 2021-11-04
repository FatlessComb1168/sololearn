'''
Python (literally).
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

from random import choice;

a = ['\\  \\', '/  /'];
print('  v\n  |\n /"\\\n/• •\\\n|   |\n\\   /\n \\  \\\n  \\  \\');

b = choice(a);
indent = ('   ' if b == a[0] else '  ');
print(indent + b);
c = b;

while len(indent) < 37:
    if len(indent) != 0:
        b = choice(a);
        if b == '/  /' and c == '\\  \\' or b == '\\  \\' and c == '/  /':
            pass;
        elif b == '/  /':
            indent = indent.replace(' ', '', 1);
        else:
            indent += ' ';
        print(indent + b);
        c = b;
    else:
        for i in range(2):
            print(indent + '\\  \\');
            indent += ' ';
print(indent + ' \\_/');
            
input('By FatlessComb1168\n' +
'A lot of thanks to Lev Fefelov for suggestions to improve it!\n');