from flask import Blueprint, json, jsonify, render_template, request, make_response, session, url_for, flash, redirect
import traceback
from sqlalchemy.exc import SQLAlchemyError
from app.models.banda import banda
from app.models.banda_historia import banda_historia
from app.models.banda_logo import banda_logo
from app.models.banda_imagem import banda_imagem
# from werkzeug.utils import secure_filename
from datetime import datetime
from app import db

bp_bandas = Blueprint("bandas", __name__, template_folder='templates')

@bp_bandas.route("/bandas", methods=['GET'])
def pagina_bandas():
    
    if request.method == 'GET':
        
        try:
            
            # bandas = db.session.execute(db.select(banda, banda_historia, banda_logo, banda_imagem).join(banda_historia).join(banda_logo).join(banda_imagem))

            # bandas = banda.query.all()

            # bandas_json = []
            
            # for bandas_imagens in bandas:
            #     bandas_json.append(bandas_imagens.to_dict())
            
            
            bandas = db.session.execute(db.select(banda, banda_imagem).join(banda_imagem)).all()
            
            bandas_json = []
            
            for bandas_imagens in bandas:
                bandas_json.append({
                    "bandas": bandas_imagens.banda.to_dict(),
                    "imagem": bandas_imagens.banda_imagem.to_dict()
                })
            
            # for bandas_imagens in bandas:
            #     bandas_json.append({
            #         "bandas": bandas_imagens.banda.to_dict(),
            #         "imagem": bandas_imagens.banda_imagem.to_dict()
            #     })
                
            if not bandas_json:
                return jsonify({ "Erro": "Não encontrado" }), 404
            
            # return jsonify(bandas_json)
            return render_template("bandas.html", nova_banda=bandas_json)
            
        except SQLAlchemyError as exception:
            print(exception)
            return jsonify({ "Erro": "Erro na requisição! " }), 500
        
    else:
        return jsonify({ "Erro": "Método não permitido" }), 405
    
@bp_bandas.route("/api/bandas", methods=['GET'])
def listar_bandas():
    
    if request.method == 'GET':
        
        try:
            
            bandas = banda.query.all()
            
            bandas_json = []
            
            for bandas_imagens in bandas:
                bandas_json.append(bandas_imagens.to_dict())
            
            if not bandas_json:
                return jsonify({ "Erro": "Não encontrado" }), 404
            
            return jsonify(bandas_json)
            
        except db.exc.SQLAlchemyError as exception:
            tb = traceback.format_exc(exception)
            print(tb)
            return jsonify({ "Erro": "Erro na requisição! " }), 500
        
    else:
        return jsonify({ "Erro": "Método não permitido" }), 405
    
@bp_bandas.route("/api/bandas/all", methods=['GET'])
def listar_todas_bandas():
    
    if request.method == 'GET':
        
        try:
            
            bandas = db.session.execute(db.select(banda, banda_imagem).join(banda_imagem)).all()
            
            bandas_json = []
            
            for bandas_imagens in bandas:
                bandas_json.append({
                    "bandas": bandas_imagens.banda.to_dict(),
                    "imagem": bandas_imagens.banda_imagem.to_dict()
                })
                
            if not bandas_json:
                return jsonify({ "Erro": "Não encontrado" }), 404
            
            return jsonify(bandas_json)
            
        except Exception as exception:
            db.session.rollback()
            print(exception)
            return jsonify({ "Erro": "Erro na requisição! " }), 500
        
    else:
        return jsonify({ "Erro": "Método não permitido" }), 405
    
@bp_bandas.route("/api/bandas", methods=['POST'])
def cadastrar_bandas():
    
    if request.method == 'POST':
        
        try:
            
            bandas = request.get_json()
            
            nova_banda_historia = banda_historia(titulo=bandas['titulo'], historia=bandas['historia'])
            db.session.add(nova_banda_historia)
            db.session.commit()
            
            nova_logo = banda_logo(logo_url=bandas['logo_url'], alt_text=bandas['alt_text'])
            db.session.add(nova_logo)
            
            new_band = banda(nome_banda=bandas['nome_banda'], ano_formacao=bandas['ano_formacao'], id_banda_historia=nova_banda_historia.id_banda_historia, id_banda_logo=nova_logo.id_banda_logo)
            db.session.add(new_band)
            db.session.commit()
            
            new_band_json = new_band.to_dict()
            print(new_band_json)
            
            nova_banda = {
                'nome_banda': bandas['nome_banda'],
                'ano_formacao': bandas['ano_formacao'],
                'titulo': bandas['titulo'],
                'historia': bandas['historia'],
                'logo_url': bandas['logo_url'],
                'alt_text': bandas['alt_text']
            }
            
            # 'banda': jsonify(new_band_json)
            
            
            return jsonify(new_band_json)
        
        except Exception as exception:
            db.session.rollback()
            print(exception)
            return jsonify({ "Erro": "Erro na requisição! " }), 500
        
    else:
        return jsonify({ "Erro": "Método não permitido" }), 405

@bp_bandas.route("/api/bandas/<int:id_banda>", methods=['PUT'])
def atualizar_banda(id_banda):
    
    if request.method == 'PUT':
        try:
            
            banda_atualizada = request.get_json()

            banda_by_id = banda.query.get(id_banda)
            print(banda_by_id.to_dict())

            if not banda_by_id:
                return jsonify({ "Erro": "Não encontrado" }), 404

            banda_by_id.nome_banda = banda_atualizada['nome_banda']
            banda_by_id.ano_formacao = banda_atualizada['ano_formacao']

            banda_historia_by_id = banda_historia.query.get(banda_by_id.id_banda_historia)
            banda_historia_by_id.titulo = banda_atualizada['titulo']
            banda_historia_by_id.historia = banda_atualizada['historia']
            db.session.query(banda_historia).filter(banda_historia.id_banda_historia == banda_historia_by_id.id_banda_historia).update({
                banda_historia.titulo: banda_historia_by_id.titulo,
                banda_historia.historia: banda_historia_by_id.historia})
            # print(banda_historia_by_id)

            banda_logo_by_id = banda_logo.query.get(banda_by_id.id_banda_logo)
            banda_logo_by_id.logo_url = banda_atualizada['logo_url']
            banda_logo_by_id.alt_text = banda_atualizada['alt_text']
            
            db.session.query(banda_logo).filter(banda_logo.id_banda_logo == banda_logo_by_id.id_banda_logo).update(
                {banda_logo.logo_url: banda_logo_by_id.logo_url,
                banda_logo.alt_text: banda_logo_by_id.alt_text})

            db.session.query(banda).filter(banda.id_banda == banda_by_id.id_banda).update(
                {banda.nome_banda: banda_by_id.nome_banda,
                banda.ano_formacao: banda_by_id.ano_formacao,
                banda.id_banda_historia: banda_by_id.id_banda_historia,
                banda.id_banda_logo: banda_by_id.id_banda_logo})
            
            db.session.commit()

            banda_atualizada_json = banda.query.get(id_banda).to_dict()
            
            return jsonify(banda_atualizada_json)
            
        except Exception as exception:
            db.session.rollback()
            print(exception)
            return jsonify({ "Erro": "Erro na requisição! " }), 500
        
    else:
        return jsonify({ "Erro": "Método não permitido" }), 405
    
@bp_bandas.route("/api/bandas/<int:id_banda>", methods=['DELETE'])
def deletar_banda(id_banda):
    
    if request.method == 'DELETE':
        
        try:
            
            banda_by_id = banda.query.get(id_banda)
            
            # banda_deletada = db.session.query(banda).filter(banda.id_banda == id_banda).delete()
            db.session.delete(banda_by_id)
            
            banda_deletada = db.session.execute(db.select(banda, banda_imagem).join(banda_imagem).where(banda.id_banda ==  banda_by_id.id_banda))
            print(banda_deletada)
            db.session.commit()
            
            return jsonify ({
                "Banda": banda_by_id.to_dict(),
                "Mensagem": f"Banda de id {banda_by_id.id_banda} deletada com sucesso"
            })
            
        except Exception as exception:
            db.session.rollback()
            print(exception)
            return jsonify({ "Erro": "Erro na requisição! " }), 500
        
    else:
        return jsonify({ "Erro": "Método não permitido" }), 405