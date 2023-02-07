---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# Algunos conceptos básicos
## Problemas de tratamiento de información, algoritmos y programas

La programación es una actividad cuyo fin es la resolución automática de *problemas de tratamiento de información*
en campos de aplicación muy diversos tales como el cálculo o cómputo (del cual procede el término computador, y de origen anglosajón), la gestión (del cual procede el término ordenador, de origen francés), el control (de procesos industriales, de robots, de vehículos espaciales, de automóviles etc.), el tratamiento de señal, la biomedicina, la inteligencia artificial (reconocimiento de imágenes, reconocimiento de voz, lenguaje natural, planificación inteligente, sistemas expertos, etc.), los juegos, etc, etc. 

Los computadores (así van a ser denominados en este curso) u ordenadores son las máquinas que se utilizan como herramientas para resolver de forma automática problemas de tratamiento de información.
El comportamiento de un computador viene regido por un programa cuya ejecución permite la resolución del problema considerado. 

A partir de un problema de tratamiento de información ¿cómo obtener el programa que lo resuelva al ser ejecutado en un computador? 

El primer paso es la identificación de uno o más métodos que permitan resolver el problema en cuestión. 
A continuación habrá que seleccionar uno de ellos atendiendo a consideraciones como su eficiencia, su sencillez, etc. 
El siguiente paso será la formalización, por escrito, del método seleccionado mediante un documento en el que se haga una descripción de la información relevante asociada al problema y una descripción del modo en que debe ser tratada esa información para resolverlo, es decir, la descripción de una secuencia ordenada _y finita. de_ pasos, exenta de ambigüedades, cuya ejecición proporcione una solución al problema considerado. 
El resultado de esta formalización recibe el nombre de algoritmo. 

Un algoritmo puede ser escrito utilizando un lenguaje de programación de computadores como, por ejemplo, Ada, C, C++, Java, Módula-2 o Pascal.
No obstante, en un curso introductorio de programación dirigido a personas que, en su vida profesional, van a utilizar un amplio conjunto de lenguajes de programación es muy recomendable tomar una cierta distancia de cualquier lenguaje de programación "comercial" concreto.
Para comprender y saber aplicar los conceptos básicos de la programación es preferible utilizar una notación de algoritmos o notación algorítmica que no se ciña estrictamente a ningún lenguaje de programación "comercial" y que además utilice unos términos y una sintaxis que sea próxima a la lengua materna de los alumnos.
Además, es bien conocido el hecho de que la vigencia de un lenguaje de programación es bastante corta ya que en unos pocos años pasa a ser obsoleto ante nuevos lenguajes de programación que son desarrollados.

Todas las razones anteriores justifican que en estas notas se utilice una notación algorítmica propia, basada en la lengua castellana.
Su sintaxis se resume en un capítulo anexo, situado al final de estas notas.

Utilizando ya esta notación algorítmica, la definición de un algoritmo responde al siguiente esquema general:
...

Un algoritmo tiene asociado un nombre mediante el cual se podrá invocar su ejecución cuantas veces se desee. 
Un algoritmo puede tener asociada una lista de parámetros cuyo fin es el intercambio de información posibilitando la entrada de
información (datos) al algoritmo en el momento de realizar su invocación y la salida de información (resultados) del algoritmo al concluir su ejecución.

Opcionalmente, un algoritmo puede definirse como función, en cuyo caso, tras la lista de parámetros debe especificarse una cláusula devuelve nombreTipo que
define el tipo de dato que devolverá la función al ser invocada. Un algoritmo sin esta última cláusula recibe el nombre de procedimiento.

Al definir un algoritmo debe incluirse una especificación que describa de forma clara y concisa el comportamiento del algoritmo, es decir, qué es lo que hace el algoritmo cuando es ejecutado

1. Precondición: una descripción de las condiciones que deben satisfacer los datos de entrada al algoritmo.
2. Postcondición: una descripción de las cond1c1ones que deben satisfacer los datos de salida o resultados del algoritmo.

3. ....
4. 
Propiedades imprescindibles de un algoritmo son:
• Corrección, es decir un algoritmo debe proporcionar una solución conecta sin errores ni omisiones, al problema planteado.
• Legibilidad, es decir, que el documento que describe el algoritmo sea fácil de entender no sólo por su autor sino por otras personas que posean unos conocimientos suficientes de programación (por ejemplo, otros programadores).

Propiedades muy deseables de un algoritmo, aunque no estrictamente necesarias, son:

# Lenguajes de programación: elementos de un programa y ejecución de un programa
Existen cientos de lenguajes de programación de computadores.
Muchos de ellos son de propósito específico, es decir, han sido concebidos para escribir programas que resuelvan problemas en ámbitos de aplicación muy concretos.
En cambio, existen lo que se denomina lenguajes de programación de propósito general.
Entre los más difundidos en los últimos años podríamos citar, entre otros, Ada, C, C++, Java, Módula-2 o Pascal.
Cualquiera de ellos pudiera ser utilizado como lenguaje de referencia en un curso de introducción a la programación como el presente aunque, por las razones aducidas anteriormente, utilizaremos una notación algorítmica  propia  que  iremos  presentando  a medida que los nuevos   conceptos  y problemas a tratar lo exijan.

Los elementos y técnicas que se presenten alrededor de nuestra notación algorítmica son, en su mayoría, generalizables a los lenguajes de programación "comerciales" antes citados.

## Elementos de un algoritmo o programa

Símbolos. Un algoritmo o programa consta de una secuencia de símbolos que pueden pertenecer a las siguientes categorías:

•	Palabras claves o palabras reservadas por la notación algorítmica (o del lenguaje de programación): algoritmo, principio, fin, si, entonces, si_no, finSi, tabla, registro, fichero, mod, div, verdad, falso, etc.

•	Identificadores: nombres que se asocian a objetos informáticos que se definen en el algoritmo o programa.

•	Operadores:    +   -    *  /   > $\geq$ = $\neq$ < $\leq$ $\neg$ $\wee$ $\wedge$ etc.
•	Separadores:  , ; . ( )	[ ] etc.

Un identificador se construye, en nuestra notación algorítmica, de acuerdo con la
siguiente regla:
identificador : := <letra> { <letra> | <dígito> | _}

Esta notación, aplicada ahora a la especificación de la sintaxis de los símbolos,
será utilizada a lo largo del curso para especificar también la sintaxis de las frases
que se puedan construir concatenando símbolos. El meta-carácter "I" permite definir
opciones alternativas, mientras que lo encerrado entre llaves "{...}" puede
reproducirse cero o más veces . La regla anterior dice que un símbolo
identificador se construye como una secuencia de caracteres tal que el primero
es una letra y los sucesivos, si existen, pueden ser o letras o dígitos o el carácter '_'.
Las definiciones de letra y digi to se presentan a continuación mediante sus
correspondientes reglas sintácticas:

letra : : = A | B | `$\cdots$` | Y | Z | a | b | `$\cdots$` | y | z
digito : := O | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9