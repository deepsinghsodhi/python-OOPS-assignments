
text1 = '[]'
text2 = '[[]]'
text3 = '[[[]]]'
text4 = ']['
text5 = '][]['
text6 = '[]][[]'
test7 = '[({])}'

def Brackets(text): #Method to calculate number of brackets and divide there length into 2 parts.
    length = len(text)
    if length % 2 == 0:
        half = length // 2  # Divide The number of brackets into half.
        left = '[' * half
        right = ']' * half
        if text[0:half] == left and text[half:length] == right: #If Num of brackets on both side are equal.
            return 'OK'
        else:
            return 'NOT OK'
    else:
        return 'NOT OK'

print (text1, "\t", Brackets(text1))
print (text2, "\t", Brackets(text2))
print (text3, "\t", Brackets(text3))
print (text4, "\t", Brackets(text4))
print (text5, "\t", Brackets(text5))
print (text6, "\t", Brackets(text6))

