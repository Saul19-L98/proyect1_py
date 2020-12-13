# Las clases fue la idea original.
# class Operation:
#     def __init__(self,add_up,subtract,multiply,divide):
#         self.add_pu = add_up
#         self.subtract = subtract
#         self.multiply = multiply
#         self.divide = devide
    
#     def oepration_1():
#         pass

#     def Operation_2():
#         pass

#     def operation_3():
#         pass

#     def operation_4():
#         pass

def operation_4(firts_number,second_number):
    result = firts_number / second_number
    return print('La división de ambos números es: ' + str(result))

def operation_3(firts_number,second_number):
    result = firts_number * second_number
    return print('La multiplicación de ambos números es ' + str(result))

def operation_2(firts_number,second_number):
    result = firts_number - second_number
    return print('La resta de ambos números es ' + str(result))

def oepration_1(firts_number,second_number):
    result = firts_number + second_number
    return print('La suma de ambos números es: ' + str(result))

def run():
    firts_number = float(input('Escriba el primer número: '))
    second_number = float(input('Escriba el segundo número: '))
    menu = """ 
            Operaciones:
            1--Suma
            2--Resta
            3--Multiplicar
            4--Dividir
    """
    print(menu)

    option = int(input('Selecciones una opción entre 1 y 4: ')) 

    if option == 1:
        #Asi estan hasta que fuecen encapsulados.😊
        # result = firts_number + second_number
        # print('La suma de ambos números es: ' + str(result))
        oepration_1( firts_number,second_number)

    elif option == 2:
        operation_2( firts_number,second_number)

    elif option == 3:
        operation_3( firts_number,second_number)

    elif option == 4:
        operation_4( firts_number,second_number)

    else:
        print('La opción seleccionada no es valida.')

if __name__ == "__main__":
    run()
