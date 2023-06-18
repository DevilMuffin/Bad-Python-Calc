mathThing = 1
def printAnswer():
    print('The answer is:', answer)

while mathThing != "+" or "-" or "*" or "/":
    numCount = int(input('Enter the amount of numbers you are going to use:\n'))
    if numCount == 1:
        print("please use more than 1 number")
        break
    elif numCount == 2:
        num1 = int(input('Enter a number:\n'))
        num2 = int(input('Enter a second number:\n'))
        mathThing = str(input('Enter either +, -, * or /:\n'))
        break
    elif numCount == 3:
        num1 = int(input('Enter a number:\n'))
        num2 = int(input('Enter a second number:\n'))
        num3 = int(input('Enter a third number:\n'))
        mathThing = str(input('Enter either +, -, * or /:\n'))
        break
    elif numCount == 4:
        num1 = int(input('Enter a number:\n'))
        num2 = int(input('Enter a second number:\n'))
        num3 = int(input('Enter a third number:\n'))
        num4 = int(input('Enter a fourth number:\n'))
        mathThing = str(input('Enter either +, -, * or /:\n'))
        break
    elif numCount == 5:
        num1 = int(input('Enter a number:\n'))
        num2 = int(input('Enter a second number:\n'))
        num3 = int(input('Enter a third number:\n'))
        num4 = int(input('Enter a fourth number:\n'))
        num5 = int(input('Enter a fith number:\n'))
        mathThing = str(input('Enter either +, -, * or /:\n'))
        break
    elif numCount == 6:
        num1 = int(input('Enter a number:\n'))
        num2 = int(input('Enter a second number:\n'))
        num3 = int(input('Enter a third number:\n'))
        num4 = int(input('Enter a fourth number:\n'))
        num5 = int(input('Enter a fith number:\n'))
        num6 = int(input('Enter a sixth number:\n'))
        mathThing = str(input('Enter either +, -, * or /:\n'))
        break
    elif numCount == 7:
        num1 = int(input('Enter a number:\n'))
        num2 = int(input('Enter a second number:\n'))
        num3 = int(input('Enter a third number:\n'))
        num4 = int(input('Enter a fourth number:\n'))
        num5 = int(input('Enter a fith number:\n'))
        num6 = int(input('Enter a sixth number:\n'))
        num7 = int(input('Enter a seventh number:\n'))
        mathThing = str(input('Enter either +, -, * or /:\n'))
        break
    elif numCount == 8:
        num1 = int(input('Enter a number:\n'))
        num2 = int(input('Enter a second number:\n'))
        num3 = int(input('Enter a third number:\n'))
        num4 = int(input('Enter a fourth number:\n'))
        num5 = int(input('Enter a fith number:\n'))
        num6 = int(input('Enter a sixth number:\n'))
        num7 = int(input('Enter a seventh number:\n'))
        num8 = int(input('Enter a eigth number:\n'))
        mathThing = str(input('Enter either +, -, * or /:\n'))
        break
    elif numCount == 9:
        num1 = int(input('Enter a number:\n'))
        num2 = int(input('Enter a second number:\n'))
        num3 = int(input('Enter a third number:\n'))
        num4 = int(input('Enter a fourth number:\n'))
        num5 = int(input('Enter a fith number:\n'))
        num6 = int(input('Enter a sixth number:\n'))
        num7 = int(input('Enter a seventh number:\n'))
        num8 = int(input('Enter a eigth number:\n'))
        num9 = int(input('Enter a ninth number:\n'))
        mathThing = str(input('Enter either +, -, * or /:\n'))
        break
    elif numCount == 10:
        num1 = int(input('Enter a number:\n'))
        num2 = int(input('Enter a second number:\n'))
        num3 = int(input('Enter a third number:\n'))
        num4 = int(input('Enter a fourth number:\n'))
        num5 = int(input('Enter a fith number:\n'))
        num6 = int(input('Enter a sixth number:\n'))
        num7 = int(input('Enter a seventh number:\n'))
        num8 = int(input('Enter a eigth number:\n'))
        num9 = int(input('Enter a ninth number:\n'))
        num10 = int(input('Enter a tenth number:\n'))
        mathThing = str(input('Enter either +, -, * or /:\n'))
        break

    else:
        print("please enter a number equal to or less than 10")
        
if mathThing == "+" and numCount == 2:
    answer = num1 + num2
    printAnswer()
elif numCount == 3 and mathThing == "+":
    answer = num1 + num2 + num3
    printAnswer()
elif numCount == 5 and mathThing == "+":
    answer = num1 + num2 + num3 + num4 + num5
    printAnswer()
elif numCount == 6 and mathThing == "+":
    answer = num1 + num2 + num3 + num4 + num5 + num6
    printAnswer()
elif numCount == 7 and mathThing == "+":
    answer = num1 + num2 + num3 + num4 + num5 + num6 + num7
    printAnswer()
elif numCount == 8 and mathThing == "+":
    answer = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
    printAnswer()
elif numCount == 9 and mathThing == "+":
    answer = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
    printAnswer()
elif numCount == 10 and mathThing == "+":
    answer = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    printAnswer()

if mathThing == "-" and numCount == 2:
    answer = num1 - num2
    printAnswer()
elif numCount == 3 and mathThing == "-":
    answer = num1 - num2 - num3
    printAnswer()
elif numCount == 5 and mathThing == "-":
    answer = num1 - num2 - num3 - num4 - num5
    printAnswer()
elif numCount == 6 and mathThing == "-":
    answer = num1 - num2 - num3 - num4 - num5 - num6
    printAnswer()
elif numCount == 7 and mathThing == "-":
    answer = num1 - num2 - num3 - num4 - num5 - num6 - num7
    printAnswer()
elif numCount == 8 and mathThing == "-":
    answer = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8
    printAnswer()
elif numCount == 9 and mathThing == "-":
    answer = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9
    printAnswer()
elif numCount == 10 and mathThing == "-":
    answer = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10
    printAnswer()

if mathThing == "*" and numCount == 2:
    answer = num1 * num2
    printAnswer()
elif numCount == 3 and mathThing == "*":
    answer = num1 * num2 * num3
    printAnswer()
elif numCount == 5 and mathThing == "*":
    answer = num1 * num2 * num3 * num4 * num5
    printAnswer()
elif numCount == 6 and mathThing == "*":
    answer = num1 * num2 * num3 * num4 * num5 * num6
    printAnswer()
elif numCount == 7 and mathThing == "*":
    answer = num1 * num2 * num3 * num4 * num5 * num6 * num7
    printAnswer()
elif numCount == 8 and mathThing == "*":
    answer = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8
    printAnswer()
elif numCount == 9 and mathThing == "*":
    answer = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9
    printAnswer()
elif numCount == 10 and mathThing == "*":
    answer = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10
    printAnswer()

if mathThing == "/" and numCount == 2:
    answer = num1 / num2
    printAnswer()
elif numCount == 3 and mathThing == "/":
    answer = num1 / num2 / num3
    printAnswer()
elif numCount == 5 and mathThing == "/":
    answer = num1 / num2 / num3 / num4 / num5
    printAnswer()
elif numCount == 6 and mathThing == "/":
    answer = num1 / num2 / num3 / num4 / num5 / num6
    printAnswer()
elif numCount == 7 and mathThing == "/":
    answer = num1 / num2 / num3 / num4 / num5 / num6 / num7
    printAnswer()
elif numCount == 8 and mathThing == "/":
    answer = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8
    printAnswer()
elif numCount == 9 and mathThing == "/":
    answer = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9
    printAnswer()
elif numCount == 10 and mathThing == "/":
    answer = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10
    printAnswer()

