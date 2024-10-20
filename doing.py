from datetime import datetime

def scan_num(l):
    if type(l) is str:
        return False
    else:
        return True

filter_start = datetime.now()
r = filter(scan_num, [1,2,3,'',0])
filter_end = datetime.now()
print("filter time: ",filter_end-filter_start)


def loop():
    result = []
    for items in [1,2,3,'',0]:
        if type(items) is str:
            pass
        else:
            result.append(items)
loop_start = datetime.now()
loop_res = loop()
loop_end = datetime.now()
print("loop time: ",loop_end-loop_start)


l = [1,2,3,'',0]
com_start = datetime.now()
list_comp = [items for items in l if type(items) is not str]
com_end = datetime.now()
print("list comp time: ",com_end-com_start)