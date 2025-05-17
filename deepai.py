import requests

def generate_image_from_text(prompt, api_key):
    url = "https://api.deepai.org/api/text2img"
    headers = {
        'api-key': api_key
    }
    data = {
        'text': prompt
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if 'output_url' in result:
            print("Generated Image URL:", result['output_url'])
            return result['output_url']
        else:
            print("Error: No output_url in response", result)
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")

if __name__ == "__main__":
    YOUR_API_KEY = "your_deepai_api_key_here"
    prompt_text = "A fantasy landscape with mountains and rivers"
    generate_image_from_text(prompt_text, YOUR_API_KEY)
