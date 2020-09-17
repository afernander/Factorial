import disassembler
def main():
     x=int(input("Ingrese le valor del al cual le desea sacar el factorial: " )) 
     print(factorial(x))

def factorial(x:int) :
    if(x==1):
        return 1
    else:
      return factorial(x-1)*x

disassembler.disassemble(main)
disassembler.disassemble(factorial)