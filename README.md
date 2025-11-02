🏠🌦️ Projeto Consultor de Endereço (CEP) e Clima com PyQt5
Este projeto é um aplicativo de desktop em Python que permite ao usuário consultar dados de endereço a partir de um CEP e, em seguida, obter a previsão do tempo (clima e temperatura) para a localidade encontrada, 
tudo através de uma interface gráfica (GUI) simples e funcional.

🎯 Objetivo
O objetivo principal deste projeto é demonstrar a integração e o consumo de diferentes APIs públicas dentro de uma aplicação desktop, utilizando:

Interface Gráfica (GUI): Criada com a biblioteca PyQt5 para fornecer um ponto de interação amigável com o usuário.

Consumo de API (CEP): Utilização da biblioteca requests para se comunicar com a API ViaCEP e buscar os dados de logradouro, bairro, cidade e estado.

Consumo de API (Clima): Utilização da biblioteca requests para se comunicar com a API HG Brasil Weather e obter as informações de clima atual e temperatura para a cidade/estado correspondente.

A aplicação liga as duas funcionalidades: primeiro busca o endereço e depois usa as informações de cidade e estado para buscar o clima.

💻 Tecnologias Utilizadas
Python 3.x

requests: Para realizar requisições HTTP e consumir as APIs.

PyQt5: Para a construção da interface gráfica do usuário.

API ViaCEP: Para a consulta de endereço.

API HG Brasil Weather: Para a consulta do clima.

⚙️ Funcionalidades
Consulta de Endereço por CEP:

Utiliza a API ViaCEP para preencher automaticamente os campos de Rua, Bairro, Cidade e UF.

Possui máscara de entrada (00000-000) para o campo CEP.

🌦️Consulta de Clima:

Permite consultar o clima e a temperatura da cidade encontrada.

O botão de consulta de clima é habilitado somente após um CEP válido ser buscado.

Validação e Tratamento de Erros:

Valida se o campo CEP foi preenchido.

Tratamento de CEPs inexistentes ("erro": "true" na API ViaCEP).

Tratamento de erros de requisição (status_code diferente de 200).

Limpeza dos campos do formulário com o botão "Limpar busca".

🚀 Como Clonar e Executar o Projeto
Para rodar este projeto na sua máquina, siga os passos abaixo:

1. Pré-requisitos
Você deve ter o Python instalado e as seguintes bibliotecas Python:

pip install requests pyqt5
2. Execução
Salve o código do projeto em um arquivo chamado, por exemplo, CepClima.py.

Execute o arquivo a partir do terminal:

python CepClima.py
Isso abrirá a janela do aplicativo de desktop.

⚠️ Nota sobre a API de Clima
O projeto utiliza a API HG Brasil Weather (em TratarClima()). APIs gratuitas, especialmente as que não exigem autenticação robusta, podem ter limites de uso ou se tornarem indisponíveis com o tempo. 
Caso a consulta de clima não funcione, verifique a validade da key utilizada na URL: key=a3c2217c.
