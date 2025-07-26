import re
# def extract_repeat_submit_token(html_text: str) -> str:
#     """提取 REPEAT_SUBMIT_TOKEN """
#     match = re.search(r"globalRepeatSubmitToken\s*=\s*'(.+?)'", html_text)
#     return match.group(1) if match else ""
#
# def extract_key_check_isChange(html_text: str) -> str:
#     """提取 key_check_isChange """
#     match = re.search(r"'key_check_isChange'\s*:\s*'(.+?)'", html_text)
#     return match.group(1) if match else ""
#
# def extract_train_location(html_text: str) -> str:
#     """提取 train_location """
#     match = re.search(r"'train_location'\s*:\s*'(.+?)'", html_text)
#     return match.group(1) if match else ""
#
# def decode_passenger_ticket_str(encoded_str: str) -> str:
#     """解析 passengerTicketStr 参数为原始字符串"""
#     return urllib.parse.unquote(encoded_str)
#
# def parse_ticket_fields(ticket_str: str) -> list:
#     """拆解 passengerTicketStr 字段为列表"""
#     return ticket_str.split(",")

def html_prase(html_text: str):
    """提取 REPEAT_SUBMIT_TOKEN """
    repeatsubmittoken = re.search(r"globalRepeatSubmitToken\s*=\s*'(.+?)'", html_text)
    """提取 key_check_isChange """
    keycheckisChange = re.search(r"'key_check_isChange'\s*:\s*'(.+?)'", html_text)
    """提取 train_location   一搬为H1 """
    train_location = re.search(r"'train_location'\s*:\s*'(.+?)'}", html_text)
    """提取 TicketStr """
    TicketStr = re.search(r"'leftTicketStr':'(.*?)'", html_text)
    """提取 train_no """
    train_no = re.search(r"'train_no':'(.*?)'", html_text)


    repeatsubmittoken = repeatsubmittoken.group(1) if repeatsubmittoken else ""
    keycheckisChange = keycheckisChange.group(1) if keycheckisChange else ""
    train_location = train_location.group(1) if train_location else ""
    TicketStr = TicketStr.group(1) if TicketStr else ""
    train_no = train_no.group(1) if train_no else ""


    return repeatsubmittoken ,keycheckisChange,train_location,TicketStr,train_no


if __name__ == '__main__': # 测试
    html = '''
    HTTP/1.1 200 OK
Date: Fri, 25 Jul 2025 09:38:38 GMT
Content-Type: text/html;charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
ct: C1_217_115_9
Content-Language: zh-CN
Content-Encoding: gzip
X-Via: 1.1 PS-CGO-01J5772:17 (Cdn Cache Server V2.0)
x-ws-request-id: 6883509e_PS-CGO-01J5772_28582-9679
X-Cdn-Src-Port: 5955

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>中国铁路12306网站</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/otn/resources/css/validation.css" rel="stylesheet" />
<link href="/otn/resources/merged/common_css.css?cssVersion=1.9093" rel="stylesheet" />
<link rel="icon" href="/otn/resources/images/ots/favicon.ico" type="image/x-icon" />
<link rel="shortcut icon" href="/otn/resources/images/ots/favicon.ico" type="image/x-icon" />
<script>
    /*<![CDATA[*/
    var ctx ='/otn/';
    var globalRepeatSubmitToken = 'e6e5b0546368c14c47e07c915c08963f';
    var global_lang = 'zh_CN';
    var sessionInit = '\u5F20\u68EE\u6797';
    var isShowNotice = null;
    var CLeftTicketUrl = null;
    var isTestFlow = null;
    var isMobileCheck = null;
    var passport_appId = null;
    var passport_login = null;
    var passport_captcha = null;
    var passport_authuam = null;
    var passport_captcha_check = null;
    var passport_authclient = null;
    var passport_loginPage = null;
    var passport_okPage = null;
    var passport_proxy_captcha =  null;
    /*]]>*/
  </script>
<script src="/otn/resources/merged/common_js.js?scriptVersion=1.94029" type="text/javascript"></script>
<!-- js i18n -->
<!-- jquery validation i18n -->
<!-- head and footer -->
<link href="/otn/resources/merged/passengerInfo_css.css?cssVersion=1.9093" rel="stylesheet" />
<script type="text/javascript" src="/otn/resources/merged/passengerInfo_js.js?scriptVersion=1.94029" xml:space="preserve"></script>
</head>
<script src="/otn/dynamicJs/opisvxm" type="text/javascript" xml:space="preserve"></script>
<link href="/otn/resources/fonts/iconfont.css" rel="stylesheet" />
<style type="text/css" xml:space="preserve">
  .nc_scale {
     height: 30px !important;
     background : rgb(243,194,129) !important;
  }
  .nc_scale span {
     height: 30px !important;
  }
</style>
<script xml:space="preserve">

/*<![CDATA[*/
 var id_type_code = '1';
 var isDw='N';
 var isWaw='0';
 var checkTrain=null;
 var isLimitTran='N';
 var CHANGETSFLAG=null;
 var canInsurance=true;
 var queryOrderWaitTimeInterval='3000';
 var canChooseSeats=null;
 var choose_Seats=null;
 var canChooseBeds=null;
 var isCanChooseMid=null;
 var trms_train_flag=null;
 var trmsDetail=null;
 var trmsDetailAll=null;
 var price_info_trms=null;
 var if_check_slide_passcode='0';
 var if_check_slide_passcode_token=null;
 /*]]>*/
</script>
<script type="text/javascript" charset="utf-8" src="https://g.alicdn.com/sd/ncpc/nc.js?t=2019121212" xml:space="preserve"></script>
<script xml:space="preserve">
    var json_ua;
</script>
<script type="text/javascript" async="async" src="https://mobile.12306.cn/otsmobile/antcaptcha/ua_rds.js?t=2025072517" xml:space="preserve"></script>
<body id="body_id"><div id="dialog_fczk" style="display: none;"><div class="mark"></div>
<div class="up-box w600"><div class="up-box-hd">温馨提示<a href="javascript:" id="dialog_fczk_close" shape="rect">关闭</a>
</div>
<div class="up-box-bd"><div class="up-con clearfix"><span class="icon i-opt"></span>
<div class="r-txt"><div class="tit">购买往返优惠票的旅客，不得单独办理往程车票的退票业务。是否继续?</div>
</div>
</div>
<div class="lay-btn"><a href="javascript:" id="dialog_fczk_cancel" class="btn92" shape="rect">取消</a>
<a href="javascript:" id="dialog_fczk_ok" class="btn92s" shape="rect">确认</a>
</div>
</div>
</div>
</div>
<div id="dialog_smoker" style="display: none;"><div class="mark"></div>
<div class="up-box w600"><div class="up-box-hd">温馨提示<a href="javascript:" id="dialog_smoker_close" shape="rect">关闭</a>
</div>
<div class="up-box-bd"><div class="up-con clearfix"><span class="icon i-opt"></span>
<div class="r-txt"><div class="tit" id="dialog_smoker_msg"></div>
</div>
</div>
<div class="lay-btn"><a href="javascript:" id="dialog_smoker_cancel" class="btn92" shape="rect">取消</a>
<a href="javascript:" id="dialog_smoker_ok" class="btn92s" shape="rect">确定</a>
</div>
</div>
</div>
</div>
<div id="dialog_xsertcj" style="display: none;"><div class="mark"></div>
<div class="up-box w600"><div class="up-box-hd">温馨提示<a href="javascript:" id="dialog_xsertcj_close" shape="rect">关闭</a>
</div>
<div class="up-box-bd"><div class="up-con clearfix"><span class="icon i-opt"></span>
<div class="r-txt"><div class="tit" id="dialog_xsertcj_msg"></div>
</div>
</div>
<div class="lay-btn"><a href="javascript:" id="dialog_xsertcj_cancel" class="btn92" shape="rect">取消</a>
<a href="javascript:" id="dialog_xsertcj_ok" class="btn92s" shape="rect">确认</a>
</div>
</div>
</div>
</div>
<div id="trms_dg" style="display: none;"><div class="mark"></div>
<div class="up-box w600"><div class="up-box-hd">温馨提示<a href="javascript:" id="trms_dg_close" shape="rect">关闭</a>
</div>
<div class="up-box-bd"><div class="up-con clearfix"><span class="icon i-opt"></span>
<div class="r-txt"><div class="tit" id="trms_dg_msg"></div>
</div>
</div>
<div class="lay-btn"><a href="javascript:" id="trms_dg_cancel" class="btn92" shape="rect">取消</a>
<a href="javascript:" id="trms_dg_ok" class="btn92s" shape="rect">确认</a>
</div>
</div>
</div>
</div>
<div id="dialog_add" style="display: none;"><div class="mark"></div>
<div class="up-box" style="width:640px;"><div class="up-box-hd">新增乘客<a href="javascript:" id="dialog_add_close" shape="rect">关闭</a>
</div>
<div class="up-box-bd" style="padding:15px 10px;border:1px solid #298CCE;"><table class="per-ticket" style="margin-left:0px;"><tr><th style="text-align:center;" rowspan="1" colspan="1">票种</th>
<th style="text-align:center;" rowspan="1" colspan="1">姓名</th>
<th style="text-align:center;" rowspan="1" colspan="1">证件类型</th>
<th style="text-align:center;" rowspan="1" colspan="1">证件号码</th>
<th style="text-align:center;" rowspan="1" colspan="1">国家/地区</th>
</tr>
<tbody id="showaddpassenger"><tr><td rowspan="1" colspan="1"><select id="ptypeselect"></select>
</td>
<td rowspan="1" colspan="1"><div><input id="pname_value" class="inptxt w110" type="text" />
</div>
</td>
<td rowspan="1" colspan="1"><select id="typeselect" class="w110"></select>
</td>
<td rowspan="1" colspan="1"><input id="pidno_value" class="inptxt w160" value="" type="text" />
</td>
<td rowspan="1" colspan="1"><select id="pcountry_value" class="w160"><option value="CN"><span>中国China</span>
</option>
<option value="AF"><span>阿富汗Afghanistan</span>
</option>
<option value="AL"><span>阿尔巴尼亚Albania</span>
</option>
<option value="DZ"><span>阿尔及利亚Algeria</span>
</option>
<option value="AD"><span>安道尔Andorra</span>
</option>
<option value="AO"><span>安哥拉Angola</span>
</option>
<option value="AG"><span>安提瓜和巴布达Antigua and Barbuda</span>
</option>
<option value="AR"><span>阿根廷Argentina</span>
</option>
<option value="AM"><span>亚美尼亚Armenia</span>
</option>
<option value="AU"><span>澳大利亚Australia</span>
</option>
<option value="AT"><span>奥地利Austria</span>
</option>
<option value="AZ"><span>阿塞拜疆Azerbaijan</span>
</option>
<option value="BS"><span>巴哈马Bahamas</span>
</option>
<option value="BH"><span>巴林Bahrain</span>
</option>
<option value="BD"><span>孟加拉国Bangladesh</span>
</option>
<option value="BB"><span>巴巴多斯Barbados</span>
</option>
<option value="BY"><span>白俄罗斯Belarus</span>
</option>
<option value="BE"><span>比利时Belgium</span>
</option>
<option value="BZ"><span>伯利兹Belize</span>
</option>
<option value="BJ"><span>贝宁Benin</span>
</option>
<option value="BT"><span>不丹Bhutan</span>
</option>
<option value="BO"><span>玻利维亚Bolivia</span>
</option>
<option value="BA"><span>波黑Bosnia and Herzegovina</span>
</option>
<option value="BW"><span>博茨瓦纳Botswana</span>
</option>
<option value="BR"><span>巴西Brazil</span>
</option>
<option value="BN"><span>文莱Brunei</span>
</option>
<option value="BG"><span>保加利亚Bulgaria</span>
</option>
<option value="BF"><span>布基纳法索Burkina Faso</span>
</option>
<option value="BI"><span>布隆迪Burundi</span>
</option>
<option value="KH"><span>柬埔寨Cambodia</span>
</option>
<option value="CM"><span>喀麦隆Cameroon</span>
</option>
<option value="CA"><span>加拿大Canada</span>
</option>
<option value="KY"><span>佛得角Cape Verde</span>
</option>
<option value="CF"><span>中非Central African Republic</span>
</option>
<option value="TD"><span>乍得Chad</span>
</option>
<option value="CL"><span>智利Chile</span>
</option>
<option value="CO"><span>哥伦比亚Colombia</span>
</option>
<option value="KM"><span>科摩罗Comoros</span>
</option>
<option value="CD"><span>刚果(金)Congo, Democratic Republic of</span>
</option>
<option value="CG"><span>刚果(布)Congo, Republic of</span>
</option>
<option value="CK"><span>库克群岛Cook Islands</span>
</option>
<option value="CR"><span>哥斯达黎加Costa Rica</span>
</option>
<option value="CI"><span>科特迪瓦Cote d’lvoire</span>
</option>
<option value="HR"><span>克罗地亚Croatia</span>
</option>
<option value="CU"><span>古巴Cuba</span>
</option>
<option value="CY"><span>塞浦路斯Cyprus</span>
</option>
<option value="CZ"><span>捷克Czech</span>
</option>
<option value="KP"><span>朝鲜DPRK</span>
</option>
<option value="DK"><span>丹麦Denmark</span>
</option>
<option value="DJ"><span>吉布提Djibouti</span>
</option>
<option value="DM"><span>多米尼克Dominica</span>
</option>
<option value="DO"><span>多米尼加Dominican Republic</span>
</option>
<option value="EC"><span>厄瓜多尔Ecuador</span>
</option>
<option value="EG"><span>埃及Egypt</span>
</option>
<option value="EV"><span>萨尔瓦多El Salvador</span>
</option>
<option value="GQ"><span>赤道几内亚Equatorial Guinea</span>
</option>
<option value="ER"><span>厄立特里亚Eritrea</span>
</option>
<option value="EE"><span>爱沙尼亚Estonia</span>
</option>
<option value="SZ"><span>斯威士兰Eswatini</span>
</option>
<option value="ET"><span>埃塞俄比亚Ethiopia</span>
</option>
<option value="FJ"><span>斐济Fiji</span>
</option>
<option value="FI"><span>芬兰Finland</span>
</option>
<option value="FR"><span>法国France</span>
</option>
<option value="GA"><span>加蓬Gabon</span>
</option>
<option value="GM"><span>冈比亚Gambia</span>
</option>
<option value="CE"><span>格鲁吉亚Georgia</span>
</option>
<option value="DE"><span>德国Germany</span>
</option>
<option value="GH"><span>加纳Ghana</span>
</option>
<option value="GR"><span>希腊Greece</span>
</option>
<option value="GL"><span>格林纳达Grenada</span>
</option>
<option value="GT"><span>危地马拉Guatemala</span>
</option>
<option value="GN"><span>几内亚Guinea</span>
</option>
<option value="GW"><span>几内亚比绍Guinea-Bissau</span>
</option>
<option value="GY"><span>圭亚那Guyana</span>
</option>
<option value="HT"><span>海地Haiti</span>
</option>
<option value="HN"><span>洪都拉斯Honduras</span>
</option>
<option value="HU"><span>匈牙利Hungary</span>
</option>
<option value="IS"><span>冰岛Iceland</span>
</option>
<option value="IN"><span>印度India</span>
</option>
<option value="ID"><span>印度尼西亚Indonesia</span>
</option>
<option value="IR"><span>伊朗Iran</span>
</option>
<option value="IQ"><span>伊拉克Iraq</span>
</option>
<option value="IE"><span>爱尔兰Ireland</span>
</option>
<option value="IL"><span>以色列Israel</span>
</option>
<option value="IT"><span>意大利Italy</span>
</option>
<option value="JM"><span>牙买加Jamaica</span>
</option>
<option value="JP"><span>日本Japan</span>
</option>
<option value="JO"><span>约旦Jordan</span>
</option>
<option value="KZ"><span>哈萨克斯坦Kazakhstan</span>
</option>
<option value="KE"><span>肯尼亚Kenya</span>
</option>
<option value="KI"><span>基里巴斯Kiribati</span>
</option>
<option value="KW"><span>科威特Kuwait</span>
</option>
<option value="KG"><span>吉尔吉斯斯坦Kyrgyzstan</span>
</option>
<option value="LA"><span>老挝Laos</span>
</option>
<option value="LV"><span>拉脱维亚Latvia</span>
</option>
<option value="LB"><span>黎巴嫩Lebanon</span>
</option>
<option value="LS"><span>莱索托Lesotho</span>
</option>
<option value="LR"><span>利比里亚Liberia</span>
</option>
<option value="LY"><span>利比亚Libya</span>
</option>
<option value="LI"><span>列支敦士登Liechtenstein</span>
</option>
<option value="LT"><span>立陶宛Lithuania</span>
</option>
<option value="LU"><span>卢森堡Luxembourg</span>
</option>
<option value="MG"><span>马达加斯加Madagascar</span>
</option>
<option value="MW"><span>马拉维Malawi</span>
</option>
<option value="MY"><span>马来西亚Malaysia</span>
</option>
<option value="MV"><span>马尔代夫Maldives</span>
</option>
<option value="ML"><span>马里Mali</span>
</option>
<option value="MT"><span>马耳他Malta</span>
</option>
<option value="MH"><span>马绍尔群岛Marshall Islands</span>
</option>
<option value="MR"><span>毛里塔尼亚Mauritania</span>
</option>
<option value="MU"><span>毛里求斯Mauritius</span>
</option>
<option value="MX"><span>墨西哥Mexico</span>
</option>
<option value="FM"><span>密克罗尼西亚联邦Micronesia</span>
</option>
<option value="MD"><span>摩尔多瓦Moldova</span>
</option>
<option value="MC"><span>摩纳哥Monaco</span>
</option>
<option value="MN"><span>蒙古Mongolia</span>
</option>
<option value="ME"><span>黑山Montenegro</span>
</option>
<option value="MA"><span>摩洛哥Morocco</span>
</option>
<option value="MZ"><span>莫桑比克Mozambique</span>
</option>
<option value="MM"><span>缅甸Myanmar</span>
</option>
<option value="NA"><span>纳米比亚Namibia</span>
</option>
<option value="NR"><span>瑙鲁Nauru</span>
</option>
<option value="NP"><span>尼泊尔Nepal</span>
</option>
<option value="NL"><span>荷兰Netherlands</span>
</option>
<option value="NZ"><span>新西兰New Zealand</span>
</option>
<option value="NI"><span>尼加拉瓜Nicaragua</span>
</option>
<option value="NE"><span>尼日尔Niger</span>
</option>
<option value="NG"><span>尼日利亚Nigeria</span>
</option>
<option value="NU"><span>纽埃Niue</span>
</option>
<option value="MK"><span>北马其顿North Macedonia</span>
</option>
<option value="NO"><span>挪威Norway</span>
</option>
<option value="OM"><span>阿曼Oman</span>
</option>
<option value="PK"><span>巴基斯坦Pakistan</span>
</option>
<option value="PW"><span>帕劳Palau</span>
</option>
<option value="BL"><span>巴勒斯坦Palestine</span>
</option>
<option value="PA"><span>巴拿马Panama</span>
</option>
<option value="PG"><span>巴布亚新几内亚Papua New Guinea</span>
</option>
<option value="PY"><span>巴拉圭Paraguay</span>
</option>
<option value="PE"><span>秘鲁Peru</span>
</option>
<option value="PH"><span>菲律宾Philippines</span>
</option>
<option value="PL"><span>波兰Poland</span>
</option>
<option value="PT"><span>葡萄牙Portugal</span>
</option>
<option value="QA"><span>卡塔尔Qatar</span>
</option>
<option value="KR"><span>韩国Republic of Korea</span>
</option>
<option value="RO"><span>罗马尼亚Romania</span>
</option>
<option value="RU"><span>俄罗斯Russia</span>
</option>
<option value="RW"><span>卢旺达Rwanda</span>
</option>
<option value="KN"><span>圣基茨和尼维斯Saint Kitts and Nevis</span>
</option>
<option value="LC"><span>圣卢西亚Saint Lucia</span>
</option>
<option value="VC"><span>圣文森特和格林纳丁斯Saint Vincent &amp; the Grenadines</span>
</option>
<option value="WS"><span>萨摩亚Samoa</span>
</option>
<option value="SM"><span>圣马力诺San Marino</span>
</option>
<option value="ST"><span>圣多美和普林西比Sao Tome and Principe</span>
</option>
<option value="SA"><span>沙特阿拉伯Saudi Arabia</span>
</option>
<option value="SN"><span>塞内加尔Senegal</span>
</option>
<option value="CS"><span>塞尔维亚Serbia</span>
</option>
<option value="SC"><span>塞舌尔Seychelles</span>
</option>
<option value="SL"><span>塞拉利昂Sierra Leone</span>
</option>
<option value="SG"><span>新加坡Singapore</span>
</option>
<option value="SK"><span>斯洛伐克Slovakia</span>
</option>
<option value="SI"><span>斯洛文尼亚Slovenia</span>
</option>
<option value="SB"><span>所罗门群岛Solomon Islands</span>
</option>
<option value="SO"><span>索马里Somalia</span>
</option>
<option value="ZA"><span>南非South Africa</span>
</option>
<option value="SS"><span>南苏丹South Sudan</span>
</option>
<option value="ES"><span>西班牙Spain</span>
</option>
<option value="LK"><span>斯里兰卡Sri Lanka</span>
</option>
<option value="SD"><span>苏丹Sudan</span>
</option>
<option value="SR"><span>苏里南Suriname</span>
</option>
<option value="SE"><span>瑞典Sweden</span>
</option>
<option value="CH"><span>瑞士Switzerland</span>
</option>
<option value="SY"><span>叙利亚Syria</span>
</option>
<option value="TJ"><span>塔吉克斯坦Tajikistan</span>
</option>
<option value="TZ"><span>坦桑尼亚Tanzania</span>
</option>
<option value="TH"><span>泰国Thailand</span>
</option>
<option value="TL"><span>东帝汶Timor-Leste</span>
</option>
<option value="TG"><span>多哥Togo</span>
</option>
<option value="TO"><span>汤加Tonga</span>
</option>
<option value="TT"><span>特立尼达和多巴哥Trinidad and Tobago</span>
</option>
<option value="TN"><span>突尼斯Tunisia</span>
</option>
<option value="TR"><span>土耳其Turkey</span>
</option>
<option value="TM"><span>土库曼斯坦Turkmenistan</span>
</option>
<option value="TV"><span>图瓦卢Tuvalu</span>
</option>
<option value="UG"><span>乌干达Uganda</span>
</option>
<option value="UA"><span>乌克兰Ukraine</span>
</option>
<option value="AE"><span>阿联酋United Arab Emirates</span>
</option>
<option value="GB"><span>英国United Kingdom</span>
</option>
<option value="UN"><span>联合国United Nations</span>
</option>
<option value="US"><span>美国United States of America</span>
</option>
<option value="UY"><span>乌拉圭Uruguay</span>
</option>
<option value="UZ"><span>乌兹别克斯坦Uzbekistan</span>
</option>
<option value="VU"><span>瓦努阿图Vanuatu</span>
</option>
<option value="VA"><span>梵蒂冈Vatican City State</span>
</option>
<option value="VE"><span>委内瑞拉Venezuela</span>
</option>
<option value="VN"><span>越南Vietnam</span>
</option>
<option value="YD"><span>也门Yemen</span>
</option>
<option value="ZM"><span>赞比亚Zambia</span>
</option>
<option value="ZW"><span>津巴布韦Zimbabwe</span>
</option>
</select>
</td>
</tr>
<tr id="error_tr" style="display: none;"><td colspan="5" rowspan="1"><span class="txt-wrong" id="error_for_nameandidno" style=""></span>
</td>
</tr>
</tbody>
</table>
<div class="lay-btn"><a href="javascript:" id="dialog_add_cancel" class="btn92" shape="rect">取消</a>
<a href="javascript:" id="dialog_add_ok" class="btn92s" shape="rect">确认</a>
</div>
</div>
</div>
</div>
<div id="dialog_update" style="display: none;"><div class="mark"></div>
<div class="up-box" style="width:640px;"><div class="up-box-hd">修改乘客信息<a href="javascript:" id="dialog_update_close" shape="rect">关闭</a>
</div>
<div class="up-box-bd" style="padding:15px 10px;border:1px solid #298CCE;"><table class="per-ticket" style="margin-left:0px;"><tr><th style="text-align:center;" rowspan="1" colspan="1">票种</th>
<th style="text-align:center;" rowspan="1" colspan="1">姓名</th>
<th style="text-align:center;" rowspan="1" colspan="1">证件类型</th>
<th style="text-align:center;" rowspan="1" colspan="1">证件号码</th>
<th style="text-align:center;" rowspan="1" colspan="1">国家/地区</th>
</tr>
<tbody id="showaddpassenger_update"><tr><td rowspan="1" colspan="1"><select id="ptypeselect_update"></select>
</td>
<td rowspan="1" colspan="1"><div><input id="pname_update_value" class="inptxt w110" type="text" />
</div>
</td>
<td rowspan="1" colspan="1"><select id="typeselect_update"></select>
</td>
<td rowspan="1" colspan="1"><input id="pidno_update_value" class="inptxt w160" value="" type="text" />
</td>
<td rowspan="1" colspan="1"><select id="pcountry_udpate_value" class="w160"><option value="CN"><span>中国China</span>
</option>
<option value="AF"><span>阿富汗Afghanistan</span>
</option>
<option value="AL"><span>阿尔巴尼亚Albania</span>
</option>
<option value="DZ"><span>阿尔及利亚Algeria</span>
</option>
<option value="AD"><span>安道尔Andorra</span>
</option>
<option value="AO"><span>安哥拉Angola</span>
</option>
<option value="AG"><span>安提瓜和巴布达Antigua and Barbuda</span>
</option>
<option value="AR"><span>阿根廷Argentina</span>
</option>
<option value="AM"><span>亚美尼亚Armenia</span>
</option>
<option value="AU"><span>澳大利亚Australia</span>
</option>
<option value="AT"><span>奥地利Austria</span>
</option>
<option value="AZ"><span>阿塞拜疆Azerbaijan</span>
</option>
<option value="BS"><span>巴哈马Bahamas</span>
</option>
<option value="BH"><span>巴林Bahrain</span>
</option>
<option value="BD"><span>孟加拉国Bangladesh</span>
</option>
<option value="BB"><span>巴巴多斯Barbados</span>
</option>
<option value="BY"><span>白俄罗斯Belarus</span>
</option>
<option value="BE"><span>比利时Belgium</span>
</option>
<option value="BZ"><span>伯利兹Belize</span>
</option>
<option value="BJ"><span>贝宁Benin</span>
</option>
<option value="BT"><span>不丹Bhutan</span>
</option>
<option value="BO"><span>玻利维亚Bolivia</span>
</option>
<option value="BA"><span>波黑Bosnia and Herzegovina</span>
</option>
<option value="BW"><span>博茨瓦纳Botswana</span>
</option>
<option value="BR"><span>巴西Brazil</span>
</option>
<option value="BN"><span>文莱Brunei</span>
</option>
<option value="BG"><span>保加利亚Bulgaria</span>
</option>
<option value="BF"><span>布基纳法索Burkina Faso</span>
</option>
<option value="BI"><span>布隆迪Burundi</span>
</option>
<option value="KH"><span>柬埔寨Cambodia</span>
</option>
<option value="CM"><span>喀麦隆Cameroon</span>
</option>
<option value="CA"><span>加拿大Canada</span>
</option>
<option value="KY"><span>佛得角Cape Verde</span>
</option>
<option value="CF"><span>中非Central African Republic</span>
</option>
<option value="TD"><span>乍得Chad</span>
</option>
<option value="CL"><span>智利Chile</span>
</option>
<option value="CO"><span>哥伦比亚Colombia</span>
</option>
<option value="KM"><span>科摩罗Comoros</span>
</option>
<option value="CD"><span>刚果(金)Congo, Democratic Republic of</span>
</option>
<option value="CG"><span>刚果(布)Congo, Republic of</span>
</option>
<option value="CK"><span>库克群岛Cook Islands</span>
</option>
<option value="CR"><span>哥斯达黎加Costa Rica</span>
</option>
<option value="CI"><span>科特迪瓦Cote d’lvoire</span>
</option>
<option value="HR"><span>克罗地亚Croatia</span>
</option>
<option value="CU"><span>古巴Cuba</span>
</option>
<option value="CY"><span>塞浦路斯Cyprus</span>
</option>
<option value="CZ"><span>捷克Czech</span>
</option>
<option value="KP"><span>朝鲜DPRK</span>
</option>
<option value="DK"><span>丹麦Denmark</span>
</option>
<option value="DJ"><span>吉布提Djibouti</span>
</option>
<option value="DM"><span>多米尼克Dominica</span>
</option>
<option value="DO"><span>多米尼加Dominican Republic</span>
</option>
<option value="EC"><span>厄瓜多尔Ecuador</span>
</option>
<option value="EG"><span>埃及Egypt</span>
</option>
<option value="EV"><span>萨尔瓦多El Salvador</span>
</option>
<option value="GQ"><span>赤道几内亚Equatorial Guinea</span>
</option>
<option value="ER"><span>厄立特里亚Eritrea</span>
</option>
<option value="EE"><span>爱沙尼亚Estonia</span>
</option>
<option value="SZ"><span>斯威士兰Eswatini</span>
</option>
<option value="ET"><span>埃塞俄比亚Ethiopia</span>
</option>
<option value="FJ"><span>斐济Fiji</span>
</option>
<option value="FI"><span>芬兰Finland</span>
</option>
<option value="FR"><span>法国France</span>
</option>
<option value="GA"><span>加蓬Gabon</span>
</option>
<option value="GM"><span>冈比亚Gambia</span>
</option>
<option value="CE"><span>格鲁吉亚Georgia</span>
</option>
<option value="DE"><span>德国Germany</span>
</option>
<option value="GH"><span>加纳Ghana</span>
</option>
<option value="GR"><span>希腊Greece</span>
</option>
<option value="GL"><span>格林纳达Grenada</span>
</option>
<option value="GT"><span>危地马拉Guatemala</span>
</option>
<option value="GN"><span>几内亚Guinea</span>
</option>
<option value="GW"><span>几内亚比绍Guinea-Bissau</span>
</option>
<option value="GY"><span>圭亚那Guyana</span>
</option>
<option value="HT"><span>海地Haiti</span>
</option>
<option value="HN"><span>洪都拉斯Honduras</span>
</option>
<option value="HU"><span>匈牙利Hungary</span>
</option>
<option value="IS"><span>冰岛Iceland</span>
</option>
<option value="IN"><span>印度India</span>
</option>
<option value="ID"><span>印度尼西亚Indonesia</span>
</option>
<option value="IR"><span>伊朗Iran</span>
</option>
<option value="IQ"><span>伊拉克Iraq</span>
</option>
<option value="IE"><span>爱尔兰Ireland</span>
</option>
<option value="IL"><span>以色列Israel</span>
</option>
<option value="IT"><span>意大利Italy</span>
</option>
<option value="JM"><span>牙买加Jamaica</span>
</option>
<option value="JP"><span>日本Japan</span>
</option>
<option value="JO"><span>约旦Jordan</span>
</option>
<option value="KZ"><span>哈萨克斯坦Kazakhstan</span>
</option>
<option value="KE"><span>肯尼亚Kenya</span>
</option>
<option value="KI"><span>基里巴斯Kiribati</span>
</option>
<option value="KW"><span>科威特Kuwait</span>
</option>
<option value="KG"><span>吉尔吉斯斯坦Kyrgyzstan</span>
</option>
<option value="LA"><span>老挝Laos</span>
</option>
<option value="LV"><span>拉脱维亚Latvia</span>
</option>
<option value="LB"><span>黎巴嫩Lebanon</span>
</option>
<option value="LS"><span>莱索托Lesotho</span>
</option>
<option value="LR"><span>利比里亚Liberia</span>
</option>
<option value="LY"><span>利比亚Libya</span>
</option>
<option value="LI"><span>列支敦士登Liechtenstein</span>
</option>
<option value="LT"><span>立陶宛Lithuania</span>
</option>
<option value="LU"><span>卢森堡Luxembourg</span>
</option>
<option value="MG"><span>马达加斯加Madagascar</span>
</option>
<option value="MW"><span>马拉维Malawi</span>
</option>
<option value="MY"><span>马来西亚Malaysia</span>
</option>
<option value="MV"><span>马尔代夫Maldives</span>
</option>
<option value="ML"><span>马里Mali</span>
</option>
<option value="MT"><span>马耳他Malta</span>
</option>
<option value="MH"><span>马绍尔群岛Marshall Islands</span>
</option>
<option value="MR"><span>毛里塔尼亚Mauritania</span>
</option>
<option value="MU"><span>毛里求斯Mauritius</span>
</option>
<option value="MX"><span>墨西哥Mexico</span>
</option>
<option value="FM"><span>密克罗尼西亚联邦Micronesia</span>
</option>
<option value="MD"><span>摩尔多瓦Moldova</span>
</option>
<option value="MC"><span>摩纳哥Monaco</span>
</option>
<option value="MN"><span>蒙古Mongolia</span>
</option>
<option value="ME"><span>黑山Montenegro</span>
</option>
<option value="MA"><span>摩洛哥Morocco</span>
</option>
<option value="MZ"><span>莫桑比克Mozambique</span>
</option>
<option value="MM"><span>缅甸Myanmar</span>
</option>
<option value="NA"><span>纳米比亚Namibia</span>
</option>
<option value="NR"><span>瑙鲁Nauru</span>
</option>
<option value="NP"><span>尼泊尔Nepal</span>
</option>
<option value="NL"><span>荷兰Netherlands</span>
</option>
<option value="NZ"><span>新西兰New Zealand</span>
</option>
<option value="NI"><span>尼加拉瓜Nicaragua</span>
</option>
<option value="NE"><span>尼日尔Niger</span>
</option>
<option value="NG"><span>尼日利亚Nigeria</span>
</option>
<option value="NU"><span>纽埃Niue</span>
</option>
<option value="MK"><span>北马其顿North Macedonia</span>
</option>
<option value="NO"><span>挪威Norway</span>
</option>
<option value="OM"><span>阿曼Oman</span>
</option>
<option value="PK"><span>巴基斯坦Pakistan</span>
</option>
<option value="PW"><span>帕劳Palau</span>
</option>
<option value="BL"><span>巴勒斯坦Palestine</span>
</option>
<option value="PA"><span>巴拿马Panama</span>
</option>
<option value="PG"><span>巴布亚新几内亚Papua New Guinea</span>
</option>
<option value="PY"><span>巴拉圭Paraguay</span>
</option>
<option value="PE"><span>秘鲁Peru</span>
</option>
<option value="PH"><span>菲律宾Philippines</span>
</option>
<option value="PL"><span>波兰Poland</span>
</option>
<option value="PT"><span>葡萄牙Portugal</span>
</option>
<option value="QA"><span>卡塔尔Qatar</span>
</option>
<option value="KR"><span>韩国Republic of Korea</span>
</option>
<option value="RO"><span>罗马尼亚Romania</span>
</option>
<option value="RU"><span>俄罗斯Russia</span>
</option>
<option value="RW"><span>卢旺达Rwanda</span>
</option>
<option value="KN"><span>圣基茨和尼维斯Saint Kitts and Nevis</span>
</option>
<option value="LC"><span>圣卢西亚Saint Lucia</span>
</option>
<option value="VC"><span>圣文森特和格林纳丁斯Saint Vincent &amp; the Grenadines</span>
</option>
<option value="WS"><span>萨摩亚Samoa</span>
</option>
<option value="SM"><span>圣马力诺San Marino</span>
</option>
<option value="ST"><span>圣多美和普林西比Sao Tome and Principe</span>
</option>
<option value="SA"><span>沙特阿拉伯Saudi Arabia</span>
</option>
<option value="SN"><span>塞内加尔Senegal</span>
</option>
<option value="CS"><span>塞尔维亚Serbia</span>
</option>
<option value="SC"><span>塞舌尔Seychelles</span>
</option>
<option value="SL"><span>塞拉利昂Sierra Leone</span>
</option>
<option value="SG"><span>新加坡Singapore</span>
</option>
<option value="SK"><span>斯洛伐克Slovakia</span>
</option>
<option value="SI"><span>斯洛文尼亚Slovenia</span>
</option>
<option value="SB"><span>所罗门群岛Solomon Islands</span>
</option>
<option value="SO"><span>索马里Somalia</span>
</option>
<option value="ZA"><span>南非South Africa</span>
</option>
<option value="SS"><span>南苏丹South Sudan</span>
</option>
<option value="ES"><span>西班牙Spain</span>
</option>
<option value="LK"><span>斯里兰卡Sri Lanka</span>
</option>
<option value="SD"><span>苏丹Sudan</span>
</option>
<option value="SR"><span>苏里南Suriname</span>
</option>
<option value="SE"><span>瑞典Sweden</span>
</option>
<option value="CH"><span>瑞士Switzerland</span>
</option>
<option value="SY"><span>叙利亚Syria</span>
</option>
<option value="TJ"><span>塔吉克斯坦Tajikistan</span>
</option>
<option value="TZ"><span>坦桑尼亚Tanzania</span>
</option>
<option value="TH"><span>泰国Thailand</span>
</option>
<option value="TL"><span>东帝汶Timor-Leste</span>
</option>
<option value="TG"><span>多哥Togo</span>
</option>
<option value="TO"><span>汤加Tonga</span>
</option>
<option value="TT"><span>特立尼达和多巴哥Trinidad and Tobago</span>
</option>
<option value="TN"><span>突尼斯Tunisia</span>
</option>
<option value="TR"><span>土耳其Turkey</span>
</option>
<option value="TM"><span>土库曼斯坦Turkmenistan</span>
</option>
<option value="TV"><span>图瓦卢Tuvalu</span>
</option>
<option value="UG"><span>乌干达Uganda</span>
</option>
<option value="UA"><span>乌克兰Ukraine</span>
</option>
<option value="AE"><span>阿联酋United Arab Emirates</span>
</option>
<option value="GB"><span>英国United Kingdom</span>
</option>
<option value="UN"><span>联合国United Nations</span>
</option>
<option value="US"><span>美国United States of America</span>
</option>
<option value="UY"><span>乌拉圭Uruguay</span>
</option>
<option value="UZ"><span>乌兹别克斯坦Uzbekistan</span>
</option>
<option value="VU"><span>瓦努阿图Vanuatu</span>
</option>
<option value="VA"><span>梵蒂冈Vatican City State</span>
</option>
<option value="VE"><span>委内瑞拉Venezuela</span>
</option>
<option value="VN"><span>越南Vietnam</span>
</option>
<option value="YD"><span>也门Yemen</span>
</option>
<option value="ZM"><span>赞比亚Zambia</span>
</option>
<option value="ZW"><span>津巴布韦Zimbabwe</span>
</option>
</select>
</td>
</tr>
<tr id="error_update_tr" style="display: none;"><td colspan="5" rowspan="1"><span class="txt-wrong" id="error_for_update_nameandidno" style=""></span>
</td>
</tr>
</tbody>
</table>
<div class="lay-btn"><a href="javascript:" id="dialog_update_cancel" class="btn92" shape="rect">取消</a>
<a href="javascript:" id="dialog_update_ok" class="btn92s" shape="rect">确认</a>
</div>
</div>
</div>
</div>
<div id="608_complain" style="display: none;"><div class="mark"></div>
<div class="up-box" style="width:640px;"><div class="up-box-hd">举报告知确认书<a href="javascript:" id="608_complain_close" shape="rect">关闭</a>
</div>
<div class="up-box-bd" style="padding:15px 10px;border:1px solid #298CCE;"><table class="per-ticket" style="margin-left:0px;"><tr><td rowspan="1" colspan="1">举报人姓名：<strong id="608_name" style="font-size:20px"></strong>
</td>
<td rowspan="1" colspan="1">联系电话：<strong id="608_tel" style="font-size:20px"></strong>
</td>
</tr>
<tr><td colspan="2" rowspan="1">身份证件号码：<strong id="608_card" style="font-size:20px"></strong>
</td>
</tr>
<tr></tr>
<tr><td colspan="2" rowspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本人确认举报身份信息被他人冒用购买<strong id="ticketInfo" style="font-size:20px"></strong>
次车票。本人承诺本次举报及购票所提交的身份信息属实，并对虚假举报后果负责。</td>
</tr>
<tr><td colspan="2" rowspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;铁路部门郑重提醒，将在车站和列车对该车票进行重点查验。根据国务院颁布的《铁路安全管理条例》，对该车票所记载身份信息与所持身份证件或者真实身份不符的持票人，铁路部门将拒绝其进站乘车。同时，公安机关将依法调查。</td>
</tr>
<tr><td colspan="2" rowspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;铁路部门将对您的举报信息保密，谢谢您的合作！</td>
</tr>
</table>
<div class="lay-btn"><a href="javascript:" id="608_complain_cancel" class="btn92" shape="rect">取消</a>
<a href="javascript:" id="608_complain_ok" class="btn92s" shape="rect">确认举报</a>
</div>
</div>
</div>
</div>
<!-- 老年优惠票提示 开始 -->
<div class="up-box w600" style="display:none;" id="cancel_lnyh_id"><div class="up-box-hd">交易提示<a href="javascript:" id="cancel_lnyh_close" shape="rect">关闭</a>
</div>
<div class="up-box-bd"><div class="up-con clearfix"><span class="icon i-opt"></span>
<div style="font-weight: bolder;font-size: 15px;color:black;" id="cancel_lnyh_alert_msg" class="r-txt"></div>
</div>
<div class="lay-btn"><a href="javascript:" class="btn92" id="cancel_lnyh_cr" shape="rect">稍后再说</a>
<a href="javascript:" class="btn92s" id="cancel_lnyh_ok" shape="rect">立即申请</a>
</div>
</div>
</div>
<!-- 老年优惠票提示 结束 -->
<div id="608_check" style="display: none;"><div class="mark"></div>
<div class="up-box"><div class="up-box-hd">温馨提示<a href="javascript:" id="608_check_close" shape="rect">关闭</a>
</div>
<div class="up-box-bd"><div class="up-con clearfix"><span class="icon i-opt"></span>
<div class="r-txt"><div class="tit" id="608_check_msg"></div>
<div class="tit" style="color:#FB7403">是否举报？</div>
</div>
</div>
<div class="lay-btn"><a href="javascript:" id="608_check_cancel" class="btn92" shape="rect">取消</a>
<a href="javascript:" id="608_check_ok" class="btn92s" shape="rect">网上举报</a>
</div>
</div>
</div>
</div>
<!--header start-->
<div class="header"><div class="wrapper"><!-- 头部内容 -->
<div class="header-con"><h1 class="logo"><a name="g_href" data-type="1" data-href="index.html" data-redirect="Y" href="javascript:;">中国铁路12306</a>
</h1>
<div class="header-right"><!-- 搜索条 -->
<div class="header-search" style="width: 380px"><div class="search-bd" style="width: 350px"><input type="password" value="" style="display:none" />
<input type="text" class="search-input" id="search-input" aria-label="搜索车票、餐饮、常旅客、相关规章" value="" auto-complete="new-password" placeholder="搜索车票、餐饮、常旅客、相关规章" aria-haspopup="true" />
<!-- 搜索提示 -->
<div class="search-down"><a href="javascript:;" class="close">关闭</a>
<ul class="search-down-list"></ul>
</div>
<!-- 搜索历史 -->
<div class="search-history"><a href="javascript:;" class="history-clear">清除</a>
<h3 class="search-history-tit">搜索历史</h3>
<ul class="search-history-list"></ul>
</div>
</div>
<a aria-label="点击搜索，搜索结果页面可能超出无障碍范围。" class="search-btn" href="javascript:;"><i class="icon icon-search"></i>
</a>
</div>
<!-- 右侧菜单 -->
<ul class="header-menu" role="menubar"><li class="menu-item"><a id="toolbarSwitch" href="javascript:;" class="menu-nav-hd">无障碍</a>
</li>
<li class="menu-item menu-line">|</li>
<li class="menu-item"><a id="caring_a" href="javascript:;" onclick="$.changebigslh();" class="menu-nav-hd">敬老版</a>
</li>
<li class="menu-item menu-line">|</li>
<li class="menu-item menu-nav" role="menuitem"><a href="https://www.12306.cn/en/index.html" class="menu-nav-hd" aria-controls="megamenu-1" aria-expanded="false" aria-haspopup="true">English
              <i class="caret"></i>
</a>
<ul class="menu-nav-bd" role="menu" aria-hidden="true" id="megamenu-1" style="width: 90px;"><li><a href="https://www.12306.cn/index/index.html">简体中文</a>
</li>
<li><a href="https://www.12306.cn/en/index.html">English</a>
</li>
</ul>
</li>
<li class="menu-item menu-line">|</li>
<li class="menu-item menu-nav" role="menuitem"><a name="g_href" data-type="2" data-href="view/index.html" data-redirect="Y" href="javascript:;" class="menu-nav-hd" aria-expanded="false" aria-haspopup="true" aria-controls="megamenu-2">我的12306
              <i class="caret"></i>
</a>
<ul class="menu-nav-bd" role="menu" aria-hidden="true" id="megamenu-2"><li><a style="color: #333;" name="g_href" data-type="2" data-href="view/train_order.html" data-redirect="Y" href="javascript:;">火车票订单</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/lineUp_order.html" data-redirect="Y" href="javascript:;">候补订单</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/commutation_order.html" data-redirect="Y" href="javascript:;">计次•定期票订单</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/commutation_ticket_order.html" data-redirect="Y" href="javascript:;">约号订单</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/snow_order.html" data-redirect="Y" href="javascript:;">雪具快运订单</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/invoice_index.html" data-redirect="Y" href="javascript:;">电子发票</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/personal_travel.html" data-redirect="Y" href="javascript:;">本人车票</a>
</li>
<li class="nav-line"></li>
<li><a style="color: #333;" name="g_href" data-type="10" data-href="queryMyOrder.html" data-redirect="Y" href="javascript:;">我的餐饮•特产</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/my_insurance.html" data-redirect="Y" href="javascript:;">我的保险</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="3" data-href="welcome.html" data-redirect="Y" href="javascript:;">我的会员</a>
</li>
<li class="nav-line"></li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/information.html" data-redirect="Y" href="javascript:;">查看个人信息</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/userSecurity.html" data-redirect="Y" href="javascript:;">账户安全</a>
</li>
<li class="nav-line"></li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/passengers.html" data-redirect="Y" href="javascript:;">乘车人</a>
</li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/address_init.html" data-redirect="Y" href="javascript:;">地址管理</a>
</li>
<li class="nav-line"></li>
<li><a style="color: #333;" name="g_href" data-type="2" data-href="view/icentre_serviceQuery.html" data-redirect="Y" href="javascript:;">温馨服务查询</a>
</li>
</ul>
</li>
<li class="menu-item menu-line">|</li>
<li role="menuitem" id="J-header-logout" class="menu-item menu-login">
            您好，<a id="login_user" name="g_href" data-type="2" data-href="view/index.html" data-redirect="Y" href="javascript:;" class="colorA" style="margin-left:-0.5px;"><span style="width:50px;">张森林</span>
</a>
<span class="txt-primary"></span>
&nbsp;|&nbsp;<a name="g_href" data-type="2" data-href="login/loginOut" data-redirect="Y" href="javascript:;">退出</a>
</li>
</ul>
</div>
</div>
</div>
<!-- 导航 -->
<div class="nav-box" role="navigation"><ul class="nav" role="menubar"><li role="menuitem" class="nav-item nav-item-w1"><a name="g_href" data-type="1" data-href="index.html" data-redirect="Y" href="javascript:;" class="nav-hd">首页</a>
</li>
<li role="menuitem" class="nav-item nav-item-w1"><a href="javascript:void(0)" class="nav-hd" aria-expanded="false" aria-haspopup="true" aria-controls="megamenu-3">车票
          <i class="icon icon-down"></i>
</a>
<div class="nav-bd" id="megamenu-3"><div class="nav-bd-item nav-col2"><h3 class="nav-tit">购买</h3>
<ul class="nav-con" role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="2" data-href="leftTicket/init?linktypeid=dc" data-redirect="Y" href="javascript:;">单程</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="leftTicket/init?linktypeid=wf" data-redirect="Y" href="javascript:;">往返</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="lcQuery/init" data-redirect="Y" href="javascript:;">中转换乘</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="view/commutation_index.html" data-redirect="Y" href="javascript:;">计次•定期票</a>
</li>
</ul>
</div>
<div class="nav-bd-item nav-col2"><h3 class="nav-tit">变更</h3>
<ul class="nav-con" role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="2" data-href="view/train_order.html?type=2" data-param="typefilt=4" data-redirect="Y" href="javascript:;">退票</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="view/train_order.html?type=2" data-param="typefilt=2" data-redirect="Y" href="javascript:;">改签</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="view/train_order.html?type=2" data-param="typefilt=3" data-redirect="Y" href="javascript:;">变更到站</a>
</li>
<li></li>
</ul>
</div>
<div class="nav-bd-item nav-col2"><h3 class="nav-tit border-none">更多</h3>
<ul class="nav-con" role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/ticket/zt_card.html" data-redirect="Y" href="javascript:;">中铁银通卡</a>
</li>
<li class="border-none" role="menuitemradio"><a name="g_href" data-type="1" data-href="view/ticket/through_train.html" data-redirect="Y" href="javascript:;">广九直通车</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/ticket/international_train.html" data-redirect="Y" href="javascript:;">国际列车</a>
</li>
</ul>
</div>
</div>
</li>
<li role="menuitem" class="nav-item "><a href="javascript:void(0)" class="nav-hd " aria-expanded="false" aria-haspopup="true" aria-controls="megamenu-4">团购服务
          <i class="icon icon-down "></i>
</a>
<div class="nav-bd " id="megamenu-4"><div class="nav-bd-item nav-col6 "><ul class="nav-con " role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/group/group_management.html?type=1" data-redirect="Y" href="javascript:;">务工人员</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/group/group_management.html?type=2" data-redirect="Y" href="javascript:;">学生团体</a>
</li>
</ul>
</div>
</div>
</li>
<li role="menuitem" class="nav-item "><a href="javascript:void(0) " class="nav-hd " aria-expanded="false" aria-haspopup="true" aria-controls="megamenu-5">会员服务
          <i class="icon icon-down "></i>
</a>
<div class="nav-bd " id="megamenu-5"><div class="nav-bd-item nav-col6"><ul class="nav-con " role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="3" data-href="index.html" data-redirect="Y" href="javascript:;">会员管理</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="3" data-href="index.html" data-redirect="Y" href="javascript:;">积分账户</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="3" data-href="index.html" data-redirect="Y" href="javascript:;">积分兑换</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="3" data-href="index.html" data-redirect="Y" href="javascript:;">会员专享</a>
</li>
<li class="border-none " role="menuitemradio"><a name="g_href" data-type="3" data-href="welcome.html" data-redirect="Y" href="javascript:;">会员中心</a>
</li>
</ul>
</div>
</div>
</li>
<li role="menuitem" class="nav-item "><a href="javascript:void(0) " class="nav-hd " aria-expanded="false" aria-haspopup="true" aria-controls="megamenu-6">站车服务
          <i class="icon icon-down "></i>
</a>
<div class="nav-bd " id="megamenu-6"><div class="nav-bd-item nav-col4 "><ul class="nav-con " role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="2" data-href="view/icentre_qxyyInfo.html" data-redirect="Y" href="javascript:;">重点旅客预约</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/station/hand.html" data-redirect="Y" href="javascript:;">便民托运</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/station/shared_Car.html" data-redirect="Y" href="javascript:;">约车服务</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="4" data-href="czyd_2143/" data-redirect="Y" href="javascript:;">车站引导</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="view/icentre_lostInfo.html" data-redirect="Y" href="javascript:;">遗失物品查找</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/station/train_intro.html" data-redirect="Y" href="javascript:;">动车组介绍</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/station/custom_PickUp.html" data-redirect="Y" href="javascript:;">定制接送</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="4" data-href="zcfc_2548/" data-redirect="Y" href="javascript:;">站车风采</a>
</li>
</ul>
</div>
</div>
</li>
<li role="menuitem" class="nav-item "><a href="javascript:void(0) " class="nav-hd " aria-expanded="false" aria-haspopup="true" aria-controls="megamenu-7">商旅服务
          <i class="icon icon-down "></i>
</a>
<div class="nav-bd " id="megamenu-7"><div class="nav-bd-item nav-col6 "><ul class="nav-con " role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="10" data-href="index.html" data-redirect="Y" href="javascript:;">餐饮•特产</a>
</li>
<!-- <li role="menuitemradio">
                <a name="g_href" data-type="5" data-href="" data-redirect="Y" href="javascript:;">旅游</a>
              </li> -->
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="view/my_insurance.html" data-redirect="Y" href="javascript:;">保险</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="view/snow_checkedBaggage.html" data-redirect="Y" href="javascript:;">雪具快运</a>
</li>
</ul>
</div>
</div>
</li>
<li role="menuitem" class="nav-item "><a href="javascript:void(0) " class="nav-hd " aria-expanded="false" aria-haspopup="true" aria-controls="megamenu-8">出行指南
          <i class="icon icon-down "></i>
</a>
<div class="nav-bd " id="megamenu-8"><div class="nav-bd-item nav-col2 "><h3 class="nav-tit ">常见问题</h3>
<ul class="nav-con " role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/ticketType.html" data-redirect="Y" href="javascript:;">车票</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/ticketWindow.html" data-redirect="Y" href="javascript:;">购票</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/windowEndorse.html" data-redirect="Y" href="javascript:;">改签</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/windowRefund.html" data-redirect="Y" href="javascript:;">退票</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/help.html" data-redirect="Y" href="javascript:;" class="txt-lighter">更多>></a>
</li>
<li></li>
</ul>
</div>
<div class="nav-bd-item nav-col2 "><h3 class="nav-tit ">旅客须知</h3>
<ul class="nav-con " role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/saleTicketMeans.html?linktypeid=means5" data-redirect="Y" href="javascript:;">身份核验</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/help.html" data-redirect="Y" href="javascript:;" class="txt-lighter">更多>></a>
</li>
<li></li>
</ul>
</div>
<div class="nav-bd-item nav-col2 "><h3 class="nav-tit border-none ">相关章程</h3>
<ul class="nav-con " role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/saleTicketMeans.html?linktypeid=means2" data-redirect="Y" href="javascript:;">铁路旅客运输规程</a>
</li>
<li class="border-none " role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/saleTicketMeans.html?linktypeid=means7" data-redirect="Y" href="javascript:;">广深港高速铁路跨境旅客运输组织规则</a>
</li>
<li role="menuitemradio" style="text-overflow: ellipsis;white-space: nowrap;"><a name="g_href" data-type="2" data-href="gonggao/saleTicketMeans.html?linktypeid=means6" data-redirect="Y" href="javascript:;">铁路旅客禁止、限制携带和托运物品目录</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="gonggao/help.html" data-redirect="Y" href="javascript:;" class="txt-lighter">更多>></a>
</li>
<li></li>
</ul>
</div>
</div>
</li>
<li role="menuitem" class="nav-item last "><a href="javascript:void(0) " class="nav-hd " aria-expanded="false" aria-haspopup="true" aria-controls="megamenu-9">信息查询
          <i class="icon icon-down "></i>
</a>
<div class="nav-bd " id="megamenu-9"><div class="nav-bd-item nav-col5 "><h3 class="nav-tit border-none ">常用查询</h3>
<ul class="nav-con " role="menu" aria-hidden="true"><li role="menuitemradio"><a name="g_href" data-type="2" data-href="zwdch/init" data-redirect="Y" href="javascript:;">正晚点</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="queryTrainInfo/init" data-redirect="Y" href="javascript:;">时刻表</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="view/queryPublicIndex.html" data-redirect="Y" href="javascript:;">公布票价</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/infos/ticket_check.html" data-redirect="Y" href="javascript:;">检票口</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/infos/sale_time.html" data-redirect="Y" href="javascript:;">起售时间</a>
</li>
<li role="menuitemradio"><a name="g_href" data-href="https://12306.weather.com.cn/pc.html" data-redirect="N" href="javascript:;">天气</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/infos/jiaotong.html" data-redirect="Y" href="javascript:;">交通查询</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="2" data-href="queryAgencySellTicket/init" data-redirect="Y" href="javascript:;">代售点</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/infos/service_number.html" data-redirect="Y" href="javascript:;">客服电话</a>
</li>
<li role="menuitemradio"><a name="g_href" data-type="1" data-href="view/infos/train-query-status.html" data-redirect="Y" href="javascript:;">列车状态</a>
</li>
<li></li>
</ul>
</div>
<div class="nav-bd-item "><ul class="nav-con nav-con-pt" role="menu" aria-hidden="true"><li class="border-none" role="menuitemradio"><a name="g_href" data-type="1" data-href="index.html#index_ads" data-redirect="Y" href="javascript:;">最新发布</a>
</li>
<li class="border-none" role="menuitemradio"><a name="g_href" data-type="6" data-href="queryDishonest/init" data-redirect="Y" href="javascript:;">信用信息</a>
</li>
</ul>
</div>
</div>
</li>
</ul>
</div>
</div>
<!--header end-->
<!--页面主体  开始-->
<div class="content"><!--列车信息 开始-->
<div class="layout t-info"><div class="lay-hd">
				列车信息<span class="small">（以下余票信息仅供参考）</span>
</div>
<div class="lay-bd"><p class="t-tit" id="ticket_tit_id"></p>
<p class="t-con" id="ticket_con_id"></p>
<p style="color: #3177BF;">*显示的价格均为实际活动折扣后票价，供您参考，查看<a style="color:#07f" href="/otn/view/queryPublicIndex.html" shape="rect">公布票价</a>
。具体票价以您确认支付时实际购买的铺别票价为准。</p>
<p id="syx_msg" style="color: #FB7403;display: none;">
					*当前乘车区间支持灵活行，旅客可在乘车当日办理最多3次灵活行变更车次手续，
					<a target="_blank" href="https://mobile.12306.cn/otsmobile/h5/otsbussiness/info/hongkongSYX.html" shape="rect">查看详情</a>
</p>
<p id="lnp_msg" style="color: #FB7403;display: none;">
					*本列车二等座支持办理老年优惠票服务。
					<a target="_blank" href="https://mobile.12306.cn/otsmobile/h5/otsbussiness/info/hongkongSYX.html" shape="rect">查看详情</a>
</p>
</div>
</div>
<!--列车信息 结束-->
<!--改签原票信息 开始-->
<!--改签原票信息 结束-->
<!--多级票价信息 开始-->
<div style="display: none;"><input style="display: none;" type="checkbox" id="fczk" />
</div>
<!--乘客信息 开始-->
<div class="layout person"><div class="lay-hd">
				乘客信息<span class="small" id="psInfo">（填写说明）</span>
<div class="s-box"><input id="quickQueryPassenger_id" type="text" value="输入乘客姓名" class="txt" />
<input id="submit_quickQueryPassenger" type="submit" class="sub" />
</div>
</div>
<div class="lay-bd"><div class="per-sel"><div class="item clearfix"><h2 class="srr" id="dg_passenger_image_id" title="受让人" style="display: none;">受让人</h2>
<ul id="dj_passenger_id"></ul>
</div>
<div class="item clearfix"><h2 class="cy" id="normal_passenger_image_id" title="乘车人" style="display: none;">乘车人</h2>
<ul id="normal_passenger_id"></ul>
<div class="btn-all" style="display: none;" id="btnAll"><a id="show_more_passenger_id" title="展开" href="javascript:" style="display: none;" shape="rect"><label id="gd">更多</label>
<b></b>
</a>
</div>
</div>
</div>
<table class="per-ticket"><tr><th width="28" rowspan="1" colspan="1">序号</th>
<th rowspan="1" colspan="1">票种</th>
<th rowspan="1" colspan="1">席别 </th>
<th rowspan="1" colspan="1">姓名</th>
<th rowspan="1" colspan="1">证件类型</th>
<th rowspan="1" colspan="1">证件号码</th>
<!-- 
						<th><input type="checkbox" class="check" id="selected_ticket_passenger_all"
							onclick="javascript:selectedTicketPassengerAll(this,true);" checked="checked" />全部</th>
						-->
<th width="70" rowspan="1" colspan="1"></th>
<th width="30" rowspan="1" colspan="1"></th>
</tr>
<tbody id="ticketInfo_id"></tbody>
</table>
<div><img src="/otn/resources/images/ins_ad7.png" alt="" />
</div>
</div>
</div>
<div style="line-height: 20px; margin-top: 10px;">提交订单表示已阅读并同意
			<a id="zl_gz" style="display: none;" target="_blank" href="https://mobile.12306.cn/otsmobile/h5/otsbussiness/zhonglao/international-organizationRules/international-organizationRules.html" shape="rect">《中老铁路跨境旅客联运组织规则》</a>
<a target="_blank" href="https://mobile.12306.cn/otsmobile/h5/otsbussiness/info/transportationRules.html" shape="rect">《国铁集团铁路旅客运输规程》</a>
<a id="kj_gz" style="display: none;" target="_blank" href="https://mobile.12306.cn/otsmobile/h5/otsbussiness/info/crossBorderPassenger.html" shape="rect">《广深港高速铁路跨境旅客运输组织规则》</a>
<a target="_blank" href="https://mobile.12306.cn/otsmobile/h5/otsbussiness/info/serviceAnnouncement.html" shape="rect">《服务条款》</a>
</div>
<!--乘客信息 结束-->
<div class="lay-btn"><a id="preStep_id" href="javascript:" class="btn92" shape="rect">上一步</a>
<a id="submitOrder_id" href="javascript:" class="btn92s" shape="rect">提交订单</a>
</div>
<div><div class="tips-txt"><h2>温馨提示：</h2>
<P>1. 一张有效身份证件同一乘车日期同一车次只能购买一张车票，高铁动卧列车除外。改签或变更到站后车票的乘车日期在春运期间，如再办理退票将按票面价格20%核收退票费。请合理安排行程，更多改签规则请查看<a target="_blank" href="https://mobile.12306.cn/otsmobile/h5/otsbussiness/info/orderWarmTips.html" style="color:blue;" shape="rect">《退改说明》</a>
。</P>
<P>2. 购买儿童票时，乘车儿童有有效身份证件的，请填写本人有效身份证件信息。自2023年1月1日起，每一名持票成年人旅客可免费携带一名未满6周岁且不单独占用席位的儿童乘车，超过一名时，超过人数应购买儿童优惠票。免费儿童可以在购票成功后添加。</P>
<P>3.
					购买残疾军人（伤残警察）优待票的，须在购票后、开车前办理换票手续方可进站乘车。换票时，不符合规定的减价优待条件，没有有效"中华人民共和国残疾军人证"或"中华人民共和国伤残人民警察证"的，不予换票，所购车票按规定办理退票手续。</P>
<P>4.一天内3次申请车票成功后取消订单（包含无座票时取消5次计为取消1次），当日将不能在12306继续购票。</P>
<P><strong>5.购买铁路乘意险的注册用户年龄须在18周岁以上，使用非中国居民身份证注册的用户如购买铁路乘意险，须在<a href="../view/information.html" shape="rect">我的12306——个人信息</a>
如实填写“出生日期”。</strong>
</P>
<P><strong>6.父母为未成年子女投保，须在<a href="../view/passengers.html" shape="rect">我的乘车人</a>
登记未成年子女的有效身份证件信息。</strong>
</P>
<P>7.未尽事宜详见《铁路旅客运输规程》等有关规定和车站公告。</P>
<P name="xjky" style="display: none;">8. 为确保乘客在旅途中有一个安全、舒适的乘坐环境，自2020年11月17日起，<span style="color:red;">旅客不得随身携带长宽高之和大于130厘米的雪具乘车</span>
。您可选择雪具快运服务，请提前1-2天选择雪具快运“门到站”或“站到站”服务，中铁快运提供雪具到站后3日免费保管，请您根据出行时间，提前咨询和办理。中铁快运客服热线：95572<br clear="none" />
</P>
</div>
</div>
</div>
<!--页面主体  结束-->
<!-- 高原旅行提示 -->
<div class="up-box w600" style="display: none;top: 30px;left: 560px;width: 800px;" id="gyalert"><div class="up-box-hd">高原旅行提示<a id="close_gyalert" href="javascript:" shape="rect">关闭</a>
</div>
<div class="up-box-bd"><div class="up-con clearfix"><span class="icon i-warn"></span>
<div style="width: 550px" class="r-txt"><div id="gyalerttext" style="height: 400px;overflow: auto;" class="tit"><span style="color: #dc9616;">高原旅行提示</span>
<br clear="none" />

	            		&nbsp;&nbsp;&nbsp;&nbsp;根据卫生部门和医生意见，旅客进入高原旅行前建议进行体检，由医生确认可进入高原旅行时，方可前往高原旅行。凡有下列疾患之一者，不宜进入3000米以上高海拔地区旅行：<br clear="none" />

	            		&nbsp;&nbsp;&nbsp;&nbsp;（一）各种器质性心脏病，显著心律失常或静息心率>100次/分，高血压Ⅱ期以上，各种血液病，脑血管疾病。<br clear="none" />

	            		&nbsp;&nbsp;&nbsp;&nbsp;（二）慢性呼吸系统疾病，中度以上阻塞性肺疾病，如支气管哮喘、支气管扩张、肺气肿、活动性肺结核、尘肺病。<br clear="none" />

	            		&nbsp;&nbsp;&nbsp;&nbsp;（三）糖尿病未获控制；癔病、癫痫、精神分裂症。<br clear="none" />

	            		&nbsp;&nbsp;&nbsp;&nbsp;（四）重症感冒、上呼吸道感染，体温在38℃以上；上呼吸道感染，虽体温不超过38℃，但全身及呼吸道症状明显者。<br clear="none" />

	            		&nbsp;&nbsp;&nbsp;&nbsp;（五）曾确诊患过高原肺水肿、高原脑水肿、血压增高明显的高原高血压症、高原心脏病及高原红细胞增多症者。<br clear="none" />

	            		&nbsp;&nbsp;&nbsp;&nbsp;（六）高危产妇、高龄孕妇。<br clear="none" />

	            		&nbsp;&nbsp;&nbsp;&nbsp;请自觉保护高原生态环境。感谢您的合作！<br clear="none" />
</div>
</div>
</div>
<div class="lay-btn"><a id="cancel_gyalert" href="javascript:" class="btn92" shape="rect">取消</a>
<a href="javascript:" class="btn92s" id="conf_gyalert" shape="rect">确认</a>
</div>
</div>
</div>
<!--页面底部  开始-->
<div class="footer"><div class="footer-con wrapper"><div class="foot-links" style="margin-right:20px;"><h2 class="foot-con-tit">友情链接</h2>
<ul class="foot-links-list"><li><a name="g_href" data-href="http://www.china-railway.com.cn/" data-redirect="N" href="javascript:;" data-target="_blank"><img src="/otn/resources/images/12306_index/link05.png" alt="中国国家铁路集团有限公司" />
</a>
</li>
<li><a name="g_href" data-href="http://www.china-ric.com/" data-redirect="N" href="javascript:;" data-target="_blank"><img src="/otn/resources/images/12306_index/link02.png" alt="中国铁路财产保险自保有限公司" />
</a>
</li>
<li><a name="g_href" data-href="http://www.95306.cn/" data-redirect="N" href="javascript:;" data-target="_blank"><img src="/otn/resources/images/12306_index/link03.png" alt="中国铁路95306网" />
</a>
</li>
<li><a name="g_href" data-href="http://www.95572.com/" data-redirect="N" href="javascript:;" data-target="_blank"><img src="/otn/resources/images/12306_index/link04.png" alt="中铁快运股份有限公司" />
</a>
</li>
</ul>
</div>
<ul class="foot-code"><li style="width: 140px;"><h2 class="foot-con-tit">中国铁路官方微信</h2>
<div class="code-pic"><img src="/otn/resources/images/zgtlwb.png" class="code-pic" alt="中国铁路官方微信" />
</div>
</li>
<li style="width: 140px;"><h2 class="foot-con-tit">中国铁路官方微博</h2>
<div class="code-pic"><img src="/otn/resources/images/zgtlwx.png" class="code-pic" alt="中国铁路官方微博" />
</div>
</li>
<li style="width: 110px;"><h2 class="foot-con-tit">12306 公众号</h2>
<div class="code-pic"><img src="/otn/resources/images/public.png" class="code-pic" alt="12306 公众号" />
</div>
</li>
<li style="width: 110px;"><h2 class="foot-con-tit">铁路12306</h2>
<div class="code-pic"><img src="/otn/resources/images/download.png" class="code-pic" alt="铁路12306" />
<div class="code-tips">官方APP下载，目前铁路未授权其他网站或APP开展类似服务内容，敬请广大用户注意。</div>
</div>
</li>
</ul>
</div>
<div class="footer-txt" style="position: relative;"><p><span class="mr">版权所有©2008-2025</span>
<span>中国铁道科学研究院集团有限公司</span>
<span>技术支持：铁旅科技有限公司</span>
</p>
<p><span class="mr"><img src="/otn/resources/images/gongan.png" alt="公安" style="width: 13px" />
<a target="blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802038392" style="color: #c1c1c1">京公网安备 11010802038392号</a>
</span>
<span class="mr">|</span>
<span class="mr">京ICP备05020493号-4</span>
<span class="mr">|</span>
<span>ICP证：京B2-20202537</span>
</p>
<div style="position: absolute;top: 17px;left: 50%;margin-left: 465px;"><img src="/otn/resources/images/footer-slh.jpg" style="display: block;width: 130px;height: 46px;" alt="适老化无障碍服务" />
</div>
</div>
<script type="text/javascript" src="https://kyfw.12306.cn/otn/resources/route/kyfw.12306.cn/route.js"></script>
</div>
<!--页面底部  结束-->
<!-- 提交订单核对车票信息弹出层 start -->
<div id="checkticketinfo_id" style="display: none; margin-left: 30%; margin-top: 30%;"><div class="mark"></div>
<div class="up-box w664" id="content_checkticketinfo_id"><div class="up-box-hd">请核对以下信息</div>
<div class="up-box-bd ticket-check"><div class="info2" id="check_ticket_tit_id"><strong class="mr5">2013-03-02（周日）</strong>
<strong class="mr5">D315</strong>
动车<strong class="ml5">北京南</strong>
站<strong>（08:22开）—上海虹桥</strong>
站（16:55到）

				</div>
<div class="table-list"><div class="table-list-head"><table class="table-a"><thead><tr><th style="width: 38px; text-align: center;" rowspan="1" colspan="1">序号</th>
<th style="width: 47px; text-align: center;" rowspan="1" colspan="1">席别</th>
<th style="width: 45px; text-align: center;" rowspan="1" colspan="1">票种</th>
<th style="width: 55px; text-align: center;" rowspan="1" colspan="1">姓名</th>
<th style="width: 90px; text-align: center;" rowspan="1" colspan="1">证件类型</th>
<th style="width: 130px; text-align: center;" rowspan="1" colspan="1">证件号码</th>
</tr>
</thead>
</table>
</div>
<div class="table-list-body" style="max-height: 164px;"><table class="table-a"><tbody id="check_ticketInfo_id"></tbody>
</table>
</div>
</div>
<p style="color: #3177BF;" id="notice_1_id"><!--   注：1.系统将随机为您申请席位，暂不支持自选席位。-->
</p>
<p style="color: red;display: none;" name="notice_child">
					*儿童需携带购票（免费乘车儿童为申明）时所使用的有效身份证件乘车。
				</p>
<p style="color: red;display: none;" name="notice_child">
					*申办“铁路临时乘车身份证明”仅限已申领中国居民身份证的旅客。
				</p>
<div class="seat-sel seat-sel-round" id="id-seat-sel" style="display: none;"><div class="seat-sel-hd"><div class="tips-xz">选座喽</div>

						已选座<span id="selectNo">1/4</span>
</div>
<div class="seat-sel-bd"><!-- 第一排 -->
<div class="sel-item" id="yideng1" style="display: none;"><!-- 一等座-->
<div class="txt">窗</div>
<ul class="seat-list"><li><a href="javascript:" id="1A" shape="rect">A</a>
</li>
<li><a href="javascript:" id="1C" shape="rect">C</a>
</li>
</ul>
<div class="txt">过道</div>
<ul class="seat-list"><li><a href="javascript:" id="1D" shape="rect">D</a>
</li>
<li><a href="javascript:" id="1F" shape="rect">F</a>
</li>
</ul>
<div class="txt txt-last">窗</div>
</div>
<div class="sel-item" id="erdeng1" style="display: none;"><!-- 二等座-->
<div class="txt">窗</div>
<ul class="seat-list"><li><a href="javascript:" id="1A" shape="rect">A</a>
</li>
<li><a href="javascript:" id="1B" shape="rect">B</a>
</li>
<li><a href="javascript:" id="1C" shape="rect">C</a>
</li>
</ul>
<div class="txt">过道</div>
<ul class="seat-list"><li><a href="javascript:" id="1D" shape="rect">D</a>
</li>
<li><a href="javascript:" id="1F" shape="rect">F</a>
</li>
</ul>
<div class="txt txt-last">窗</div>
</div>
<div class="sel-item" id="tedeng1" style="display: none;"><!-- 特等座-->
<div class="txt">窗</div>
<ul class="seat-list"><li><a href="javascript:" id="1A" shape="rect">A</a>
</li>
<li><a href="javascript:" id="1C" shape="rect">C</a>
</li>
</ul>
<div class="txt">过道</div>
<ul class="seat-list"><li><a href="javascript:" id="1F" shape="rect">F</a>
</li>
</ul>
<div class="txt txt-last">窗</div>
</div>
<div class="sel-item" id="shangwu1" style="display: none;"><!-- 商务座-->
<div class="txt">窗</div>
<ul class="seat-list"><li><a href="javascript:" id="1A" shape="rect">A</a>
</li>
</ul>
<div class="txt">过道</div>
<ul class="seat-list"><li><a href="javascript:" id="1F" shape="rect">F</a>
</li>
</ul>
<div class="txt txt-last">窗</div>
</div>
<!-- 第二排 -->
<div class="sel-item" id="yideng2" style="display: none;"><!-- 一等座-->
<div class="txt">窗</div>
<ul class="seat-list"><li><a href="javascript:" id="2A" shape="rect">A</a>
</li>
<li><a href="javascript:" id="2C" shape="rect">C</a>
</li>
</ul>
<div class="txt">过道</div>
<ul class="seat-list"><li><a href="javascript:" id="2D" shape="rect">D</a>
</li>
<li><a href="javascript:" id="2F" shape="rect">F</a>
</li>
</ul>
<div class="txt txt-last">窗</div>
</div>
<div class="sel-item" id="erdeng2" style="display: none;"><!-- 二等座-->
<div class="txt">窗</div>
<ul class="seat-list"><li><a href="javascript:" id="2A" shape="rect">A</a>
</li>
<li><a href="javascript:" id="2B" shape="rect">B</a>
</li>
<li><a href="javascript:" id="2C" shape="rect">C</a>
</li>
</ul>
<div class="txt">过道</div>
<ul class="seat-list"><li><a href="javascript:" id="2D" shape="rect">D</a>
</li>
<li><a href="javascript:" id="2F" shape="rect">F</a>
</li>
</ul>
<div class="txt txt-last">窗</div>
</div>
<div class="sel-item" id="tedeng2" style="display: none;"><!-- 特等座-->
<div class="txt">窗</div>
<ul class="seat-list"><li><a href="javascript:" id="2A" shape="rect">A</a>
</li>
<li><a href="javascript:" id="2C" shape="rect">C</a>
</li>
</ul>
<div class="txt">过道</div>
<ul class="seat-list"><li><a href="javascript:" id="2F" shape="rect">F</a>
</li>
</ul>
<div class="txt txt-last">窗</div>
</div>
<div class="sel-item" id="shangwu2" style="display: none;"><!-- 商务座-->
<div class="txt">窗</div>
<ul class="seat-list"><li><a href="javascript:" id="2A" shape="rect">A</a>
</li>
</ul>
<div class="txt">过道</div>
<ul class="seat-list"><li><a href="javascript:" id="2F" shape="rect">F</a>
</li>
</ul>
<div class="txt txt-last">窗</div>
</div>
</div>
</div>
<div class="seat-sel seat-sel-round" id="id-bed-sel" style="display: none;"><div class="seat-sel-hd"><div class="tips-xz">选铺喽</div>

		               	 已选铺<span id="selectBedNo">1/4</span>
</div>
<div class="seat-sel-bd"><div class="sel-item"><div class="bed-item"><div class="txt">下铺</div>
<div class="number-control-mini"><a href="javascript:" class="num-reduce" onclick="javascript:numSet(&#39;reduce&#39;,&#39;x_no&#39;);" shape="rect">-</a>
<span class="num" id="x_no">0</span>
<a href="javascript:" class="num-increase" onclick="javascript:numSet(&#39;add&#39;,&#39;x_no&#39;);" shape="rect">+</a>
</div>
</div>
<div class="bed-item" style="display: none;" id="mid_bed"><div class="txt">中铺</div>
<div class="number-control-mini"><a href="javascript:" class="num-reduce" onclick="javascript:numSet(&#39;reduce&#39;,&#39;z_no&#39;);" shape="rect">-</a>
<span class="num" id="z_no">0</span>
<a href="javascript:" class="num-increase" onclick="javascript:numSet(&#39;add&#39;,&#39;z_no&#39;);" shape="rect">+</a>
</div>
</div>
<div class="bed-item"><div class="txt">上铺</div>
<div class="number-control-mini"><a href="javascript:" class="num-reduce" onclick="javascript:numSet(&#39;reduce&#39;,&#39;s_no&#39;);" shape="rect">-</a>
<span class="num" id="s_no">0</span>
<a href="javascript:" class="num-increase" onclick="javascript:numSet(&#39;add&#39;,&#39;s_no&#39;);" shape="rect">+</a>
</div>
</div>
</div>
</div>
</div>
<div id="jy_div" style="display: none;" class="sel-seat-quiet"><input type="checkbox" id="seat-jy" />
<label for="seat-jy">请优先为我分配“静音车厢”席位</label>
<i id="jyalert" class="icon icon-plaint-fill"></i>
</div>
<div id="cj_div" style="display: none;" class="sel-seat-quiet"><input type="checkbox" id="seat-cj" checked="checked" />
<label for="seat-cj">请优先为我分配残疾人专用席位</label>
</div>
<div id="zl_div" style="display: none;" class="sel-seat-quiet"><label for="seat-cj">出发时间和到达时间为车站所在时区时间！</label>
</div>
<p style="color: #FF0000;" id="notice_2_id"><!--  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.根据现行规定，外国人在购买进西藏火车票时，须出示西藏自治区外事办公室或旅游局、商务厅的批准函（电），或者出示中国内地司局级接待单位出具的、已征得自治区上述部门同意的证明信函。台湾同胞赴藏从事旅游、商务活动，须事先向西藏自治区旅游局或商务厅提出申请，购买进藏火车票时须出示有关批准函。-->
</p>
<p style="color: #FF0000;" id="notice_3_id"><!--  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.按现行规定，学生票购票区间必须与学生证上的乘车区间一致，否则车站将不予换票。-->
</p>
<p style="color:#3177BF;" id="notice_4_id"><!--  *购买铁路乘意险的注册用户年龄须在18周岁以上，使用非中国居民身份证注册的用户如购买铁路乘意险，须在<a th:href="@{../modifyUser/initQueryUserInfo}" href="/otsweb/modifyUser/initQueryUserInfo">“我的12306—个人信息”</a>如实填写“出生日期”。<br />
	                 *父母为未成年子女投保，须在<a th:href="@{../view/passengers.html}" href="/otsweb/passengers/init">我的乘车人</a>登记未成年子女的有效身份证件信息。   -->
</p>
<p style="color: #FF0000;" id="notice_5_id"></p>
<p id="sy_ticket_num_id"><!--  尊敬的旅客，本次列车您选择的席别尚有余票<strong>1135</strong>张，无座<strong>840</strong>张。特此提醒。<br /> 请确认信息是否正确。如正确请点击“确定”，系统将为您随机分配席位。-->
</p>
<div class="lay-btn" id="confirmDiv"><a id="back_edit_id" href="javascript:" class="btn92" shape="rect">返回修改</a>
<a href="javascript:" class="btn92s" id="qr_submit_id" shape="rect">确认</a>
</div>
</div>
</div>
</div>
<!-- 提交订单核对车票信息弹出层 end -->
<!-- 交易提示框 start  -->
<div id="transforNotice_id" style="display: none; margin-left: 30%; margin-top: 30%;"><div class="mark"></div>
<div class="up-box" id="content_transforNotice_id"><div class="up-box-hd" id="up-box-hd_id"><!--  <a id="closeTranforDialog_id" style="display: none;" href="javascript:">关闭</a>-->


				提示

				

			</div>
<div class="up-box-bd"><div class="up-con clearfix"><span class="icon i-work" id="iamge_status_id"></span>
<div class="r-txt" id="orderResultInfo_id"><!--  信息提示 -->
</div>
</div>
<div class="lay-btn" id="lay-btn_id"><!-- <a href="javascript:" id="qr_closeTranforDialog_id" style="display: none;" class="btn92s">确认</a> -->
</div>
</div>
</div>
</div>
<!--说明文字 start -->
<div class="srr-tips"><ul><li>请按乘车时所使用的有效身份证件准确、完整填写乘车填写乘车人姓名和证件号码。</li>
<li>如姓名中包含生僻字，可输入汉语拼音代替。<br clear="none" />
例如“李鵢”可输入“李shen”
			</li>
</ul>
</div>
<!--说明文字 end -->
<!--积分支付 提示信息 start -->
<div class="srr-tips"><ul><li>请按乘车时所使用的有效身份证件准确、完整填写乘车人姓名和证件号码。</li>
<li>如姓名中包含生僻字，可输入汉语拼音代替。<br clear="none" />
例如“李燊”可输入“李shen”
			</li>
<li>如您准备使用积分支付票款，请选择本人或受让人作为乘车人。</li>
<li>不支持网银和积分混合支付</li>
</ul>
</div>
<!--积分支付 提示信息 end -->
<!-- 交易提示框 end  -->
<form id="_es_hiddenform" method="post" enctype="application/x-www-form-urlencoded"><input type="hidden" name="_json_att" value="" />
</form>
</body>
</html>
<!-- 页面js模块 -->
<script xml:space="preserve">

/*<![CDATA[*/
           var leftTicketPopCode = '00';
           var country_flag = 'CHN,CHN';
           var service_type = '2';
           var dw_flag = '0,0,0,0,z,0,43,z';
		   var is_jy = 'N';
		   var is_cj = 'N';
           var can_add = 'Y';
           var member_tourFlag = 'dc';
  		   var IsStudentDate=true;
           var init_seatTypes=[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}];

           var defaultTicketTypes=[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u6210\u4EBA\u7968'},{'end_station_name':null,'end_time':null,'id':'2','start_station_name':null,'start_time':null,'value':'\u513F\u7AE5\u7968'},{'end_station_name':null,'end_time':null,'id':'3','start_station_name':null,'start_time':null,'value':'\u5B66\u751F\u7968'},{'end_station_name':null,'end_time':null,'id':'4','start_station_name':null,'start_time':null,'value':'\u6B8B\u519B\u7968'}];

           var init_cardTypes=[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u5C45\u6C11\u8EAB\u4EFD\u8BC1'},{'end_station_name':null,'end_time':null,'id':'K','start_station_name':null,'start_time':null,'value':'\u6E2F\u6FB3\u5C45\u6C11\u5C45\u4F4F\u8BC1'},{'end_station_name':null,'end_time':null,'id':'P','start_station_name':null,'start_time':null,'value':'\u53F0\u6E7E\u5C45\u6C11\u5C45\u4F4F\u8BC1'},{'end_station_name':null,'end_time':null,'id':'H','start_station_name':null,'start_time':null,'value':'\u5916\u56FD\u4EBA\u6C38\u4E45\u5C45\u7559\u8EAB\u4EFD\u8BC1'},{'end_station_name':null,'end_time':null,'id':'A','start_station_name':null,'start_time':null,'value':'\u5916\u56FD\u62A4\u7167'},{'end_station_name':null,'end_time':null,'id':'B','start_station_name':null,'start_time':null,'value':'\u4E2D\u56FD\u62A4\u7167'},{'end_station_name':null,'end_time':null,'id':'C','start_station_name':null,'start_time':null,'value':'\u6E2F\u6FB3\u5C45\u6C11\u6765\u5F80\u5185\u5730\u901A\u884C\u8BC1'},{'end_station_name':null,'end_time':null,'id':'G','start_station_name':null,'start_time':null,'value':'\u53F0\u6E7E\u5C45\u6C11\u6765\u5F80\u5927\u9646\u901A\u884C\u8BC1'}];

           var ticket_seat_codeMap={'3':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}],'2':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}],'1':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}],'4':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}]};

           var ticketInfoForPassengerForm={'cardTypes':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u5C45\u6C11\u8EAB\u4EFD\u8BC1'},{'end_station_name':null,'end_time':null,'id':'K','start_station_name':null,'start_time':null,'value':'\u6E2F\u6FB3\u5C45\u6C11\u5C45\u4F4F\u8BC1'},{'end_station_name':null,'end_time':null,'id':'P','start_station_name':null,'start_time':null,'value':'\u53F0\u6E7E\u5C45\u6C11\u5C45\u4F4F\u8BC1'},{'end_station_name':null,'end_time':null,'id':'H','start_station_name':null,'start_time':null,'value':'\u5916\u56FD\u4EBA\u6C38\u4E45\u5C45\u7559\u8EAB\u4EFD\u8BC1'},{'end_station_name':null,'end_time':null,'id':'A','start_station_name':null,'start_time':null,'value':'\u5916\u56FD\u62A4\u7167'},{'end_station_name':null,'end_time':null,'id':'B','start_station_name':null,'start_time':null,'value':'\u4E2D\u56FD\u62A4\u7167'},{'end_station_name':null,'end_time':null,'id':'C','start_station_name':null,'start_time':null,'value':'\u6E2F\u6FB3\u5C45\u6C11\u6765\u5F80\u5185\u5730\u901A\u884C\u8BC1'},{'end_station_name':null,'end_time':null,'id':'G','start_station_name':null,'start_time':null,'value':'\u53F0\u6E7E\u5C45\u6C11\u6765\u5F80\u5927\u9646\u901A\u884C\u8BC1'}],'isAsync':'1','key_check_isChange':'325CCCCA9B12B800EB3E829D3B041C1DBBD383781C9E781C17B9F48B','leftDetails':['\u786C\u5367(\u4E2D\u94FA \u00A5132.0\u5143  \u4E0B\u94FA \u00A5136.0\u5143  \u4E0A\u94FA \u00A5129.0\u5143 )\u65E0\u7968','\u65E0\u5EA7( \u00A572.0\u5143 )2\u5F20\u7968','\u786C\u5EA7( \u00A572.0\u5143 )\u6709\u7968','\u8F6F\u5367(\u4E0A\u94FA \u00A5197.0\u5143  \u4E0B\u94FA \u00A5204.0\u5143 )\u65E0\u7968'],'leftTicketStr':'msjzlZuDwdjwrtsHstj0G%2Bt3ZWPh6ibujSN0zlerbiVLBL6ObYOPBP5rPXE%3D','limitBuySeatTicketDTO':{'seat_type_codes':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}],'ticket_seat_codeMap':{'3':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}],'2':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}],'1':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}],'4':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u786C\u5EA7'}]},'ticket_type_codes':[{'end_station_name':null,'end_time':null,'id':'1','start_station_name':null,'start_time':null,'value':'\u6210\u4EBA\u7968'},{'end_station_name':null,'end_time':null,'id':'2','start_station_name':null,'start_time':null,'value':'\u513F\u7AE5\u7968'},{'end_station_name':null,'end_time':null,'id':'3','start_station_name':null,'start_time':null,'value':'\u5B66\u751F\u7968'},{'end_station_name':null,'end_time':null,'id':'4','start_station_name':null,'start_time':null,'value':'\u6B8B\u519B\u7968'}]},'maxTicketNum':'9','orderRequestDTO':{'adult_num':0,'append_list_per_ticket':null,'appendix_list_sequence':null,'appidToken':null,'apply_order_no':null,'bed_level_order_num':null,'bureau_code':null,'cancel_flag':null,'card_num':null,'channel':null,'child_num':0,'choose_seat':null,'country_flag':'CHN,CHN','disability_num':0,'dw_flag':'0,0,0,0,z,0,43,z','end_time':{'date':1,'day':4,'hours':8,'minutes':9,'month':0,'seconds':0,'time':540000,'timezoneOffset':-480,'year':70},'exchange_train_flag':'0','from_station_name':'\u90D1\u5DDE','from_station_telecode':'ZZF','get_ticket_pass':null,'id_mode':'Y','isShowPassCode':null,'leftTicketGenTime':null,'orderBatchNo':null,'orderId':null,'order_date':null,'passengerFlag':null,'realleftTicket':null,'reqIpAddress':null,'reqTimeLeftStr':null,'reserve_flag':'A','saleTimeSecond':613420,'seat_detail_type_code':null,'seat_type_code':null,'sequence_no':null,'start_time':{'date':1,'day':4,'hours':0,'minutes':47,'month':0,'seconds':0,'time':-25980000,'timezoneOffset':-480,'year':70},'start_time_str':null,'station_train_code':'K519','student_num':0,'ticket_num':0,'ticket_type_order_num':null,'to_station_name':'\u897F\u5B89','to_station_telecode':'XAY','tour_flag':'dc','trainCodeText':null,'train_date':{'date':1,'day':5,'hours':0,'minutes':0,'month':7,'seconds':0,'time':1753977600000,'timezoneOffset':-480,'year':125},'train_date_str':null,'train_location':null,'train_no':'480000K52202','train_order':null,'trms_train_flag':null,'varStr':null},'purpose_codes':'00','queryLeftNewDetailDTO':{'BXRZ_num':'-1','BXRZ_price':'0','BXYW_num':'-1','BXYW_price':'0','EDRZ_num':'-1','EDRZ_price':'0','EDSR_num':'-1','EDSR_price':'0','ERRB_num':'-1','ERRB_price':'0','GG_num':'-1','GG_price':'0','GR_num':'-1','GR_price':'0','HBRW_num':'-1','HBRW_price':'0','HBRZ_num':'-1','HBRZ_price':'0','HBYW_num':'-1','HBYW_price':'0','HBYZ_num':'-1','HBYZ_price':'0','RW_num':'0','RW_price':'01970','RZ_num':'-1','RZ_price':'0','SRRB_num':'-1','SRRB_price':'0','SWZ_num':'-1','SWZ_price':'0','TDRZ_num':'-1','TDRZ_price':'0','TZ_num':'-1','TZ_price':'0','WZ_num':'2','WZ_price':'00720','WZ_seat_type_code':'1','YB_num':'-1','YB_price':'0','YDRZ_num':'-1','YDRZ_price':'0','YDSR_num':'-1','YDSR_price':'0','YRRB_num':'-1','YRRB_price':'0','YW_num':'0','YW_price':'01290','YYRW_num':'-1','YYRW_price':'0','YZ_num':'28','YZ_price':'00720','ZE_num':'-1','ZE_price':'0','ZY_num':'-1','ZY_price':'0','arrive_time':'0809','arrive_time_local':null,'bed_level_info':'43019704102040330129031013603201320','control_train_day':'','controlled_train_flag':null,'controlled_train_message':null,'country_flag':null,'day_difference':null,'end_station_name':null,'end_station_telecode':null,'from_station_name':'\u90D1\u5DDE','from_station_telecode':'ZZF','infoAll_list':null,'is_support_card':null,'lishi':'07:22','seat_discount_info':'','seat_feature':'','start_station_name':null,'start_station_telecode':null,'start_time':'0047','start_time_local':null,'start_train_date':'','station_train_code':'K519','to_station_name':'\u897F\u5B89','to_station_telecode':'XAY','train_class_name':null,'train_no':'480000K52202','train_seat_feature':'','ypInfoDetail':'1007200028401970000030129000001007203002','yp_ex':''},'queryLeftTicketRequestDTO':{'arrive_time':'08:09','arrive_time_local':'','bed_level_info':'43019704102040330129031013603201320','bigger20':'Y','country_flag':'CHN,CHN','dw_flag':'0,0,0,0,z,0,43,z','exchange_train_flag':'0','from_station':'ZZF','from_station_name':'\u90D1\u5DDE','from_station_no':'07','lishi':'07:22','login_id':null,'login_mode':null,'login_site':null,'purpose_codes':'00','query_type':null,'saleTimeSecond':613420,'seatTypeAndNum':null,'seat_discount_info':'','seat_types':'1431','start_time':'00:47','start_time_begin':null,'start_time_end':null,'start_time_local':'','station_train_code':'K519','ticket_type':null,'to_station':'XAY','to_station_name':'\u897F\u5B89','to_station_no':'09','train_date':'20250801','train_flag':null,'train_headers':null,'train_no':'480000K52202','trms_train_flag':null,'useMasterPool':true,'useWB10LimitTime':true,'usingGemfireCache':false,'ypInfoDetail':'msjzlZuDwdjwrtsHstj0G%2Bt3ZWPh6ibujSN0zlerbiVLBL6ObYOPBP5rPXE%3D'},'tour_flag':'dc','train_location':'H1'};

           var orderRequestDTO={'adult_num':0,'append_list_per_ticket':null,'appendix_list_sequence':null,'appidToken':null,'apply_order_no':null,'bed_level_order_num':null,'bureau_code':null,'cancel_flag':null,'card_num':null,'channel':null,'child_num':0,'choose_seat':null,'country_flag':'CHN,CHN','disability_num':0,'dw_flag':'0,0,0,0,z,0,43,z','end_time':{'date':1,'day':4,'hours':8,'minutes':9,'month':0,'seconds':0,'time':540000,'timezoneOffset':-480,'year':70},'exchange_train_flag':'0','from_station_name':'\u90D1\u5DDE','from_station_telecode':'ZZF','get_ticket_pass':null,'id_mode':'Y','isShowPassCode':null,'leftTicketGenTime':null,'orderBatchNo':null,'orderId':null,'order_date':null,'passengerFlag':null,'realleftTicket':null,'reqIpAddress':null,'reqTimeLeftStr':null,'reserve_flag':'A','saleTimeSecond':613420,'seat_detail_type_code':null,'seat_type_code':null,'sequence_no':null,'start_time':{'date':1,'day':4,'hours':0,'minutes':47,'month':0,'seconds':0,'time':-25980000,'timezoneOffset':-480,'year':70},'start_time_str':null,'station_train_code':'K519','student_num':0,'ticket_num':0,'ticket_type_order_num':null,'to_station_name':'\u897F\u5B89','to_station_telecode':'XAY','tour_flag':'dc','trainCodeText':null,'train_date':{'date':1,'day':5,'hours':0,'minutes':0,'month':7,'seconds':0,'time':1753977600000,'timezoneOffset':-480,'year':125},'train_date_str':null,'train_location':null,'train_no':'480000K52202','train_order':null,'trms_train_flag':null,'varStr':null};

           var init_limit_ticket_num='9';

           var oldTicketDTOs="";

           var oldAllOrder = "";

           var goOrderDTO="";

           var gqComeFrom="";

           var transport_in_SF=false;
           

           if(ticketInfoForPassengerForm.tour_flag==ticket_submit_order.tour_flag.gc){

        	   oldTicketDTOs =null;

        	   oldAllOrder = null;

        	   gqComeFrom=null;
        	   transport_in_SF=null;

               }else if(ticketInfoForPassengerForm.tour_flag==ticket_submit_order.tour_flag.fc){
            	   goOrderDTO=null;

                   }

           $.views.helpers({
       		getUserName : function(name) {
       			 if(name.length>3){
       				name=name.substr(0,3)+'…';
       			 }
       			 return name;
       		},
       		formatForeginTime : function(time,time_new) {
      			 if(time_new){
      				return time_new.substring(8,10) + ":" + time_new.substring(10,12);
      			 }
      			 return time;
      		},
       		isNewChildRule : function(train_date) {
       			if(!train_date){
           			train_date = ticketInfoForPassengerForm.queryLeftTicketRequestDTO.train_date;
               	}
       			train_date = train_date.replace('-', '').replace('-', '')
       			var year = train_date.substring(0,8);
       			if(year >= 20230101){
       				return true;
       			}
       			return false;
      		},
       		formatStationName:function(name){
    	 		if(name.length>5){
    	 			name=name.substr(0,3)+'..';
    			    }
    	 		return name;
    	 	}
       	});
 /*]]>*/

</script>
<script id="checkTicketInfoTemplate" type="text/x-jsrender" xml:space="preserve"><!--

<tr {{if tour_flag==~getTourFlagByKey('fc') || tour_flag==~getTourFlagByKey('gc')}} {{if save_status == "" }}style="display:none;"{{else}}{{/if}}{{else}}{{/if}}>

	<td style="width: 38px; text-align: center;">{{:#index+1}}</td>

    {{if ~isExistWZ(seat_type)}}

				<td style="width: 47px; text-align: center;" class="no-seat">无座</td>

			{{else !~isExistWZ(seat_type)}}

				{{if seat_type_name.indexOf("（")>-1}}
				  	<td style="width: 47px; text-align: center;">{{>seat_type_name.substring(0,seat_type_name.indexOf("（"))}}</td>
				{{else}}
					<td style="width: 47px; text-align: center;">{{>seat_type_name}}</td>
				{{/if}}	

			{{else}}

				Original version only, without subtitles.

			{{/if}}

	<td style="width: 45px; text-align: center;">{{>ticket_type_name}}</td>

	<td style="width: 55px; text-align: center;" title="{{>name}}">{{>~getUserName(name)}}</td>

	<td style="width: 90px; text-align: center;">{{>id_type_name}}</td>

	<td style="width: 130px; text-align: center;">{{>id_no}}</td>

</tr>

-->
</script>
<script id="checkTicketInfoTemplate_choose" type="text/x-jsrender" xml:space="preserve"><!--

<tr {{if tour_flag==~getTourFlagByKey('fc') || tour_flag==~getTourFlagByKey('gc')}} {{if save_status == "" }}style="display:none;"{{else}}{{/if}}{{else}}{{/if}}>

	<td align="center" >{{:#index+1}}</td>
		
	{{if ~isExistWZ(seat_type)}}

			<td class="no-seat">无座</td>

	{{else !~isExistWZ(seat_type)}}
			{{if seat_type_name.indexOf("（")>-1}}
				<td>{{>seat_type_name.substring(0,seat_type_name.indexOf("（"))}}</td>
			{{else}}
				<td>{{>seat_type_name}}</td>
			{{/if}}	
	{{else}}

			Original version only, without subtitles.

	{{/if}}		


    {{if "3" == seat_type}}
		<td>
			<select style="height: 27px;FONT-SIZE: 12px;FONT-FAMILY: '宋体','Verdana';BACKGROUND-COLOR: #FFFFF0;color: #FB7403;MARGIN-LEFT: 3px;" id="ticketype_{{:#index}}">
             	<option value="{{>seat_type}}#{{>ticket_type}}#{{>name}}#{{>id_no}}_0" selected="selected">不限</option>
				<option value="{{>seat_type}}#{{>ticket_type}}#{{>name}}#{{>id_no}}_3">上铺 </option>
				<option value="{{>seat_type}}#{{>ticket_type}}#{{>name}}#{{>id_no}}_2">中铺 </option>
				<option value="{{>seat_type}}#{{>ticket_type}}#{{>name}}#{{>id_no}}_1">下铺 </option>
			</select>
		</td>
	{{else "4" == seat_type}}
		<td>
			<select style="height: 27px;FONT-SIZE: 12px;FONT-FAMILY: '宋体','Verdana';BACKGROUND-COLOR: #FFFFF0;color: #FB7403;MARGIN-LEFT: 3px;"  id="ticketype_{{:#index}}">
             	<option value="{{>seat_type}}#{{>ticket_type}}#{{>name}}#{{>id_no}}_0" selected="selected">不限</option>
				<option value="{{>seat_type}}#{{>ticket_type}}#{{>name}}#{{>id_no}}_3">上铺 </option>
				<option value="{{>seat_type}}#{{>ticket_type}}#{{>name}}#{{>id_no}}_1">下铺 </option>
			</select>
		</td>	
	{{else}}
		<td></td>	
	{{/if}}


	<td>{{>ticket_type_name}}</td>

	<td title="{{>name}}">{{>~getUserName(name)}}</td>

	<td>{{>id_type_name}}</td>

	<td>{{>id_no}}</td>

</tr>

-->
</script>
<script id="ticketTitTemplate" type="text/x-jsrender" xml:space="preserve"><!--

<strong class="mr5">{{>date}}（{{>week}}）</strong><strong class="ml5">{{>station_train_code}}</strong>次<strong

			 title="{{>from_station}}" class="ml5">{{>~formatStationName(from_station)}}</strong>站<strong title="{{>to_station}}">（{{>start_time}}开）—{{>~formatStationName(to_station)}}</strong>站（{{>~formatForeginTime(arrive_time,arrive_time_local)}}到）

-->
</script>
<script id="ticketTitTemplateLong" type="text/x-jsrender" xml:space="preserve"><!--

<strong class="mr5">{{>date}}（{{>week}}）</strong><strong class="ml5">{{>station_train_code}}</strong>次<strong

			 title="{{>from_station}}" class="ml5">{{>from_station}}</strong>站<strong title="{{>to_station}}">（{{>start_time}}开）—{{>to_station}}</strong>站（{{>~formatForeginTime(arrive_time,arrive_time_local)}}到）

-->
</script>
<script id="ticketConTemplate" type="text/x-jsrender" xml:space="preserve"><!--

<span  id="ticket_status_id"  class="{{>wp_statu ? 's2' : 's1'}}">
{{>seat_type_name}}
{{if ticket_price!=""}}（<span class="colorA">{{>ticket_price}}</span>）{{else}}{{/if}}
{{if ticketDisCount!=""}}<span class="colorD">{{>ticketDisCount}}</span>{{else}}{{/if}}
{{>ticket_statu}}</span> 
		

-->
</script>
<script id="djPassengerTemplate" type="text/x-jsrender" xml:space="preserve"><!--

<li>
<input aria-label="按空格键进行操作" title="设置为乘车人，按空格键进行操作" totalTimes="{{>total_times}}" typeFlag="{{>passenger_id_type_code}}"  id="djPassenger_{{>index_id}}"      
{{if passenger_id_type_code=="2"}}
  disabled="disabled" style="color:#999999" title="请修改身份信息"
{{else passenger_id_type_code!="B"}}
  {{if (total_times != "93") && (total_times != "95") && (total_times != "97")  && (total_times != "99")}} 
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{/if}}   
{{else}}
  {{if (country_code=="CN") && (total_times != "93") && (total_times != "95") && (total_times != "97") && (total_times != "99")}}
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{else (country_code!="CN") && (total_times != "93") && (total_times != "98") && (total_times != "99")&& (total_times != "97") && (total_times != "91")}} 
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{/if}} 
{{/if}}

{{if (~getCurrentUserIdType()!=~getIdType('one'))&&(~getCurrentUserIdType()!=~getIdType('two'))}}  
  {{if (passenger_id_type_code==~getIdType('one'))||(passenger_id_type_code==~getIdType('two'))}}  disabled="disabled"
  {{else}}
  {{/if}} 
{{else}}
{{/if}}    type="checkbox" class="check"   /><label 
{{if passenger_id_type_code=="2"}}
  disabled="disabled" style="color:#999999" title="请修改身份信息"
{{else passenger_id_type_code!="B"}}
  {{if (total_times != "93") && (total_times != "95") && (total_times != "97")  && (total_times != "99")}} 
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{/if}}   
{{else}} 
  {{if (country_code=="CN") && (total_times != "93") && (total_times != "95") && (total_times != "97") && (total_times != "99")}}
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{else (country_code!="CN") && (total_times != "93") && (total_times != "98") && (total_times != "99")&& (total_times != "97") && (total_times != "91")}} 
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{/if}} 
{{/if}} >{{>~getSuitName(passenger_name, (passenger_type == ~getTicketType('student')?true:false))}}</label>
</li>

-->
</script>
<script id="normalPassengerTemplate" type="text/x-jsrender" xml:space="preserve"><!--

<li>
<input aria-label="按空格键进行操作" title="设置为乘车人，按空格键进行操作" totalTimes="{{>total_times}}" allencstr="{{>allEncStr}}" typeFlag="{{>passenger_id_type_code}}" id="normalPassenger_{{>index_id}}"      
{{if passenger_id_type_code=="2"}}
  disabled="disabled" style="color:#999999" title="请修改身份信息"
{{else}}
  {{if (total_times != "93") && (total_times != "95") && (total_times != "97")  && (total_times != "99")}} 
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{/if}}   
{{else}} 
  {{if (country_code=="CN") && (total_times != "93") && (total_times != "95") && (total_times != "97") && (total_times != "99")}}
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{else (country_code!="CN") && (total_times != "93") && (total_times != "98") && (total_times != "99")&& (total_times != "97") && (total_times != "91")}} 
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{/if}}   
{{/if}}

{{if (~getCurrentUserIdType()!=~getIdType('one'))&&(~getCurrentUserIdType()!=~getIdType('two'))&&(~getCurrentUserIdType()!=~getIdType('work'))}}  
  {{if (passenger_id_type_code==~getIdType('one'))||(passenger_id_type_code==~getIdType('two'))||(passenger_id_type_code==~getIdType('work'))}}  
	 disabled="disabled" title="不允许为该乘车人购票"
  {{/if}} 
{{/if}}    type="checkbox" class="check"   /><label 
{{if passenger_id_type_code=="2"}}
  disabled="disabled" style="color:#999999" title="请修改身份信息"
{{else passenger_id_type_code!="B"}}
  {{if (total_times != "93") && (total_times != "95") && (total_times != "97") && (total_times != "99")}} 
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{/if}}   
{{else}} 
  {{if (country_code=="CN") && (total_times != "93") && (total_times != "95") && (total_times != "97") && (total_times != "99")}}
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{else (country_code!="CN") && (total_times != "93") && (total_times != "98") && (total_times != "99") && (total_times != "97")&& (total_times != "91")}} 
     disabled="disabled" style="color:#999999" title="请修改身份信息"
  {{/if}}   
{{/if}} 
{{if (~getCurrentUserIdType()!=~getIdType('one'))&&(~getCurrentUserIdType()!=~getIdType('two'))&&(~getCurrentUserIdType()!=~getIdType('work'))}}  
  {{if (passenger_id_type_code==~getIdType('one'))||(passenger_id_type_code==~getIdType('two'))||(passenger_id_type_code==~getIdType('work'))}}  
	 style="color:#999999" title="不允许为该乘车人购票"
  {{else}}
  {{/if}} 
{{else}}
{{/if}}>{{>~getSuitName(passenger_name, (passenger_type == ~getTicketType('student')?true:false))}}</label>
</li>

-->
</script>
<script id="ticketInfoTemplate" type="text/x-jsrender" xml:space="preserve"><!--

<tr id="tr_id_{{:#index+1}}">
				<td align="center">{{:#index+1}}</td>

						<td {{if (tour_flag == ~getTourFlagByKey('gc'))||(tour_flag == ~getTourFlagByKey('fc'))}} title="不允许变更票种信息" {{else}}{{/if}}>

    <select id="ticketType_{{:#index+1}}" name="confirmTicketType" onchange="javascript:updateSeatTypeByeTickeType(this);" {{if (tour_flag == ~getTourFlagByKey('gc') || tour_flag ==~getTourFlagByKey('fc')) ||isAccompanyChild }} {{if isDisabled}}  disabled="disabled" style="color:#999999"{{else}}{{/if}}{{else}}{{/if}} >

                          {{for ticketTypes}}

 			{{if id==#parent.parent.data.ticket_type&&(#parent.parent.parent.data.IsStudentDate==true||id!=3)}}
				<option name="ticket_type_option" value="{{>id}}" selected="selected" >{{>value}}</option>
			{{else  id!=#parent.parent.data.ticket_type||id==3}}

				 <option value="{{>id}}">{{>value}} </option>

			{{else}}

			{{/if}}

				         

            {{else}}

            {{/for}}

</select>

                        </td>

			<td><select style="width:151px;" onclick="javascript:stepFirValidatorTicketInfo(true);" id="seatType_{{:#index+1}}">

                         {{for seatTypes}}

             {{if id==#parent.parent.data.seat_type}}
				<option value="{{>id}}" selected="selected" >
                  {{if (null!=~seatTypePriceForSeatName(value))&&(""!=~seatTypePriceForSeatName(value))}}
                   {{>value}}（{{>~seatTypePriceForSeatName(value)}}） 
                  {{else}}
                   {{>value}}
                  {{/if}}
                </option>

			{{else  id!=#parent.parent.data.seat_type}}

				<option value="{{>id}}" >
                  {{if (null!=~seatTypePriceForSeatName(value))&&(""!=~seatTypePriceForSeatName(value))}}
                   {{>value}}（{{>~seatTypePriceForSeatName(value)}}）
                  {{else}}
                   {{>value}}
                  {{/if}}
                </option>

			{{else}}

				Original version only, without subtitles.

			{{/if}}

				

            {{else}}

            {{/for}}

             </select>

                         </td>

						<td {{if (tour_flag == ~getTourFlagByKey('gc'))||(tour_flag == ~getTourFlagByKey('fc'))}}title="不允许变更乘车人信息"{{else}}{{/if}}><div class="pos-rel"><input onkeyup="javascript:elemOnkeyupNotice(this);"  id="passenger_name_{{:#index+1}}" class="inptxt w110" value="{{>name}}"   {{if isDisabled || ~isCanAdd()=="N" ||(#data.ticket_type==2)}}  disabled="disabled" title="不允许变更乘车人信息"  {{else}} {{/if}}  size="12" maxlength="20"/><div class="w110-focus" id="passenger_name_{{:#index+1}}_notice"></div></div></td>


						<td {{if (tour_flag == ~getTourFlagByKey('gc'))||(tour_flag == ~getTourFlagByKey('fc'))}}title="不允许变更乘车人信息"{{else}}{{/if}}><select id="passenger_id_type_{{:#index+1}}"  {{if isDisabled || ~isCanAdd()=="N" ||(#data.ticket_type==2)}}  disabled="disabled" title="不允许变更乘车人信息"  style="color:#999999"  {{else}} {{/if}} >

                       {{for cardTypes ~id_type_name=id_type_name}}

 {{if id == #parent.parent.data.id_type}}

				<option value="{{>id}}" selected="selected" >{{if ~id_type_name ne ''}} {{>~id_type_name}} {{else}} {{>value}} {{/if}}</option>

			{{else  id!=#parent.parent.data.id_type}}

				 <option value="{{>id}}">{{>value}}</option>

			{{else}}

			{{/if}}

				

           {{else}}

           {{/for}}

        </select>

             </td>

<td {{if (tour_flag == ~getTourFlagByKey('gc'))||(tour_flag == ~getTourFlagByKey('fc'))}} title="不允许变更乘车人信息"{{else}}{{/if}}><div class="pos-rel"><input onkeyup="javascript:elemOnkeyupNotice(this);"  id="passenger_id_no_{{:#index+1}}" class="inptxt w160" value="{{>id_no}}"   {{if isDisabled || ~isCanAdd()=="N" ||(#data.ticket_type==2)}}  disabled="disabled" title="不允许变更乘车人信息"   {{else}} {{/if}}   size="20" maxlength="35"/><div class="w160-focus" id="passenger_id_no_{{:#index+1}}_notice"></div></div></td>


 {{if tour_flag == ~getTourFlagByKey('gc') }}
<td>
	<input id="save_{{:#parent.index+1}}" onclick="javascript:updateAllCheckBox()" type="checkbox" class="check"  {{>#parent.data.save_status}}    /> 
     {{if ~isChangeStation() == '0' }}
                变更到站
	 {{/if}}
	{{if ~isChangeStation() == '1' }}
                改签
	 {{/if}}
	{{if ~isChangeStation() == '2' }}
                灵活行
	 {{/if}}
      
</td>
			{{else  tour_flag==~getTourFlagByKey('fc')}}
<td>
			<input id="save_{{:#parent.index+1}}" onclick="javascript:updateAllCheckBox()" type="checkbox" class="check"  {{>#parent.data.save_status}} /> 

                返程
</td>
            {{else}}


			{{else}}

			{{/if}}
{{if ((tour_flag ==  ~getTourFlagByKey('dc')  || tour_flag  == ~getTourFlagByKey('wc')) && (#data.id_no!="") && (#data.ticket_type==1|| #data.ticket_type==4)) && !~isNewChildRule() }}
	<td title="添加儿童票">
		<a href="javascript:" onClick="javascript:addChildPassengerInfo(this);" id="addchild_{{:#parent.index+1}}" name="addchild_{{>only_id}}">添加儿童票 
		</a>
		
	</td>
{{else}}
	<td style="width:40;">
		<a aria-label="占位符" href="javascript:" id="addchild_{{:#parent.index+1}}" name="addchild_{{>only_id}}"></a>
	</td>
{{/if}}

{{if tour_flag ==  ~getTourFlagByKey('dc')  || tour_flag  == ~getTourFlagByKey('wc') }}

<td {{if (tour_flag == ~getTourFlagByKey('dc'))||(tour_flag == ~getTourFlagByKey('wc'))}}title="删除乘车人"{{else}}{{/if}}>

<span aria-label="点击删除乘车人" onkeydown="javascript:delPasskeydown(this,event);" tabindex="0" class="i-del"  onClick="javascript:delPassengerInfo(this);" id="del_{{:#parent.index+1}}_{{>only_id}}" ></span>

</td>
{{else}}
 <td style="display:none;">

 <span  id="del_{{:#parent.index+1}}_{{>only_id}}" ></span>

</td>
{{/if}}

		</tr>

   <tr id="tr_id_{{:#index+1}}_check" class="tips"  style="display:none" >

                    <td colspan="1">&nbsp;</td>

                    <td colspan="2"><span class="txt-wrong" style="display:none" id="seatType_{{:#index+1}}_check">请输入旅客姓名</span></td>

                    <td colspan="2"><span class="txt-wrong" style="display:none" id="passenger_name_{{:#index+1}}_check">请输入旅客姓名</span></td>

                    <td colspan="1"><span class="txt-wrong" style="display:none" id="passenger_id_no_{{:#index+1}}_check">请输入旅客姓名</span></td>

  </tr>

-->
</script>
<script id="ticketInfoTemplateForTrms" type="text/x-jsrender" xml:space="preserve"><!--

<tr id="tr_id_{{:#index+1}}">
				<td align="center">{{:#index+1}}</td>

						<td {{if (tour_flag == ~getTourFlagByKey('gc'))||(tour_flag == ~getTourFlagByKey('fc'))}} title="不允许变更票种信息" {{else}}{{/if}}>

    <select id="ticketType_{{:#index+1}}" name="confirmTicketType" onchange="javascript:updateSeatTypeByeTickeType(this);" {{if (tour_flag == ~getTourFlagByKey('gc') || tour_flag ==~getTourFlagByKey('fc')) ||isAccompanyChild }} {{if isDisabled}}  disabled="disabled" style="color:#999999"{{else}}{{/if}}{{else}}{{/if}} >

                          {{for ticketTypes}}

 			{{if id==#parent.parent.data.ticket_type&&(#parent.parent.parent.data.IsStudentDate==true||id!=3)}}
				<option name="ticket_type_option" value="{{>id}}" selected="selected" >{{>value}}</option>
			{{else  id!=#parent.parent.data.ticket_type||id==3}}

				 <option value="{{>id}}">{{>value}} </option>

			{{else}}

			{{/if}}

				         

            {{else}}

            {{/for}}

</select>

                        </td>

			<td><div class="seat-select">
				</div>
            </td>

						<td {{if (tour_flag == ~getTourFlagByKey('gc'))||(tour_flag == ~getTourFlagByKey('fc'))}}title="不允许变更乘车人信息"{{else}}{{/if}}><div class="pos-rel"><input onkeyup="javascript:elemOnkeyupNotice(this);"  id="passenger_name_{{:#index+1}}" class="inptxt w110" value="{{>name}}"   {{if isDisabled || ~isCanAdd()=="N" ||(#data.ticket_type==2)}}  disabled="disabled" title="不允许变更乘车人信息"  {{else}} {{/if}}  size="12" maxlength="20"/><div class="w110-focus" id="passenger_name_{{:#index+1}}_notice"></div></div></td>


						<td {{if (tour_flag == ~getTourFlagByKey('gc'))||(tour_flag == ~getTourFlagByKey('fc'))}}title="不允许变更乘车人信息"{{else}}{{/if}}><select id="passenger_id_type_{{:#index+1}}"  {{if isDisabled || ~isCanAdd()=="N" ||(#data.ticket_type==2)}}  disabled="disabled" title="不允许变更乘车人信息"  style="color:#999999"  {{else}} {{/if}} >

                       {{for cardTypes ~id_type_name=id_type_name}}

 {{if id == #parent.parent.data.id_type}}

				<option value="{{>id}}" selected="selected" >{{if ~id_type_name ne ''}} {{>~id_type_name}} {{else}} {{>value}} {{/if}}</option>

			{{else  id!=#parent.parent.data.id_type}}

				 <option value="{{>id}}">{{>value}}</option>

			{{else}}

			{{/if}}

				

           {{else}}

           {{/for}}

        </select>

             </td>

<td {{if (tour_flag == ~getTourFlagByKey('gc'))||(tour_flag == ~getTourFlagByKey('fc'))}} title="不允许变更乘车人信息"{{else}}{{/if}}><div class="pos-rel"><input onkeyup="javascript:elemOnkeyupNotice(this);"  id="passenger_id_no_{{:#index+1}}" class="inptxt w160" value="{{>id_no}}"   {{if isDisabled || ~isCanAdd()=="N" ||(#data.ticket_type==2)}}  disabled="disabled" title="不允许变更乘车人信息"   {{else}} {{/if}}   size="20" maxlength="35"/><div class="w160-focus" id="passenger_id_no_{{:#index+1}}_notice"></div></div></td>


 {{if tour_flag == ~getTourFlagByKey('gc') }}
<td>
	<input id="save_{{:#parent.index+1}}" onclick="javascript:updateAllCheckBox()" type="checkbox" class="check"  {{>#parent.data.save_status}}    /> 
     {{if ~isChangeStation() == '0' }}
                变更到站
	 {{/if}}
	{{if ~isChangeStation() == '1' }}
                改签
	 {{/if}}
	{{if ~isChangeStation() == '2' }}
                灵活行
	 {{/if}}
      
</td>
			{{else  tour_flag==~getTourFlagByKey('fc')}}
<td>
			<input id="save_{{:#parent.index+1}}" onclick="javascript:updateAllCheckBox()" type="checkbox" class="check"  {{>#parent.data.save_status}} /> 

                返程
</td>
            {{else}}


			{{else}}

			{{/if}}
{{if ((tour_flag ==  ~getTourFlagByKey('dc')  || tour_flag  == ~getTourFlagByKey('wc')) && (#data.id_no!="") && (#data.ticket_type==1|| #data.ticket_type==4)) && !~isNewChildRule() }}
	<td title="添加儿童票">
		<a href="javascript:" onClick="javascript:addChildPassengerInfo(this);" id="addchild_{{:#parent.index+1}}" name="addchild_{{>only_id}}">添加儿童票 
		</a>
		
	</td>
{{else}}
	<td style="width:40;">
		<a href="javascript:" id="addchild_{{:#parent.index+1}}" name="addchild_{{>only_id}}"></a>
	</td>
{{/if}}

{{if tour_flag ==  ~getTourFlagByKey('dc')  || tour_flag  == ~getTourFlagByKey('wc') }}

<td {{if (tour_flag == ~getTourFlagByKey('dc'))||(tour_flag == ~getTourFlagByKey('wc'))}}title="删除乘车人"{{else}}{{/if}}>

 <span	class="i-del"  onClick="javascript:delPassengerInfo(this);" id="del_{{:#parent.index+1}}_{{>only_id}}" ></span>

</td>
{{else}}
 <td style="display:none;">

 <span  id="del_{{:#parent.index+1}}_{{>only_id}}" ></span>

</td>
{{/if}}

		</tr>

   <tr id="tr_id_{{:#index+1}}_check" class="tips"  style="display:none" >

                    <td colspan="1">&nbsp;</td>

                    <td colspan="2"><span class="txt-wrong" style="display:none" id="seatType_{{:#index+1}}_check">请输入旅客姓名</span></td>

                    <td colspan="2"><span class="txt-wrong" style="display:none" id="passenger_name_{{:#index+1}}_check">请输入旅客姓名</span></td>

                    <td colspan="1"><span class="txt-wrong" style="display:none" id="passenger_id_no_{{:#index+1}}_check">请输入旅客姓名</span></td>

  </tr>

-->
</script>
<script id="oldTicketInfoForGcTemplate" type="text/x-jsrender" xml:space="preserve"><!--
<tr>
<td>{{:#index+1}}</td>

<td>{{>train_date}}  {{>start_time}}开<br />{{>station_train_code}}{{>from_station}}-{{>to_station}}</td>

<td>{{>seat_type_name}} {{>coach_name}}车厢<br />{{>seat_name}} </td>

<td>{{>passenger_name}}<br />{{>id_type_name}}</td>

<td>{{>ticket_type_name}}<br /><span class="colorA">{{>ticket_price}}元</span></td>

</tr>

-->
</script>
'''
    print(html_prase(html))
