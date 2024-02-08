import sys
import time
"""
HINT:
(0+1)%10=1
(1+2)%10=3
(9+4)%10=3
Therefore, with NumericStrings, 124+19=133

(0*1)%10=0
(1*2)%10=2
(9*4)%10=6
Therefore, with NumericStrings, 124+19=26
"""


class NumericString:
    #Implement class here!
    def __init__(self, n):
        if n < 0:
            raise ValueError("number must be non-negative")

        self.v = str(n);


    def __add__(self, nstring):
        if isinstance(nstring, NumericString):
            new_values = list()
            svalues = [x for x in self.v]
            nvalues = [x for x in nstring.v]

            dif_len = len(svalues) - len(nvalues)
            if(dif_len < 0):
                dif_len = dif_len * -1
            if(len(svalues) < len(nvalues)):
                for i in range(0,dif_len):
                    svalues.insert(i, '0')
            elif(len(svalues) > len(nvalues)):
                for i in range(0,dif_len):
                    nvalues.insert(i, '0')

            for index, x in enumerate(svalues):
                new_values.append(str((int(x) + int(nvalues[index]))%10))

            temp_string = "".join(new_values)
            return NumericString(int(temp_string))
        else:
            return NotImplemented

    def __mul__(self, nstring):
        if isinstance(nstring, NumericString):
            new_values = list()
            svalues = [x for x in self.v]
            nvalues = [x for x in nstring.v]

            dif_len = len(svalues) - len(nvalues)
            if(dif_len < 0):
                dif_len = dif_len * -1
            if(len(svalues) < len(nvalues)):
                for i in range(0,dif_len):
                    svalues.insert(i, '0')
            elif(len(svalues) > len(nvalues)):
                for i in range(0,dif_len):
                    nvalues.insert(i, '0')
            
            for index, x in enumerate(svalues):
                new_values.append(str((int(x) * int(nvalues[index]))%10))

            temp_string = "".join(new_values)
            return NumericString(int(temp_string))
        else:
            return NotImplemented

    def __str__(self):
        return self.v
if __name__ == "__main__":
    #Sample test program you can use to test your implementation

    #Create test objects and test value limit
    o16=NumericString(16)
    try:
        print('Initializing with negative integer...', end=' ')
        o_exception=NumericString(-1)
        got_exception=False
    except:
        got_exception=True

    assert got_exception
    print('Got exception -- ok')

    o124=NumericString(124)
    o19=NumericString(19)
    o0=NumericString(0)
    o1=NumericString(1)

    def test(o1, o2, expected_value1, expected_value2):
        res1=str(o1+o2)
        print(str(o1)+'+'+str(o2)+'='+res1, end='  ')
        assert res1==expected_value1
        print('ok')
        res2=str(o1*o2)
        print(str(o1)+'*'+str(o2)+'='+res2, end='  ')
        assert res2==expected_value2
        print('ok')

    #Test results of addition and multiplication
    test(o124, o19, '133', '26')
    test(o124, o0, '124', '0')
    test(o124, o1, '125', '4')

    test(o19, o124, '133', '26')
    test(o0, o124, '124', '0')
    test(o1, o124, '125', '4')

    res1=str(o19+o124+o1)
    print(str(o19)+'+'+str(o124)+'+'+str(o1)+'='+str(res1), end='  ')
    assert res1=='134'
    print('ok')

    res2=str((o19+o124)*o1)
    print('('+str(o19)+'+'+str(o124)+')'+'*'+str(o1)+'='+res2, end='  ')
    assert res2=='3'
    print('ok')

    #Check types
    type_o1=type(o1)
    if 'NumericString' in str(type_o1):
        print('Type of NumericString(1) is ok')
    else:
        assert False

    type_o1_plus_o124=type(o1+o124)
    if 'NumericString' in str(type_o1_plus_o124):
        print('Type of NumericString(1)+NumericString(124) is ok')
    else:
        assert False

    type_o1_times_o124=type(o1+o124)
    if 'NumericString' in str(type_o1_times_o124):
        print('Type of NumericString(1)*NumericString(124) is ok')
    else:
        assert False
