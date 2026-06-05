from datetime import datetime
from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

PDF_DIR = Path("pdfs")
PDF_DIR.mkdir(exist_ok=True)


def gerar_pdf(texto, caminho_pdf):
    doc = SimpleDocTemplate(str(caminho_pdf))

    styles = getSampleStyleSheet()

    elementos = []

    for linha in texto.split("\n"):
        if linha.strip():
            elementos.append(Paragraph(linha, styles["BodyText"]))

        elementos.append(Spacer(1, 6))

    doc.build(elementos)


def carregar_resumo(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def salvar_pdf(resumo):

    data = datetime.now().strftime("%Y%m%d_%H%M%S")

    caminho_pdf = PDF_DIR / f"resumo_{data}.pdf"

    gerar_pdf(resumo, caminho_pdf)

    print(f"PDF salvo em: {caminho_pdf}")
