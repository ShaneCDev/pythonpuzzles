mapping_dict = {
    "1": "One",
    "2": "Two",
    "4": "Four",
    "7": "Seven",
    "8": "Eight",
    "11": "Eleven",
    "13": "Thirteen",
    "14": "Fourteen",
    "16": "Sixteen",
    "17": "Seventeen",
    "19": "Nineteen",
    "22": "Twentytwo",
    "23": "Twentythree",
    "26": "Twentysix",
    "28": "Twentyeight",
    "29": "Twentynine",
    "31": "Thirtyone",
    "32": "Thirtytwo",
    "34": "Thirtyfour",
    "37": "Thirtyseven",
    "38": "Thirtyeight",
    "41": "Fortyone",
    "43": "Fortythree",
    "44": "Fortyfour",
    "46": "Fortysix",
    "47": "Fortyseven",
    "49": "Fortynine",
    "52": "Fiftytwo",
    "53": "Fiftythree",
    "56": "Fiftysix",
    "58": "Fiftyeight",
    "59": "Fiftynine",
    "61": "Sixtyone",
    "62": "Sixtytwo",
    "64": "Sixtyfour",
    "67": "Sixtyseven",
    "68": "Sixtyeight",
    "71": "Seventyone",
    "73": "Seventythree",
    "74": "Seventyfour",
    "76": "Seventysix",
    "77": "Seventyseven",
    "79": "Seventynine",
    "82": "Eightytwo",
    "83": "Eightythree",
    "86": "Eightysix",
    "88": "Eightyeight",
    "89": "Eightynine",
    "91": "Ninetyone",
    "92": "Ninetytwo",
    "94": "Ninetyfour",
    "97": "Ninetyseven",
    "98": "Ninetyeight",
}



def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + ': FizzBuzz')
        elif i % 3 == 0:
            print(str(i) + ': Fizz')
        elif i % 5 == 0:
            print(str(i) + ': Buzz')
        else:
            num_as_string = mapping_dict[str(i)]
            print(str(i) + ': ' + num_as_string[::-1])
fizz_buzz()


