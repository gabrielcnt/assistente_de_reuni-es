from datetime import datetime
from pathlib import Path

from openai import OpenAI

from config import OPENAI_API_KEY
from prompt import PROMPT_ANALISE_REUNIAO

client = OpenAI(api_key=OPENAI_API_KEY)

AUDIO_DIR = Path("audio")
TRANS_DIR = Path("transcricoes")
TRANS_DIR.mkdir(exist_ok=True)


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

    prompt = PROMPT_ANALISE_REUNIAO.format(
        transcricao=transcricao
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    print("Análise concluida")

    return response.output_text

def main():
    print("Buscando chunks de áudio...")

    chunks = encontrar_chunks()

    print(f"{len(chunks)} partes encontradas!")

    texto = transcrever_chunks(chunks)

    salvar_transcricao(texto)

    print("\n---- TRANSCRIÇÂO COMPLETA ----\n")
    print(texto[:1000])


if __name__ == "__main__":
    main()
