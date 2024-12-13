from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Constraint, Text

# Definindo caminhos de UPLOAD de imagem
UPLOAD_FOLDER_LOGO = 'app/static/img/logo'
UPLOAD_FOLDER_BANDA = 'app/static/img/banda'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}


# Define ORM do DB sendo como de SQLAlchemy
db = SQLAlchemy()

# Cria a função para montar a aplicação Flask e a RETORNA
def create_app():
    
    # Define a aplicação como aplicação Flask
    app = Flask(__name__, static_folder='static')
    
    # Aplicando o CORS no app Flask para a API poder ser consumida por outra aplicação
    CORS(app)
        
    # Configuração do banco dados MySQL através do SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/imagine_backend'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados para o app
    db.init_app(app)
    
    # Importação dos Models
    from .models.banda import banda
    from .models.banda_historia import banda_historia
    from .models.banda_logo import banda_logo
    from .models.banda_imagem import banda_imagem
    from .models.album import album
    
    # Início da importação e registro de Blueprint para as rotas
    
    from .routes.routes import bp
    app.register_blueprint(bp)
    
    from .routes.bandas_routes import bp_bandas
    app.register_blueprint(bp_bandas)
    
    from .routes.banda_imagem_routes import bp_bandas_imagem
    app.register_blueprint(bp_bandas_imagem)
    
    from .routes.templates_routes import bp_templates
    app.register_blueprint(bp_templates)
    
    # Fim da importação e registro de Blueprint para as rotas   
    
    # Retorna app FLASK
    return app
