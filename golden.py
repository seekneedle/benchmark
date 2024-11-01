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


class FormItemModel:
    def __init__(self, key, name, type="text", options=["是", "否"]):
        self.key = key
        self.name = name
        self.type = type
        self.options = options

    def __repr__(self):
        return f"Model(key={self.key}, name={self.name}, type={self.type}), options={self.options}"


# 产品详情
if st.session_state.current_tab == 0:
    st.subheader("产品详情")
    keys = [FormItemModel(key="childAgeBegin", name="儿童年龄标准区间开始值"),
            FormItemModel(key="childAgeEnd", name="儿童年龄标准区间结束值"),
            FormItemModel(key="childHeightBegin", name="儿童身高标准区间开始值"),
            FormItemModel(key="childHeightEnd", name="儿童身高标准区间结束值"),
            FormItemModel(key="childHasTraffic", name="儿童价格是否含大交通", type="select"),
            FormItemModel(key="childHasBed", name="儿童价是否含床", type="select"),
            FormItemModel(key="childRule", name="儿童标准说明"),
            FormItemModel(key="insuranceIncluded", name="是否包含保险", type="select"),
            FormItemModel(key="productTitle", name="产品名称"),        
            FormItemModel(key="productSubtitle", name="产品副标题"),
            FormItemModel(key="departureCountryName", name="出发国家名字"),
            FormItemModel(key="departureProvinceNam", name="出发省份"),
            FormItemModel(key="departureCityName", name="出发城市名字"),
            FormItemModel(key="returnCityName", name="返回城市名字")]

    for item in keys:
        key_string = item.key
        key_name = item.name
        key_type = item.type
        key_options = item.options

        if key_type == "select":
            st.session_state.multi_level_dict["product"][key_string] = st.radio(key_name,
                                                                                options=key_options,
                                                                                index=0 if get_default(
                                                                                    st.session_state.multi_level_dict[
                                                                                        "product"].get(key_string,
                                                                                                       None),
                                                                                    key_string) == "是" else 1)
        else:
            st.session_state.multi_level_dict["product"][key_string] = st.text_input(key_name,
                                                                                     **get_default(
                                                                                         st.session_state.multi_level_dict[
                                                                                             "product"][key_string],
                                                                                         key_string))

    # 动态添加和删除列表输入框
    dests = st.session_state.multi_level_dict["product"]["dests"]
    for i, dest in enumerate(dests):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"目的地{i + 1}")
        with col2:
            if st.button("❌", key=f"del_dests{i}"):
                if len(dests) > 1 and i < len(dests):
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

    insurances = st.session_state.multi_level_dict["product"]["insurance"]
    for i, insurance in enumerate(insurances):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"保险信息{i+1}")
        with col2:
            if st.button("❌", key=f"del_insurances{i}"):
                if len(insurances) > 1:
                    del insurances[i]
                else:
                    st.warning("至少需要一个保险信息。")
                refresh()    
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
    if st.button("添加保险信息"):
        insurances.append({"content": "", "name": "", "typeName": ""})
        st.rerun()
    
    themes = st.session_state.multi_level_dict["product"]["themes"]
    for i, theme in enumerate(themes):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"产品主题{i+1}")
        with col2:
            if st.button("❌", key=f"del_themes{i}"):
                if len(themes) > 1:
                    del themes[i]
                else:
                    st.warning("至少需要一个产品主题。")
                refresh()    
        theme["name"] = st.text_input(f"主题名称", **get_default(theme["name"], f"theme_name{i}",
                                                                       need_refresh=True))
    if st.button("添加产品主题"):
        themes.append({"name": ""})
        st.rerun()
        
    tags = st.session_state.multi_level_dict["product"]["tags"]
    for i, tag in enumerate(tags):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"产品标签{i+1}")
        with col2:
            if st.button("❌", key=f"del_tags{i}"):
                if len(tags) > 1:
                    del tags[i]
                else:
                    st.warning("至少需要一个产品主题。")
                refresh()    
        tag["name"] = st.text_input(f"标签名称", **get_default(tag["name"], f"tag_name{i}",
                                                                       need_refresh=True))
    if st.button("添加产品标签"):
        tags.append({"name": ""})
        st.rerun()
    
    markets = st.session_state.multi_level_dict["product"]["markets"]
    for i, market in enumerate(markets):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"营销标签{i+1}")
        with col2:
            if st.button("❌", key=f"del_markets{i}"):
                if len(markets) > 1:
                    del markets[i]
                else:
                    st.warning("至少需要一个产品主题。")
                refresh()    
        market["name"] = st.text_input(f"营销标签名称", **get_default(market["name"], f"market_name{i}",
                                                                       need_refresh=True))
    if st.button("添加营销标签"):
        markets.append({"name": ""})
        st.rerun()

# 线路信息
if st.session_state.current_tab == 1:
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
            st.session_state.multi_level_dict["line"][key_string] = st.radio(key_name,
                                                                                options=key_options,
                                                                                index=0 if get_default(st.session_state.multi_level_dict["line"].get(key_string, None), key_string) == "是" else 1 ) 
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
    num_columns = 5  # 你可以根据需要调整列数

    backAirports = st.session_state.multi_level_dict["line"]["backAirports"]    
    for i, airport in enumerate(backAirports):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"返程航班信息{i+1}")
        with col2:
            if st.button("❌", key=f"del_backAirports{i}"):
                if len(backAirports) > 1:
                    del backAirports[i]
                else:
                    st.warning("至少需要一个返程航班信息。")
                refresh()
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
                
    if st.button("添加返程航班信息"):
        backAirports.append(default_airport_value)
        st.rerun()
    
    goAirports = st.session_state.multi_level_dict["line"]["goAirports"]
    for i, airport in enumerate(goAirports):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"去程航班信息{i+1}")
        with col2:
            if st.button("❌", key=f"del_goAirports{i}"):
                if len(goAirports) > 1:
                    del goAirports[i]
                else:
                    st.warning("至少需要一个去程航班信息。")
                refresh()
        columns = st.columns(num_columns)
        for j, item in enumerate(airports_keys):
            key_string = item.key
            key_name = item.name
            key_type = item.type
            key_options = item.options

            col_index = j % num_columns
            with columns[col_index]:
                airport[key_string] = st.text_input(key_name,
                                                    **get_default(airport[key_string], f"goAirports_{key_name}{i}", need_refresh=True))
                
    if st.button("添加去程航班信息"):
        goAirports.append(default_airport_value)
        st.rerun()
    
    passCities_keys = [FormItemModel(key="countryName", name="途径国家名称"),
            FormItemModel(key="provinceName", name="途径省份名称"),
            FormItemModel(key="cityName", name="途径城市名称")]
    default_passCities_value = {
            "countryName": "",
            "provinceName": "",
            "cityName": ""}
    passCities = st.session_state.multi_level_dict["line"]["passCities"]
    for i, city in enumerate(passCities):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"途经城市{i+1}")
        with col2:
            if st.button("❌", key=f"del_passCities{i}"):
                if len(passCities) > 1:
                    del passCities[i]
                else:
                    st.warning("至少需要一个途经城市。")
                refresh()
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
                
    if st.button("添加途经城市"):
        passCities.append(default_passCities_value)
        st.rerun()

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
    default_visa_value = {
            "content": "",
            "country": "",
            "district": "",
            "freeVisa": "",
            "signPlace": ""}
    visas = st.session_state.multi_level_dict["line"]["visaBasic"]['visas']
    for i, visa in enumerate(visas):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(f"签证信息{i+1}")
        with col2:
            if st.button("❌", key=f"del_visa{i}"):
                if len(visas) > 1:
                    del visas[i]
                else:
                    st.warning("至少需要一个签证信息。")
                refresh()
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

    if st.button("添加签证信息"):
        visas.append(default_visa_value)
        st.rerun()

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
                if st.button("❌", key=f"del_return{i}"):
                    if len(lineReturns) > 0 and i < len(lineReturns):
                        del lineReturns[i]
                    else:
                        st.warning("没有可删除退费规则。")
                    refresh()
        if st.button("添加退费规则"):
            lineReturns.append({
                "begin": "",
                "cost": "",
                "end": ""
            })
            st.rerun()

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
                if st.button("❌", key=f"del_self{i}"):
                    if len(selfCosts) > 0 and i < len(selfCosts):
                        del selfCosts[i]
                    else:
                        st.warning("没有可删除自费项目。")
                    refresh()
        if st.button("添加自费项目"):
            selfCosts.append({
                "address": "",
                "fee": "",
                "name": "",
                "remark": "",
                "stay": ""
            })
            st.rerun()

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
                if st.button("❌", key=f"del_shop{i}"):
                    if len(shops) > 0 and i < len(shops):
                        del shops[i]
                    else:
                        st.warning("没有可删除购物项目。")
                    refresh()
        if st.button("添加购物项目"):
            shops.append({
                "address": "",
                "shopProduct": "",
                "shopName": "",
                "remark": "",
                "stay": ""
            })
            st.rerun()

# 行程信息
if st.session_state.current_tab == 4:
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
            if st.button("❌", key=f"del_trip{i}"):
                if len(trips) > 1 and i < len(trips):
                    del trips[i]
                else:
                    st.warning("至少需要一个行程。")
                refresh()

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
                                                          f"hotel_{key_string}{i}{j}",
                                                          need_refresh=True))
                with col2:
                    key_string = "star"
                    key_name = "酒店星级(一星到五星)"
                    hotel[key_string] = st.text_input(key_name,
                                                      **get_default(
                                                          hotel[key_string],
                                                          f"hotel_{key_string}{i}{j}",
                                                          need_refresh=True))
                with col3:
                    if st.button("❌", key=f"del_hotel{i}{j}"):
                        if len(hotels) > 0 and j < len(hotels):
                            del hotels[j]
                        else:
                            st.warning("没有可删除酒店。")
                        refresh()

            if st.button("添加酒店", key=f"add_hotel{i}"):
                hotels.append({
                    "name": "",
                    "star": ""
                })
                st.rerun()

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
                                                            f"traffic_{key_string}{i}{j}",
                                                            need_refresh=True))

                with col2:
                    key_string = "departure"
                    key_name = "出发地"
                    traffic[key_string] = st.text_input(key_name,
                                                        **get_default(
                                                            traffic[key_string],
                                                            f"traffic_{key_string}{i}{j}",
                                                            need_refresh=True))
                with col3:
                    key_string = "departureTime"
                    key_name = "出发时间"
                    traffic[key_string] = st.text_input(key_name,
                                                        **get_default(
                                                            traffic[key_string],
                                                            f"traffic_{key_string}{i}{j}",
                                                            need_refresh=True))

                with col4:
                    key_string = "destination"
                    key_name = "目的地"
                    traffic[key_string] = st.text_input(key_name,
                                                        **get_default(
                                                            traffic[key_string],
                                                            f"traffic_{key_string}{i}{j}",
                                                            need_refresh=True))
                with col5:
                    key_string = "arrivalTime"
                    key_name = "到达时间"
                    traffic[key_string] = st.text_input(key_name,
                                                        **get_default(
                                                            traffic[key_string],
                                                            f"traffic_{key_string}{i}{j}",
                                                            need_refresh=True))
                with col6:
                    if st.button("❌", key=f"del_traffic{i}{j}"):
                        if len(traffics) > 0 and j < len(traffics):
                            del traffics[j]
                        else:
                            st.warning("没有可删除交通方式。")
                        refresh()

            if st.button("添加交通信息", key=f"add_traffic{i}"):
                traffics.append({
                    "departure": "",
                    "departureTime": "",
                    "destination": "",
                    "arrivalTime": "",
                    "trafficType": ""
                })
                st.rerun()

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
                                                          f"scene_{key_string}{i}{j}",
                                                          need_refresh=True))
                with col2:
                    key_string = "consumingTime"
                    key_name = "停留时间"
                    scene[key_string] = st.text_input(key_name,
                                                      **get_default(
                                                          scene[key_string],
                                                          f"scene_{key_string}{i}{j}",
                                                          need_refresh=True))
                with col3:
                    key_string = "description"
                    key_name = "景点介绍"
                    scene[key_string] = st.text_input(key_name,
                                                      **get_default(
                                                          scene[key_string],
                                                          f"scene_{key_string}{i}{j}",
                                                          need_refresh=True))
                with col4:
                    if st.button("❌", key=f"del_scene{i}{j}"):
                        if len(scenes) > 0 and j < len(scenes):
                            del scenes[j]
                        else:
                            st.warning("没有可删除景点。")
                        refresh()
            if st.button("添加景点", key=f"add_scene{i}"):
                scenes.append({
                    "name": "",
                    "description": "",
                    "consumingTime": ""
                })
                st.rerun()

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
