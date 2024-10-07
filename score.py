from sklearn.metrics import f1_score

def flatten_json(json_obj, parent_key='', sep='_'):
    flattened_dict = {}
    for key, value in json_obj.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_json(value, new_key, sep=sep))
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
