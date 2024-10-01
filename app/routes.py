from flask import jsonify
from . import db
from .models import Documento

@app.route('/documentos', methods=['GET'])
def get_documentos():
    documentos = Documento.query.all()
    resultado = [documento.format() for documento in documentos]
    return jsonify(resultado)
