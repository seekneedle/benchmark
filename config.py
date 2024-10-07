import yaml
import os

def load_yaml_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config

# 使用函数加载配置
config = load_yaml_config(os.path.join('res', 'prod', 'config.yml'))

# 输出配置内容以验证是否正确加载
print(config)
