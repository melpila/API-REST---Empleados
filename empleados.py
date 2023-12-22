import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'
empleados = requests.get(url).json()
print(empleados)


if empleados['status'] == 'success':
    lista_empleados = empleados['data']

    # Inicializar variables para cálculos
    total_salario = 0
    total_edad = 0
    salario_min = float('inf')
    salario_max = float('-inf')
    edad_min = float('inf')
    edad_max = float('-inf')


    for empleado in lista_empleados:
        salario = int(empleado['employee_salary'])
        edad = int(empleado['employee_age'])

        total_salario += salario
        total_edad += edad

        if salario < salario_min:
            salario_min = salario
        if salario > salario_max:
            salario_max = salario

        if edad < edad_min:
            edad_min = edad
        if edad > edad_max:
            edad_max = edad

    promedio_salario = total_salario / len(lista_empleados)
    promedio_edad = total_edad / len(lista_empleados)

    print(f"Promedio de salario: {promedio_salario}")
    print(f"Promedio de edad: {promedio_edad}")
    print(f"Salario mínimo: {salario_min}")
    print(f"Salario máximo: {salario_max}")
    print(f"Edad mínima: {edad_min}")
    print(f"Edad máxima: {edad_max}")
else:
    print("Error al obtener los datos de los empleados")