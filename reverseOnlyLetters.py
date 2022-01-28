class Sol:
    def reverseOnlyLetters(self,str):
        rev_str=str[::-1]
        output=''
        for letter in rev_str:
            if (ord(letter)>64 and ord(letter)<91) or (ord(letter)>96 and ord(letter)<123):
                output+=letter
        for i,letter in enumerate(str):
            if not((ord(letter)>64 and ord(letter)<91) or (ord(letter)>96 and ord(letter)<123)):
                output=output[0:i]+letter+output[i:]
        return output

if __name__ == '__main__':
    p = Sol()
    print(p.reverseOnlyLetters(str="ab-cd"))
