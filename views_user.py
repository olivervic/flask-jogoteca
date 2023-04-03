from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import session
from flask import url_for
from jogoteca import app
from models import Usuarios
from helpers import FormularioUsuario
@app.route('/login')
def login():
    form = FormularioUsuario()
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima , titulo='Novo Jogo', form=form)
##
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    if usuario:
      if form.senha.data == usuario.senha:
           session['usuario_logado'] = usuario.nickname
           flash(usuario.nickname + ' logado com sucesso', 'success')
           proxima_pagina = request.form['proxima']
           return redirect(url_for('index'))
      flash('Usuario não encontrado', 'danger')
    return redirect(url_for('index'))
@app.route('/logout')
def logout():
        session['usuario_logado'] = None
        flash('Usuário deslogado com sucesso' , 'success')
        return redirect(url_for('index'))