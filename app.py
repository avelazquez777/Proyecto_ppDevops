import requests

from flask import (
    Flask, 
    render_template,
    request,
    redirect,
)

listado_nombre =['Ana', 'Juan', 'Jose']
diccionario_nombre =[
    dict(
        name =dict(
            first = "Agustin",
            last="Invaldi"
    ),
    location=dict(
        city = "Canals",
    ),
    email = "agustin.@nollenalacancha.com"
),
    dict(
        name =dict(
            first = "Ana",
            last="Garcia",
    ),
    location=dict(
        city = "Rio cuarto",
    ),
    email = "Anagarcia@gmail.com"
),
        dict(
        name =dict(
            first = "Jose",
            last="Alcatraz",
    ),
    location=dict(
        city = "Higueras",
    ),
    email = "Jose@gmail.com"
),
    dict(
        name =dict(
            first = "Azul",
            last="Escudero",
    ),
    location=dict(
        city = "Rio cuarto",
    ),
    email = "Escuderoazul@gmail.com"
    ),
]

app = Flask(__name__)


@app.route('/') # app es la instancia, route el metodo, '/' es el disparador
def index():
    return render_template(
        'index.html',
    )

@app.route('/info') # app es la instancia, route el metodo, '/' es el disparador
def informacion():
    return render_template(
        'informacion.html',
    )

#import requests
@app.route('/personas') # app es la instancia, route el metodo, '/' es el disparador
def personas():
    # peticion = requests.get('https://randomuser.me/api/?results=50')
    # listado_personas = peticion.json()['results']
    # print(listado_personas)
    Listado_personas= diccionario_nombre
    return render_template(
        'personas.html',
        listado = Listado_personas
    )


@app.route('/bienvenido/<nombre>')
def bienvenida(nombre):
    return render_template(
        'bienvenida.html',
    )

@app.route('/personas_add', methods=['GET','POST'])
def agregar_personas():
    if request.method == 'GET':
        print("Hice un Get")

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        ciudad = request.form['ciudad']
        
        persona = dict(
            name =dict(
                first = nombre,
                last= apellido,
            ),
            location=dict(
                city = ciudad
            ),
            email = email
        )

        diccionario_nombre.append (persona)

        return redirect ('personas')
    return render_template ('add_personas.html')


linea_modificada = "1234"
print("Taller de DevOps 2024")