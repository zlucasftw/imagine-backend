from flask import Blueprint, jsonify, render_template, request, make_response, session, url_for, flash, redirect, current_app as app
# from sqlalchemy import Text
# from sqlalchemy.engine import Engine
from app.models.banda import banda
from app.models.banda_historia import banda_historia
from app.models.banda_logo import banda_logo
from app.models.banda_imagem import banda_imagem
from werkzeug.utils import secure_filename
from datetime import datetime
from app import db
import os

bp_form = Blueprint("form", __name__, template_folder='templates')

@bp_form.route("/cadastrar_banda", methods=['POST'])
def salvar_banda():
    
    if request.method == 'POST':
        
        try:
            nome_banda = request.form['nome_banda']
            ano_formacao = request.form['ano_formacao']

            titulo_historia = request.form['titulo_historia']
            historia_banda = request.form['historia_banda']
    
            logo = request.files.get('url_logo')
            alt_text_logo = request.form['alt_text_logo']
        
            imagem_banda = request.files.get('url_imagem')
            alt_text_imagem = request.form['alt_text_imagem']
        
            logo_url = ''
            imagem_url = ''
        
            if logo.filename == '' or imagem_banda.filename == '':
                return make_response("Arquivo não selecionado", 400)
        
            filename_logo =  secure_filename(logo.filename_logo)
            logo.save(os.path.join(app.config['UPLOAD_FOLDER_LOGO'], filename_logo))
            logo_url = filename_logo.lstrip("app/static/")
        
            filename_imagem = secure_filename(imagem_banda.filename)
            imagem_banda.save(os.path.join(app.config['UPLOAD_FOLDER_IMAGEM'], filename_imagem))
            imagem_url = filename_imagem.lstrip("app/static/")

            # nova_banda_historia = banda_historia(titulo_historia=titulo_historia, historia_banda=historia_banda)
            
            # nova_banda_logo = banda_logo(logo_url=logo_url, alt_text=alt_text_logo)
            
            # nova_banda = banda(nome_banda=nome_banda, ano_formacao=ano_formacao)
            
            # nova_banda_imagem = banda_imagem(imagem_url=imagem_url, alt_text=alt_text_imagem, tipo_imagem="banda")
            
            return jsonify({
                "nome_banda": nome_banda,
                "ano_formacao": ano_formacao,
                "titulo_historia": titulo_historia,
                "historia_banda": historia_banda,
                "logo": logo_url,
                "alt_text": alt_text_logo,
                "imagem": imagem_url,
                "alt_text_imagem": alt_text_imagem,
                "tipo_imagem": "banda"
            })
            
        except Exception as exception:
            return make_response("Erro na requisição! ", 500)
    
    else:
        return make_response("Método não permitido", 405)