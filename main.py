x = int(input("digite um valor inteiro"))
y = int(input("digite um valor inteiro"))
z = int(input("digite um valor inteiro"))
if((x+y)> z and (x+z)> y and (y+z)>x):
    if(x==y and y==z):
        print("Os valores formam um triângulo equilátero")
    elif(x==y or y==z):
        print("Os valores formam um triângulo isóceles")
    else:
        print("Os valores formam um triângulo esqualeno")
else:
    print("Os valores não formam um triângulo ") 
