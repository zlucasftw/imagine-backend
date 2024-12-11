from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import relationship

class Banda(db.Model):
    __tablename__ = 'banda'
    id_banda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_banda = db.Column(db.String(100), nullable=False)
    ano_formacao = db.Column(db.String(4), nullable=False)
    id_banda_historia = db.Column(db.Integer, db.ForeignKey('banda_historia.id_banda_historia', name="fk_banda_banda_historia"), nullable=False)
    # banda_historia = relationship("BandaHistoria", backref="banda")
    fk_banda_banda_historia = db.relationship("BandaHistoria", back_populates="fk_banda_historia_banda")

    def to_dict(self):
        return {
            "id_banda": self.id_banda,
            "nome_banda": self.nome_banda,
            "ano_formacao": self.ano_formacao,
            "historia": self.fk_banda_banda_historia.to_dict()
        }
        # "banda_historia": [banda_historia.to_dict() for banda_historia in self.banda_historia]