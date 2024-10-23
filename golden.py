import streamlit as st
import json
import os

# 设置页面配置
st.set_page_config(layout="wide")

# 设置页面标题
st.title("旅行产品行程信息表单")

# 初始化行程天数
if 'num_days' not in st.session_state:
    st.session_state.num_days = 1

# 初始化景点数量
if 'num_attractions' not in st.session_state:
    st.session_state.num_attractions = 1


# 创建一个函数来处理增加/减少天数
def update_num_days(delta):
    st.session_state.num_days += delta
    if st.session_state.num_days < 1:
        st.session_state.num_days = 1


# 创建一个函数来处理增加/减少景点数量
def update_num_attractions(delta):
    st.session_state.num_attractions += delta
    if st.session_state.num_attractions < 1:
        st.session_state.num_attractions = 1


# 显示天数控制按钮
col1, col2 = st.columns(2)
with col1:
    st.button('减少天数', on_click=update_num_days, args=(-1,))
with col2:
    st.button('增加天数', on_click=update_num_days, args=(1,))

# 主行程信息输入
itinerary = {}
for day in range(1, st.session_state.num_days + 1):
    itinerary[f'Day {day}'] = {}
    st.subheader(f"第{day}天 行程")

    # 显示景点数量控制按钮
    col1, col2 = st.columns(2)
    with col1:
        st.button(f'减少第{day}天的景点', on_click=update_num_attractions, args=(-1,))
    with col2:
        st.button(f'增加第{day}天的景点', on_click=update_num_attractions, args=(1,))

    # 输入每一天的行程内容
    itinerary[f'Day {day}']['行程内容'] = st.text_area(f"请输入第{day}天的行程内容", key=f'day_{day}_content')

    # 输入酒店餐饮情况
    meals = ['早餐', '午餐', '晚餐']
    meal_options = {}
    for meal in meals:
        meal_options[meal] = st.checkbox(f"{meal}", key=f'day_{day}_{meal}', value=False)
    itinerary[f'Day {day}']['餐饮'] = meal_options

    # 景点名称输入
    attractions = []
    for attraction in range(st.session_state.num_attractions):
        attractions.append(st.text_input(f"请输入第{attraction + 1}个景点名称",
                                         key=f'day_{day}_attraction_{attraction + 1}'))
    itinerary[f'Day {day}']['景点'] = attractions

# 提交按钮
file_name = st.text_input("请输入JSON文件名（含.json扩展名）", "itinerary.json")
if st.button('提交'):
    # 构建完整的文件路径
    file_path = os.path.join("res", "golden", file_name)

    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 将数据写入JSON文件
    try:
        with open(file_path, 'w') as f:
            json.dump(itinerary, f, ensure_ascii=False, indent=4)
        st.success(f"行程信息已成功保存至 {file_path}")
    except Exception as e:
        st.error(f"保存文件时发生错误：{e}")