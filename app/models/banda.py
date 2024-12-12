from app import db

class banda(db.Model):
    __tablename__ = 'banda'
    id_banda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_banda = db.Column(db.String(100), nullable=False)
    ano_formacao = db.Column(db.Integer, nullable=False)
    
    id_banda_historia = db.Column(db.Integer, db.ForeignKey('banda_historia.id_banda_historia', name="fk_banda_banda_historia"), nullable=False)
    id_banda_logo = db.Column(db.Integer, db.ForeignKey('banda_logo.id_banda_logo', name="fk_banda_banda_logo"), nullable=False)
    
    fk_banda_banda_historia = db.relationship("banda_historia", back_populates="fk_banda_historia_banda", cascade="all, delete")
    fk_banda_banda_logo = db.relationship("banda_logo", back_populates="fk_banda_logo_banda", cascade="all, delete")
    fk_banda_banda_imagem = db.relationship("banda_imagem", back_populates="fk_banda_imagem_banda", cascade="all, delete")
    
    def to_dict(self):
        return {
            "id_banda": self.id_banda,
            "nome_banda": self.nome_banda,
            "ano_formacao": self.ano_formacao,
            "historia": self.fk_banda_banda_historia.to_dict(),
            "logo": self.fk_banda_banda_logo.to_dict()
        }