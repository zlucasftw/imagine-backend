from app import db
from enum import Enum

class categoria_imagem(Enum):
    album = 'album'
    banda = 'banda'
    cards = 'cards'
    marquee = 'marquee'

class banda_imagem(db.Model):
    __tablename__= 'banda_imagem'
    id_banda_imagem = db.Column(db.Integer, primary_key=True, autoincrement=True)
    imagem_url = db.Column(db.String(255), nullable=False)
    alt_text = db.Column(db.String(255), nullable=False)
    tipo_imagem = db.Column(db.Enum(categoria_imagem), nullable=False)
    id_banda = db.Column(db.Integer, db.ForeignKey('banda.id_banda', name="fk_banda_imagem_banda"), nullable=False)
    
    fk_banda_imagem_banda = db.relationship("banda", back_populates="fk_banda_banda_imagem", cascade="all, delete")
    
    def to_dict(self):
        return {
            "id_banda_imagem": self.id_banda_imagem,
            "imagem_url": self.imagem_url,
            "alt_text": self.alt_text,
            "tipo_imagem": self.tipo_imagem.value,
            "id_banda": self.id_banda
        }