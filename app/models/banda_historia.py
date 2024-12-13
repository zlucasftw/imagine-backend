from app import db

class banda_historia(db.Model):
    __tablename__ = 'banda_historia'
    id_banda_historia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    historia = db.Column(db.Text, nullable=False)

    fk_banda_historia_banda = db.relationship("banda", back_populates="fk_banda_banda_historia", cascade='all, delete')
    
    def to_dict(self):
        return {
            "id_banda_historia": self.id_banda_historia,
            "titulo": self.titulo,
            "historia": self.historia
        }
