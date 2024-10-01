from . import db

class Documento(db.Model):
    __tablename__ = 'documentos'

    id_documento = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    resumen = db.Column(db.Text, nullable=True)
    uri = db.Column(db.String(255), nullable=True)
    fecha = db.Column(db.String(4), nullable=True)
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