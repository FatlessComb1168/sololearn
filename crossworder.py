'''
Crossworder.
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

b = True;
while b:
    a = input('1st word: ');
    b = input('2nd word: ');

    l_a = list(a);
    l_b = list(b);
    letters = [];
    proof = 0;
    count = 1;

    for i in l_a:
        for i1 in l_b:
            if i == i1:
                proof = 1;
                letters.append(i);

    if proof == 1:
        letters = list(set(letters));

        for i in letters:
            letter = i;
            spaces = l_a.index(letter);
            enters = l_b.index(letter);
            proof = 0;
        
            print('\nResult ' + str(count) + ':\n');
            count += 1;
            for i in l_b:
                if i != letter or i == letter and proof == 1:
                    print(' ' * spaces + i);
                elif i == letter and proof == 0:
                    print(a);
                    proof = 1;
        
            proof = 0;
            print('\nResult ' + str(count) + ':\n');
            count += 1;
            for i in l_a:
                if i != letter or i == letter and proof == 1:
                    print(' ' * enters + i);
                elif i == letter and proof == 0:
                    print(b);
                    proof = 1;
        
    else:
        print('Type words with common letters');

    work = input('\nContinue?\nAny typing - Yes\n1 - Exit\n');
    if work == '1':
        b = False;
    system('cls');