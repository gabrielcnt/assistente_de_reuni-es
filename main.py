from datetime import datetime
from pathlib import Path

from openai import OpenAI

from config import OPENAI_API_KEY
from pdf_generator import salvar_pdf
from prompt import PROMPT_ANALISE_REUNIAO

client = OpenAI(api_key=OPENAI_API_KEY)

AUDIO_DIR = Path("audio")
TRANS_DIR = Path("transcricoes")
TRANS_DIR.mkdir(exist_ok=True)
RESUMO_DIR = Path("resumos")
RESUMO_DIR.mkdir(exist_ok=True)


def encontrar_audio():

    arquivos = list(AUDIO_DIR.glob("*"))

    if not arquivos:
        raise FileNotFoundError("Nenhum áudio encontrado na pasta 'audio/'")

    audio = arquivos[0]

    print(f"Áudio encontrado: {audio}")

    return audio


def encontrar_chunks(pasta="audio/partes"):
    arquivos = sorted(Path(pasta).glob("*mp3"))
    if not arquivos:
        raise FileNotFoundError("Nenhum chunk encontrado")
    return arquivos


def transcrever_audio(caminho_audio):
    print("Transcrevendo audio...")

    with open(caminho_audio, "rb") as audio:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe", file=audio
        )

    texto = transcript.text

    print("Transcrição concluida!")

    return texto


def transcrever_chunks(arquivos):

    transcricao_total = []

    for i, arquivo in enumerate(arquivos):
        print(f"Transcrevendo parte {i + 1}/{len(arquivos)}: {arquivo}")

        with open(arquivo, "rb") as audio:
            transcript = client.audio.transcriptions.create(
                model="gpt-4o-mini-transcribe", file=audio
            )
        transcricao_total.append(transcript.text)
    return "\n".join(transcricao_total)


def salvar_transcricao(texto):
    data = datetime.now().strftime("%Y%m%d_%H%M%S")

    nome_arquivo = f"transcricao_{data}.txt"
    caminho = TRANS_DIR / nome_arquivo

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"Transcrição salva em: {caminho}")
    return caminho


def analisar_reuniao(transcricao):
    print("Analisando reunião...")

    prompt = PROMPT_ANALISE_REUNIAO.format(transcricao=transcricao)

    response = client.responses.create(model="gpt-4.1-mini", input=prompt)

    print("Análise concluida")

    return response.output_text


def salvar_resumo(resumo):
    data = datetime.now().strftime("%Y%m%d_%H%M%S")

    nome_arquivo = f"resumo_{data}.md"

    caminho = RESUMO_DIR / nome_arquivo

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(resumo)

    print(f"Resumo salvo em: {caminho}")

    return caminho


def encontrar_transcricao():
    arquivos = sorted(TRANS_DIR.glob("*.txt"))

    if not arquivos:
        return None

    return arquivos[-1]


def carregar_transcricao(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


def main():

    caminho_transcricao = encontrar_transcricao()

    if caminho_transcricao:
        print(f"Usando transcrição existente: {caminho_transcricao}")

        texto = carregar_transcricao(caminho_transcricao)

    else:
        print("Nenhuma transcrição encontrada.")

        chunks = encontrar_chunks()

        print(f"{len(chunks)} partes encontradas!")

        texto = transcrever_chunks(chunks)

        salvar_transcricao(texto)

    resumo = analisar_reuniao(texto)

    data_reuniao = datetime.now().strftime("%d/%m/%Y")
    cabecalho = f"""# Ata de Reunião
    
    Data: {data_reuniao}

"""

    resumo = cabecalho + resumo

    salvar_resumo(resumo)
    salvar_pdf(resumo)


if __name__ == "__main__":
    main()
