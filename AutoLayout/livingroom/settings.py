# _*_ coding:utf-8 _*_
import AutoLayout.settings as settings
import math
LIVINGROOM_MAX_LEN = 10600
LIVINGROOM_MIN_LEN = 3100
# 电视柜
LIVINGROOM_TV_BENCH_LEN = 450
LIVINGROOM_TV_BENCH_WIDTH = (1500, 1800, 2100, 2400, 2700, 3000, 3200, 3300, 3400)
# 电视柜和茶几最小距离
DIS_TVBEN_TEA_MIN = 600
# 沙发、茶几距离
DIS_SOFA_TEA = 300
# L型沙发
SOFAL_L1_L2 = {2200:1600, 2600:1800, 3000:1800, 3300:1920, 3600:2000}
SOFAL_L3 = 900
SOFAL_L4 = 900
# 1字沙发, 三人
SOFA1_LEN = 750
SOFA1_WIDTH = (1800, 2100, 2400)
# 边几
SIDE_TABLE_WIDTH = (450, 500, 550, 600)
SIDE_TABLE_LEN = 450
# 茶几
REC_TEA_WIDTH_LEN = {600:450, 750:600, 1200:600, 1500:600, 1800:800}
SQUARE_TEA_WIDTH_LEN = {600:600, 750:750, 900:900, 1050:1050,1200:1200,1350:1350}
CIRCLE_TEA_WIDTH_LEN = {600:600, 750:750, 900:900, 1050:1050,1200:1200}
# 电视柜和茶几最小距离below
DIS_TVBEN_TEA_MIN = 600
# 沙发、茶几最小距离below
DIS_SOFA_TEA = 300
# 边几below
SIDE_TABLE_WIDTH = (450, 500, 550, 600)
SIDE_TABLE_LEN = 450
#地毯
CARPET_WIDTH_LEN = {1500:2400, 1800:2700 , 2400:3000, 2700:3600, 3000:4200}
# 沙发茶几区
alist0 = list(REC_TEA_WIDTH_LEN.values())
alist0[-1:-1] = list(SQUARE_TEA_WIDTH_LEN)
alist0[-1:-1] = list(CIRCLE_TEA_WIDTH_LEN)
SOFAANDTEA_MAX_LEN = max(alist0) + max(SOFAL_L4, SOFA1_LEN) + DIS_SOFA_TEA
SOFAANDTEA_MIN_LEN = min(alist0) + min(SOFAL_L4, SOFA1_LEN) + DIS_SOFA_TEA
SOFAL_WIDTH_THREATHOLD = min(SOFAL_L1_L2.keys())
SOFA1_WIDTH_THREATHOLD = min(SOFA1_WIDTH)
# 单椅斜向60度放置
CHAIR_ANGLE = 60
rad = math.radians(60)
wid0 = int(settings.CHAIR_WIDTH * math.sin(rad) + settings.CHAIR_LEN * math.cos(rad))
len0 = int(settings.CHAIR_WIDTH * math.cos(rad) + settings.CHAIR_LEN * math.sin(rad))
OBLIQUE_CHAIR_WIDTH_LEN = (wid0, len0)
# 单椅距离电视柜？ mm，到茶几距离？
OB_CHAIR_DIS_TV_BENCH = 300
OB_CHAIR_DIS_TEA_END = 600
OB_CHAIR_DIS_TEA_SIDE = 300
#门靠客厅区域预留站人的地方900*900
DOUBLE_LEN = 900