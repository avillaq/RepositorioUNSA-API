from flask import jsonify, request
from app.api.models import Documento, Coleccion, Autor
from app.api import bp
from app.extensions import db, limiter, cache

@bp.route('/documentos', methods=['GET'])
@limiter.limit("10/minute")
@cache.cached(query_string=True)
def get_documentos():
    titulo = request.args.get('titulo')
    fecha = request.args.get('fecha')

    # TODO: Agregar filtros adicionales: autor, coleccion y palabra clave

    # Parametros para ordenar
    sort = request.args.get('sort', 'titulo')  # Por defecto es el título
    order = request.args.get('order', 'asc')  # Por defecto en orden ascendente

    # Paginación
    page = request.args.get('page', 1, type=int)  # Página actual. 1 por defecto
    limit = request.args.get('limit', 10, type=int)  # Resultados por página. 10 por defecto

    documentos = Documento.query

    # Filtrar la consulta
    if titulo:
        documentos = documentos.filter(Documento.titulo.like(f'%{titulo}%'))
    if fecha:
        documentos = documentos.filter_by(fecha=fecha)

    # Ordenar la consulta
    if sort in ['titulo', 'fecha']:
        if order == 'desc':
            documentos = documentos.order_by(db.desc(getattr(Documento, sort)))
        else:
            documentos = documentos.order_by(getattr(Documento, sort))

    # Aplicar paginación
    documentos_paginados = documentos.paginate(page=page, per_page=limit)

    resultado = {
        'page': documentos_paginados.page,
        'total_pages': documentos_paginados.pages,
        'total_items': documentos_paginados.total,
        'items': [documento.format() for documento in documentos_paginados.items]
    }
    return jsonify(resultado)

@bp.route('/documentos/<int:id>/', methods=['GET'])
@limiter.limit("10/minute")
@cache.cached(query_string=True)
def get_documento(id):
    documento = Documento.query.get_or_404(id)
    return jsonify(documento.format())

@bp.route('/colecciones', methods=['GET'])
@limiter.limit("10/minute")
@cache.cached(query_string=True)
def get_colecciones():
    nombre_coleccion = request.args.get('nombre_coleccion')

    # Parametros para ordenar
    order = request.args.get('order', 'asc')  # Por defecto en orden ascendente

    # Paginación
    page = request.args.get('page', 1, type=int)  # Página actual. 1 por defecto
    per_page = request.args.get('per_page', 10, type=int)  # Resultados por página. 10 por defecto

    colecciones = Coleccion.query

    # Filtrar la consulta
    if nombre_coleccion:
        colecciones = colecciones.filter(Coleccion.nombre_coleccion.like(f'%{nombre_coleccion}%'))

    # Ordenar la consulta
    if order == 'desc':
        colecciones = colecciones.order_by(db.desc(Coleccion.nombre_coleccion))
    else:
        colecciones = colecciones.order_by(Coleccion.nombre_coleccion)

    # Aplicar paginación
    colecciones_paginados = colecciones.paginate(page=page, per_page=per_page)

    resultado = {
        'page': colecciones_paginados.page,
        'total_pages': colecciones_paginados.pages,
        'total_items': colecciones_paginados.total,
        'items': [coleccion.format() for coleccion in colecciones_paginados.items]
    }
    return jsonify(resultado)

@bp.route('/colecciones/<int:id>/', methods=['GET'])
@limiter.limit("10/minute")
@cache.cached(query_string=True)
def get_coleccion(id):
    coleccion = Coleccion.query.get_or_404(id)
    return jsonify(coleccion.format())

@bp.route('/colecciones/<int:id>/documentos', methods=['GET'])
@limiter.limit("10/minute")
@cache.cached(query_string=True)
def get_documentos_de_coleccion(id):
    coleccion = Coleccion.query.get_or_404(id)

    titulo = request.args.get('titulo')
    fecha = request.args.get('fecha')

    # TODO: Agregar filtros adicionales: autor, palabra clave

    # Ordenar
    sort = request.args.get('sort', 'titulo')  # Por defecto es el título
    order = request.args.get('order', 'asc')  # Por defecto en orden ascendente

    # Paginación
    page = request.args.get('page', 1, type=int)  # Página actual. 1 por defecto
    limit = request.args.get('limit', 10, type=int)  # Resultados por página. 10 por defecto

    documentos = Documento.query.filter_by(id_coleccion=coleccion.id_coleccion)

    # Filtrar la consulta
    if titulo:
        documentos = documentos.filter(Documento.titulo.like(f'%{titulo}%'))
    if fecha:
        documentos = documentos.filter_by(fecha=fecha)

    # Ordenar la consulta
    if sort in ['titulo', 'fecha']:
        if order == 'desc':
            documentos = documentos.order_by(db.desc(getattr(Documento, sort)))
        else:
            documentos = documentos.order_by(getattr(Documento, sort))
            
    # Aplicar paginación
    documentos_paginados = documentos.paginate(page=page, per_page=limit)

    resultado = {
        'page': documentos_paginados.page,
        'total_pages': documentos_paginados.pages,
        'total_items': documentos_paginados.total,
        'items': [documento.format() for documento in documentos_paginados.items]
    }
    return jsonify(resultado)

@bp.route('/autores', methods=['GET'])
@limiter.limit("10/minute")
@cache.cached(query_string=True)
def get_autores():
    nombre_autor = request.args.get('nombre_autor')

    # Ordenar
    order = request.args.get('order', 'asc')  # Por defecto en orden ascendente

    # Paginación
    page = request.args.get('page', 1, type=int)  # Página actual. 1 por defecto
    limit = request.args.get('limit', 10, type=int)  # Resultados por página. 10 por defecto

    autores = Autor.query

    # Filtrar la consulta
    if nombre_autor:
        autores = autores.filter(Autor.nombre_autor.like(f'%{nombre_autor}%'))

    # Ordenar la consulta
    if order == 'desc':
        autores = autores.order_by(db.desc(Autor.nombre_autor))
    else:
        autores = autores.order_by(Autor.nombre_autor)

    # Aplicar paginación
    autores_paginados = autores.paginate(page=page, per_page=limit)

    resultado = {
        'page': autores_paginados.page,
        'total_pages': autores_paginados.pages,
        'total_items': autores_paginados.total,
        'items': [autor.format() for autor in autores_paginados.items]
    }
    return jsonify(resultado)

@bp.route('/autores/<int:id>/', methods=['GET'])
@limiter.limit("10/minute")
@cache.cached(query_string=True)
def get_autor(id):
    autor = Autor.query.get_or_404(id)
    return jsonify(autor.format())

@bp.route('/autores/<int:id>/documentos', methods=['GET'])
@limiter.limit("10/minute")
@cache.cached(query_string=True)
def get_documentos_de_autor(id):
    autor = Autor.query.get_or_404(id)

    titulo = request.args.get('titulo')
    fecha = request.args.get('fecha')

    # TODO: Agregar filtros adicionales: coleccion y palabra clave

    # Ordenar
    sort = request.args.get('sort', 'titulo')  # Por defecto es el título
    order = request.args.get('order', 'asc')  # Por defecto en orden ascendente

    # Paginación
    page = request.args.get('page', 1, type=int)  # Página actual. 1 por defecto
    limit = request.args.get('limit', 10, type=int)  # Resultados por página. 10 por defecto

    documentos = Documento.query.filter_by(id_editor=autor.id_autor)

    # Filtrar la consulta
    if titulo:
        documentos = documentos.filter(Documento.titulo.like(f'%{titulo}%'))
    if fecha:
        documentos = documentos.filter_by(fecha=fecha)

    # Ordenar la consulta
    if sort in ['titulo', 'fecha']:
        if order == 'desc':
            documentos = documentos.order_by(db.desc(getattr(Documento, sort)))
        else:
            documentos = documentos.order_by(getattr(Documento, sort))

    # Aplicar paginación
    documentos_paginados = documentos.paginate(page=page, per_page=limit)

    resultado = {
        'page': documentos_paginados.page,
        'total_pages': documentos_paginados.pages,
        'total_items': documentos_paginados.total,
        'items': [documento.format() for documento in documentos_paginados.items]
    }
    return jsonify(resultado)

@bp.errorhandler(429)
def ratelimit_error(e):
    return jsonify(error="Rate limit exceeded", message=str(e.description)), 429

@bp.errorhandler(404)
def not_found_error(e):
    return jsonify(error="Not found", message=str(e.description)), 404

@bp.route('/')
def index():
    return jsonify(message="Welcome to the API")