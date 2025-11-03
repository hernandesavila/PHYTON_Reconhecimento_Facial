# 🧾 Reconhecimento Facial

Aplicação de **reconhecimento facial** escrita em **Python 3** utilizando **OpenCV** para demonstrar captura, detecção e identificação de rostos em tempo real. O repositório inclui exemplos que vão desde a simples exibição da webcam até o uso de um modelo **LBPH** previamente treinado para reconhecer pessoas conhecidas.

---

## 🛠️ Tecnologias Utilizadas

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="30" height="30"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" alt="OpenCV" width="30" height="30"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" alt="NumPy" width="30" height="30"/>
</p>

- **Python 3** – linguagem principal
- **OpenCV (opencv-contrib-python)** – captura de vídeo, detecção com Haar Cascade e reconhecimento LBPH
- **NumPy** – manipulação matricial das imagens
- **Pillow** – conversão de imagens durante o pré-processamento

---

## 📂 Estrutura do Projeto

- `Reconhecimento Facial/face_recognition` – detecção de rostos em tempo real usando `haarcascade_frontalface_default.xml`
- `Reconhecimento Facial/face_recognition_with_photo.py` – reconhecimento LBPH treinado a partir de imagens locais
- `Reconhecimento Facial/face_recognition_with_photo_com_modelo.py` – reconhecimento LBPH utilizando o modelo salvo `modelo_lbph.xml`
- `Reconhecimento Facial/imagem.py` – exibição simples do feed da webcam
- `Reconhecimento Facial/imagem_com_filtro.py` – exemplo aplicando filtro negativo na webcam
- `Reconhecimento Facial/haarcascade_frontalface_default.xml` – classificador Haar Cascade para detecção de faces
- `Reconhecimento Facial/modelo_lbph.xml` – modelo LBPH pré-treinado

---

## ✅ Pré-requisitos

- **Python 3.8+** instalado
- Webcam ou vídeo compatível com OpenCV
- Dependências Python: `opencv-contrib-python`, `numpy`, `Pillow`

```bash
pip install opencv-contrib-python numpy Pillow
```

---

## ⚙️ Configuração

1. **Preparar o conjunto de imagens**
   - Crie a pasta `Reconhecimento Facial/imagens/` e adicione fotos em escala de cinza ou coloridas.
   - Nomeie cada arquivo com o identificador numérico do indivíduo (`1.jpg`, `2.png` etc.).

2. **Treinar o modelo LBPH (opcional)**
   - Execute `face_recognition_with_photo.py` para treinar um modelo diretamente a partir das imagens locais.
   - Salve o modelo resultante com `recognizer.write('modelo_lbph.xml')` se desejar reutilizá-lo posteriormente.

3. **Utilizar o modelo fornecido**
   - O arquivo `modelo_lbph.xml` contém pesos prontos para teste rápido.
   - Ajuste o dicionário `nomes` nos scripts para associar IDs às pessoas reconhecidas.

---

## ▶️ Execução

1. **Detecção simples de rostos**
   ```bash
   python "Reconhecimento Facial/face_recognition"
   ```
2. **Reconhecimento em tempo real a partir de imagens locais**
   ```bash
   python "Reconhecimento Facial/face_recognition_with_photo.py"
   ```
3. **Reconhecimento usando o modelo pré-treinado**
   ```bash
   python "Reconhecimento Facial/face_recognition_with_photo_com_modelo.py"
   ```
4. **Exemplos com webcam**
   ```bash
   python "Reconhecimento Facial/imagem.py"
   python "Reconhecimento Facial/imagem_com_filtro.py"
   ```

Durante a execução, pressione **`q`** para encerrar a aplicação e liberar a webcam.

---

## 🔎 Funcionamento

- O classificador Haar Cascade detecta faces em cada frame capturado.
- O algoritmo **LBPH** extrai padrões locais e compara com o banco de imagens treinado.
- Os nomes exibidos na tela são definidos pelo dicionário `nomes` presente nos scripts de reconhecimento.
- A confiança retornada pelo modelo auxilia na decisão entre rosto reconhecido ou desconhecido.

---

## 📌 Observações

- Certifique-se de que apenas uma aplicação acesse a webcam por vez.
- Ajuste os limiares de confiança (`confidence`) conforme a qualidade das imagens de treino.
- Considere normalizar iluminação e alinhar rostos para melhores resultados.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
