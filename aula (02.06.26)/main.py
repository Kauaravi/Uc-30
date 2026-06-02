from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def cadastro():

    mensagem = ""

    if request.method == "POST":
        nome = request.form.get("nome")
        if not nome:
            mensagem = "Por favor, preencha o campo nome."
        else:
            mensagem = f"Cadastro realizado com sucesso! {nome}!"
    return render_template("cadastro.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
