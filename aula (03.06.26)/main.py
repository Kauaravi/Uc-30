@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def cadastro():
    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    idade = request.form.get('idade', '').strip().title()
   
    return f"""
    Nome: {nome}<br>
    Email: {email}<br>
    Idade: {idade}
    """
if __name__ == '__main__':
    app.run(debug=True)
