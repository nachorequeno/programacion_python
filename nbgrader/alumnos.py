import csv
import sys

def adduser(filename):
    with open(filename) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            name = row["NOMBRE COMPLETO"].split(',')
            name = f'{name[1].strip()} {name[0].strip()}'
            username = row["CORREO"].replace("@ucm.es","")
            print(f'adduser --home /srv/home/{username} --disabled-login -gecos "{name}" {username}')
            print(f'addgroup {username} progI2223')

def deluser(filename):
    with open(filename) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            name = row["NOMBRE COMPLETO"].split(',')
            name = f'{name[1].strip()} {name[0].strip()}'
            username = row["CORREO"].replace("@ucm.es","")
            print(f'deluser --remove-all-files {username}')


def puertos(filename):
    port=271
    with open(filename) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            name = row["NOMBRE COMPLETO"]
            username = row['CORREO'].replace('@ucm.es', '')
            print(f'"{name}", {username}, {port}XX')
            port += 1

def lista_users(filename):
    with open(filename) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            username = row['CORREO'].replace('@ucm.es', '')
            print(f'{username}')


CREATE_MONGO_USER = \
    """
db.createUser(
{{
    user: "{user}",
    pwd: "{user}",
    roles: [ {{ role: "readWrite", db: "{user}" }},
             {{ role: "read", db: "test"}},
             {{ role: "read", db: "admin"}}  ]
}})
    """

def mongo_users(filename):
    with open(filename) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            email = row["CORREO"].replace("@ucm.es","")
            print(CREATE_MONGO_USER.format(user=email))

def nbgrader(filename):
    with open(filename) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            name = row["NOMBRE COMPLETO"].split(',')
            firstname = f'{name[1].strip()}'
            lastname = f'{name[0].strip()}'
            email = row["CORREO"]
            username = email.replace("@ucm.es","")
            print(f'nbgrader db student add  --first-name "{firstname}" --last-name "{lastname}" --email {email} {username}')

if __name__ == '__main__':
    #adduser(sys.argv[1])
    #mongo_users(sys.argv[1])
    #puertos(sys.argv[1])
    nbgrader(sys.argv[1])
    #lista_users(sys.argv[1])
