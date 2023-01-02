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

# Variables y tipos de datos básicos

En este capítulo aprenderemos los principales tipos de datos básicos que un programa en Python puede manejar. 
También aprenderemos cómo usar variables para representar datos en nuestros programas.

Un algoritmo tiene asociado un nombre mediante el cual se podrá invocar s11 ejecución cuantas veces se desee.
Un algoritmo puede tener asociada una lista de parámetros cuyo fin es el intercambio de información posibilitando la entrada de información (datos) al algoritmo en el momento de realizar su invocación y la salida de información (resultados) del algoritmo al concluir su ejecución.

Opcionalmente, un algoritmo puede definirse como función, en cuyo caso, tras la lista de parámetros debe especificarse una cláusula devuelve nombreTipo que define el tipo de dato que devolverá la función al ser invocada.
Un algoritmo sin esta última cláusula recibe el nombre de procedimiento.

Al definir un algoritmo debe incluirse una especificación que describa de forma clara y concisa el comportamiento del algoritmo, es decir, qllé es lo que hace el