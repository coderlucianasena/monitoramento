# Monitoramento Mainframe

Este é um projeto de monitoramento baseado na web para acompanhar o uso da CPU, Disco e Memória de um mainframe em tempo real. O projeto utiliza duas interfaces web para exibir as informações do mainframe,possui também um servidor Flask e uma conexão SSH para acessar e coletar informações do mainframe Linux. Os dados coletados são armazenados em um banco de dados SQLite3 para referência futura.

## Requisitos

Antes de iniciar, verifique se você possui os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- [Python](https://www.python.org/downloads/) (versão 3.6 ou superior)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Paramiko](https://www.paramiko.org/)
- [SQLite3](https://www.sqlite.org/index.html)
- Um cliente SSH (como o [PuTTY](https://www.putty.org/) para ambiente Windows)

## Configuração

1. Clone este repositório em seu ambiente de desenvolvimento:

   ```bash
   git clone https://github.com/englucianasena/monitoramento.git
   ```

2. Instale as dependências Python usando `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure a chave SSH:

   - Substitua `'hostname'` e `'caminho_chave_privada'` nas configurações do mainframe com os valores apropriados.
   - Certifique-se de que a chave privada SSH seja válida para se conectar ao mainframe Linux.


## Uso

1. Ative o ambiente virtual:

 ```
    source venv/bin/activate  # No Linux/Mac
 ```
```
    venv\Scripts\activate    # No Windows
```

2. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

3. Acesse a interface em seu navegador:

   ```
   http://localhost:5000/
   ```
      ```
   http://localhost:5000/dados
   ```

4. Faça a sua autenticação por par de chaves SSH.

5. Após a autenticação bem-sucedida, você será redirecionado para a página de monitoramento.

6. A página de monitoramento exibirá informações em tempo real sobre o uso da CPU, Disco e Memória do mainframe.


## Lógica de Comando Real

Os comandos de exemplo (`comando_cpu`, `comando_disco`, `comando_memoria`) no arquivo `app.py` devem ser substituídos por comandos reais que retornem informações válidas do seu mainframe Linux. Os comandos reais devem ser configurados para obter informações da CPU, disco e memória do mainframe.

## Créditos

Este projeto foi desenvolvido por Luciana Sena. 

## Contribuições

Contribuições são bem-vindas! Para sugestões, melhorias ou correções de bugs, abra uma issue ou envie uma solicitação de pull request.
























# Ative o ambiente virtual:
source venv/bin/activate  # No Linux/Mac
venv\Scripts\activate    # No Windows

# Inicie o servidor Flask:
python app.py

# Acesse o aplicativo no navegador:
http://localhost:5000/

# Verifique a recuperação de dados:
Clique com o botão direito na página e selecione "Inspecionar" (ou pressione F12) para abrir as ferramentas de desenvolvedor do navegador.

# Teste a autenticação SSH 