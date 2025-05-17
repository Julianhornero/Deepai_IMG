
# Deepai_IMG

AI IMAGE GENERATOR using DeepAI API

---

## Overview

This project provides a simple Python script to generate AI images from text prompts using the DeepAI API. It demonstrates how to interact with the DeepAI `text2img` endpoint to create images based on user input.

---

## Features

- Generate images from text prompts using DeepAI's AI models.
- Simple and minimal Python code.
- Outputs the URL of the generated image for easy access or download.

---

## Requirements

- Python 3.6 or higher
- DeepAI API key (free to get from [DeepAI](https://deepai.org/))
- Python packages:
  - `requests`
  - `Pillow` (optional, if you want to download and save images locally)

---

## Installation

1. Clone the repository:

```
git clone https://github.com/Julianhornero/Deepai_IMG.git
cd Deepai_IMG
```

2. Install required Python packages:

```
pip install requests pillow
```

3. Obtain your DeepAI API key by signing up at [DeepAI](https://deepai.org/).

---

## Usage

Edit the `deepai.py` script to insert your API key and change the text prompt as desired.

Run the script:

```
python deepai.py
```

The script will print the URL of the generated image.

---

## Example Code Snippet

```
import requests

API_KEY = 'YOUR_DEEPAI_API_KEY'

def generate_image(prompt):
    response = requests.post(
        'https://api.deepai.org/api/text2img',
        data={'text': prompt},
        headers={'api-key': API_KEY}
    )
    if response.status_code == 200:
        output_url = response.json().get('output_url')
        print('Generated Image URL:', output_url)
        return output_url
    else:
        print('Error:', response.text)
        return None

if __name__ == "__main__":
    prompt = "A fantasy landscape with mountains and rivers"
    generate_image(prompt)
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

