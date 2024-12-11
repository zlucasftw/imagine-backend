from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import relationship

from app import db

class BandaHistoria(db.Model):
    __tablename__ = 'banda_historia'
    id_banda_historia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    historia = db.Column(Text, nullable=False)

    fk_banda_historia_banda = relationship("Banda", back_populates="fk_banda_banda_historia")    
    # fk_banda_historia_banda = db.ForeignKeyConstraint(['id_banda'], ['banda.id_banda'])
    
    def to_dict(self):
        return {
            "id_banda_historia": self.id_banda_historia,
            "titulo": self.titulo,
            "historia": self.historia
        }
