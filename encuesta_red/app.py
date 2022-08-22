from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "database/database.db")

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



class Encuesta(db.Model):
    __tablename__ = "encuesta"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    age = db.Column(db.String(1))
    gender = db.Column(db.String(1))
    socialmedia = db.Column(db.String(1))
    whatsapptime = db.Column(db.Integer)
    facebooktime = db.Column(db.Integer)
    twittertime = db.Column(db.Integer)
    instagramtime = db.Column(db.Integer)
    tiktoktime = db.Column(db.Integer)

def Resultados(red):
    datos = {
		'red': red,
		'favorite':0,
		'suma':0,
		'total':0,
  		'edadA': 0,
		'edadB': 0,
		'edadC': 0,
		'edadD': 0,
	}
    return datos

def agregar(nombre,d):
    red = Resultados(nombre)
    red['total'] = red['total'] + 1
    if d.gender == 'A':
        red['edadA'] = red['edadA'] + 1
    elif d.gender == 'B':
        red['edadB'] = red['edadB'] + 1
    elif d.gender == 'C':
        red['edadC'] = red['edadC'] + 1
    elif d.gender == 'D':
        red['edadD'] = red['edadD'] + 1
    return red

@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})
    
@app.route("/formulario")
def index():
    print('Formulario')
    return render_template('index.html')    

@app.route("/prueba", methods = ['GET'])
def prueba():
    print('prueba')
    return 'Prueba'

@app.route('/submitted', methods = ['POST'])
def submitted():
    request_data = request.get_json()
    encuesta = Encuesta(
		email=request_data['email'],
		age=request_data['age'],
		gender=request_data['gender'],
		socialmedia=request_data['socialmedia'],
		whatsapptime = request_data['whatsapptime'],
    	facebooktime = request_data['facebooktime'],
    	twittertime = request_data['twittertime'],
    	instagramtime = request_data['instagramtime'],
    	tiktoktime = request_data['tiktoktime']
	)
    db.session.add(encuesta)
    db.session.commit()
    print('Recibido')
    Mensaje = 'Guardado'
    return jsonify(Mensaje)
    
@app.route("/stadistic",methods=["POST"])
def get_encuesta():
    Datos = Encuesta.query.all()
    totalEncuesta = Encuesta.query.count()
    whatsapp = Resultados(red='whatsapp')
    facebook = Resultados(red='facebook')
    twitter = Resultados(red='twitter')
    instagram = Resultados(red='instagram')
    tiktok = Resultados(red='tiktok')
            
    for d in Datos:
        if d.whatsapptime > 0:
            whatsapp = agregar(nombre = 'whatsapp',d=d)
            whatsapp['suma'] = whatsapp['suma'] + d.whatsapptime
        if d.facebooktime > 0:
            facebook = agregar(nombre = 'facebook',d=d)
            facebook ['suma'] = facebook ['suma'] + d.facebooktime
        if d.twittertime > 0:
            twitter = agregar(nombre = 'twitter',d=d)
            twitter['suma'] = twitter['suma'] + d.twittertime
        if d.instagramtime > 0:
            instagram = agregar(nombre = 'instagram',d=d)
            instagram['suma'] = instagram['suma'] + d.instagramtime
        if d.tiktoktime > 0:
            tiktok = agregar(nombre = 'tiktok',d=d)
            tiktok['suma'] = tiktok['suma'] + d.tiktoktime
    
        if d.socialmedia == 'A':
            whatsapp['favorite'] = whatsapp['favorite'] + 1
        elif d.socialmedia == 'B':
            facebook['favorite'] = facebook['favorite'] + 1
        elif d.socialmedia == 'C':
            twitter['favorite'] = twitter['favorite'] + 1
        elif d.socialmedia == 'D':
            instagram['favorite'] = instagram['favorite'] + 1
        else:
            tiktok['favorite'] = tiktok['favorite'] + 1
            
    result = {
		'totalencuesta':totalEncuesta,
  		'whatsapp': whatsapp,
		'facebook': facebook,
		'twitter': twitter,
		'instagram': instagram,
		'tiktok': tiktok
	}
    
    return (jsonify(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    