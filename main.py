from pathlib import Path

from openai import OpenAI

from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

AUDIO_DIR = Path("audio")


def encontrar_audio():

    arquivos = list(AUDIO_DIR.glob("*"))

    if not arquivos:
        raise FileNotFoundError("Nenhum áudio encontrado na pasta 'audio/'")

    audio = arquivos[0]

    print(f"Áudio encontrado: {audio}")

    return audio


def transcrever_audio(caminho_audio):
    print("Transcrevendo audio...")

    with open(caminho_audio, "rb") as audio:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe", file=audio
        )

    texto = transcript.text

    print("Transcrição concluida!")

    return texto

def main():
    audio = encontrar_audio()

    texto = transcrever_audio(audio)

    print("\n---- TRANSCRIÇÂO ----\n")
    print(texto[:1000])


if __name__ == "__main__":
    main()
