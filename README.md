# oswrite

CLI tool for running audio through the OpenAI whisper API

See oswrite: a CLI tool for running audio through the OpenAI whisper API.

PS: It is inspired by Simon Willamson's [osread](https://github.com/simonw/ospeak)
Installation
Install this tool using pip:

```python
pip install oswrite
```

## Usage

```
oswrite --audio_file "test.mp3"
```

You will need an OpenAI API key. You can set that as an environment variable:

```
export OPENAI_API_KEY="..."
```

Or you can pass it using --token:

```
oswrite --token "..." --audio_file "test.mp3"
```
