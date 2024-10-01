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

    # Paginación
    page = request.args.get('page', 1, type=int)  # Página actual. 1 por defecto
    per_page = request.args.get('per_page', 10, type=int)  # Resultados por página. 10 por defecto

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

    # Aplicar paginación
    documentos_paginados = query.paginate(page=page, per_page=per_page)

    resultado = [documento.format() for documento in documentos_paginados.items]
    return jsonify(resultado)

@bp.route('/')
def index():
    return 'This is The Main Blueprint'