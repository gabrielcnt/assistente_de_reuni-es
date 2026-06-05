from pathlib import Path

AUDIO_DIR = Path("audio")


def encontrar_audio():

    arquivos = list(AUDIO_DIR.glob("*"))

    if not arquivos:
        raise FileNotFoundError("Nenhum áudio encontrado na pasta 'audio/'")

    audio = arquivos[0]

    print(f"Áudio encontrado: {audio}")

    return audio

encontrar_audio()