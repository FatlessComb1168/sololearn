'''
Integer to text version converter.
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

def func():
        global buff, b;
        b = 0;
        buff = [];
        for i in range(1, len(number) + 1):
            c = int(number) % (10 ** i) - int(number) % (10 ** (i - 1));
            buff.append(c);
            b += c;
        buff = buff[::-1];
        for i in range(buff.count(0)):
            buff.remove(0);

def func1():
    global text, buff, b;
    if 0 < int(number) < 10:
        text += n1[number];

    elif 10 <= int(number) < 20:
        text += n2[number];

    elif 20 <= int(number) < 100:
        b = 0;
        buff = [];

        if int(number) % 10 == 0:
            text += n3[number];

        else:
            func();
            text += n3[str(buff[0])] + ' ' + n1[str(buff[1])];
    
    elif 100 <= int(number) < 1000:
        b = 0;
        buff = [];

        if int(number) % 100 == 0:
            text += n4[number];

        else:
            func();
            if len(buff) == 2 and buff[1] < 10:
                text += n4[str(buff[0])] + ' ' + n1[str(buff[1])];

            elif len(buff) == 2 and buff[1] > 10:
                text += n4[str(buff[0])] + ' ' + n3[str(buff[1])];

            elif buff[1] == 10:
                text += n4[str(buff[0])] + ' ' + n2[str(buff[1] + buff[2])];

            else:
                text += n4[str(buff[0])] + ' ' + n3[str(buff[1])] + ' ' + n1[str(buff[2])];

def func2():
    global array;
    b = len(number1) // 3;
    c = len(number1) - b*3;
    array = [];
    if c == 0:
        begin = 0;
        end = 3;
        while end <= len(number1):
            array.append(number1[begin:end]);
            begin += 3;
            end += 3;
        
    elif c == 1:
        array.append(number1[0]);
        begin = 1;
        end = 4;
        while end <= len(number1):
            array.append(number1[begin:end]);
            begin += 3;
            end += 3;
        
    elif c == 2:
        array.append(number1[0:2]);
        begin = 2;
        end = 5;
        while end <= len(number1):
            array.append(number1[begin:end]);
            begin += 3;
            end += 3;

n1 = {"1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", "7": "семь", "8": "восемь", "9": "девять"};
n2 = {"10": "десять", "11": "одиннадцать", "12": "двенадцать", "13": "тринадцать", "14": "четырнадцать", "15": "пятнадцать", "16": "шестнадцать", "17": "семнадцать", "18": "восемнадцать", "19": "девятнадцать"};
n3 = {"20": "двадцать", "30": "тридцать", "40": "сорок", "50": "пятьдесят", "60": "шестьдесят", "70": "семьдесят", "80": "восемьдесят", "90": "девяносто"};
n4 = {"100": "сто", "200": "двести", "300": "триста", "400": "четыреста", "500": "пятьсот", "600": "шестьсот", "700": "семьсот", "800": "восемьсот", "900": "девятьсот"};
n6 = {-1: "", -2: "тысяч", -3: "миллионов", -4: "миллиардов"};

while True:
    try:
        text = '';
        standard = '';
        number = input('Введите число: ');

        if '-' in number:
            number = number.replace('-', '');
            text = 'минус ' + text;
            standard = '-' + standard;

        if '+' in number:
            number = number.replace('+', '');
            text = 'плюс ' + text;
            standard = '+' + standard;
        
        if number[0] == '0':
            while number[0] == '0':
                number = number.replace('0', '', 1);

        number1 = number;

        if number == '0':
            print('ноль');
            continue;

        elif 0 < int(number) < 1000:
            func1();
        else:
            func2();
            count = len(array) * (-1);
            i = count;
            while count <= i < 0:
                number = str(array[i]);
                func1();
                text += ' ' + n6[i] + ' ';
                i += 1;
        
        text = text.replace('один тысяч', 'одна тысяча');
        text = text.replace('два тысяч', 'две тысячи');
        text = text.replace('три тысяч', 'три тысячи');
        text = text.replace('четыре тысяч', 'четыре тысячи');

        text = text.replace('один миллионов', 'один миллион');
        text = text.replace('два миллионов', 'два миллиона');
        text = text.replace('три миллионов', 'три миллиона');
        text = text.replace('четыре миллионов', 'четыре миллиона');

        text = text.replace('один миллиардов', 'один миллиард');
        text = text.replace('два миллиардов', 'два миллиарда');
        text = text.replace('три миллиардов', 'три миллиарда');
        text = text.replace('четыре миллиардов', 'четыре миллиарда');

        text = text.replace('  миллионов', '');
        text = text.replace('  тысяч', '');

        b = len(number1) // 3;
        c = len(number1) - b*3;
        func2();

        for i in array:
            standard += str(i) + ' ';
        standard = standard[0:-1];

        print('Стандарт:', standard);
        print('Текстовая версия:', text, '\n');
    except:
       print();
