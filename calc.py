def multiply (n1,n2):
    return n1 * n2
def add (n1,n2):
    return n1+n2
def substract (n1 ,n2):
    return n1-n2
def devide (n1,n2):
    return (n1/n2)

operations = {
    "*":multiply,
    "/":devide,
    "-":substract,
    "+":add,
}

num1 = input ("what is the first num")
for symbol in operations :
    print (symbol)

operation = input ("Pick and operation !")