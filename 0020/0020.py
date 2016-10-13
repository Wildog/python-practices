# -*- coding: utf-8 -*-
# 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。

from pyexcel_xls import get_data
from collections import defaultdict
import re

def time_fmt(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    w, d = divmod(d, 7)
    units = ['w', 'd', 'h', 'm', 's']
    parts = [str(eval(unit)) + str(unit) for unit in units if eval(unit) > 0]
    time = ' '.join(parts)
    return time

def get_stat(file):
    data = get_data(file)
    sheet = data.values()[0]
    stat = defaultdict(lambda: defaultdict(lambda: {'duration': 0, 'fee': 0}))
    stat_sum = {'duration': 0, 'fee': 0}
    for rn, row in enumerate(sheet):
        if rn == 0:
            continue
        date = row[2].split()[0]
        calltype = row[4]
        number = row[5]
        place = row[8]
        fee = float(row[-1])
        dul = re.findall('\d+', row[3])
        duration, multipliers = 0, [1, 60, 60]
        for i, part in enumerate(reversed(dul)):
            part = int(part) * multipliers[i]
            duration += part
        stat_sum['duration'] += duration
        stat_sum['fee'] += fee
        stat['by_place'][place]['duration'] += duration
        stat['by_place'][place]['fee'] += fee
        stat['by_number'][number]['duration'] += duration
        stat['by_number'][number]['fee'] += fee
        stat['by_date'][date]['duration'] += duration
        stat['by_date'][date]['fee'] += fee
        stat['by_calltype'][calltype]['duration'] += duration
        stat['by_calltype'][calltype]['fee'] += fee

    print '总计通话: %s, 总计费用: %.2f元' % (time_fmt(stat_sum['duration']), stat_sum['fee'])
    print '按呼叫类型:'
    for calltype, perstat in stat['by_calltype'].items():
        print '呼叫类型: %s, 总计通话: %s, 总计费用: %.2f元' % (calltype.encode('utf8'), time_fmt(perstat['duration']), perstat['fee'])
    print '按通话类型:'
    for place, perstat in stat['by_place'].items():
        print '通话类型: %s, 总计通话: %s, 总计费用: %.2f元' % (place.encode('utf8'), time_fmt(perstat['duration']), perstat['fee'])
    print '按日期:'
    for place, perstat in stat['by_date'].items():
        print '日期: %s, 总计通话: %s, 总计费用: %.2f元' % (date.encode('utf8'), time_fmt(perstat['duration']), perstat['fee'])
    print '按通话号码:'
    for number, perstat in stat['by_number'].items():
        print '通话号码: %s, 总计通话: %s, 总计费用: %.2f元' % (number.encode('utf8'), time_fmt(perstat['duration']), perstat['fee'])

if __name__ == '__main__':
    get_stat('stat.xls')
