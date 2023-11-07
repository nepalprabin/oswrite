from click.testing import CliRunner
from oswrite.cli import cli
import pytest
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
runner = CliRunner()


def test_input_file_format():
    result = runner.invoke(cli, ["--audio_file", "demo.txt"])
    assert result.exit_code == 2
    assert "Input file must be .mp3 or .wav format" in result.output
