# O prima varianta de testare
# def sumFromNumbers(a,b):
#     return a+b

# firstNumber = 2
# secondNumber = 3
# expectedResult = 5
 
# result = sumFromNumbers(firstNumber,secondNumber)

# if result == expectedResult:
#     print("Test passed")
# else:
#     print("Test failed")

# A doua varianta de testare. Folosim clase si doua fisiere
# class Calculator:
#     def sumFromNumbers(self,firstNumber,secondNumber):
#         result = firstNumber +secondNumber
#         return result

# A treia varianta este prin utilizarea bibliotecii unittest
class Calculator:
    def sumFromNumbers(self,firstNumber,secondNumber):
        result = firstNumber +secondNumber
        return result    