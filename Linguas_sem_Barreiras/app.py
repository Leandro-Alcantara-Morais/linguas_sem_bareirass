



from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import subprocess
from braille import texto_para_braille  # Importe o código de Braille
from PIL import Image
import pytesseract  # Biblioteca para OCR
from gtts import gTTS  # Biblioteca para conversão de texto em áudio
from googletrans import Translator  # Para tradução

app = Flask(__name__)

# Configurações para upload de arquivos
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'jpg', 'png', 'jpeg'}

# Função para verificar as extensões de arquivos permitidos
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Função para conversão de texto para áudio
def texto_para_audio(texto):
    tts = gTTS(text=texto, lang='pt')
    output_file = "output.mp3"
    tts.save(output_file)
    return output_file

# Função para traduzir o texto
def traduzir_texto(texto, idioma_destino='en'):
    translator = Translator()
    return translator.translate(texto, dest=idioma_destino).text

# Função para extrair texto de imagem com OCR
def extrair_texto_imagem(imagem_path):
    img = Image.open(imagem_path)
    texto = pytesseract.image_to_string(img)
    return texto

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    texto = request.form.get('input-text')
    output_type = request.form.get('output-type')
    resultado = {}

    if request.files.get('input-file'):
        file = request.files['input-file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Se for imagem ou PDF, tentamos extrair o texto
            if filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png']:
                texto = extrair_texto_imagem(file_path)
            elif filename.rsplit('.', 1)[1].lower() == 'pdf':
                # Para PDF, use uma biblioteca como PyPDF2 ou pdfminer para extrair texto
                pass

    # Se o tipo de saída for áudio
    if output_type == 'audio':
        output_file = texto_para_audio(texto)
        return send_file(output_file, as_attachment=True)

    # Se o tipo de saída for Braille
    elif output_type == 'braille':
        braille_texto = texto_para_braille(texto)
        resultado['braille'] = braille_texto
        return render_template('resultado.html', resultado=resultado)

    # Se o tipo de saída for tradução
    elif output_type == 'traducao':
        idioma_destino = request.form.get('language', 'en')
        traduzido = traduzir_texto(texto, idioma_destino)
        resultado['traduzido'] = traduzido
        return render_template('resultado.html', resultado=resultado)

    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
