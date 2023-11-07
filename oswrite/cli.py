import click
from openai import OpenAI

client = OpenAI()


def transcribe(audio_file, api_key=None):
    client = OpenAI(api_key=api_key)
    audio_file = open(audio_file, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file, response_format="text"
    )
    print(transcript)
    return transcript


@click.command()
@click.version_option()
@click.option("--audio_file", help="Audio file path")
@click.option(
    "--token",
    help="OpenAI API key",
    envvar="OPENAI_API_KEY",
)
def cli(audio_file, token):
    transcribe(audio_file, token)


if __name__ == "__main__":
    cli()
