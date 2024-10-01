from flask import jsonify
from ..models import Documento
from app.api import bp

@bp.route('/documentos', methods=['GET'])
def get_documentos():
    documentos = Documento.query.all()
    resultado = [documento.format() for documento in documentos]
    return jsonify(resultado)

@bp.route('/')
def index():
    return 'This is The Main Blueprint'