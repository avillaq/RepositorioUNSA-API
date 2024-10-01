from flask import jsonify, request
from app.api.models import Documento
from app.api import bp

@bp.route('/documentos', methods=['GET'])
def get_documentos():
    titulo = request.args.get('titulo')
    fecha = request.args.get('fecha')
    uri = request.args.get('uri')

    query = Documento.query

    # Filtrar la consulta
    if titulo:
        query = query.filter(Documento.titulo.like(f'%{titulo}%'))
    if fecha:
        query = query.filter_by(fecha=fecha)
    if uri:
        query = query.filter_by(uri=uri)

    documentos = query.all()

    resultado = [documento.format() for documento in documentos]
    return jsonify(resultado)

@bp.route('/')
def index():
    return 'This is The Main Blueprint'