from click.testing import CliRunner
from oswrite.cli import cli
import pytest

runner = CliRunner()


def test_input_file_format():
    result = runner.invoke(cli, ["--audio_file", "demo.txt", "OpenAI"])
    assert result.exit_code == 2
    assert "Input file must be .mp3 or .wav format" in result.output
