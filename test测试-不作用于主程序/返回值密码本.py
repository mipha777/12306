
def deal(data):
    fields = data.split('|')
    field_index_map = {
        3: '车次',
        8: '出发时间',
        9: '到达时间',
        10: '历时',
        11: '能否预定',
        32: '商务座/特等座',
        31: '一等座',
        30: '二等座',
        29: '硬座',
        28: '硬卧/二等卧',
        27: '软座',
        26: '无座',
        25: '其他',
        23: '软卧/动卧/一等卧',
        21: '高级软卧',
        20: '优选一等座'
    }

    for i in range(len(fields)):
        if  0<= i :
            print( i,'-->',fields[i] ,'|',end='')
    print()


if __name__ == '__main__':
    data=["zv3%2FMHmdeQAXwuslfURd2IUl3F38b71ZobspJSBC2wz68m6cA%2FQuE%2BmzwPfMVdqHKaL4yfxO1Ek8%0A%2BBMupBh9EpfzC6lKmU6oWMcQPrVdEl9WHl66DsvRhVEdCfl4XJFGq4Ds%2B677eQuUVjINa7XgsIuq%0Ank%2BWx0FfmjWzOp%2BA0vtGAnA%2B2%2FLUa8HRdSGqnlCvkEvqx4Gfh2VAKTEryp2N7hRaNJ28ddYxU786%0AJoCuQFhXQRKXTATn7k%2FUaV16GOh6Fq%2BR%2FZ%2FOgkLogpOjZUh%2Bqvh7cMPwIeiOfbhtABYuLkZVBSwe%0AU7s%2F6hAuS3V0AADHH8GPQ%2B9S2dS7aPA3n5DgYC3YDpJtZCw5f1PrrLXzfUY%3D|预订|390000Z2920H|Z293|WCN|WAR|ZZF|XAY|00:34|06:32|05:58|N|5w9rTMpaJSrjgpoJRZRbzpMjWGCJoKZZx7qQ1JVNLm7Kd7o%2FKqt5cC0CnEwN2Qcp9%2FTi%2FMdztGU%3D|20250802|3|N3|07|09|1|0||||无|无||无||无|无|||||30402010W0|34211|0|1||30129000004019700000201130000010072000001007203000|0|||||1|0#0#0#0#z#0#34#z|||CHN,CHN|||N#N#|33012903101360320132043019704102040||202507201515|Y|",
      "q%2FnzhlVldmICic3P5dyrP%2BCWxX4qN8KsfiXIUkvjIG68XpZvWomF0mXIHzULmdKSBaOh01jEiXQZ%0AeFtFfDnFU1gijYT3CuGLi8X1vbagTkNyJ7p4TmSfnER2IUKFO%2BOdjc6KdYuXG67%2FC9ZCiaSOvaVn%0AHguUoiiXhXlDiOs1SM3%2BNVYsQ6VQoL3uQRkQAoq8BjjlE1UKIUyo4sd0Wr%2FTVoW9NuMIsdL%2FZdZS%0AWQM1cxGFWIwZrMq%2BPR5u8fl4CPFwcPdFsX%2B6dyADjuX2wBEdU9JuPaco1%2FDPpFycB7KyG6WtbPl2%0A2o%2B0XWH0iX%2BaXzud738j2fmgGgbNxbRC%2FaxEIbsO5xlmtvML|预订|480000K52202|K519|UKH|BJY|ZZF|XAY|00:47|08:09|07:22|Y|7yNhrACyukxXn7U4DIqnAfUJMVJFlVrNp3hI5qCXFAag6i2rHjNSvouK%2FLw%3D|20250802|3|H1|07|09|1|0||||无|||无||无|11|||||104030W0|1431|0|1||1007200011401970000030129000001007203000|0|||||1|0#0#0#0#z#0#43#z|||CHN,CHN|||N#N#|43019704102040330129031013603201320||202507201515|Y|"]


    for i in data:
        deal(i)




'''
1 | 预订               | 操作按钮显示内容
2 | 240000G1011F      | 车次编号（内部ID）
3 | G101              | 车次名称
4 | VNP               | 出发站（站点代码）
5 | AOH               | 到达站（站点代码）
6 | VNP               | 出发站（显示）
7 | AOH               | 到达站（显示）
8 | 06:10             | 出发时间
9 | 12:09             | 到达时间
10| 05:59             | 历时
11| Y                 | 是否可订（Y = 是）
12| ....              | 一大串加密信息（token）
13| 20250801          | 乘车日期
14| 3                 | 可用席位数（某种座位）
15| P2                | 出发站序号
16| 01                | 到达站序号
17| 11                | 列车类型
18| 1                 | 是否有票（1=有）
...
'''