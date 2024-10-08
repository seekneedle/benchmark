from sklearn.metrics import f1_score

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

def calculate_f1_score(golden_json, predict_json):
    golden_flat = flatten_json(golden_json)
    predict_flat = flatten_json(predict_json)

    common_keys = golden_flat.keys()

    golden_labels = [golden_flat.get(key, '') for key in common_keys]
    predict_labels = [predict_flat.get(key, '') for key in common_keys]

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
