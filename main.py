def add(n1, n2):
  return n1 + n2
# substract
def substract(n3, n4):
  return n3 - n4

#multiply
def multiply(n5, n6):
  return n5 * n6

#divide
def divide(n7, n8):
  return n7 / n8

operations = { "+" : add,
             "-" : substract,
             "*" : multiply,
             "/" : divide
             }
def Calculator(): # recursion function to start from the begainning again
  num1 = float(input("What is your first number?: "))
  for sympol in operations:
      print(sympol)
  while True:
    operations_sympol = input("Pick an operation: ")
    num2 = float(input("What is your next number?: "))
    calculator_function = operations[operations_sympol]
    answer = calculator_function(num1,num2)
    print(f"{num1} {operations_sympol} {num2} = {answer}.")
    should_continue = input(f"Type 'y' to continue with {answer} ,type 'c' to start a new calculation , or type 'n' to exit: ")
    if should_continue =="y":
         num1 = answer
    elif should_continue =="c":
         Calculator()
         break
    else:
        print('Goodbye')
        break

Calculator()