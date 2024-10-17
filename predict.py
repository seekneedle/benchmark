import requests
import json
from config import config
from security import decrypt
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
        'Authorization': decrypt(config['predict_key'])
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


def send_request_workflow(pdf_url):
    data = {
        "pdf_url": pdf_url
    }
    headers = {
        'Authorization': decrypt(config['auth'])
    }
    workflow_url = f'http://{config["ip"]}:{config["port"]}/getProductInfoFromPdf'
    try:
        response = requests.post(workflow_url, headers=headers, json=data)
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        return {}


def download(pdf_url, rename: str=''):
    # json_resp = send_request(pdf_url)
    json_resp = send_request_workflow(pdf_url)
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
            json.dump(json_resp, json_file, ensure_ascii=False, indent=4)
        print(f"Data was successfully written to {filepath}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    download('https://i1.uuxlink.com/ai/doubao/U167051.pdf')
    download('https://i1.uuxlink.com/ai/doubao/U167046.pdf')
    download('https://i1.uuxlink.com/ai/doubao/U167030.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2024/0528/15/c3ace3d3e63060456f2933262521bc90.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2024/0919/16/44252e31ad74dd1faed36f1e399c0b9f.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2024/0920/16/97bcc070651cdd088ddcbf67aefd2b0d.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2023/0807/19/b6e6aac450f9c71350f2699af29e7454.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2024/0821/17/ccf46f2c99a6eedad6ca100f8104d4c4.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2024/0715/15/c0452f6a46a4c686b80bde4699ed0626.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2024/0718/15/9c31733a4562a5bc5dadb1477706c562.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2024/0921/10/9a6fc493a4b2f802ef39ef3c0dd8c328.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2024/0523/11/e01a4b0909760c4b7a926a75a2433703.pdf')
    download('https://ncstatic-file.clewm.net/rsrc/2024/0523/11/e01a4b0909760c4b7a926a75a2433703.pdf')
