from datetime import datetime
from pathlib import Path

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

PDF_DIR = Path("pdfs")
PDF_DIR.mkdir(exist_ok=True)


def gerar_pdf(texto, caminho_pdf):
    doc = SimpleDocTemplate(str(caminho_pdf))

    styles = getSampleStyleSheet()

    h1 = ParagraphStyle("H1", parent=styles["Heading1"])

    h2 = ParagraphStyle("H2", parent=styles["Heading2"])

    body = styles["BodyText"]

    elementos = []

    for linha in texto.splitlines():
        linha = linha.strip()

        if not linha:
            elementos.append(Spacer(1, 8))
            continue

        # H1
        if linha.startswith("# "):
            elementos.append(Paragraph(linha[2:], h1))
            elementos.append(Spacer(1, 12))

        # H2
        elif linha.startswith("## "):
            elementos.append(Paragraph(linha[3:], h2))
            elementos.append(Spacer(1, 8))

        # Lista
        elif linha.startswith("- "):
            elementos.append(Paragraph(f"• {linha[2:]}", body))

        # Texto comum
        else:
            elementos.append(Paragraph(linha, body))

    doc.build(elementos)


def carregar_resumo(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def salvar_pdf(resumo):

    data = datetime.now().strftime("%Y%m%d_%H%M%S")

    caminho_pdf = PDF_DIR / f"resumo_{data}.pdf"

    gerar_pdf(resumo, caminho_pdf)

    print(f"PDF salvo em: {caminho_pdf}")


def main():
    resumo_path = Path("resumos/resumo_20260605_180726.md")

    texto = resumo_path.read_text(encoding="utf-8")

    pdf_path = Path("pdfs/resumo_teste.pdf")

    gerar_pdf(texto, pdf_path)

    print(f"PDF gerado em: {pdf_path}")

if __name__ == "__main__":
    main()