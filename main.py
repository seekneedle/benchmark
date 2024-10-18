import json
import os
import glob
from score import calculate_f1_score
from tabulate import tabulate


def wrap_text(text, max_length):
    """Wrap text to ensure it does not exceed the maximum length."""
    text = str(text)
    return '\n'.join(text[i:i+max_length] for i in range(0, len(text), max_length))


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
    # print('---predict---')
    # print(predict_data)

    # 设置要读取的目录路径
    golden_path = 'res/golden'  # 替换为你的目录路径
    # 加载所有JSON文件的数据
    golden_data = load_json_files(golden_path)
    # 输出结果
    # print('---golden---')
    # print(golden_data)

    if not keys:
        keys = golden_data.keys()
    for json_key in keys:
        predict_json = predict_data.get(json_key, {})
        golden_json = golden_data.get(json_key, {})
        f1_score, common_keys, golden_labels, predict_labels, error_predictions = calculate_f1_score(golden_json,
                                                                                                     predict_json)
        print(f"---{json_key}.json---")
        print("F1 Score:", f1_score)

        if error_predictions:
            # 定义表头
            headers = ["Keys", "Golden Labels", "Predict Labels"]

            table_data = []
            for error_pred in error_predictions:
                table_data.append((error_pred['key'], wrap_text(error_pred['golden_label'], 10), wrap_text(error_pred[
                    'predict_label'], 10)))
            # 使用tabulate打印表格
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    score(['U167051', '9a6fc493a4b2f802ef39ef3c0dd8c328'])
