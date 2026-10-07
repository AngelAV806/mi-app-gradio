import gradio as gr

informacion = """
# 🎓 Universidad Autónoma del Estado de México

*Información general de la universidad*

La **Universidad Autónoma del Estado de México (UAEMéx)** es una universidad pública
ubicada en el Estado de México.

---

## 📋 Datos de la universidad

**🏫 Nombre:** Universidad Autónoma del Estado de México

**🔤 Siglas:** UAEMéx

**📍 Ubicación:** Toluca, Estado de México

**🏛️ Tipo:** Universidad pública

**📖 Lema:** *Patria, Ciencia y Trabajo*

---

## 📚 Áreas de estudio

- 💼 Administración
- 📊 Contaduría
- ⚖️ Derecho
- 💻 Ingeniería
- 🖥️ Informática
- 🩺 Medicina
- 👥 Ciencias Sociales

---

## 🛠️ Servicios

- 📖 Bibliotecas
- 💻 Laboratorios de cómputo
- ⚽ Actividades deportivas
- 🎭 Actividades culturales
- 🎓 Becas
- 🌐 Plataformas educativas

---

## 📞 Contacto

**📍 Ciudad:** Toluca, Estado de México

**☎️ Teléfono:** (722) 000-0000

**✉️ Correo:** contacto@uaemex.mx

**🌐 Sitio web:** www.uaemex.mx

---

### 💡 Proyecto

*Esta página es una práctica realizada con Python y Gradio.*
"""

css = """
body {
    background: linear-gradient(135deg, #f4f7f5, #e4eee8);
}

.gradio-container {
    max-width: 950px !important;
    margin: auto;
}

.markdown-body {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.10);
}

h1 {
    color: #1b5e20 !important;
    text-align: center;
    font-size: 36px !important;
}

h2 {
    color: #2e7d32 !important;
    border-bottom: 2px solid #81c784;
    padding-bottom: 8px;
}

h3 {
    color: #388e3c !important;
}

strong {
    color: #2e7d32;
}
"""

with gr.Blocks(
    title="UAEMéx",
    css=css
) as pagina:

    gr.Markdown(informacion)

pagina.launch(
    server_name="0.0.0.0",
    server_port=7860
)
