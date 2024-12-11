from flask import Blueprint, jsonify, render_template, request, make_response, session, url_for, flash, redirect
# from sqlalchemy import Text
# from sqlalchemy.engine import Engine
from app.models.banda import Banda 
# from werkzeug.utils import secure_filename
from datetime import datetime
from app import db

bp_bandas = Blueprint("bandas", __name__, template_folder='../templates/')

@bp_bandas.route("/bandas", methods=['GET'])
def pagina_bandas():
    
    if request.method == 'GET':
        return render_template('bandas.html')
    else:
        return make_response("Não encontrado", 404)