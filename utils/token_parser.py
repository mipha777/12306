import re

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


    return repeatsubmittoken ,keycheckisChange,train_location,TicketStr


if __name__ == '__main__': # 测试入口
    html = ''' '''
    print(html_prase(html))
