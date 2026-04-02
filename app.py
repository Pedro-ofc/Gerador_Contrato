from flask import Flask, render_template, request, send_file
from datetime import datetime
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    dados = request.form

    empresa = dados.get('empresa')
    cnpj = dados.get('cnpj')
    endereco = dados.get('endereco')
    cep = dados.get('cep')
    representante = dados.get('representante')
    cpf = dados.get('cpf')
    rg = dados.get('rg')

    contrato = f"""
CONTRATO DE LOCAÇÃO DE EQUIPAMENTO(S) REPROGRÁFICO(S) – {empresa}

Pelo presente instrumento particular e na melhor forma de direito, de um lado como LOCADORA, WPrinter Soluções em Impressão e Tecnologia Eireli, pessoa jurídica de direito privado, inscrita no CNPJ sob o nº 15.678.705/0001-30, estabelecida a Avenida Norte Miguel Arraes e Alencar, 3003, Encruzilhada, CEP 52.041-080, Recife – PE,

de outro lado como LOCATÁRIO, {empresa}, inscrito no CNPJ sob o número {cnpj}, sediada {endereco}, CEP {cep} – Pernambuco,

neste ato representado por {representante}, inscrito no CPF/MF nº {cpf}, e portador do RG {rg},

resolvem celebrar entre si o presente contrato de locação de equipamentos, conforme cláusulas a seguir:

----------------------------------------

CLÁUSULA 1 – DO OBJETO
Locação de equipamentos de impressão com manutenção e suporte técnico.

CLÁUSULA 2 – DO PRAZO
12 meses.

CLÁUSULA 3 – DO PAGAMENTO
Pagamento mensal conforme proposta comercial.

----------------------------------------

Data: {datetime.now().strftime("%d/%m/%Y")}

____________________________________
LOCATÁRIO

____________________________________
WPRINTER SOLUÇÕES
"""

    nome_arquivo = f"contrato_{empresa.replace(' ', '_')}.txt"
    caminho = os.path.join(os.getcwd(), nome_arquivo)

    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(contrato)

    return send_file(caminho, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)