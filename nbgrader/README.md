Para que funcione correctamente nbgrader es conveniente
- crear un entorno virutal de python, lo llamaré nbragder, pero podéis
elegir el nombre que queráis.

python -m venv nbgrader

si lo cambiais de nombre, insertadlo en el .gitignore para que no haya conflictos.

- Activarlo
. ./nbgrader/bin/activate  # esto puede ser diferente en windows

- Instalar jupyterlab y nbgrader en este entorno

pip install jupyterlab nbgrader

- Descargarse un fichero de alumnos. Desde GEA, grabándolo en formato
  csv

- Hay un script que genera los comandos para añadir los alumnos a la
