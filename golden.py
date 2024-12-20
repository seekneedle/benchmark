import streamlit as st
import os
from pathlib import Path
import json

# 设置页面配置
st.set_page_config(
    page_title="填写产品信息",
    layout="wide",  # 设置页面布局为宽模式
)

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

# 创建上传文件的目录
upload_dir = Path(os.path.join('res', 'pdf'))
upload_dir.mkdir(parents=True, exist_ok=True)

if "refresh_event" not in st.session_state:
    st.session_state.refresh_event = False

if "current_tab" not in st.session_state:
    st.session_state.current_tab = 0

# 初始化 session_state 变量
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

if 'rewrite' not in st.session_state:
    st.session_state.rewrite = ""

if 'confirm' not in st.session_state:
    st.session_state.confirm = False

product_json = {
        "product": {
            "childAgeBegin": 0,
            "childAgeEnd": 0,
            "childHasBed": 0,
            "childHasTraffic": 0,
            "childHeightBegin": "",
            "childHeightEnd": "",
            "childRule": "",
            "departureCityName": "",
            "departureCountryName": "",
            "departureProvinceNam": "",
            "dests": [
                {
                    "countryName": "",
                    "destCityName": "",
                    "destProvinceName": ""
                }
            ],
            "insurance": [{
                "content": "",
                "name": "",
                "typeName": ""
            }],
            "insuranceIncluded": 0,
            "markets": [
                {
                    "name": ""
                }
            ],
            "productSubtitle": "",
            "productTitle": "",
            "returnCityName": "",
            "tags": [
                {
                    "name": ""
                }
            ],
            "themes": [
                {
                    "name": ""
                }
            ]
        },
        "line": {
            "backAirports": [
                {
                    "airlineCode": "",
                    "airlineName": "",
                    "arriveAirportName": "",
                    "arriveTime": "",
                    "days": 0,
                    "flightNo": "",
                    "flightSort": "",
                    "startAirportName": "",
                    "startTime": ""
                }
            ],
            "backTransportName": "",
            "goAirports": [
                {
                    "airlineCode": "",
                    "airlineName": "",
                    "arriveAirportName": "",
                    "arriveTime": "",
                    "days": 0,
                    "flightNo": "",
                    "flightSort": "",
                    "startAirportName": "",
                    "startTime": ""
                }
            ],
            "goTransportName": "",
            "hotelStarName": "",
            "lineFeature": "",
            "lineSimpleTitle": "",
            "lineSortTitle": "",
            "lineTitle": "",
            "needVisa": 1,
            "passCities": [
                {
                    "cityName": "",
                    "countryName": "",
                    "provinceName": ""
                }
            ],
            "tripDays": "",
            "tripNight": "",
            "visaBasic": {
                "postAddress": "",
                "postContact": "",
                "postPhone": "",
                "visas": [
                    {
                        "content": "",
                        "country": "",
                        "district": "",
                        "freeVisa": 0,
                        "signPlace": ""
                    }
                ]
            }
        },
        "cal": {
            "channelPut": [{
                "adultSalePrice": "",
                "childSalePrice": "",
                "sellRemark": ""
            }],
            "departDate": [
                ""
            ]
        },
        "cost": {
            "bookRule": "",
            "costExclude": "",
            "costInclude": "",
            "lineReturns": [
                {
                    "begin": "",
                    "cost": "",
                    "end": ""
                },
            ],
            "otherRule": "",
            "returnContent": "",
            "selfCostContent": "",
            "selfCosts": [
                {
                    "address": "",
                    "fee": "",
                    "name": "",
                    "remark": "",
                    "stay": ""
                }
            ],
            "shopContent": "",
            "shops": [
                {
                    "address": "",
                    "remark": "",
                    "shopName": "",
                    "shopProduct": "",
                    "stay": ""
                }
            ],
            "tipsContent": ""
        },
        "trips": [
            {
                "breakfast": 0,
                "content": "",
                "dinner": 0,
                "hotels": [
                    {
                        "name": "",
                        "star": ""
                    }
                ],
                "lunch": 0,
                "scenes": [
                    {
                        "consumingTime": "",
                        "description": "",
                        "name": ""
                    }
                ],
                "scheduleTraffics": [
                    {
                        "arrivalTime": "",
                        "departure": "",
                        "departureTime": "",
                        "destination": "",
                        "trafficType": ""
                    }
                ],
                "title": "",
                "tripDay": 1
            }
        ]
    }

# 初始化 session state 中的多级字典
if 'multi_level_dict' not in st.session_state:
    st.session_state.multi_level_dict = product_json

default_airport_value = {
            "airlineCode": "",
            "airlineName": "",
            "arriveAirportName": "",
            "arriveTime": "",
            "days": "",
            "flightNo": "",
            "flightSort": "",
            "startAirportName": "",
            "startTime": ""
        }

default_passCities_value = {
    "countryName": "",
    "provinceName": "",
    "cityName": ""}

default_visa_value = {
    "content": "",
    "country": "",
    "district": "",
    "freeVisa": 0,
    "signPlace": ""}

default_channel_put_value = {
    "adultSalePrice": "",
    "childSalePrice": "",
    "sellRemark": ""}


def overlap(uploaded_file, file_name):
    st.session_state.uploaded_file = uploaded_file
    st.session_state.rewrite = file_name

    json_file_name = file_name.split('.pdf')[0] + '.json'
    json_path = os.path.join('res', 'golden', json_file_name)

    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            st.session_state.multi_level_dict = json_data
        print("JSON data loaded successfully.")
    except FileNotFoundError:
        print(f"File not found: {json_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {json_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# 定义上一页按钮点击函数
def on_previous_page_click():
    st.session_state.current_tab = st.session_state.current_tab - 1


# 定义下一页按钮点击函数
def on_next_page_click():
    if st.session_state.current_tab == 0 and st.session_state.uploaded_file is None:
        st.error("请上传一个旅行产品 PDF 文件！")
    else:
        st.session_state.current_tab = st.session_state.current_tab + 1


# 定义完成按钮点击函数
def on_finish_click():
    st.session_state.confirm = True


# 定义确定按钮点击函数
def on_confirm_click():
    st.session_state.confirm = False
    try:
        uploaded_file = st.session_state.uploaded_file
        # 获取文件名
        file_name = uploaded_file.name

        # 构建保存路径
        save_path = upload_dir / file_name

        json_file_name = file_name.split('.pdf')[0] + '.json'
        json_path = os.path.join('res', 'golden', json_file_name)

        # 将文件保存到指定目录
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f'文件已成功覆盖并保存到 {save_path}')
        st.session_state.show_result = True

        # 将文件保存到指定目录
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(st.session_state.multi_level_dict, json_file, ensure_ascii=False, indent=4)

        st.session_state.multi_level_dict = product_json
        st.session_state.refresh_event = False
        st.session_state.current_tab = 0
        st.session_state.uploaded_file = None
        st.session_state.rewrite = ""

    except Exception as e:
        st.error(f"上传异常，请检查：{e}")


def add_dest():
    st.session_state.multi_level_dict["product"]["dests"].append({"countryName": "", "destCityName": "", "destProvinceName": ""})


def del_dest(i):
    dests = st.session_state.multi_level_dict["product"]["dests"]
    if len(dests) > 1 and i < len(dests):
        st.session_state.refresh_event = True
        del dests[i]


def add_insure():
    st.session_state.multi_level_dict["product"]["insurance"].append({"content": "", "name": "", "typeName": ""})


def del_insure(i):
    insurances = st.session_state.multi_level_dict["product"]["insurance"]
    if len(insurances) > 1 and i < len(insurances):
        st.session_state.refresh_event = True
        del insurances[i]


def add_theme():
    st.session_state.multi_level_dict["product"]["themes"].append({"name": ""})


def del_theme(i):
    themes = st.session_state.multi_level_dict["product"]["themes"]
    if len(themes) > 1 and i < len(themes):
        st.session_state.refresh_event = True
        del themes[i]


def add_tag():
    st.session_state.multi_level_dict["product"]["tags"].append({"name": ""})


def del_tag(i):
    tags = st.session_state.multi_level_dict["product"]["tags"]
    if len(tags) > 1 and i < len(tags):
        st.session_state.refresh_event = True
        del tags[i]


def add_market():
    st.session_state.multi_level_dict["product"]["markets"].append({"name": ""})


def del_market(i):
    markets = st.session_state.multi_level_dict["product"]["markets"]
    if len(markets) > 1 and i < len(markets):
        st.session_state.refresh_event = True
        del markets[i]


def add_go_airport():
    st.session_state.multi_level_dict["line"]["goAirports"].append(default_airport_value)


def del_go_airport(i):
    go_airports = st.session_state.multi_level_dict["line"]["goAirports"]
    if len(go_airports) > 1 and i < len(go_airports):
        st.session_state.refresh_event = True
        del go_airports[i]


def add_back_airport():
    st.session_state.multi_level_dict["line"]["backAirports"].append(default_airport_value)


def del_back_airport(i):
    back_airports = st.session_state.multi_level_dict["line"]["backAirports"]
    if len(back_airports) > 1 and i < len(back_airports):
        st.session_state.refresh_event = True
        del back_airports[i]


def add_pass_city():
    st.session_state.multi_level_dict["line"]["passCities"].append(default_passCities_value)


def del_pass_city(i):
    pass_cities = st.session_state.multi_level_dict["line"]["passCities"]
    if len(pass_cities) > 1 and i < len(pass_cities):
        st.session_state.refresh_event = True
        del pass_cities[i]


def add_visa():
    st.session_state.multi_level_dict["line"]["visaBasic"]['visas'].append(default_visa_value)


def del_visa(i):
    visas = st.session_state.multi_level_dict["line"]["visaBasic"]['visas']
    if len(visas) > 1 and i < len(visas):
        st.session_state.refresh_event = True
        del visas[i]


def add_channel_put():
    st.session_state.multi_level_dict["cal"]["channelPut"].append({
                "adultSalePrice": "",
                "childSalePrice": "",
                "sellRemark": ""
            })


def del_channel_put(i):
    channelPuts = st.session_state.multi_level_dict["cal"]["channelPut"]
    if len(channelPuts) > 1 and i < len(channelPuts):
        st.session_state.refresh_event = True
        del channelPuts[i]


def add_depart_date():
    st.session_state.multi_level_dict["cal"]["departDate"].append("")


def del_depart_date(i):
    departDates = st.session_state.multi_level_dict["cal"]["departDate"]
    if len(departDates) > 1 and i < len(departDates):
        st.session_state.refresh_event = True
        del departDates[i]


def add_return():
    st.session_state.multi_level_dict["cost"]["lineReturns"].append({
                "begin": "",
                "cost": "",
                "end": ""
            })


def del_return(i):
    lineReturns = st.session_state.multi_level_dict["cost"]["lineReturns"]
    if len(lineReturns) > 1 and i < len(lineReturns):
        st.session_state.refresh_event = True
        del lineReturns[i]


def add_self_cost():
    st.session_state.multi_level_dict["cost"]["selfCosts"].append({
                "address": "",
                "fee": "",
                "name": "",
                "remark": "",
                "stay": ""
            })


def del_self_cost(i):
    selfCosts = st.session_state.multi_level_dict["cost"]["selfCosts"]
    if len(selfCosts) > 1 and i < len(selfCosts):
        st.session_state.refresh_event = True
        del selfCosts[i]


def add_shop():
    st.session_state.multi_level_dict["cost"]["shops"].append({
                "address": "",
                "shopProduct": "",
                "shopName": "",
                "remark": "",
                "stay": ""
            })


def del_shop(i):
    shops = st.session_state.multi_level_dict["cost"]["shops"]
    if len(shops) > 1 and i < len(shops):
        st.session_state.refresh_event = True
        del shops[i]


def add_hotel(i):
    st.session_state.multi_level_dict["trips"][i]['hotels'].append({
                    "name": "",
                    "star": ""
                })


def del_hotel(i, j):
    hotels = st.session_state.multi_level_dict["trips"][i]['hotels']
    if len(hotels) > 1 and j < len(hotels):
        st.session_state.refresh_event = True
        del hotels[j]


def add_traffic(i):
    st.session_state.multi_level_dict["trips"][i]['scheduleTraffics'].append({
                    "departure": "",
                    "departureTime": "",
                    "destination": "",
                    "arrivalTime": "",
                    "trafficType": ""
                })


def del_traffic(i, j):
    scheduleTraffics = st.session_state.multi_level_dict["trips"][i]['scheduleTraffics']
    if len(scheduleTraffics) > 1 and j < len(scheduleTraffics):
        st.session_state.refresh_event = True
        del scheduleTraffics[j]


def add_scene(i):
    st.session_state.multi_level_dict["trips"][i]['scenes'].append({
                    "name": "",
                    "description": "",
                    "consumingTime": ""
                })


def del_scene(i, j):
    scenes = st.session_state.multi_level_dict["trips"][i]['scenes']
    if len(scenes) > 1 and j < len(scenes):
        st.session_state.refresh_event = True
        del scenes[j]


def add_trip():
    st.session_state.multi_level_dict["trips"].append({
            "breakfast": 0,
            "content": "",
            "dinner": 0,
            "hotels": [
                {
                    "name": "",
                    "star": ""
                }
            ],
            "lunch": 0,
            "scenes": [
                {
                    "consumingTime": "",
                    "description": "",
                    "name": ""
                }
            ],
            "scheduleTraffics": [
                {
                    "arrivalTime": "",
                    "departure": "",
                    "departureTime": "",
                    "destination": "",
                    "trafficType": ""
                }
            ],
            "title": "",
            "tripDay": 1
        })


def del_trip(i):
    trips = st.session_state.multi_level_dict["trips"]
    if len(trips) > 1 and i < len(trips):
        st.session_state.refresh_event = True
        del trips[i]


def get_default(cache, key, need_refresh=False):
    if need_refresh and st.session_state.refresh_event:
        value = cache
    else:
        value = st.session_state.get(key, cache)
    return {
        "value": value,
        "key": key
    }


class FormItemModel:
    def __init__(self, key, name, type="text", options=["是", "否"]):
        self.key = key
        self.name = name
        self.type = type
        self.options = options

    def __repr__(self):
        return f"Model(key={self.key}, name={self.name}, type={self.type}), options={self.options}"


if st.session_state.current_tab == 0:
    # 创建一个文件上传器
    uploaded_file = st.file_uploader("上传旅行产品 PDF 文件", type=["pdf"], accept_multiple_files=False)

    if uploaded_file is not None:
        # 获取文件名
        file_name = uploaded_file.name

        # 构建保存路径
        save_path = upload_dir / file_name

        if os.path.exists(save_path) and file_name != st.session_state.rewrite:
            st.warning(f"旅行产品 {file_name} 已存在，是否覆盖？")
            st.button("覆盖", on_click=overlap, args=(uploaded_file, file_name))
        else:
            st.session_state.uploaded_file = uploaded_file

    if st.session_state.uploaded_file is not None:
        st.write(f"已上传旅行产品：{st.session_state.uploaded_file.name}")

# 产品详情
if st.session_state.current_tab == 1:
    st.subheader("产品详情")
    keys = [FormItemModel(key="productTitle", name="产品名称"),        
            FormItemModel(key="productSubtitle", name="产品副标题"),
            FormItemModel(key="departureCountryName", name="出发国家名字"),
            FormItemModel(key="departureProvinceNam", name="出发省份"),
            FormItemModel(key="departureCityName", name="出发城市名字"),
            FormItemModel(key="returnCityName", name="返回城市名字"),
            FormItemModel(key="childAgeBegin", name="儿童年龄标准区间开始值"),
            FormItemModel(key="childAgeEnd", name="儿童年龄标准区间结束值"),
            FormItemModel(key="childHeightBegin", name="儿童身高标准区间开始值"),
            FormItemModel(key="childHeightEnd", name="儿童身高标准区间结束值"),
            FormItemModel(key="childHasTraffic", name="儿童价格是否含大交通", type="select"),
            FormItemModel(key="childHasBed", name="儿童价是否含床", type="select"),
            FormItemModel(key="childRule", name="儿童标准说明")]

    for item in keys:
        key_string = item.key
        key_name = item.name
        key_type = item.type
        key_options = item.options

        if key_type == "select":
            current_value = st.session_state.multi_level_dict["product"].get(key_string, None) 
            index = 0 if current_value == 1 else 1
            st.session_state.multi_level_dict["product"][key_string] = st.radio( key_name, options=key_options, index=index )
            selected_option = st.session_state.multi_level_dict["product"][key_string]
            st.session_state.multi_level_dict["product"][key_string] = 1 if selected_option == "是" else 0
        else:
            st.session_state.multi_level_dict["product"][key_string] = st.text_input(key_name,
                                                                                     **get_default(
                                                                                         st.session_state.multi_level_dict[
                                                                                             "product"][key_string],
                                                                                         key_string))

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    # 动态添加和删除列表输入框
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>目的地信息</h2>", unsafe_allow_html=True )
    dests = st.session_state.multi_level_dict["product"]["dests"]
    for i, dest in enumerate(dests):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>目的地{i + 1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_dests{i}", on_click=del_dest, args=(i,))
        col1, col2, col3 = st.columns([3, 3, 1])
        with col1:
            dest["countryName"] = st.text_input(f"国家", **get_default(dest["countryName"], f"countryName{i}",
                                                                       need_refresh=True))
        with col2:
            dest["destProvinceName"] = st.text_input(f"省份",
                                                     **get_default(dest["destProvinceName"], f"destProvinceName{i}",
                                                                   need_refresh=True))
        with col3:
            dest["destCityName"] = st.text_input(f"城市", **get_default(dest["destCityName"], f"destCityName{i}",
                                                                        need_refresh=True))

    st.button("添加目的地", on_click=add_dest)

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>保险信息</h2>", unsafe_allow_html=True )

    keys = [FormItemModel(key="insuranceIncluded", name="是否包含保险", type="select")]

    for item in keys:
        key_string = item.key
        key_name = item.name
        key_type = item.type
        key_options = item.options

        if key_type == "select":
            current_value = st.session_state.multi_level_dict["product"].get(key_string, None) 
            index = 0 if current_value == 1 else 1
            st.session_state.multi_level_dict["product"][key_string] = st.radio( key_name, options=key_options, index=index )
            selected_option = st.session_state.multi_level_dict["product"][key_string]
            st.session_state.multi_level_dict["product"][key_string] = 1 if selected_option == "是" else 0
        else:
            st.session_state.multi_level_dict["product"][key_string] = st.text_input(key_name,
                                                                                     **get_default(
                                                                                         st.session_state.multi_level_dict[
                                                                                             "product"][key_string],
                                                                                         key_string))
            
    insurances = st.session_state.multi_level_dict["product"]["insurance"]
    for i, insurance in enumerate(insurances):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>保险信息{i+1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_insurances{i}", on_click=del_insure, args=(i,))
        col1, col2, col3 = st.columns([3, 3, 1])
        with col1:
            insurance["content"] = st.text_input(f"保险内容", **get_default(insurance["content"], f"insurance_content{i}",
                                                                       need_refresh=True))
        with col2:
            insurance["name"] = st.text_input(f"保险名称",  **get_default(insurance["name"], f"insurance_name{i}",
                                                                   need_refresh=True))
        with col3:
            insurance["typeName"] = st.text_input(f"保险类型（境内外旅游险、航空险等）", **get_default(insurance["typeName"], f"insurance_typeName{i}",
                                                                        need_refresh=True))
    st.button("添加保险信息", on_click=add_insure)

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>产品主题</h2>", unsafe_allow_html=True )

    themes = st.session_state.multi_level_dict["product"]["themes"]
    for i, theme in enumerate(themes):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>产品主题{i+1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_themes{i}", on_click=del_theme, args=(i,))
        theme["name"] = st.text_input(f"主题名称", **get_default(theme["name"], f"theme_name{i}",
                                                                       need_refresh=True))
    st.button("添加产品主题", on_click=add_theme)

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>产品标签</h2>", unsafe_allow_html=True )

    tags = st.session_state.multi_level_dict["product"]["tags"]
    for i, tag in enumerate(tags):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>产品标签{i+1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_tags{i}", on_click=del_tag, args=(i,))
        tag["name"] = st.text_input(f"标签名称", **get_default(tag["name"], f"tag_name{i}",
                                                                       need_refresh=True))
    st.button("添加产品标签", on_click=add_tag)

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>营销标签</h2>", unsafe_allow_html=True )

    markets = st.session_state.multi_level_dict["product"]["markets"]
    for i, market in enumerate(markets):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>营销标签{i+1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_markets{i}", on_click=del_market, args=(i,))
        market["name"] = st.text_input(f"营销标签名称", **get_default(market["name"], f"market_name{i}",
                                                                       need_refresh=True))
    st.button("添加营销标签", on_click=add_market)

# 线路信息
if st.session_state.current_tab == 2:
    st.subheader("线路信息")
    keys = [FormItemModel(key="backTransportName", name="返程交通名称"),
            FormItemModel(key="goTransportName", name="去程交通名称"),
            FormItemModel(key="hotelStarName", name="酒店星级"),
            FormItemModel(key="lineFeature", name="线路特色"),
            FormItemModel(key="lineSimpleTitle", name="线路简标题"),
            FormItemModel(key="lineSortTitle", name="线路缩写"),
            FormItemModel(key="lineTitle", name="线路名称"),
            FormItemModel(key="needVisa", name="是否需要签证", type="select"),
            FormItemModel(key="tripDays", name="总共几天"),        
            FormItemModel(key="tripNight", name="总共几晚")]
    for item in keys:
        key_string = item.key
        key_name = item.name
        key_type = item.type
        key_options = item.options

        if key_type == "select":
            current_value = st.session_state.multi_level_dict["line"].get(key_string, None) 
            index = 0 if current_value == 1 else 1
            st.session_state.multi_level_dict["line"][key_string] = st.radio( key_name, options=key_options, index=index )
            selected_option = st.session_state.multi_level_dict["line"][key_string]
            st.session_state.multi_level_dict["line"][key_string] = 1 if selected_option == "是" else 0
        else:
            st.session_state.multi_level_dict["line"][key_string] = st.text_input(key_name,
                                                                                 **get_default(
                                                                                     st.session_state.multi_level_dict[
                                                                                         "line"][key_string],
                                                                                     key_string))

    airports_keys = [FormItemModel(key="airlineCode", name="航空公司编码"),
            FormItemModel(key="airlineName", name="航空公司名称"),
            FormItemModel(key="arriveAirportName", name="到达机场名称"),
            FormItemModel(key="arriveTime", name="到达时间"),
            FormItemModel(key="days", name="日期差"),
            FormItemModel(key="flightNo", name="航班号"),
            FormItemModel(key="flightSort", name="航班顺序"),
            FormItemModel(key="startAirportName", name="出发机场名称"),
            FormItemModel(key="startTime", name="出发时间")]

    num_columns = 5  # 你可以根据需要调整列数

    st.markdown("<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='font-size: 20px; color: black;'>去程航班</h2>", unsafe_allow_html=True)
    goAirports = st.session_state.multi_level_dict["line"]["goAirports"]
    for i, airport in enumerate(goAirports):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<h2 style='font-size: 18px; color: #333333;'>去程航班信息{i + 1}</h2>",
                        unsafe_allow_html=True)
        with col2:
            st.button("❌", key=f"del_goAirports{i}", on_click=del_go_airport, args=(i,))
        columns = st.columns(num_columns)
        for j, item in enumerate(airports_keys):
            key_string = item.key
            key_name = item.name
            key_type = item.type
            key_options = item.options

            col_index = j % num_columns
            with columns[col_index]:
                airport[key_string] = st.text_input(key_name,
                                                    **get_default(airport[key_string], f"goAirports_{key_name}{i}",
                                                                  need_refresh=True))

    st.button("添加去程航班信息", on_click=add_go_airport)

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>返程航班</h2>", unsafe_allow_html=True )
    backAirports = st.session_state.multi_level_dict["line"]["backAirports"]    
    for i, airport in enumerate(backAirports):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>返程航班信息{i+1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_backAirports{i}", on_click=del_back_airport, args=(i,))
        columns = st.columns(num_columns)
        for j, item in enumerate(airports_keys):
            key_string = item.key
            key_name = item.name
            key_type = item.type
            key_options = item.options

            col_index = j % num_columns
            with columns[col_index]:
                airport[key_string] = st.text_input(key_name,
                                                    **get_default(airport[key_string], f"backAirports_{key_name}{i}", need_refresh=True))
                
    st.button("添加返程航班信息", on_click=add_back_airport)

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>途经城市</h2>", unsafe_allow_html=True )
    passCities_keys = [FormItemModel(key="countryName", name="途径国家名称"),
            FormItemModel(key="provinceName", name="途径省份名称"),
            FormItemModel(key="cityName", name="途径城市名称")]

    passCities = st.session_state.multi_level_dict["line"]["passCities"]
    for i, city in enumerate(passCities):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>途经城市{i+1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_passCities{i}", on_click=del_pass_city, args=(i,))
        passCities_num_columns = 3
        columns = st.columns(passCities_num_columns)
        for j, item in enumerate(passCities_keys):
            key_string = item.key
            key_name = item.name
            key_type = item.type
            key_options = item.options

            col_index = j % passCities_num_columns
            with columns[col_index]:
                city[key_string] = st.text_input(key_name,
                                                    **get_default(city[key_string], f"passCities_{key_name}{i}", need_refresh=True))
                
    st.button("添加途经城市", on_click=add_pass_city)

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>签证邮递信息</h2>", unsafe_allow_html=True )
    visaBasicinfo = st.session_state.multi_level_dict["line"]["visaBasic"]

    visa_info_keys = [FormItemModel(key="postAddress", name="签证邮寄地址"),
            FormItemModel(key="postContact", name="签证邮寄人"),
            FormItemModel(key="postPhone", name="签证邮件人手机")]
    for item in visa_info_keys:
        key_name = item.name
        key_string = item.key
        st.session_state.multi_level_dict["line"]["visaBasic"][key_string] = st.text_input(key_name,
                                                                                 **get_default(
                                                                                     st.session_state.multi_level_dict["line"]["visaBasic"][key_string],
                                                                                     key_string))

    visas_keys = [FormItemModel(key="content", name="签证及面签说明"),
            FormItemModel(key="country", name="签证国家"),
            FormItemModel(key="district", name="签证领区"),
            FormItemModel(key="freeVisa", name="免签标志1:免签2:面签"),
            FormItemModel(key="signPlace", name="送签地")]

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>签证信息</h2>", unsafe_allow_html=True )
    visas = st.session_state.multi_level_dict["line"]["visaBasic"]['visas']
    for i, visa in enumerate(visas):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>签证信息{i+1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_visa{i}", on_click=del_visa, args=(i,))
        visas_num_columns = 3
        columns = st.columns(visas_num_columns)
        for j, item in enumerate(visas_keys):
            key_string = item.key
            key_name = item.name
            key_type = item.type
            key_options = item.options

            col_index = j % visas_num_columns
            with columns[col_index]:
                visa[key_string] = st.text_input(key_name,
                                                    **get_default(visa[key_string], f"visa_{key_name}{i}", need_refresh=True))

    st.button("添加签证信息", on_click=add_visa)

# 成团信息
if st.session_state.current_tab == 3:
    st.subheader("成团信息")

    channel_put_keys = [FormItemModel(key="adultSalePrice", name="成人零售价"),
            FormItemModel(key="childSalePrice", name="儿童零售价"),
            FormItemModel(key="sellRemark", name="销售说明")]

    st.markdown( f"<h2 style='font-size: 20px; color: black;'>投放信息</h2>", unsafe_allow_html=True )
    channel_puts = st.session_state.multi_level_dict["cal"]["channelPut"]
    for i, channel in enumerate(channel_puts):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>投放信息{i+1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_channel_put{i}", on_click=del_channel_put, args=(i,))
        channels_num_columns = 3
        columns = st.columns(channels_num_columns)
        for j, item in enumerate(channel_put_keys):
            key_string = item.key
            key_name = item.name
            col_index = j % channels_num_columns
            with columns[col_index]:
                channel[key_string] = st.text_input(key_name,
                                                    **get_default(channel[key_string], f"channel_put_{key_name}{i}", need_refresh=True))
    st.button("添加投放信息", on_click=add_channel_put)

    st.markdown( "<hr style='border: 1px lightgrey solid; margin: 20px 0;'>", unsafe_allow_html=True )
    st.markdown( f"<h2 style='font-size: 20px; color: black;'>出团日期</h2>", unsafe_allow_html=True )        
    departDates = st.session_state.multi_level_dict["cal"]["departDate"]
    for i, departDate in enumerate(departDates):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown( f"<h2 style='font-size: 18px; color: #333333;'>出团日期{i+1}</h2>", unsafe_allow_html=True )
        with col2:
            st.button("❌", key=f"del_depart_date{i}", on_click=del_depart_date, args=(i,))
        departDates[i] = st.text_input(f"出团日期", **get_default(departDate, f"depart_date{i}",
                                                                       need_refresh=True))
    st.button("添加出团日期", on_click=add_depart_date)

# 消费信息
if st.session_state.current_tab == 4:
    keys = [FormItemModel(key="bookRule", name="订购规定"),
            FormItemModel(key="otherRule", name="其他规定"),
            FormItemModel(key="tipsContent", name="温馨提示"),
            FormItemModel(key="costInclude", name="费用内包含"),
            FormItemModel(key="costExclude", name="费用内不含")]

    st.subheader("消费信息")
    for item in keys:
        key_string = item.key
        key_name = item.name

        st.session_state.multi_level_dict["cost"][key_string] = st.text_input(key_name,
                                                                             **get_default(
                                                                                 st.session_state.multi_level_dict[
                                                                                     "cost"][key_string],
                                                                                 key_string))

    key_string = "returnContent"
    key_name = "退费规定"
    st.session_state.multi_level_dict["cost"][key_string] = st.text_input(key_name,
                                                                          **get_default(
                                                                              st.session_state.multi_level_dict[
                                                                                  "cost"][key_string],
                                                                              key_string))
    col1, col2 = st.columns([1, 30])
    with col1:
        st.empty()
    with col2:
        lineReturns = st.session_state.multi_level_dict["cost"]["lineReturns"]
        for i, lineReturn in enumerate(lineReturns):
            col1, col2, col3, col4 = st.columns([5, 5, 5, 1])
            with col1:
                key_string = "begin"
                key_name = "开始时间段"
                lineReturn[key_string] = st.text_input(key_name,
                                             **get_default(
                                                 lineReturn[key_string],
                                                 f"return_{key_string}{i}",
                                             need_refresh=True))
            with col2:
                key_string = "end"
                key_name = "截止时间段"
                lineReturn[key_string] = st.text_input(key_name,
                                             **get_default(
                                                 lineReturn[key_string],
                                                 f"return_{key_string}{i}",
                                             need_refresh=True))
            with col3:
                key_string = "cost"
                key_name = "退费比例"
                lineReturn[key_string] = st.text_input(key_name,
                                             **get_default(
                                                 lineReturn[key_string],
                                                 f"return_{key_string}{i}",
                                             need_refresh=True))
            with col4:
                st.button("❌", key=f"del_return{i}", on_click=del_return, args=(i,))
        st.button("添加退费规则", on_click=add_return)

    key_string = "selfCostContent"
    key_name = "自费项目介绍"
    st.session_state.multi_level_dict["cost"][key_string] = st.text_input(key_name,
                                                                          **get_default(
                                                                              st.session_state.multi_level_dict[
                                                                                  "cost"][key_string],
                                                                              key_string))

    col1, col2 = st.columns([1, 30])
    with col1:
        st.empty()
    with col2:
        selfCosts = st.session_state.multi_level_dict["cost"]["selfCosts"]
        for i, selfCost in enumerate(selfCosts):
            col1, col2, col3, col4, col5, col6 = st.columns([3, 3, 3, 3, 3, 1])
            with col1:
                key_string = "name"
                key_name = "自费项目名称"
                selfCost[key_string] = st.text_input(key_name,
                                                       **get_default(
                                                           selfCost[key_string],
                                                           f"self_{key_string}{i}",
                                                           need_refresh=True))
            with col2:
                key_string = "fee"
                key_name = "自费项目费用"
                selfCost[key_string] = st.text_input(key_name,
                                                       **get_default(
                                                           selfCost[key_string],
                                                           f"self_{key_string}{i}",
                                                           need_refresh=True))
            with col3:
                key_string = "stay"
                key_name = "自费项目停留时间"
                selfCost[key_string] = st.text_input(key_name,
                                                       **get_default(
                                                           selfCost[key_string],
                                                           f"self_{key_string}{i}",
                                                           need_refresh=True))
            with col4:
                key_string = "address"
                key_name = "自费项目地址"
                selfCost[key_string] = st.text_input(key_name,
                                                       **get_default(
                                                           selfCost[key_string],
                                                           f"self_{key_string}{i}",
                                                           need_refresh=True))
            with col5:
                key_string = "remark"
                key_name = "自费项目备注"
                selfCost[key_string] = st.text_input(key_name,
                                                       **get_default(
                                                           selfCost[key_string],
                                                           f"self_{key_string}{i}",
                                                           need_refresh=True))
            with col6:
                st.button("❌", key=f"del_self{i}", on_click=del_self_cost, args=(i,))
        st.button("添加自费项目", on_click=add_self_cost)

    key_string = "shopContent"
    key_name = "购物项目介绍"
    st.session_state.multi_level_dict["cost"][key_string] = st.text_input(key_name,
                                                                          **get_default(
                                                                              st.session_state.multi_level_dict[
                                                                                  "cost"][key_string],
                                                                              key_string))

    col1, col2 = st.columns([1, 30])
    with col1:
        st.empty()
    with col2:
        shops = st.session_state.multi_level_dict["cost"]["shops"]
        for i, shop in enumerate(shops):
            col1, col2, col3, col4, col5, col6 = st.columns([3, 3, 3, 3, 3, 1])
            with col1:
                key_string = "shopName"
                key_name = "购物项目名称"
                shop[key_string] = st.text_input(key_name,
                                                     **get_default(
                                                         shop[key_string],
                                                         f"shop_{key_string}{i}",
                                                         need_refresh=True))
            with col2:
                key_string = "shopProduct"
                key_name = "购物项目可选产品"
                shop[key_string] = st.text_input(key_name,
                                                     **get_default(
                                                         shop[key_string],
                                                         f"shop_{key_string}{i}",
                                                         need_refresh=True))
            with col3:
                key_string = "stay"
                key_name = "购物项目停留时间"
                shop[key_string] = st.text_input(key_name,
                                                     **get_default(
                                                         shop[key_string],
                                                         f"shop_{key_string}{i}",
                                                         need_refresh=True))
            with col4:
                key_string = "address"
                key_name = "购物项目地址"
                shop[key_string] = st.text_input(key_name,
                                                     **get_default(
                                                         shop[key_string],
                                                         f"shop_{key_string}{i}",
                                                         need_refresh=True))
            with col5:
                key_string = "remark"
                key_name = "购物项目备注"
                shop[key_string] = st.text_input(key_name,
                                                     **get_default(
                                                         shop[key_string],
                                                         f"shop_{key_string}{i}",
                                                         need_refresh=True))
            with col6:
                st.button("❌", key=f"del_shop{i}", on_click=del_shop, args=(i,))
        st.button("添加购物项目", on_click=add_shop)

# 行程信息
if st.session_state.current_tab == 5:
    keys = [FormItemModel(key="title", name="行程标题"),
            FormItemModel(key="content", name="行程介绍")]

    trips = st.session_state.multi_level_dict["trips"]
    for i, trip in enumerate(trips):
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"第{i + 1}天行程")
            trip["tripDay"] = i + 1
        with col2:
            st.button("❌", key=f"del_trip{i}", on_click=del_trip, args=(i,))

        for item in keys:
            key_string = item.key
            key_name = item.name
            trip[key_string] = st.text_input(key_name,
                                             **get_default(
                                                 trip[key_string],
                                                 f"{key_string}{i}",
                                                 need_refresh=True))

        col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
        with col1:
            key_string = "breakfast"
            key_name = "包含早餐"
            default_dict = get_default(trip[key_string], f"{key_string}{i}", need_refresh=True)
            default_value = default_dict["value"]
            if default_value == 1:
                default_dict["value"] = True
            else:
                default_dict["value"] = False
            checkbox_value = st.checkbox(key_name, **default_dict)
            trip[key_string] = 1 if checkbox_value else 0
        with col2:
            key_string = "lunch"
            key_name = "包含午餐"
            default_dict = get_default(trip[key_string], f"{key_string}{i}", need_refresh=True)
            default_value = default_dict["value"]
            if default_value == 1:
                default_dict["value"] = True
            else:
                default_dict["value"] = False
            checkbox_value = st.checkbox(key_name, **default_dict)
            trip[key_string] = 1 if checkbox_value else 0
        with col3:
            key_string = "dinner"
            key_name = "包含晚餐"
            default_dict = get_default(trip[key_string], f"{key_string}{i}", need_refresh=True)
            default_value = default_dict["value"]
            if default_value == 1:
                default_dict["value"] = True
            else:
                default_dict["value"] = False
            checkbox_value = st.checkbox(key_name, **default_dict)
            trip[key_string] = 1 if checkbox_value else 0

        col1, col2 = st.columns([1, 30])
        with col1:
            st.empty()
        with col2:
            hotels = trip["hotels"]
            for j, hotel in enumerate(hotels):

                col1, col2, col3 = st.columns([15, 15, 1])
                with col1:
                    key_string = "name"
                    key_name = "酒店名称"
                    hotel[key_string] = st.text_input(key_name,
                                                      **get_default(
                                                          hotel[key_string],
                                                          f"hotel_{key_string}_{i}_{j}",
                                                          need_refresh=True))
                with col2:
                    key_string = "star"
                    key_name = "酒店星级(一星到五星)"
                    hotel[key_string] = st.text_input(key_name,
                                                      **get_default(
                                                          hotel[key_string],
                                                          f"hotel_{key_string}_{i}_{j}",
                                                          need_refresh=True))
                with col3:
                    st.button("❌", key=f"del_hotel_{i}_{j}", on_click=del_hotel, args=(i,j))

            st.button("添加酒店", key=f"add_hotel{i}", on_click=add_hotel, args=(i,))

        col1, col2 = st.columns([1, 30])
        with col1:
            st.empty()
        with col2:
            traffics = trip["scheduleTraffics"]
            for j, traffic in enumerate(traffics):
                col1, col2, col3, col4, col5, col6 = st.columns([6, 6, 6, 6, 6, 1])

                with col1:
                    key_string = "trafficType"
                    key_name = "交通方式"
                    traffic[key_string] = st.text_input(key_name,
                                                        **get_default(
                                                            traffic[key_string],
                                                            f"traffic_{key_string}_{i}_{j}",
                                                            need_refresh=True))

                with col2:
                    key_string = "departure"
                    key_name = "出发地"
                    traffic[key_string] = st.text_input(key_name,
                                                        **get_default(
                                                            traffic[key_string],
                                                            f"traffic_{key_string}_{i}_{j}",
                                                            need_refresh=True))
                with col3:
                    key_string = "departureTime"
                    key_name = "出发时间"
                    traffic[key_string] = st.text_input(key_name,
                                                        **get_default(
                                                            traffic[key_string],
                                                            f"traffic_{key_string}_{i}_{j}",
                                                            need_refresh=True))

                with col4:
                    key_string = "destination"
                    key_name = "目的地"
                    traffic[key_string] = st.text_input(key_name,
                                                        **get_default(
                                                            traffic[key_string],
                                                            f"traffic_{key_string}_{i}_{j}",
                                                            need_refresh=True))
                with col5:
                    key_string = "arrivalTime"
                    key_name = "到达时间"
                    traffic[key_string] = st.text_input(key_name,
                                                        **get_default(
                                                            traffic[key_string],
                                                            f"traffic_{key_string}_{i}_{j}",
                                                            need_refresh=True))
                with col6:
                    st.button("❌", key=f"del_traffic_{i}_{j}", on_click=del_traffic, args=(i,j))

            st.button("添加交通信息", key=f"add_traffic{i}", on_click=add_traffic, args=(i,))

        col1, col2 = st.columns([1, 30])
        with col1:
            st.empty()
        with col2:
            scenes = trip["scenes"]
            for j, scene in enumerate(scenes):
                col1, col2, col3, col4 = st.columns([10, 10, 10, 1])
                with col1:
                    key_string = "name"
                    key_name = "景点名称"
                    scene[key_string] = st.text_input(key_name,
                                                      **get_default(
                                                          scene[key_string],
                                                          f"scene_{key_string}_{i}_{j}",
                                                          need_refresh=True))
                with col2:
                    key_string = "consumingTime"
                    key_name = "停留时间"
                    scene[key_string] = st.text_input(key_name,
                                                      **get_default(
                                                          scene[key_string],
                                                          f"scene_{key_string}_{i}_{j}",
                                                          need_refresh=True))
                with col3:
                    key_string = "description"
                    key_name = "景点介绍"
                    scene[key_string] = st.text_input(key_name,
                                                      **get_default(
                                                          scene[key_string],
                                                          f"scene_{key_string}_{i}_{j}",
                                                          need_refresh=True))
                with col4:
                    st.button("❌", key=f"del_scene_{i}_{j}", on_click=del_scene, args=(i,j))
            st.button("添加景点", key=f"add_scene{i}", on_click=add_scene, args=(i,))

    st.button("添加行程", on_click=add_trip)


st.empty()
st.divider()  # 插入一个水平分割线
st.empty()

col1, col2, col3 = st.columns([1, 5, 1])

# 根据点击状态执行对应操作
with col1:
    if st.session_state.current_tab > 0:
        st.button("上一页", on_click=on_previous_page_click)

with col3:
    if st.session_state.current_tab < 5:
        st.button("下一页", on_click=on_next_page_click)
    else:
        if not st.session_state.confirm:
            st.button("完成", on_click=on_finish_click)
        else:
            st.warning("确定要上传么？")
            st.button("确定", on_click=on_confirm_click)


# 左侧显示 JSON 数据
st.sidebar.json(st.session_state.multi_level_dict)

st.session_state.refresh_event = False
