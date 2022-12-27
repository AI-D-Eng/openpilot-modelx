# flake8: noqa

from collections import namedtuple
from selfdrive.car import dbc_dict
from cereal import car
from selfdrive.car.modules.CFG_module import load_bool_param

Button = namedtuple('Button', ['event_type', 'can_addr', 'can_msg', 'values'])
AngleRateLimit = namedtuple('AngleRateLimit', ['speed_points', 'max_angle_diff_points'])

class CAR:
  AP2_MODELS = 'TESLA AP2 MODEL S'
  AP1_MODELS = 'TESLA AP1 MODEL S'
  PREAP_MODELS = 'TESLA MODEL S'
  AP1_MODELX = 'TESLA AP1 MODEL X'
  AP2_MODELX = 'TESLA AP2 MODEL X'


FINGERPRINTS = {
  # ap2.5 2017
  CAR.AP2_MODELX: [
    {


    },
  ],

  CAR.AP2_MODELS: [
    {
      1: 8, 3: 8, 14: 8, 21: 4, 69: 8, 109: 4, 257: 3, 264: 8, 267: 5, 277: 6, 280: 6, 283: 5, 293: 4, 296: 4, 309: 5, 325: 8, 328: 5, 336: 8, 341: 8, 357: 8, 360: 7, 373: 8, 389: 8, 390: 7, 415: 8, 513: 5, 516: 8, 518: 8, 520: 4, 522: 8, 523: 7, 524: 8, 525: 4, 526: 8, 527: 8, 529: 8, 532: 3, 536: 8, 537: 3, 539: 8, 542: 8, 545: 8, 546: 2, 551: 5, 552: 2, 556: 8, 558: 8, 568: 8, 569: 8, 574: 8, 577: 8, 582: 5, 583: 8, 584: 4, 585: 8, 590: 8, 601: 8, 606: 8, 608: 1, 622: 8, 627: 6, 638: 8, 641: 8, 643: 8, 660: 5, 665: 8, 692: 8, 693: 8, 695: 8, 696: 8, 697: 8, 699: 8, 700: 8, 701: 8, 702: 8, 703: 8, 704: 8, 708: 8, 709: 8, 710: 8, 711: 8, 712: 8, 728: 8, 744: 8,         760: 8, 771: 2, 772: 8, 775: 8, 776: 8, 777: 8, 778: 8, 780: 2, 781: 8, 782: 8,         785: 8, 787: 8, 788: 8, 791: 8, 792: 8, 796: 2, 797: 8, 798: 6, 799: 8, 804: 8, 805: 8, 807: 8, 808: 1, 809: 8, 811: 8, 812: 8, 813: 8, 814: 5, 815: 8, 820: 8, 823: 8, 824: 8, 829: 8, 830: 5, 831:8,  836: 8, 840: 8, 841: 8, 843: 8, 845: 8, 846: 5, 848: 8, 849: 8, 852: 8, 853: 8, 856: 4, 857: 6, 859: 8, 861: 8, 862: 5, 863: 8, 872: 8,         875: 8, 876: 8, 877: 8, 878: 8, 879: 8, 880: 8, 882: 8, 884: 8, 888: 8, 889: 8, 893: 8, 894: 8, 896: 8, 901: 6, 904: 3, 905: 8, 906: 8, 907: 8, 908: 2, 909: 8, 910: 8, 912: 8, 920: 8, 921: 8, 925: 4, 926: 6, 936: 8,         941: 8, 949: 8, 952: 8, 953: 6, 957: 8, 968: 8, 969: 6, 970: 8, 971: 8, 973: 8, 977: 8, 984: 8, 986: 8, 987: 8, 989: 8, 990: 8, 1000: 8, 1001: 8, 1006: 8, 1007: 8, 1008: 8, 1010: 6, 1014: 1, 1015: 8, 1016: 8, 1017: 8, 1018: 8, 1019: 5, 1020: 8, 1026: 8, 1028: 8, 1029: 8, 1030: 8, 1032: 1, 1033: 1, 1034: 8, 1035: 6, 1048: 1, 1049: 8, 1061: 8, 1064: 8, 1065: 8, 1070: 8, 1080: 8, 1081: 8, 1097: 8, 1113: 8, 1129: 8, 1145: 8, 1160: 4, 1177: 8, 1281: 8, 1291: 8, 1307: 8, 1328: 8, 1329: 8, 1332: 8, 1335: 8, 1337: 8, 1339: 2, 1353: 8, 1361: 6, 1362: 6, 1368: 8, 1412: 8,                   1436: 8,          1456: 8, 1463: 8, 1465: 8, 1469: 8, 1476: 8, 1481: 8, 1486: 8, 1497: 8, 1513: 8, 1519: 8, 1521: 8, 1524: 8, 1527: 8, 1593: 8, 1601: 8, 1605: 8, 1609: 8, 1610: 2, 1611: 8, 1614: 8, 1617: 8, 1621: 8, 1625: 8, 1627: 8, 1630: 8, 1800: 4, 1804: 8, 1812: 8, 1815: 8, 1816: 8, 1824: 8, 1828: 8, 1831: 8, 1832: 8, 1840: 8, 1848: 8, 1864: 8, 1880: 8, 1892: 8, 1896: 8, 1912: 8, 1960: 8, 1992: 8, 2008: 3, 2043: 5, 2045: 4
    },
  ],
  CAR.AP1_MODELS: [
    {
      1: 8, 3: 8, 14: 8, 21: 4, 69: 8, 109: 4, 257: 3, 264: 8, 267: 5, 277: 6, 280: 6, 283: 5, 293: 4, 296: 4, 309: 5, 325: 8, 328: 5, 336: 8, 341: 8, 357: 8, 360: 7, 373: 8, 389: 8, 390: 7, 415: 8, 513: 5, 516: 8, 518: 8, 520: 4, 522: 8, 523: 7, 524: 8, 525: 4, 526: 8, 527: 8, 529: 8, 532: 3, 536: 8, 537: 3, 539: 8, 542: 8, 545: 8, 546: 2, 551: 5, 552: 2, 556: 8, 558: 8, 568: 8, 569: 8, 574: 8, 577: 8, 582: 5, 583: 8, 584: 4, 585: 8, 590: 8,         606: 8,         622: 8, 627: 6, 638: 8, 641: 8, 643: 8, 660: 5, 665: 8, 692: 8, 693: 8, 695: 8, 696: 8, 697: 8, 699: 8, 700: 8, 701: 8, 702: 8, 703: 8, 704: 8, 708: 8, 709: 8, 710: 8, 711: 8, 712: 8, 728: 8, 744: 8,         760: 8, 771: 2, 772: 8, 775: 8, 776: 8, 777: 8, 778: 8, 780: 2, 781: 8, 782: 8, 783: 8, 785: 8, 787: 8, 788: 8, 791: 8, 792: 8, 796: 2, 797: 8, 798: 6, 799: 8, 804: 8, 805: 8, 807: 8, 808: 1, 809: 8,         812: 8, 813: 8, 814: 5, 815: 8, 820: 8, 823: 8, 824: 8, 829: 8, 830: 5, 831: 8, 836: 8, 840: 8, 841: 8, 843: 8, 845: 8, 846: 5,         849: 8, 852: 8, 853: 8, 856: 4, 857: 6, 859: 8, 861: 8, 862: 5, 863: 8, 872: 8, 873: 8, 875: 8,         877: 8, 878: 8, 879: 8, 880: 8, 882: 8, 884: 8, 888: 8, 889: 8, 893: 8, 894: 8, 896: 8, 901: 6, 904: 3, 905: 8,         907: 8, 908: 2, 909: 8, 910: 8, 912: 8, 920: 8, 921: 8, 925: 4, 926: 6, 936: 8, 937: 8, 941: 8, 949: 8, 952: 8, 953: 6, 957: 8, 968: 8,         970: 8,         973: 8, 977: 8, 984: 8, 986: 8, 987: 8, 989: 8, 990: 8, 1000: 8, 1001: 8, 1006: 8,                                              1016: 8,                   1019: 5,          1026: 8, 1028: 8, 1029: 8, 1030: 8, 1032: 1, 1033: 1, 1034: 8, 1035: 6, 1048: 1,                   1064: 8,          1070: 8, 1080: 8,                                              1160: 4,          1281: 8, 1291: 8, 1307: 8, 1328: 8, 1329: 8, 1332: 8, 1335: 8, 1337: 8, 1339: 2,          1361: 6, 1362: 6, 1368: 8, 1412: 8,                   1436: 8,          1456: 8, 1463: 8, 1465: 8, 1469: 8, 1476: 8,          1486: 8, 1497: 8,          1519: 8, 1521: 8, 1524: 8, 1527: 8, 1593: 8, 1601: 8, 1605: 8, 1609: 8, 1610: 2, 1611: 8, 1614: 8, 1617: 8, 1621: 8, 1625: 8, 1627: 8, 1630: 8, 1800: 4, 1804: 8, 1812: 8, 1815: 8, 1816: 8, 1824: 8, 1828: 8, 1831: 8, 1832: 8, 1840: 8, 1848: 8, 1864: 8, 1880: 8, 1892: 8, 1896: 8, 1912: 8, 1960: 8, 1992: 8, 2008: 3, 2043: 5, 2045: 4
    },
    {
      1: 8, 3: 8, 14: 8, 21: 4, 69: 8, 109: 4, 257: 3, 264: 8, 267: 5, 277: 6, 280: 6, 283: 5, 293: 4, 296: 4, 309: 5, 325: 8, 328: 5, 336: 8, 341: 8, 357: 8, 360: 7, 373: 8, 389: 8, 390: 7, 415: 8, 513: 5, 516: 8, 518: 8, 520: 4, 522: 8, 523: 7, 524: 8, 525: 4, 526: 8, 527: 8, 529: 8, 532: 3, 536: 8, 537: 3, 539: 8, 542: 8, 545: 8, 546: 2, 551: 5, 552: 2, 556: 8, 558: 8, 568: 8, 569: 8, 574: 8, 577: 8, 582: 5, 583: 8, 584: 4, 585: 8, 590: 8,         606: 8,         622: 8, 627: 6, 638: 8, 641: 8, 643: 8, 660: 3, 665: 8, 692: 8, 693: 8, 695: 8, 696: 8, 697: 8, 699: 8, 700: 8, 701: 8, 702: 8, 703: 8, 704: 8, 708: 8, 709: 8, 710: 8, 711: 8, 712: 8, 728: 8, 744: 8,         760: 8, 771: 2, 772: 8, 775: 8, 776: 8, 777: 8, 778: 8, 780: 2, 781: 8, 782: 8, 783: 8, 785: 8, 787: 8, 788: 8, 791: 8, 792: 8, 796: 2, 797: 8, 798: 6, 799: 8, 804: 8, 805: 8, 807: 8, 808: 1, 809: 8,         812: 8, 813: 8, 814: 5, 815: 8, 820: 8, 823: 8, 824: 8, 829: 8, 830: 5, 831: 8, 836: 8, 840: 8, 841: 8, 843: 8, 845: 8, 846: 5,         849: 8, 852: 8, 853: 8, 856: 4, 857: 5, 859: 8, 861: 8, 862: 5, 863: 8, 872: 8, 873: 8, 875: 8,         877: 8, 878: 8, 879: 8, 880: 8, 882: 8, 884: 8, 888: 8, 889: 8, 893: 8, 894: 8, 896: 8, 901: 6, 904: 3, 905: 8,         907: 8, 908: 2, 909: 8, 910: 8, 912: 8, 920: 8, 921: 8, 925: 4, 926: 6, 936: 8, 937: 8, 941: 8, 949: 8, 952: 8, 953: 6, 957: 8, 968: 8,         970: 8,         973: 8, 977: 8, 984: 8, 986: 8, 987: 8, 989: 8, 990: 8, 1000: 8, 1001: 8, 1006: 8,                                              1016: 8,                   1019: 5,          1026: 8, 1028: 8, 1029: 8, 1030: 8, 1032: 1, 1033: 1, 1034: 8, 1035: 6, 1048: 1,                   1064: 8,          1070: 8, 1080: 8,                                              1160: 4,          1281: 8, 1291: 8, 1307: 8, 1328: 8, 1329: 8, 1332: 8, 1335: 8, 1337: 8, 1339: 2,          1361: 6, 1362: 6, 1368: 8, 1412: 8,                   1436: 8,          1456: 8, 1463: 8, 1465: 8, 1469: 8, 1476: 8,          1486: 8, 1497: 8,          1519: 8, 1521: 8, 1524: 8, 1527: 8, 1593: 8, 1601: 8, 1605: 8, 1609: 8, 1610: 2, 1611: 8, 1614: 8, 1617: 8, 1621: 8, 1625: 8, 1627: 8, 1630: 8, 1800: 4, 1804: 8, 1812: 8, 1815: 8, 1816: 8, 1824: 8, 1828: 8, 1831: 8, 1832: 8, 1840: 8, 1848: 8, 1864: 8, 1880: 8, 1892: 8, 1896: 8, 1912: 8, 1960: 8, 1992: 8, 2008: 3, 2043: 5, 2045: 4
    },
  ],
  CAR.AP1_MODELX: [
    {
      1: 8, 3: 8, 14: 8, 21: 4, 69: 8, 109: 4, 257: 3, 264: 8, 267: 5, 277: 6, 280: 6, 283: 5, 293: 4, 296: 4, 309: 5, 325: 8, 328: 5, 336: 8, 341: 8,         360: 7, 373: 8, 389: 8, 390: 7, 415: 8,         516: 8, 518: 8, 520: 4, 522: 8, 523: 7, 524: 8, 525: 4, 526: 8, 527: 8, 529: 8, 532: 3, 536: 8, 537: 3, 539: 8, 542: 8, 545: 8, 546: 2, 551: 5, 552: 2, 556: 8, 558: 8, 568: 8, 569: 8, 574: 8, 577: 8, 582: 5, 583: 8, 584: 4, 585: 8, 590: 8,         606: 8,         622: 8, 627: 6, 638: 8, 641: 8, 643: 8, 660: 5, 665: 8, 692: 8, 693: 8, 695: 8, 696: 8, 697: 8, 699: 8, 700: 8, 701: 8, 702: 8, 703: 8, 704: 8, 708: 8, 709: 8, 710: 8, 711: 8, 712: 8, 728: 8, 744: 8, 753: 8, 760: 8, 771: 8, 772: 8, 775: 8, 776: 8, 777: 8, 778: 8, 780: 2, 781: 8, 782: 8, 783: 8, 785: 8, 787: 8, 788: 8, 791: 8, 792: 8, 796: 2, 797: 8, 798: 6, 799: 8, 804: 8, 805: 8, 807: 8, 808: 1, 809: 8,         812: 8, 813: 8, 814: 5, 815: 8, 820: 8, 823: 8, 824: 8, 829: 8, 830: 5, 831: 8, 836: 8, 840: 8, 841: 8, 843: 8, 845: 8, 846: 5,         849: 8, 852: 8, 853: 8, 856: 4, 857: 6, 859: 8, 861: 8, 862: 5, 863: 8, 872: 8, 873: 8, 875: 8,         877: 8, 878: 8, 879: 8, 880: 8, 881: 8, 882: 8, 884: 8, 888: 8, 891: 8, 893: 8, 896: 8, 901: 6, 904: 3, 905: 8,         907: 8, 908: 2, 909: 8, 910: 8, 912: 8, 920: 8, 921: 8, 925: 4, 926: 6, 936: 8, 937: 8, 941: 8, 949: 8, 952: 8, 953: 6, 957: 8, 968: 8,         970: 8,         973: 8, 977: 8, 984: 8, 986: 8, 987: 8, 989: 8, 990: 8, 1000: 8, 1001: 8, 1006: 8,                                              1016: 8,                   1019: 5,          1026: 8, 1028: 8, 1029: 8, 1030: 8, 1032: 1, 1033: 1, 1034: 8, 1035: 6, 1048: 1,                   1064: 8,          1070: 8, 1080: 8,                                              1160: 4,          1281: 8, 1291: 8, 1307: 8, 1328: 8, 1329: 8, 1332: 8, 1335: 8, 1337: 8, 1339: 2,          1361: 6, 1362: 6, 1368: 8, 1412: 8, 1416: 8, 1432: 8, 1436: 8, 1448: 8, 1456: 8, 1463: 8, 1465: 8, 1469: 8, 1476: 8,          1486: 8, 1497: 8,          1519: 8, 1521: 8, 1524: 8, 1527: 8, 1593: 8, 1601: 8, 1605: 8, 1609: 8, 1610: 2, 1611: 8, 1614: 8, 1617: 8, 1621: 8, 1625: 8, 1627: 8, 1630: 8, 1800: 4, 1804: 8, 1812: 8, 1815: 8, 1816: 8, 1824: 8, 1828: 8, 1831: 8, 1832: 8, 1840: 8, 1848: 8, 1864: 8, 1880: 8, 1892: 8, 1896: 8, 1912: 8, 1960: 8, 1992: 8, 2008: 3, 2043: 5, 2045: 4
    }
  ],
  CAR.PREAP_MODELS: [
    #for tesla with ibooster we need to actually force the fingerprint....
    {
      # 2013 base model
      1: 8, 3: 8, 14: 8, 21: 4, 69: 8, 109: 4, 257: 3, 264: 8, 277: 6, 280: 6, 293: 4, 296: 4, 309: 5, 325: 8, 336: 8, 341: 8, 360: 7, 373: 8, 389: 8, 415: 8, 513: 5, 516: 8, 520: 4, 522: 8, 524: 8, 527: 8, 536: 8, 551: 4, 552: 2, 556: 8, 568: 8, 582: 5, 638: 8, 643: 8, 693: 8, 696: 8, 712: 8, 728: 8, 744: 8, 760: 8, 771: 2, 772: 8, 775: 8, 776: 8, 778: 8, 780: 2, 783: 8, 785: 8, 787: 8, 788: 8, 791: 8, 792: 8, 796: 2, 799: 8, 804: 8, 805: 8, 807: 8, 808: 1, 812: 8, 815: 8, 820: 8, 823: 8, 824: 8, 831: 8, 836: 8, 840: 8, 856: 4, 863: 8, 872: 8, 880: 8, 888: 8, 896: 8, 901: 6, 904: 3, 920: 8, 936: 8, 949: 8, 952: 8, 953: 6, 968: 8, 984: 8, 1000: 8, 1006: 8, 1026: 8, 1028: 8, 1029: 8, 1030: 8, 1032: 1, 1034: 8, 1048: 1, 1064: 8, 1080: 8, 1281: 8, 1285: 8, 1332: 8, 1335: 8, 1362: 6, 1368: 8, 1412: 8, 1436: 8, 1456: 8, 1463: 8, 1476: 8, 1524: 8, 1527: 8, 1601: 8, 1605: 8, 1617: 8, 1621: 8, 1800: 4, 1804: 8, 1812: 8, 1815: 8, 1816: 8, 1828: 8, 1831: 8, 1832: 8, 1840: 8, 1848: 8, 1864: 8, 1880: 8, 1892: 8, 1896: 8, 1912: 8, 1960: 8, 1992: 8, 2008: 3, 2043: 5
      }
  ],

}
dbc_file_name = 'tesla_can'
if not load_bool_param("TinklaPost1916Fix",True):
  dbc_file_name = 'tesla_can_pre1916'

DBC = {
  CAR.AP2_MODELX: dbc_dict('tesla_powertrain', 'tesla_radar', chassis_dbc=dbc_file_name),
  CAR.AP2_MODELS: dbc_dict('tesla_powertrain', 'tesla_radar', chassis_dbc=dbc_file_name),
  CAR.AP1_MODELS: dbc_dict(None, 'tesla_radar', chassis_dbc=dbc_file_name),
  CAR.PREAP_MODELS: dbc_dict(None, 'tesla_radar', chassis_dbc=dbc_file_name),
  CAR.AP1_MODELX: dbc_dict(None, 'tesla_radar', chassis_dbc=dbc_file_name),
}

CAN_CHASSIS = {
  CAR.AP2_MODELX: 0,
  CAR.AP2_MODELS: 0,
  CAR.AP1_MODELS: 0,
  CAR.PREAP_MODELS: 0,
  CAR.AP1_MODELX: 0,
}

CAN_RADAR = {
  CAR.AP2_MODELX: 1,
  CAR.AP2_MODELS: 1,
  CAR.AP1_MODELS: 1,
  CAR.PREAP_MODELS: 1,
  CAR.AP1_MODELX: 1,
}

CAN_AUTOPILOT = {
  CAR.AP2_MODELX: 0,
  CAR.AP2_MODELS: 2,
  CAR.AP1_MODELS: 2,
  CAR.PREAP_MODELS: -1,
  CAR.AP1_MODELX: 2,
}

CAN_EPAS = {
  CAR.AP2_MODELX: 0,
  CAR.AP2_MODELS: 0,
  CAR.AP1_MODELS: 0,
  CAR.PREAP_MODELS: 0,
  CAR.AP1_MODELX: 0,
}

CAN_POWERTRAIN = {
  CAR.AP2_MODELX: 1,
  CAR.AP2_MODELS: 4,
  CAR.AP1_MODELS: 0,
  CAR.PREAP_MODELS: -1,
  CAR.AP1_MODELX: 4,
}

USE_REAL_PID = {
  CAR.AP2_MODELX: False,
  CAR.AP2_MODELS: False,
  CAR.AP1_MODELS: False,
  CAR.PREAP_MODELS: True,
  CAR.AP1_MODELX: False,
}

CAN_AP_POWERTRAIN = {
  CAR.AP2_MODELX: 1,
  CAR.AP2_MODELS: 6,
  CAR.AP1_MODELS: 2,
  CAR.PREAP_MODELS: -1,
  CAR.AP1_MODELX: 6,
}

TESLA_MAX_ACCEL = 2.0  # m/s^2
TESLA_MIN_ACCEL = -4.5 # m/s^2

#tesla uses various tires, this is for now for the 245/45R19s or 245/35ZR21s and they are 27.8" diameter = 0.353m
#TODOBB: sometimes tesla on the rear has 265/35ZR21 and they are 28.3" diameter 0.359m
#for now OP does not allow for various uom per tire ... to look into it
WHEEL_RADIUS = 0.353

class CANBUS:
  # Lateral harness
  chassis = 0
  radar = 1
  autopilot_chassis = 0

  # Longitudinal harness
  powertrain = 1
  private = 5
  autopilot_powertrain = 1

GEAR_MAP = {
  "DI_GEAR_INVALID": car.CarState.GearShifter.unknown,
  "DI_GEAR_P": car.CarState.GearShifter.park,
  "DI_GEAR_R": car.CarState.GearShifter.reverse,
  "DI_GEAR_N": car.CarState.GearShifter.neutral,
  "DI_GEAR_D": car.CarState.GearShifter.drive,
  "DI_GEAR_SNA": car.CarState.GearShifter.unknown,
}

DOORS = ["DOOR_STATE_FL", "DOOR_STATE_FR", "DOOR_STATE_RL", "DOOR_STATE_RR", "DOOR_STATE_FrontTrunk", "BOOT_STATE"]

# Make sure the message and addr is also in the CAN parser!
BUTTONS = [
  Button(car.CarState.ButtonEvent.Type.leftBlinker, "STW_ACTN_RQ", "TurnIndLvr_Stat", [1]),
  Button(car.CarState.ButtonEvent.Type.rightBlinker, "STW_ACTN_RQ", "TurnIndLvr_Stat", [2]),
  Button(car.CarState.ButtonEvent.Type.accelCruise, "STW_ACTN_RQ", "SpdCtrlLvr_Stat", [4, 16]),
  Button(car.CarState.ButtonEvent.Type.decelCruise, "STW_ACTN_RQ", "SpdCtrlLvr_Stat", [8, 32]),
  Button(car.CarState.ButtonEvent.Type.cancel, "STW_ACTN_RQ", "SpdCtrlLvr_Stat", [1]),
  Button(car.CarState.ButtonEvent.Type.resumeCruise, "STW_ACTN_RQ", "SpdCtrlLvr_Stat", [2]),
  Button(car.CarState.ButtonEvent.Type.altButton1, "STW_ACTN_RQ", "StW_Sw05_Psd", [1]), # menu button on STW
]

class CarControllerParams:
  RATE_LIMIT_UP = AngleRateLimit(speed_points=[0., 5., 15.], max_angle_diff_points=[5., .8, .15])
  RATE_LIMIT_DOWN = AngleRateLimit(speed_points=[0., 5., 15.], max_angle_diff_points=[5., 3.5, 0.4])
  JERK_LIMIT_MAX = 8
  JERK_LIMIT_MIN = -8
  ACCEL_TO_SPEED_MULTIPLIER = 3
  ACCEL_TO_SPEED_MULTIPLIER_ACC = 1
  ACCEL_TO_SPEED_MULTIPLIER_PCC = 1


class CruiseButtons:
    # VAL_ 69 SpdCtrlLvr_Stat 32 "DN_1ST" 16 "UP_1ST" 8 "DN_2ND" 4 "UP_2ND" 2 "RWD" 1 "FWD" 0 "IDLE" ;
    RES_ACCEL = 16
    RES_ACCEL_2ND = 4
    DECEL_SET = 32
    DECEL_2ND = 8
    CANCEL = 1
    MAIN = 2
    IDLE = 0

    @classmethod
    def is_accel(cls, btn):
        return btn in [cls.RES_ACCEL, cls.RES_ACCEL_2ND]

    @classmethod
    def is_decel(cls, btn):
        return btn in [cls.DECEL_SET, cls.DECEL_2ND]

    @classmethod
    def should_be_throttled(cls, btn):
        # Some buttons should not be spammed or they may overwhelm the SCCM.
        return btn not in [cls.MAIN, cls.IDLE]

class CruiseState:
    # DI_cruiseState from the DBC
    OFF = 0
    STANDBY = 1
    ENABLED = 2
    STANDSTILL = 3
    OVERRIDE = 4
    FAULT = 5
    PRE_FAULT = 6
    PRE_CANCEL = 7

    @classmethod
    def is_enabled_or_standby(cls, state):
        return state in [cls.ENABLED, cls.STANDBY]

    @classmethod
    def is_faulted(cls, state):
        return state in [cls.PRE_FAULT, cls.FAULT]

    @classmethod
    def is_off(cls, state):
        return state in [cls.OFF]
