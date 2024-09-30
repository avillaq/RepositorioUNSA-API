from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost:3306/repositorio_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Documentos(db.Model):
    id_documento = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    resumen = db.Column(db.Text, nullable=True)
    uri = db.Column(db.String(255), nullable=True)
    fecha = db.Column(db.String(4), nullable=True)
    url_pdf = db.Column(db.String(255), nullable=True)
    id_coleccion = db.Column(db.Integer, nullable=True)
    id_editor = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            'id_documento': self.id_documento,
            'titulo': self.titulo,
            'resumen': self.resumen,
            'uri': self.uri,
            'fecha': self.fecha,
            'url_pdf': self.url_pdf,
            'id_coleccion': self.id_coleccion,
            'id_editor': self.id_editor
        }


@app.route("/api/docs")
def hello_world():
    return "<p>Hello, World!</p>"
