from sklearn.metrics import f1_score
import requests
from security import decrypt
from config import config
import json

def flatten_json(json_obj, parent_key='', sep='_'):
    flattened_dict = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            # 如果是字典，递归调用
            flattened_dict.update(flatten_json(value, new_key, sep=sep))
        elif isinstance(value, list):
            # 如果是列表，迭代每个元素
            for i, item in enumerate(value):
                # 使用索引来区分列表中的不同元素
                list_item_key = f"{new_key}{sep}{i}"
                if isinstance(item, dict):
                    # 如果列表中的元素是字典，递归调用
                    flattened_dict.update(flatten_json(item, list_item_key, sep=sep))
                else:
                    # 否则直接添加到结果字典中
                    flattened_dict[list_item_key] = item
        else:
            flattened_dict[new_key] = value
    return flattened_dict


# HTTPS接口的URL
url = 'https://api.coze.cn/v1/workflow/run'
workflow_id = "7423313180841197622"

def send_request(golden, predict):
    data = {
        "workflow_id": workflow_id,
        "parameters": {
            "golden": golden,
            "predict": predict
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
            return False
    except requests.exceptions.RequestException as e:
        return False


def align_predict(golden_flat, predict_flat):
    for key in golden_flat.keys():
        golden = golden_flat[key]
        predict = predict_flat.get(key, '')
        if golden != '' and predict != '' and golden != predict:
            is_same = send_request(golden, predict)
            if is_same:
                predict_flat[key] = golden
    return predict_flat

def calculate_f1_score(golden_json, predict_json):
    golden_flat = flatten_json(golden_json)
    predict_flat = flatten_json(predict_json)
    if config['align_predict']:
        predict_flat = align_predict(golden_flat, predict_flat)

    common_keys = golden_flat.keys()

    golden_labels = [str(golden_flat.get(key, '')) for key in common_keys]
    predict_labels = [str(predict_flat.get(key, '')) for key in common_keys]

    f1 = f1_score(golden_labels, predict_labels, average='weighted')

    error_predictions = []
    for key in common_keys:
        if key in common_keys:
            if golden_flat.get(key, '') != predict_flat.get(key, ''):
                error_predictions.append({
                    'key': key,
                    'golden_label': golden_flat.get(key, ''),
                    'predict_label': predict_flat.get(key, '')
                })

    return f1, common_keys, golden_labels, predict_labels, error_predictions

if __name__ == "__main__":
    # 示例Golden JSON和Predict JSON（含有二级key）
    golden_json = {
        "content": "This is a good example.",
        "metadata": {
            "label": "positive"
        },
        "other": "hello world"
    }

    predict_json = {
        "content": "This is a good example.",
        "metadata": {
            "label": "negative"
        }
    }

    f1_score, common_keys, golden_labels, predict_labels, error_predictions = calculate_f1_score(golden_json, predict_json)

    print("F1 Score:", f1_score)
    print("Common Keys:", common_keys)
    print("Golden Labels:", golden_labels)
    print("Predict Labels:", predict_labels)
    print("Error Predictions:")
    for error_pred in error_predictions:
        print(f"Key: {error_pred['key']}, Golden Label: {error_pred['golden_label']}, Predicted Label: {error_pred['predict_label']}")
