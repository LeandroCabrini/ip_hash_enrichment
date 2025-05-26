
# 🛡️ IP & Hash Enrichment Tool

Ferramenta em Python para enriquecimento de informações de **IPs**, **domínios**, **hashes** e **URLs** usando a API do [VirusTotal](https://www.virustotal.com/).

---

## 🚀 Funcionalidades

- 🔍 Detecta automaticamente o tipo da entrada (IP, domínio, hash ou URL)  
- 📡 Consulta a API do VirusTotal para enriquecer os dados  
- 🔐 Uso seguro de API key com `.env`  
- 💡 Código modular e organizado  

---

## 🧰 Requisitos

- Python 3.8 ou superior  
- Conta no [VirusTotal](https://virustotal.com/) com API Key (gratuita ou premium)  

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/LeandroCabrini/ip_hash_enrichment.git
cd ip_hash_enrichment
```

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Crie um arquivo chamado `.env` na raiz do projeto contendo a sua chave da API do VirusTotal:

```env
VIRUSTOTAL_API_KEY=sua_chave_aqui
```

**Importante:** Não compartilhe essa chave publicamente.

---

## ▶️ Como usar

Execute o script principal:

```bash
python main.py
```

Você verá o seguinte prompt:

```bash
Digite um IP, domínio ou hash: 
```

Digite qualquer um dos seguintes exemplos válidos:

- `8.8.8.8` (IP)  
- `fiap.com.br` (domínio)  
- `https://on.fiap.com.br/index.php` (URL)  
- `44d88612fea8a8f36de82e1278abb02f` (MD5 de exemplo)  

A saída exibirá os dados de enriquecimento retornados pela API do VirusTotal.

---

## 📂 Estrutura do Projeto

```plaintext
ip_hash_enrichment/
├── apis/
│   └── virustotal.py       # Integração com a API do VirusTotal
├── utils/
│   └── validation.py       # Validação e classificação da entrada do usuário
├── config.py               # Carregamento seguro da API key
├── main.py                 # Script principal
├── .env                    # (Ignorado no Git)
├── .gitignore              # Ignora arquivos sensíveis
├── requirements.txt        # Dependências
└── README.md               # Este arquivo
```

---

## 📫 Contato

Leandro — [linkedin.com/in/leandro-cabrini-jr/](https://linkedin.com/in/leandro-cabrini-jr/)

---
