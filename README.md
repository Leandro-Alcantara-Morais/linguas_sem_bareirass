# linguas_sem_bareirass
Projeto de lógita de progamaçã onde cria um site que traduz texto em audio e liguagem libras.

# 📄 Línguas sem Barreiras

Aplicação web em Flask focada em acessibilidade, desenvolvida para processar textos e documentos (PDF e TXT) convertendo-os em diferentes formatos de saída: **áudio (TTS)**, **Braille** e **texto formatado**.

---

## 🛠️ O que foi feito no Projeto

### 1. **Estrutura e Arquitetura Web (Flask)**
- **Servidor Web Principal (`app.py`)**: Implementação de rotas para renderização da interface e processamento das requisições POST.
- **Roteamento de Mídia**: Criação da rota `/audio/<nome>` para servir dinamicamente os arquivos de áudio gerados via `send_from_directory`.
- **Templates e Interface Frontend**: 
  - `templates/index.html`: Formulário de envio de texto e upload de arquivos.
  - `templates/resultado.html`: Exibição e reprodução do conteúdo processado.
  - `static/css/style.css` e `static/js/scripts.js`: Estilização e comportamentos assíncronos do cliente.

### 2. **Módulos de Conversão e Processamento**
- **Transcrição para Braille (`braille.py`)**: Módulo exclusivo dedicado a traduzir caracteres de texto para representação em Braille.
- **Utilitários Complementares (`forms.py`, `text.py`)**: Tratamento e validação de entradas do usuário.
- **Síntese de Voz (gTTS)**: Integração com a biblioteca `gTTS` para geração automática de arquivos `.mp3` no idioma português.
- **Extração de Texto PDF (`pypdf`)**: Leitura automatizada de documentos em formato `.pdf` utilizando `pypdf.PdfReader`.

### 3. **Gerenciamento de Arquivos e Segurança**
- **Diretórios Dinâmicos**: Criação automatizada de diretórios de sistema (`uploads/`, `generated/audio/`, `temp/`) usando `pathlib.Path`.
- **Nomes Únicos e Seguros**: Sanitização de arquivos enviados com `secure_filename` e geração de identificadores únicos via `uuid.uuid4()`.
- **Controle de Payload**: Limitação do tamanho máximo de upload para 10 MB com manipulador personalizado para o erro `HTTP 413`.

---

## 📁 Estrutura de Pastas do Repositório

```text
Linguas_sem_Barreiras/
├── generated/           # Arquivos estáticos gerados (ex: áudios)
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── scripts.js
├── templates/
│   ├── index.html
│   └── resultado.html
├── uploads/             # Diretório para armazenamento temporário de uploads
├── app.py               # Servidor principal Flask
├── braille.py           # Módulo de conversão para Braille
├── forms.py             # Validações e formulários
├── text.py              # Utilitários de manipulação de texto
└── README.md
