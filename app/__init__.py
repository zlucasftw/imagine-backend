from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Constraint, Text

# base = declarative_base()

# Define ORM do DB com método SQLAlchemy()
db = SQLAlchemy()

# Cria a função para montar a aplicação Flask e a RETORNA
def create_app():
    
    app = Flask(__name__, static_folder='static')
    
    # Aplicando o CORS no app Flask para a API poder ser consumida por outra aplicação
    CORS(app)
        
    # Configuração banco dados MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/imagine_backend'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Criando Engine para conexão co mo banco de dados
    # engine = create_engine('mysql+pymysql://root:root@localhost:3306/imagine_backend')
    # app = engine
    
    # engine = create_engine('mysql+pymysql://root:root@localhost:3306/quiz')
    
    # SESSION = sessionmaker(engine)
    
    #Inicializa o metódo db para app
    db.init_app(app)
    
    # Importação dos Models
    from .models.banda import Banda
    from .models.banda_historia import BandaHistoria
    
    # Início: Importamos e registramos o Blueprint para as rotas
    
    from .routes.routes import bp
    app.register_blueprint(bp)
    
    from .routes.bandas_routes import bp_bandas
    app.register_blueprint(bp_bandas)
    
    # Fim: Importamos e registramos o Blueprint para as rotas    
    
    # Retorno do app FLASK
    return app    
