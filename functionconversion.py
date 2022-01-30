#To check Binary Number
def CheckBinary(Number):
    BinaryNumber=[0,1]
    #Float Binary Number
    try:
        if "." in Number:
            for i in Number:
                if i==".":
                    continue
                else:
                    if int(i) not in BinaryNumber:
                        return False
                        break
            return True
        #Without Float Binary Number
        else:
            for i in Number:
                if int(i) not in BinaryNumber:
                    return False
                    break
            return True
    except:
        return False
def CheckDecimal(Number):
        Number=str(Number)
        #Decimal Range
        DecimalNumber=[n for n in range(0,10)]
        #If it is Float Number
        try:
            if "." in Number:
                for i in Number:
                    if i==".":
                        continue
                    else:
                        if int(i) not in DecimalNumber:
                            return False
                            break
                return True
        #IF it is Without Float
            else:
                for i in Number:
                    if int(i) not in DecimalNumber:
                        return False
                        break
                return True
        except:
            return False
#This Check Octal Numbers
def CheckOctal(Number):
    Number=str(Number)
    #Octal Range
    OctalNumbers=[n for n in range(0,8)]
    try:
        for i in Number:
            if i==".":
                continue
            else:
                if int(i) not in OctalNumbers:
                    return False
                    break
        return True 
    except:
        return False
def CheckHexaDecimal(Number):
        Number=str(Number)
        #Hexadecimal Range
        HexaDecimalNumbers=["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        try:
            for i in Number:
                if i==".":
                    continue
                if i not in HexaDecimalNumbers:
                    return False
                    break
            return True
        except:
            return False
#This Function Converts Decimal Number to HexaDecimal
def DecimalToHexa(Number):
    if CheckDecimal(Number):
        Number=str(Number)
        if "." in Number:
            HexaNumber=hex(int(float(Number)))
            HexaNumber=HexaNumber.removeprefix("0x").upper()
            #Decimal Number Floating Point
            DecimalNumber="0"+Number[len(str(int(float(Number)))):len(Number)]
            DecimalNumber=float(DecimalNumber)
            #Hexa Decimal Dictionary
            HexaNumbersLetters={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
            #Adding Decimal Point After Integer Number conversion
            HexaNumber+="."
            for i in range(4):
                DecimalNumber*=16
                if int(DecimalNumber) in HexaNumbersLetters.keys():
                    HexaNumber+= HexaNumbersLetters[int(DecimalNumber)]
                    DecimalNumber-=int(DecimalNumber)
                else:
                    HexaNumber+=str(int(DecimalNumber))
                    DecimalNumber-=int(DecimalNumber)
            return HexaNumber
        else:
            #Decimal To Hexa
            HexaNumber=hex(int(Number))
            HexaNumber=HexaNumber.removeprefix("0x").upper()
            return HexaNumber
    else:
        return "It is not a Decimal Number"
#This Function Converts Binary Number Into Decimal
def BinaryToDecimal(Number): #IT has to be corrected
    Number=str(Number)
    DecimalNumber=0
    if CheckBinary(Number):
        if "." in Number:
           #To fetch Single Single Elements of number 
            array=0 
            #For Integer Part
            for iter in range(Number.index(".")-1,-1,-1):
                if Number[array]!=".":
                    DecimalNumber+=int(Number[array])*(2**(iter))
                    array+=1
            array+=1
            #For fractional Part
            for iter in range(-1,-(len(Number)-Number.index(".")),-1):
                DecimalNumber+=int(Number[array])*(2**(iter))
                array+=1
            return DecimalNumber
        else:
            #To fetch Single Single Elements of number 
            index=0
            for iter in range(len(Number)-1,-1,-1):
                DecimalNumber+=int(Number[index])*(2**iter)
                index+=1
            return DecimalNumber
    else:
        return "It is not a Binary Number"
#This Function Converts Hexadecimal Number to Decimal
def HexaToDecimal(Number): 
    Number=str(Number)
    DecimalNumber=0
    HexaNumberLetters={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    if CheckHexaDecimal(Number):
        if "." in Number:
            array=0
            for iter in range(len(Number[0:Number.index(".")+1])-2,-1,-1):
                if Number[array] in HexaNumberLetters:
                    DecimalNumber+=int(HexaNumberLetters[Number[array]])*(16**iter)
                    array+=1
                else:
                    if Number[array]!=".":
                        DecimalNumber+=int(Number[array])*(16**iter)
                    array+=1
            array+=1
            for iter in range(-1,-(len(Number)-Number.index(".")),-1):
                if Number[array] in HexaNumberLetters:
                    DecimalNumber+= int(HexaNumberLetters[Number[array]])*(16**iter)
                    array+=1
                else:
                    DecimalNumber+=int(Number[array])*(16**iter)
                    array+=1
            return DecimalNumber
        #Hexa Number Without Floating Point Converion
        else:
            array=0
            for iter in range(len(Number)-1,-1,-1):
                if Number[array] in HexaNumberLetters:
                    DecimalNumber+=int(HexaNumberLetters[Number[array]])*(16**iter)
                    array+=1
                else:
                    DecimalNumber+=int(Number[array])*(16**iter)
                    array+=1
            return DecimalNumber
    else:
        return "It is not a HexaDecimal Number"
#This Function Converts Octal Number to HexaDecimal
def OctalToHexa(Number):
    Number=str(Number)
    #First It is converted into Decimal Than into hexa
    DecimalNumber=0
    if CheckOctal(Number):
        if "." in Number:
            array=0
            for iter in range(len(Number)-(len(Number)-Number.index("."))-1,-1,-1):
                DecimalNumber+=int(Number[array])*(8**iter)
                array+=1
            array+=1
            print(array)
            for iter in range(-1,-(len(Number)-Number.index(".")),-1):
                DecimalNumber+=int(Number[array])*(8**iter)
                array+=1
            return DecimalToHexa(DecimalNumber)
        else:
            array=0
            for iter in range(len(Number)-1,-1,-1):
                DecimalNumber+=int(Number[array])*(8**iter)
                array+=1
            return DecimalToHexa(DecimalNumber)
    else:
        return "It is not an Octal Number"
#It Converts Octal Number to Decimal
def OctalToDecimal(Number):
    Number=str(Number)
    DecimalNumber=0
    if CheckOctal(Number):
        if "." in Number:
            array=0
            for iter in range(len(Number)-(len(Number)-Number.index("."))-1,-1,-1):
                DecimalNumber+=int(Number[array])*(8**iter)
                array+=1
            array+=1
            for iter in range(-1,-(len(Number)-Number.index(".")),-1):
                if Number[array]!=".":
                    DecimalNumber+=int(Number[array])*(8**iter)
                array+=1
            return DecimalNumber
        else:
            array=0
            for iter in range(len(Number)-1,-1,-1):
                DecimalNumber+=int(Number[array])*(8**iter)
                array+=1
            return DecimalNumber
    else:
        return "It is not an Octal Number"
#It Converts Hexadecimal Number to Octal
def HexaToOctal(Number):
    Number=str(Number)
    if CheckHexaDecimal(Number):
        return DecimalToHexa(HexaToDecimal(Number))
    else:
        return "It is not a HexaDecimal Number"
#It converts Decimal Number ot Binary
def DecimalToBinary(Number):
    Number=str(Number)
    #Original Number
    OriginalNumber=str(Number)
    BinaryNumber=str()
    if CheckDecimal(Number):
        if "." in Number:
            #Binary Integer without Floating point
            BinaryInteger=int(float(Number))
            for iter in range(100):
                BinaryNumber+=str(int(BinaryInteger)%2)
                BinaryInteger=str(int(BinaryInteger)//2)
                if int(BinaryInteger)<2:
                    BinaryNumber+=str(int(BinaryInteger)%2)
                    break
            BinaryNumber=BinaryNumber[::-1]+"."
            #Binary Float Number
            BinaryFloat=float("0"+OriginalNumber[len(str(int(float(Number)))):len(OriginalNumber)+1])
            #Now for Float
            for iter in range(4):
                BinaryFloat*=2
                BinaryNumber+= str(int(float(BinaryFloat)))
                BinaryFloat-=int(float(BinaryFloat))
            return BinaryNumber
        else:
            for iter in range(100):
                BinaryNumber+=str(int(Number)%2)
                Number=str(int(Number)//2)
                if int(Number)<2:
                    BinaryNumber+=str(int(Number)%2)
                    break
            return BinaryNumber[::-1]


def main():
    print(BinaryToDecimal(10101010.101010)) #ETC
    print(DecimalToBinary(123.123))

main()
