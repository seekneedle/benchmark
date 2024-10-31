import streamlit as st

# 设置页面配置
st.set_page_config(
    page_title="填写产品信息",
    layout="wide",  # 设置页面布局为宽模式
)

# 初始化 session state 中的多级字典
if 'multi_level_dict' not in st.session_state:
    st.session_state.multi_level_dict = {
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
            "insurance": {
                "content": "",
                "name": "",
                "typeName": ""
            },
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
            "channelPut": {
                "adultSalePrice": "",
                "childSalePrice": "",
                "sellRemark": ""
            },
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

# 右侧选项卡
tabs = st.tabs(["产品详情", "线路信息", "成团信息", "消费信息", "旅行信息"])

# 产品详情
with tabs[0]:
    st.subheader("产品详情")
    st.session_state.multi_level_dict["product"]["productTitle"] = st.text_input("产品标题", st.session_state.multi_level_dict["product"]["productTitle"])
    st.session_state.multi_level_dict["product"]["productSubtitle"] = st.text_input("产品副标题", st.session_state.multi_level_dict["product"]["productSubtitle"])
    st.session_state.multi_level_dict["product"]["departureCityName"] = st.text_input("出发城市", st.session_state.multi_level_dict["product"]["departureCityName"])
    st.session_state.multi_level_dict["product"]["returnCityName"] = st.text_input("返回城市", st.session_state.multi_level_dict["product"]["returnCityName"])

# 线路信息
with tabs[1]:
    st.subheader("线路信息")
    st.session_state.multi_level_dict["line"]["lineTitle"] = st.text_input("线路标题", st.session_state.multi_level_dict["line"]["lineTitle"])
    st.session_state.multi_level_dict["line"]["lineSimpleTitle"] = st.text_input("线路简标题", st.session_state.multi_level_dict["line"]["lineSimpleTitle"])
    st.session_state.multi_level_dict["line"]["tripDays"] = st.text_input("行程天数", st.session_state.multi_level_dict["line"]["tripDays"])
    st.session_state.multi_level_dict["line"]["tripNight"] = st.text_input("行程夜数", st.session_state.multi_level_dict["line"]["tripNight"])

# 成团信息
with tabs[2]:
    st.subheader("成团信息")
    st.session_state.multi_level_dict["cal"]["channelPut"]["adultSalePrice"] = st.text_input("成人销售价格", st.session_state.multi_level_dict["cal"]["channelPut"]["adultSalePrice"])
    st.session_state.multi_level_dict["cal"]["channelPut"]["childSalePrice"] = st.text_input("儿童销售价格", st.session_state.multi_level_dict["cal"]["channelPut"]["childSalePrice"])
    st.session_state.multi_level_dict["cal"]["departDate"] = st.text_input("出发日期", st.session_state.multi_level_dict["cal"]["departDate"])

# 消费信息
with tabs[3]:
    st.subheader("消费信息")
    st.session_state.multi_level_dict["cost"]["costInclude"] = st.text_area("费用包含", st.session_state.multi_level_dict["cost"]["costInclude"])
    st.session_state.multi_level_dict["cost"]["costExclude"] = st.text_area("费用不包含", st.session_state.multi_level_dict["cost"]["costExclude"])
    st.session_state.multi_level_dict["cost"]["bookRule"] = st.text_area("预订规则", st.session_state.multi_level_dict["cost"]["bookRule"])

# 旅行信息
with tabs[4]:
    st.subheader("旅行信息")
    st.session_state.multi_level_dict["trips"][0]["title"] = st.text_input("行程标题", st.session_state.multi_level_dict["trips"][0]["title"])
    st.session_state.multi_level_dict["trips"][0]["content"] = st.text_area("行程内容", st.session_state.multi_level_dict["trips"][0]["content"])
    st.session_state.multi_level_dict["trips"][0]["breakfast"] = st.checkbox("包含早餐", st.session_state.multi_level_dict["trips"][0]["breakfast"])
    st.session_state.multi_level_dict["trips"][0]["lunch"] = st.checkbox("包含午餐", st.session_state.multi_level_dict["trips"][0]["lunch"])
    st.session_state.multi_level_dict["trips"][0]["dinner"] = st.checkbox("包含晚餐", st.session_state.multi_level_dict["trips"][0]["dinner"])

# 左侧显示 JSON 数据
st.sidebar.json(st.session_state.multi_level_dict)
