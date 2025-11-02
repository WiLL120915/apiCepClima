import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox      
from PyQt5.QtGui import QIcon



def limpaCampos():

    caixaTextoCEP.clear()
    caixaTextoRua.clear()
    caixaTextoBairro.clear()
    caixaTextoCidade.clear()
    caixaTextoUF.clear()
    caixaTextoCEP.setFocus()

def validaCampo():

        codigoCEP = caixaTextoCEP.text()

        if codigoCEP == "":
            QMessageBox.critical(telaCadastro, "Atenção", "CEP precisa ser informado, verifique.")
            caixaTextoCEP.setFocus()

        else:
            tratarCEP(codigoCEP)
            botaoClima.setEnabled(True)



def tratarCEP(codigoCEP):

        url = f"https://viacep.com.br/ws/{codigoCEP}/json/"            

        try:
            response = requests.get(url)

            if response.status_code == 200:
                dados = response.json()

                if dados.get("erro") == "true":
                    QMessageBox.critical(telaCadastro, "Erro", "CEP não encontrado na base de dados do VIACEP. ")
                else:
                    caixaTextoRua.setText(dados.get('logradouro', ''))   
                    caixaTextoBairro.setText(dados.get('bairro','')) 
                    caixaTextoCidade.setText(dados.get('localidade',''))
                    caixaTextoUF.setText(dados.get('uf',''))

                    botaoClima.setEnabled(True)


                    QMessageBox.information(telaCadastro, "Consulta de CEP", "Endereço encontrado")

            else:
                QMessageBox.critical(telaCadastro, "Erro", f"Erro na requisição. Códigode status:{response.status_code} ") 

        except Exception as e:
            QMessageBox.critical(telaCadastro, "Erro", f"Ocorreu uma exceção: {str(e)}") 


    
     
def TratarClima():
    
    if caixaTextoCidade.text() == "" or caixaTextoUF.text() == "":
     QMessageBox.warning(telaCadastro, "Atenção", "Você precisa buscar o CEP antes de consultar o clima.")
     return

    from urllib.parse import quote

    cidade = caixaTextoCidade.text()
    estado = caixaTextoUF.text()
    localizacao = quote(f"{cidade}, {estado}")


    cli = f"https://api.hgbrasil.com/weather?format=json-cors&key=a3c2217c&city_name={localizacao}"


    try:
        
        response = requests.get(cli)
        if response.status_code == 200:
            dados = response.json()
            
            if "results" in dados:
                clima = dados["results"]["description"]
                temperatura = dados["results"]["temp"]
                QMessageBox.information(telaCadastro, "Clima Atual", f"Clima: {clima}\nTemperatura: {temperatura}°C")
            else:
                QMessageBox.critical(telaCadastro, "Erro", "Não foi possível obter os dados climáticos.")
        else:
            QMessageBox.critical(telaCadastro, "Erro", f"Erro ao buscar clima. Código: {response.status_code}")
    except Exception as e:
        QMessageBox.critical(telaCadastro, "Erro", f"Erro na requisição: {str(e)}")


app = QApplication(sys.argv)


telaCadastro = QWidget()
telaCadastro.setWindowTitle("Consulte seu endereço e clima Cº")
telaCadastro.setGeometry(100, 100, 600, 140)
telaCadastro.setWindowIcon(QIcon("climaIcon"))

textoRotuloCEP = QLabel('CEP:', telaCadastro)
textoRotuloCEP.move(10,10)

textoRotuloRua = QLabel('Rua:', telaCadastro)
textoRotuloRua.move(300,10)

textoRotuloBairro = QLabel('Bairro:', telaCadastro)
textoRotuloBairro.move(10,60)

textoRotuloCidade = QLabel('Cidade:', telaCadastro)
textoRotuloCidade.move(270,60)

textoRotuloUF = QLabel('UF:', telaCadastro)
textoRotuloUF.move(530,60)


caixaTextoCEP = QLineEdit(telaCadastro)
caixaTextoCEP.setFixedWidth(80)
caixaTextoCEP.setInputMask("00000-000")
caixaTextoCEP.move(10,30)

caixaTextoRua = QLineEdit(telaCadastro)
caixaTextoRua.setFixedWidth(260)
caixaTextoRua.move(300,30)
caixaTextoRua.setEnabled(False)

caixaTextoBairro = QLineEdit(telaCadastro)
caixaTextoBairro.setFixedWidth(250)
caixaTextoBairro.move(10,80)
caixaTextoBairro.setEnabled(False)

caixaTextoCidade = QLineEdit(telaCadastro)
caixaTextoCidade.setFixedWidth(250)
caixaTextoCidade.move(270,80)
caixaTextoCidade.setEnabled(False)

caixaTextoUF = QLineEdit(telaCadastro)
caixaTextoUF.setFixedWidth(30)
caixaTextoUF.move(530,80)
caixaTextoUF.setEnabled(False)


botaoBuscarCEP = QPushButton('Buscar CEP', telaCadastro)
botaoBuscarCEP.move(100,25)

botaoBuscarCEP.clicked.connect(validaCampo)

botaoLimpar = QPushButton('Limpar busca', telaCadastro)
botaoLimpar.move(200,25)

botaoLimpar.clicked.connect(limpaCampos)

botaoClima = QPushButton('Consultar clima do endereço', telaCadastro)
botaoClima.move(210,110)

botaoClima.clicked.connect(TratarClima)
botaoClima.setEnabled(False)



telaCadastro.show()


sys.exit(app.exec_())