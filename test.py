import pysnooper


@pysnooper.snoop()
def number_to_bits(number):
    global global_test
    global_test = 6
    number += number+1
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]


global_test = 5
number_to_bits(6)
