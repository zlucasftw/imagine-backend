from flask import Blueprint, jsonify, render_template, request, make_response, session, url_for, flash, redirect
# from sqlalchemy import Text
# from sqlalchemy.engine import Engine
from app.models.banda import banda
from app.models.banda_historia import banda_historia
from app.models.banda_logo import banda_logo
from app.models.banda_imagem import banda_imagem
# from werkzeug.utils import secure_filename
from datetime import datetime
from app import db

bp_bandas_imagem = Blueprint("bandas_imagem", __name__, template_folder='templates')

@bp_bandas_imagem.route("/api/bandas/imagens", methods=['GET'])
def listar_imagens():
    
    if request.method == 'GET':
        
        
        bandas = banda_imagem.query.all()
        bandas_json = []
        
        for band in bandas:
            bandas_json.append(band.to_dict())
        
        if not bandas_json:
            return jsonify({ "Erro": "Não encontrado" }), 404
        
        return jsonify(bandas_json)
        
    else:
        return jsonify({ "Erro": "Método não permitido" }), 405
        
@bp_bandas_imagem.route("/api/bandas/imagens", methods=['POST'])
def cadastrar_imagens():
    
    if request.method == 'POST':
        
        try:
            
            imagens = request.get_json()
            nova_imagem_json = []
            
            for imagem in imagens:
                nova_imagem = banda_imagem(imagem_url=imagem['imagem_url'], alt_text=imagem['alt_text'], tipo_imagem=imagem['tipo_imagem'], id_banda=imagem['id_banda'])
                db.session.add(nova_imagem)
                nova_imagem_json.append(nova_imagem.to_dict())
            db.session.commit()
            
            return jsonify(nova_imagem_json)
            
        except Exception as exception:
            db.session.rollback()
            return jsonify({ "Erro": "Erro na requisição! " }), 500

    else:
        return jsonify({ "Erro": "Método não permitido" }), 405