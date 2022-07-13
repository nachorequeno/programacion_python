# Ejercicio 1.- Pendiente de una recta
Escribir un programa que solicite al usuario las coordenadas (x, y) de dos puntos, P_1(x_1,y_1) y P_2(x_2,y_2), y calcule la pendiente de la recta que pasa por ambos puntos. La pendiente de una recta se calcula como:

$$
  m = \frac{y_2 - y_1}{x_2 - x_1}
$$

# Ejercicio 2.- Super ofertas 3x2
En el Supermercado ``AhorraMucho'' se ofrece la promoción de llevarse tres productos por el precio de los dos más caros. Escribir un programa que, dados los tres precios de los productos, determine la cantidad a pagar.


# Ejercicio 3.- Nota de Programación
Escribe un programa que te muestre la nota que sacarás en Programación I si has decidido seguir la evaluación continua. Deberá de escribir en pantalla la nota (el valor numérico) y una de las siguientes palabras según corresponda (suspenso, aprobado, notable, sobresaliente, MH). La nota se calculará según lo que aparece en la ficha de la asignatura:
- Ejercicios de clase evaluados (60%), la nota de los ejercicios se ponderará, el primer examen un 40 % y el segundo un 60%.
- Realización y defensa de prácticas de laboratorio, consistentes en programas informáticos propuestos por el profesor (30%)
- Participación del estudiante en el aula, en las actividades formativas propuestas por el profesor y en las tutorías (10%)


# Ejercicio 4.- Número de días de un mes
Escribe un programa que partiendo de un número de mes (1..12) y el año, nos diga el número de días que tiene el mes dado. Si el año es bisiesto febrero tendrá 29 días.
“Son bisiestos todos los años divisibles por 4, excluyendo los que sean divisibles por 100, pero no los que sean divisibles por 400.”

# Ejercicio 5.- ¿Es triángulo?
Escribir un programa que solicite tres cantidades reales positivas, compruebe si esas cantidades pueden corresponder a las longitudes de los lados de un triángulo, si pueden formar un triángulo que nos diga el tipo: equilátero, isósceles o escaleno y si no pueden formar un triángulo que escriba un mensaje en pantalla.
Tres cantidades pueden representar las longitudes de los lados de un triángulo si se verifica siempre que la suma de dos de ellas es mayor que la otra.

# Ejercicio 6.- Cálculo de la masa corporal de una persona
Escribir un programa que calcule el índice de masa corporal de una persona (IMC = peso [kg]/altura2 [m]), dado su peso y su altura, e indique el estado en el que se encuentra esa persona en función del valor de IMC:


# Ejercicio 7.- Calcular la letra del NIF
Para calcular la letra del N.I.F. se toma el número del D.N.I. y se divide por 23, se quitan los decimales y se multiplica el resultado por 23, se resta la cifra así obtenida del número del D.N.I., la letra del N.I.F. es la que corresponda según el cuadro siguiente:

| A=3  | J=13 | S=15 |
| B=11 | K=21 | T=0  |
| C=20 | L=19 | V=17 |
| D=9  | M=5  | W=2  |
| E=22 | N=12 | X=10 |
| F=7  | P=8  | Y=6  |
| G=4  | Q=16 | Z=14 |
| H=18 | R=1  |      |

Este proceso equivale a calcular el resto entero de la división entera del D.N.I. por 23.
Escribir un programa que solicite al usuario el número del DNI y calcule la letra del NIF.