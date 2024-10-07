import json
import os
import glob
from score import calculate_f1_score


def load_json_files(directory):
    # 创建一个空字典来存储结果
    json_data = {}

    # 获取目录下所有的.json文件
    json_files = glob.glob(os.path.join(directory, '*.json'))

    # 遍历每个找到的.json文件
    for file_path in json_files:
        # 获取文件名，不包括路径和扩展名
        file_name = os.path.splitext(os.path.basename(file_path))[0]

        # 打开文件并加载JSON内容
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # 将数据添加到字典中
            json_data[file_name] = data

    return json_data

def score(keys=None):
    # 设置要读取的目录路径
    if keys is None:
        keys = []
    predict_path = 'res/predict'  # 替换为你的目录路径
    # 加载所有JSON文件的数据
    predict_data = load_json_files(predict_path)
    # 输出结果
    print('---predict---')
    print(predict_data)

    # 设置要读取的目录路径
    golden_path = 'res/golden'  # 替换为你的目录路径
    # 加载所有JSON文件的数据
    golden_data = load_json_files(golden_path)
    # 输出结果
    print('---golden---')
    print(golden_data)

    if not keys:
        keys = golden_data.keys()
    for json_key in keys:
        predict_json = predict_data.get(json_key, {})
        golden_json = golden_data.get(json_key, {})
        f1_score, common_keys, golden_labels, predict_labels, error_predictions = calculate_f1_score(golden_json,
                                                                                                     predict_json)
        print(f"---{json_key}---")
        print("F1 Score:", f1_score)
        print("Common Keys:", common_keys)
        print("Golden Labels:", golden_labels)
        print("Predict Labels:", predict_labels)
        print("Error Predictions:")
        for error_pred in error_predictions:
            print(
                f"Key: {error_pred['key']}, Golden Label: {error_pred['golden_label']}, Predicted Label: {error_pred['predict_label']}")

if __name__ == "__main__":
    score()
