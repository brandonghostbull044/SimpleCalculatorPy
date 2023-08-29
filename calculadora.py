print("""------------------------------Bienvenido a mi calculadora------------------------------
         ---------------|||El funcionamiento es el siguiente|||---------------
         ---------> 1. Introduces el primer valor a operar
         ---------> 2. Introduces el símbolo de la operación a realizar, los cuales son:
         ------------> 2.1 Para multiplicar usa 'x'
         ------------> 2.2 Para dividir usa '/'
         ------------> 2.3 Para sumar usa '+'
         ------------> 2.4 Para restar usa '-'
         ---------> 3. Introduce el segundo valor a operar
         ---------> 4. Pulsa enter.
         ------------> 4.1. Si en la nueva operación quieres utilizar como valor el 
                        resultado de tu operacion anterior introduce la letra 'r' 
                        como valor. Igualmente puedes hacer uso de 'r2' para usar el resultado
                        ante-anterior y 'r3' para usar anterior al ante-anterior.
         ------> Al terminar tu operación, el prompt te permitirá hacer otra.<------
         -----------------> ¡¡¡¡Para salir de la calculadora teclea Ctrl+C !!!! <-----------------
         
         ------------------------------Empezemos------------------------------
      """)
contador = 1
contador2 = 0
resultado = 0
resultado_anterior1 = 0
resultado_anterior2 = 0

while contador == 1:
    valor1 = str(input('--->').lower())
    if valor1 == 'r':
        if  not resultado:
            print('Aún no tienes resultados registrados. Intentalo de nuevo.')
            continue
        else:
            valor1 = resultado
    elif valor1 == 'r2':
        if  not resultado_anterior1:
            print('Aún no tienes un segundo resultado registrado. Intentalo de nuevo.')
            continue
        else:
            valor1 = resultado_anterior1
    elif valor1 == 'r3':
        if  not resultado_anterior2:
            print('Aún no tienes un tercer resultado registrado. Intentalo de nuevo.')
            continue
        else:
            valor1 = resultado_anterior2
    elif valor1 == 'show':
        if resultado:
            print(f'Primer resultado: {resultado}')
            if resultado_anterior1:
                print(f'Segundo resultado: {resultado_anterior1}')
            if resultado_anterior2:
                print(f'Tercer resultado: {resultado_anterior2}')
            continue
        else:
            print('Aún no tienes resultados')
            continue
        
    else:
        valor1 = float(valor1)
        
    operador = input('--->')
    
    valor2 = str(input('--->').lower())
    if valor2 == 'r':
        if not resultado:
            print('Aún no tienes resultados registrados. Intentalo de nuevo.')
            continue
        else:
            valor2 = resultado
    elif valor2 == 'r2':
        if  not resultado_anterior1:
            print('Aún no tienes un segundo resultado registrado. Intentalo de nuevo.')
            continue
        else:
            valor2 = resultado_anterior1
    elif valor2 == 'r3':
        if  not resultado_anterior2:
            print('Aún no tienes un tercer resultado registrado. Intentalo de nuevo.')
            continue
        else:
            valor2 = resultado_anterior2
    else:
        valor2 = float(valor2)
    
    contador2 += 1
    
    if operador == 'x':
        print(f'Resultado: {valor1 * valor2}')
        resultado = valor1 * valor2
        if contador2 >= 2:
            resultado_anterior1 = resultado
        if contador2 >= 3:            
            resultado_anterior2 = resultado_anterior1
    elif operador == '/':
        print(f'Resultado: {valor1 / valor2}')
        resultado = valor1 / valor2
        if contador2 >= 2:
            resultado_anterior1 = resultado
        if contador2 > 3:            
            resultado_anterior2 = resultado_anterior1
    elif operador == '+':
        print(f'Resultado: {valor1 + valor2}')
        resultado = valor1 + valor2
        if contador2 >= 2:
            resultado_anterior1 = resultado
        if contador2 > 3:            
            resultado_anterior2 = resultado_anterior1
    elif operador == '-':
        print(f'Resultado: {valor1 - valor2}')
        resultado = valor1 - valor2
        if contador2 >= 2:
            resultado_anterior1 = resultado
        if contador2 > 3:            
            resultado_anterior2 = resultado_anterior1
    else:
        print('El operador que introduciste es incorrecto, intentalo de nuevo')