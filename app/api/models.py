from app.extensions import db

class Documento(db.Model):
    __tablename__ = 'documentos'

    id_documento = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    resumen = db.Column(db.Text, nullable=True)
    uri = db.Column(db.String(255), nullable=True)
    fecha = db.Column(db.Date, nullable=True)
    url_pdf = db.Column(db.String(255), nullable=True)
    id_coleccion = db.Column(db.Integer, nullable=True)
    id_editor = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Documento {self.titulo}>"

    def format(self):
        return {
            'id': self.id_documento,
            'titulo': self.titulo,
            'resumen': self.resumen,
            'uri': self.uri,
            'fecha': self.fecha,
            'url_pdf': self.url_pdf,
            'id_coleccion': self.id_coleccion,
            'id_editor': self.id_editor
        }

class Coleccion(db.Model):
    __tablename__ = 'colecciones'

    id_coleccion = db.Column(db.Integer, primary_key=True)
    nombre_coleccion = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Coleccion {self.nombre_coleccion}>"

    def format(self):
        return {
            'id': self.id_coleccion,
            'nombre_coleccion': self.nombre_coleccion,
        }
    
class Autor(db.Model):
    __tablename__ = 'autores'

    id_autor = db.Column(db.Integer, primary_key=True)
    nombre_autor = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Autor {self.nombre_autor}>"

    def format(self):
        return {
            'id': self.id_autor,
            'nombre_autor': self.nombre_autor,
        }

class Documento_Autor(db.Model):
    __tablename__ = 'documento_autores'

    id_documento = db.Column(db.Integer, primary_key=True)
    id_autor = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<Documento_Autor {self.id_documento}>"

    def format(self):
        return {
            'id_documento': self.id_documento,
            'id_autor': self.id_autor,
        }