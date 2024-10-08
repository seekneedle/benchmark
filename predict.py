import requests
import json
from config import config
from security import decrypt_config
import os
from urllib.parse import urlparse

# HTTPS接口的URL
url = 'https://api.coze.cn/v1/workflow/run'
workflow_id = "7409550376623751195"

def send_request(pdf_url):
    data = {
        "workflow_id": workflow_id,
        "parameters": {
            "BOT_USER_INPUT": pdf_url
        }
    }

    # 请求头（如果需要的话）
    headers = {
        'Content-Type': 'application/json',
        'Authorization': decrypt_config(config['predict_key'])
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        content = response.text
        try:
            json_data = json.loads(content)
            inner_data = json.loads(json_data["data"])
            data = json.loads(inner_data["data"])
            return data
        except json.JSONDecodeError:
            return {}
    except requests.exceptions.RequestException as e:
        return {}

def download(pdf_url, rename: str=''):
    json_resp = send_request(pdf_url)
    if rename == '':
        parsed_url = urlparse(pdf_url)
        path = parsed_url.path
        filename_with_extension = path.split('/')[-1]
        filename = filename_with_extension.split('.')[0] + '.json'
    else:
        filename = rename + '.json'
    filepath = os.path.join('res', 'predict', filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as json_file:
            json.dump(json_resp, json_file, ensure_ascii=False)
        print(f"Data was successfully written to {filepath}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    download('https://i1.uuxlink.com/ai/doubao/U167051.pdf')