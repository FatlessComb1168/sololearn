'''
Guess the number.
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

while True:
    a = randint(1, 10);
    print('The computer riddled a number from 1 to 10.');
    b = int(input('Guess it: '));
    system('cls');

    if a == b:
        print("Well done! It's the number", str(b) + '!');

    else:
        print("Unfortunately, it's the number", str(a) + '!');