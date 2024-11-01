import streamlit as st

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

if "refresh_event" not in st.session_state:
    st.session_state.refresh_event = False

if "current_tab" not in st.session_state:
    st.session_state.current_tab = 0

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


def refresh():
    st.session_state.refresh_event = True
    st.rerun()


def get_default(cache, key, need_refresh=False):
    if need_refresh and st.session_state.refresh_event:
        value = cache
    else:
        value = st.session_state.get(key, cache)
    return {
        "value": value,
        "key": key
    }


# 产品详情
if st.session_state.current_tab == 0:
    st.subheader("产品详情")
    keys = [ {"key": "productTitle", "name": "产品名称"}, 
            {"key": "productSubtitle", "name": "产品副标题"},
            {"key": "departureCountryName", "name": "出发国家名字"},
            {"key": "departureProvinceNam", "name": "出发省份"},
            {"key": "departureCityName", "name": "出发城市名字"},
            {"key": "returnCityName", "name": "返回城市名字"},
            {"key": "childAgeBegin", "name": "儿童年龄标准区间开始值"},
            {"key": "childAgeEnd", "name": "儿童年龄标准区间结束值"},
            {"key": "childHeightBegin", "name": "儿童身高标准区间开始值"},
            {"key": "childHeightEnd", "name": "儿童身高标准区间结束值"},
            {"key": "childHasTraffic", "name": "儿童价格是否含大交通"},
            {"key": "childHasBed", "name": "儿童价是否含床"},
            {"key": "childRule", "name": "儿童标准说明"},
            {"key": "insuranceIncluded", "name": "是否包含保险"}
        ]
    
    for key in keys:
        st.session_state.multi_level_dict["product"][key['key']] = st.text_input(key['name'],
                                                                                 **get_default(
                                                                                     st.session_state.multi_level_dict[
                                                                                         "product"][key['key']],
                                                                                     key['key']))

    # 动态添加和删除列表输入框
    dests = st.session_state.multi_level_dict["product"]["dests"]

    for i, dest in enumerate(dests):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"目的地{i+1}")
        with col2:
            if st.button("❌", key=f"del_dests{i}"):
                if len(dests) > 1:
                    del dests[i]
                else:
                    st.warning("至少需要一个目的地。")
                refresh()    
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
        
    if st.button("添加目的地"):
        dests.append({"countryName": "", "destCityName": "", "destProvinceName": ""})
        st.rerun()

# 线路信息
if st.session_state.current_tab == 1:
    st.subheader("线路信息")
    st.session_state.multi_level_dict["line"]["lineTitle"] = st.text_input("线路标题",
                                                                           **get_default(
                                                                               st.session_state.multi_level_dict[
                                                                                   "line"]["lineTitle"],
                                                                               "lineTitle"))
    st.session_state.multi_level_dict["line"]["lineSimpleTitle"] = st.text_input("线路简标题",
                                                                                 **get_default(
                                                                                     st.session_state.multi_level_dict[
                                                                                         "line"]["lineSimpleTitle"],
                                                                                     "lineSimpleTitle"))
    st.session_state.multi_level_dict["line"]["tripDays"] = st.text_input("行程天数",
                                                                          **get_default(
                                                                              st.session_state.multi_level_dict[
                                                                                  "line"]["tripDays"],
                                                                              "tripDays"))
    st.session_state.multi_level_dict["line"]["tripNight"] = st.text_input("行程夜数",
                                                                           **get_default(
                                                                               st.session_state.multi_level_dict[
                                                                                   "line"]["tripNight"],
                                                                               "tripNight"))

# 成团信息
if st.session_state.current_tab == 2:
    st.subheader("成团信息")
    st.session_state.multi_level_dict["cal"]["channelPut"]["adultSalePrice"] = st.text_input("成人销售价格",
                                                                                             **get_default(
                                                                                                 st.session_state.multi_level_dict[
                                                                                                     "cal"][
                                                                                                     "channelPut"][
                                                                                                     "adultSalePrice"],
                                                                                                 "adultSalePrice"))
    st.session_state.multi_level_dict["cal"]["channelPut"]["childSalePrice"] = st.text_input("儿童销售价格",
                                                                                             **get_default(
                                                                                                 st.session_state.multi_level_dict[
                                                                                                     "cal"][
                                                                                                     "channelPut"][
                                                                                                     "childSalePrice"],
                                                                                                 "childSalePrice"))
    st.session_state.multi_level_dict["cal"]["departDate"] = st.text_input("出发日期",
                                                                           **get_default(
                                                                               st.session_state.multi_level_dict[
                                                                                   "cal"][
                                                                                   "departDate"],
                                                                               "departDate"))

# 消费信息
if st.session_state.current_tab == 3:
    st.subheader("消费信息")
    st.session_state.multi_level_dict["cost"]["costInclude"] = st.text_area("费用包含",
                                                                            **get_default(
                                                                                st.session_state.multi_level_dict[
                                                                                    "cost"][
                                                                                    "costInclude"],
                                                                                "costInclude"))
    st.session_state.multi_level_dict["cost"]["costExclude"] = st.text_area("费用不包含",
                                                                            **get_default(
                                                                                st.session_state.multi_level_dict[
                                                                                    "cost"][
                                                                                    "costExclude"],
                                                                                "costExclude"))
    st.session_state.multi_level_dict["cost"]["bookRule"] = st.text_area("预订规则",
                                                                         **get_default(
                                                                             st.session_state.multi_level_dict[
                                                                                 "cost"][
                                                                                 "bookRule"],
                                                                             "bookRule"))

# 行程信息
if st.session_state.current_tab == 4:
    trips = st.session_state.multi_level_dict["trips"]
    for i, trip in enumerate(trips):
        st.subheader(f"第{i+1}天行程")
        col1, col2, col3, col4 = st.columns([3, 3, 3, 1])
        with col1:
            trip["breakfast"] = st.checkbox(f"包含早餐", **get_default(trip["breakfast"], f"breakfast{i}",
                                                                               need_refresh=True))
        with col2:
            trip["lunch"] = st.checkbox(f"包含午餐", **get_default(trip["lunch"], f"lunch{i}",
                                                                           need_refresh=True))
        with col3:
            trip["dinner"] = st.checkbox(f"包含晚餐", **get_default(trip["dinner"], f"dinner{i}",
                                                                            need_refresh=True))
        with col4:
            if st.button(f"删除行程 {i + 1}"):
                if len(trips) > 1:
                    del trips[i]
                else:
                    st.warning("至少需要一个行程。")
                refresh()

    if st.button("添加行程"):
        trips.append({
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
        st.rerun()

st.empty()
st.divider()  # 插入一个水平分割线
st.empty()

col1, col2, col3 = st.columns([1, 5, 1])

with col1:
    if st.session_state.current_tab > 0:
        if st.button("上一页"):
            st.session_state.current_tab = st.session_state.current_tab - 1
            st.rerun()

with col3:
    if st.session_state.current_tab < 4:
        if st.button("下一页"):
            st.session_state.current_tab = st.session_state.current_tab + 1
            st.rerun()
    else:
        if st.button("完成"):
            # TODO 上传逻辑
            st.rerun()

# 左侧显示 JSON 数据
st.sidebar.json(st.session_state.multi_level_dict)

st.session_state.refresh_event = False
