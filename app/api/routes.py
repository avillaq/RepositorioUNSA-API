from flask import jsonify, request
from app.api.models import Documento
from app.api import bp
from app.extensions import db

@bp.route('/documentos', methods=['GET'])
def get_documentos():
    titulo = request.args.get('titulo')
    fecha = request.args.get('fecha')
    uri = request.args.get('uri')

    # Parametros para ordenar
    sort_by = request.args.get('sort_by', 'titulo')  # Por defecto es el título
    order = request.args.get('order', 'asc')  # Por defecto en orden ascendente

    query = Documento.query

    # Filtrar la consulta
    if titulo:
        query = query.filter(Documento.titulo.like(f'%{titulo}%'))
    if fecha:
        query = query.filter_by(fecha=fecha)
    if uri:
        query = query.filter_by(uri=uri)

    # Ordenar la consulta
    if sort_by in ['titulo', 'fecha', 'uri']:
        if order == 'desc':
            query = query.order_by(db.desc(getattr(Documento, sort_by)))
        else:
            query = query.order_by(getattr(Documento, sort_by))

    # Consultamos
    documentos = query.all()

    resultado = [documento.format() for documento in documentos]
    return jsonify(resultado)

@bp.route('/')
def index():
    return 'This is The Main Blueprint'