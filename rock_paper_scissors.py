'''
Rock-paper-scissors.
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

computer = 0;
user = 0;
# array = ['Rock', 'Paper', 'Scissors'];

while True:
    print("Rock-paper-scissors");
    print("Computer's score:", computer);
    print("Your score:", user);
    cc = randint(1, 3);
    # print('Computer chose', array[cc - 1]);
    print("\nComputer chose one of these items:");
    print("1) Rock\n2) Paper\n3) Scissors\n");
    uc = int(input('Your choice (only numbers): '));
    system('cls');
    if uc == cc: print("It's a draw");
    
    elif cc > uc:
        if cc == 3 and uc == 1:
            print('You won');
            user += 1;
        else:
            print('Computer won');
            computer += 1;
    
    else:
        if cc == 1 and uc == 3:
            print('Computer won');
            computer += 1;
        else:
            print('You won');
            user += 1;