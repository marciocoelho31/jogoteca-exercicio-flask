from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')

    form = FormularioUsuario()

    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)

    proxima_pagina = request.form['proxima']

    usuario_ok = False

    usuario = Usuarios.query.filter_by(nickname = form.nickname.data).first()
    if usuario:
        senha_confere = check_password_hash(usuario.senha, form.senha.data)
        if senha_confere:
            session['usuario_logado'] = usuario.nickname
            usuario_ok = True

    if usuario_ok:
        flash(f'Usuário {usuario.nickname} logado com sucesso!')
        return redirect(proxima_pagina if proxima_pagina != 'None' else url_for('index'))
    else:
        flash('Usuário não logado')
        return redirect(url_for('login', proxima=proxima_pagina))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect(url_for('index'))

