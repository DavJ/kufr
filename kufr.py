def opens(code,digits):
    return code[0:1] == digits[0:1] or code[1:2] == digits[1:2] or code[0]+code[2] == digits[0]+digits[2]

def suitcase():

    combinations = []
    for number1 in range(10):
        for number2 in range(5):
            d1=number1
            d2=2*number2+1
            d3=(d2+d1-1) % 10
            combinations.append(f'{d1}{d2}{d3}')

    return combinations, len(combinations)

def open(combinations):

    def find_opening_combination(digits):
        for c in combinations:
            if opens(digits, c):
                print(f'OPENED {digits}: {c}')
                return c

    for i in range(1000):
        digits = f'{i:03d}'
        if find_opening_combination(digits) is None:
           raise AssertionError(f'NOT OPENED {digits}: {combinations}')

    print(f'all opened using {len(combinations)} combinations {combinations} ')

if __name__ == '__main__':
    open(suitcase()[0])
