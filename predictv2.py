import requests
import json
from config import config
from security import decrypt
import os
from urllib.parse import urlparse, unquote
from tqdm import tqdm
import time


def send_request_workflow(pdf_url):
    data = {
        "pdf_url": pdf_url
    }
    headers = {
        'Authorization': decrypt(config['auth'])
    }
    workflow_url = f'http://{config["ip"]}:{config["port"]}/v2/getProductInfoFromPdf'
    try:
        response = requests.post(workflow_url, headers=headers, json=data)
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        return {}


def send_status_workflow(task_id):
    data = {
        "task_id": task_id
    }
    headers = {
        'Authorization': decrypt(config['auth'])
    }
    workflow_url = f'http://{config["ip"]}:{config["port"]}/v2/getProductInfoParserStatus'
    try:
        response = requests.post(workflow_url, headers=headers, json=data)
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        return {}


def download(pdf_url, rename: str=''):
    # json_resp = send_request(pdf_url)
    json_resp = send_request_workflow(pdf_url)
    return json_resp['task_id']


def get_result(task_id):
    status_result = send_status_workflow(task_id)
    return status_result['data']


if __name__ == "__main__":
    files = ['https://uux-public.oss-cn-beijing.aliyuncs.com/ai/golden/CA%E3%80%90%E5%85%A8%E5%AE%B6%E6%80%BB%E5%8A%A8%E5%91%98%20%E6%98%A5%E8%8A%82%E7%89%B9%E8%BE%91%E3%80%91%E7%BE%8E%E5%9B%BD%E4%B8%9C%E6%B5%B7%E5%B2%B8%E5%90%8D%E5%9F%8E%E5%90%8D%E6%A0%A1%2B%E4%BD%9B%E5%B7%9E15%E6%97%A5.pdf']

    tasks = []

    for file in files:
        task_id = download(file)
        tasks.append(task_id)

    for task_id, pdf_url in tqdm(zip(tasks, files)):
        json_resp = None
        while True:
            time.sleep(30)
            json_resp = get_result(task_id)
            finish = json_resp['finish']
            if len(finish) == 5:
                del json_resp['finish']
                break
        parsed_url = urlparse(pdf_url)
        path = parsed_url.path
        filename_with_extension = path.split('/')[-1]
        filename = filename_with_extension.split('.pdf')[0] + '.json'
        filename = unquote(filename)
        filepath = os.path.join('res', 'predict', filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as json_file:
                json.dump(json_resp, json_file, ensure_ascii=False, indent=4)
            print(f"Data was successfully written to {filepath}")
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

