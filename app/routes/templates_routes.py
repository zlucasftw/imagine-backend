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

bp_templates = Blueprint("templates", __name__, template_folder='templates')

@bp_templates.route("/cadastrar_banda", methods=['GET'])
def cadastrar_banda():
    
    if request.method == 'GET':
        return render_template('cadastrar_bandas.html')
    else:
        return make_response("Não encontrado", 404)