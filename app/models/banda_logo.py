from app import db

class banda_logo(db.Model):
    __tablename__ = 'banda_logo'
    id_banda_logo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    logo_url = db.Column(db.String(255), nullable=False)
    alt_text = db.Column(db.String(255), nullable=False)
    
    fk_banda_logo_banda = db.relationship("banda", back_populates="fk_banda_banda_logo")
    
    def to_dict(self):
        return {
            "id_banda_logo": self.id_banda_logo,
            "logo_url": self.logo_url,
            "alt_text": self.alt_text
        }
