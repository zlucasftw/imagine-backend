from flask import Blueprint, jsonify, render_template, request, make_response, session, url_for, flash, redirect
# from sqlalchemy import Text
# from sqlalchemy.engine import Engine
from app.models.banda import Banda
from app import create_engine, text
# from werkzeug.utils import secure_filename
from datetime import datetime
from app import db

bp = Blueprint("main", __name__, template_folder='../templates/')

# @bp.route("/", methods=['GET', 'POST'])
# def index():
    
#     if request.method == 'GET':
#         return render_template('index.html')
#     else:
#         return make_response("Não encontrado", 404)
    
#     if request.method == 'POST':
#         return make_response("Método inválido!", 405)
    
# @bp.route("/home", methods=['GET'])
# def rota_home():
#     if request.method == 'GET':
#         return render_template('home.html')
#     else:
#         return make_response("Não encontrado", 404)
    
# @bp.route("/contato", methods=['GET'])
# def rota_contato():

#     if request.method == 'GET':
#         return render_template('contato.html')
#     else:
#         return make_response("Não encontrado", 404)
    
# @bp.route('/categorias', methods=['GET'])
# def quiz_categorias():
#     categorias = Categorias.query.all()
#     categorias_quiz = []
#     for categoria in categorias:
#         categorias.append(Categorias(fruta))
#     print(frutasQuitanda)
#     return jsonify(frutasQuitanda)

""" 

Serviço de tratamento para requisições no Endpoint de categoria.

"""

# @bp.route('/categoria/<nome_categoria>', methods=['POST'])
# def listar_quiz_categorias(nome_categoria : str):
#     query = text("SELECT IF EXISTS nome FROM categoria WHERE nome = :n_c")
#     categoria_bd = db.engine.execute(query, n_c=nome_categoria)
    
#     return []

""" 

Serviço de tratamento para requisições no Endpoint de login.
Realiza validação de login.

"""

# @bp.route("/contato", methods=["POST"])
# def registrar_contato():
    
#     nome_form, email_form, mensagem_form, telefone_form = None, None, None, None
    
#     if request.method == 'POST':
        
#         # nome_form = request.form('nome')
#         # email_form = request.form('email')
#         # mensagem_form = request.form('mensagem')
#         # telefone_form = request.form('telefone')
#         contato = request.get_json()
        
#         nome_form = contato['nome']
#         email_form = contato['email']
#         mensagem_form = contato['mensagem']
#         telefone_form = contato['telefone']
        
#         emails = Contato.query.all()

#         for email in emails:
        
#             if email.email == email_form:
#                 return jsonify({ "Erro": "Contato já enviado!" }), 400
        
#         novo_contato = Contato(nome=nome_form,email=email_form,mensagem=mensagem_form,telefone=telefone_form)
#         novo_contato_resposta = {}
        
#         try:
            
#             db.session.add(novo_contato)
#             db.session.commit()
            
#             novo_contato_resposta['nome'] = novo_contato.nome
#             novo_contato_resposta['email'] = novo_contato.email
#             novo_contato_resposta['mensagem'] = novo_contato.mensagem
#             novo_contato_resposta['telefone'] = novo_contato.telefone
#             print(jsonify(novo_contato_resposta))
#             return jsonify(novo_contato_resposta), 201
        
#         except Exception as exception:
#             db.session.rollback()
#             db.session.close()
#             print(exception)
#             return 500
        
#     else:
#         return jsonify({ "mensagem": "Login inválido!" }), 405

# @bp.route("/contato", methods=["GET"])
# def listar_contatos():
    
#     try:
        
#         # contatos = Contato.query.all()
        
#         # if contatos is None:
#         #     return jsonify({ "Erro": "Erro no servidor" }), 500
        
#         contato_resposta = []
        
#         # for contato in contatos:
#             contato_resposta.append(contato)
        
#         # print(contato)
        
#         # if not contato:
#         #     return jsonify({ "Erro": "Não encontrado" }), 404
#         # else:
#         return jsonify(contato_resposta), 302
    
#     except Exception as exception:
#         return jsonify({ "Erro": "Erro no servidor" }), 500


@bp.route("/", methods=['GET'])
def index():

    bandas = Banda.query.all()
    bandas_resposta = []
    
    engine = create_engine('mysql+pymysql://root:root@localhost:3306/imagine_backend')
    
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM banda"))
        for row in result:
            print("Nome da banda: ", row.nome_banda)

    for banda in bandas:
        bandas_resposta.append(Banda.to_dict(banda))

    print(bandas_resposta)
    
    album_cards = [
        {
            "titulo": "This is Why",
            "ano": "2013",
            "banda": "Paramore",
            "imagem_url": "static/img/albumcards01.webp",
            "alt_text": "Imagem do album This is Why da banda Paramore"
        }
    ]
    return render_template('index.html', album_cards=album_cards)

# @bp.route("/cards", methods=['POST'])
# def listar_cards():
    # cards = Card.query.all()
    # cards_resposta = []
    # for card in cards:
    #     cards_resposta.append(card)
    # return jsonify(cards_resposta)
