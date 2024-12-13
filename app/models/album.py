from app import db

class album(db.Model):
    __tablename__ = 'album'
    id_album = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    ano_lancamento = db.Column(db.Integer, nullable=False)
    id_banda = db.Column(db.Integer, db.ForeignKey('banda.id_banda', name="fk_album_banda", ondelete="CASCADE"), nullable=False)
    
    fk_album_banda = db.relationship("banda", back_populates="fk_banda_album", cascade='all, delete')
    
    def to_dict(self):
        return {
            "id_album": self.id_album,
            "titulo": self.titulo,
            "genero": self.genero,
            "ano_lancamento": self.ano_lancamento,
            "id_banda": self.id_banda
        }
