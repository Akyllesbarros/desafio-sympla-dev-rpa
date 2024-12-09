# Desafio Sympla Dev RPA

Bem-vindo ao repositório do **Desafio Sympla Dev RPA**! Este projeto foi desenvolvido para demonstrar habilidades em automação de processos utilizando Python, Selenium, Pandas e SQLite. A solução coleta dados sobre estados brasileiros, suas capitais, populações e regiões, processa essas informações e gera insights acionáveis em diferentes formatos.

---

## **Índice**

1. [Objetivo do Projeto](#objetivo-do-projeto)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Estrutura do Repositório](#estrutura-do-repositório)
5. [Guia de Uso](#guia-de-uso)
6. [Outputs Gerados](#outputs-gerados)
7. [Próximos Passos e Expansões](#próximos-passos-e-expansões)
8. [Autor](#autor)

---

## **Objetivo do Projeto**

O objetivo deste projeto é automatizar a coleta, processamento e análise de dados de estados brasileiros para gerar insights de forma eficiente, reduzindo erros manuais e otimizando o tempo de execução. A solução também visa garantir rastreabilidade por meio de logs detalhados.

---

## **Funcionalidades**

- **Coleta de Dados**:
  - Utiliza Selenium para scraping de dados sobre estados brasileiros, suas capitais e regiões.

- **Processamento de Dados**:
  - Processa informações de populações a partir de um arquivo Excel.

- **Armazenamento**:
  - Insere os dados em um banco de dados SQLite estruturado.

- **Consultas e Exportações**:
  - Realiza consultas SQL para identificar:
    - As 3 regiões mais populosas.
    - Quantidade de capitais por região.
    - Os 2 estados com as capitais mais populosas.
  - Exporta os resultados para arquivos CSV e XLS.

- **Geração de Logs**:
  - Registra logs detalhados para todas as etapas do processo, facilitando diagnóstico e auditoria.

---

## **Tecnologias Utilizadas**

- **Linguagem**: Python 3.11
- **Bibliotecas Principais**:
  - Selenium
  - Pandas
  - Pyexcel
  - SQLite3
  - Logging

---

## **Estrutura do Repositório**

```plaintext
/desafio-sympla-dev-rpa
├── main.py                  # Arquivo principal para execução do processo.
├── scraping.py              # Funções de scraping para coleta de dados.
├── data_processing.py       # Funções para manipulação e processamento de dados.
├── database.py              # Funções para manipulação do banco de dados.
├── logger_config.py         # Configuração de logs.
├── requirements.txt         # Dependências do projeto.
├── database/                # Diretório para o banco de dados.
│   └── estados.db           # Arquivo do banco de dados SQLite.
├── logs/                    # Diretório para os arquivos de log.
├── outputs/                 # Diretório para arquivos de saída (CSV/XLS).
│   ├── top3_regioes_populosas.csv
│   ├── regioes_n_capitais.xls
│   └── estados_mais_populosos.xls
```

---

## **Guia de Uso**

### **1. Clonar o Repositório**

Execute o seguinte comando no terminal:

```bash
git clone https://github.com/Akyllesbarros/desafio-sympla-dev-rpa.git
```

### **2. Configurar o Ambiente Virtual**

#### No Windows:
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### No Mac:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **3. Executar o Sistema**

Com o ambiente virtual ativo, execute o seguinte comando:

```bash
python main.py
```

### **4. Verificar Resultados**

- **Outputs**: Localizados na pasta `outputs/`.
- **Logs**: Disponíveis na pasta `logs/`.
- **Banco de Dados**: Armazenado em `database/estados.db`.

---

## **Outputs Gerados**

1. **Arquivos de Saída**:
   - `top3_regioes_populosas.csv`: Regiões e suas populações totais, ordenadas pelas mais populosas.
   - `regioes_n_capitais.xls`: Quantidade de capitais por região.
   - `estados_mais_populosos.xls`: Dois estados com as capitais mais populosas.

2. **Banco de Dados**:
   - `estados.db`: Contém todos os dados processados e estruturados.

3. **Logs**:
   - Arquivos de log detalhando cada etapa do processo.

---

## **Próximos Passos e Expansões**

- **Validação de Dados**: Implementar validações automáticas para entradas incorretas.
- **Integração com APIs**: Adicionar coleta de dados diretamente de APIs oficiais.
- **Interface Gráfica**: Criar uma interface para facilitar o uso por usuários finais.

---

## **Autor**

**Akylles Barros**  
**Função**: Desenvolvedor RPA  
[LinkedIn](https://www.linkedin.com/in/akyllesbarros) | [GitHub](https://github.com/Akyllesbarros)

---

