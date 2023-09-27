'''
Caesar encrypt.
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
array = ([chr(i) for i in range(33, 127)]
    + [chr(i) for i in range(1040, 1104)]);
    
array.insert(132, 'ё');
array.insert(100, 'Ё');

def encrypt(number):
    if number >= 160:
        while number >= 160:
            number -= 160;

    elif number <= -160:
        while number <= -160:
            number += 160;
            
    caesar_encrypt = '';
    for i in range(len(text)):
        try:
            if text[i] in array:
                caesar_encrypt += array[array.index(text[i]) + number];
            else:
                caesar_encrypt += text[i];
            
        except:
            caesar_encrypt += array[array.index(text[i])
                + number - len(array)];
    return caesar_encrypt;

ask_for_exit = '';
while ask_for_exit != 'y':
    system('cls');
    number = input('Input any integer positive or negative number: ');

    try:
        number = int(number);
    except:
        ask_for_exit = input('Exit? (y/n): ');
        continue;

    text = input('Input any text using latin and cyrrilic ' +
        'alphabets, digits and special symbols: ');
    caesar = encrypt(number);
    number *= -1;
    caesar_reversed = encrypt(number);

    print('\nOriginal:', text);
    print('Encrypted:', caesar);
    print('Encrypted reversed:', caesar_reversed);
    input();
