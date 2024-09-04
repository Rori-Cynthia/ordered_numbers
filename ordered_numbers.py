# Define funcion que ordena 3 numeros dados de mayor a menor (de izquierda a derecha)
def ordered_numbers(first_number, second_number, third_number):
    highest_number = None
    middle_number = None
    lowest_number = None
    
    if first_number > second_number and first_number > third_number:
        highest_number = first_number
        if second_number > third_number:
            middle_number = second_number
            lowest_number = third_number
        else:
            middle_number = third_number
            lowest_number = second_number
    elif second_number > first_number and second_number > third_number:
        highest_number = second_number
        if first_number > third_number:
            middle_number = first_number
            lowest_number = third_number
        else:
            middle_number = third_number
            lowest_number = first_number
    elif third_number > first_number and third_number > second_number:
        highest_number = third_number
        if first_number > second_number:
            middle_number = first_number
            lowest_number = second_number
        else:
            middle_number = second_number
            lowest_number = third_number

    print(f"Sus numeros ordenados de mayor a menor son los siguientes: {highest_number}, {middle_number}, {lowest_number}")

# Muestra opción al usuario para permitirle ingresar un número.
# Si no ingresa un entero o flotate advertirá el error y pedirá nuevamente los números
def input_prompt():
    try:
        print("--- Bienvenido al ordenador de numeros. Por favor, ingrese 3 numeros para evaluar ---")
        first_number = float(input("Ingrese el primer número: "))
        second_number = float(input("Ingrese el segundo número: "))
        third_number = float(input("Ingrese el tercer número: "))      
        ordered_numbers(first_number, second_number, third_number)
    except Exception:
        print("Ingresó una entrada no valida, por favor indique un número para evaluar")
        input_prompt()

# Añade convención
if __name__ == "__main__":
    input_prompt()



