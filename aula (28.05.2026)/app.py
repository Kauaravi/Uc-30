from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome', ''].strip()
        email = request.form['email', ''].strip().lower()
        
        if not nome:
            flash('O campo nome é obrigatório.', 'erro')
            return redirect(url_for('cadastro'))
        if not email:
            flash('O campo email é obrigatório.', 'erro')
            return redirect(url_for('cadastro'))
        
        return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
