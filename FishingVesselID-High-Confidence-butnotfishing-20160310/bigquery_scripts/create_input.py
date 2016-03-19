from os import listdir
from os.path import isfile, join
import random
from operator import itemgetter

mypath = "../../data/vessels_20160310_hclc/"
files = [f.replace(".json","") for f in listdir(mypath) if isfile(join(mypath, f)) and ".json" in f]

vessels_doubled = [f.split("_")[0] for f in files]
vessels = []
for v in vessels_doubled:
	if v not in vessels:
		vessels.append(v)


# vessels = [412002777,316008961,412423199,412328565,412469022,440000690,412418996,412430414,251194540,200000055,412212518,227101600,412479576,100704340,412061922,412332837,110701275,412432048,247155210,412437435,257488620,412448749,416004801,412284083,412762020,412444188,224055250,412447295,412464376,413000110,412443322,412413220,412462593,800017081,412322577,412352633,412444796,412470461,412419975,412286699,413011032,432845000,412008170,251415440,412412715,412443614,219019804,412425899,412421803,412449545,412416335,900007537,231184000,796917797,701000662,725009500,412360539,257311740,900658520,412416586,412441214,998508330,257705500,800021303,900405802,247051730,100706176,900000328,257001210,412480156,412596013,412450746,412123411,345903913,265502370,251415640,800028837,412428092,200001801,900303106,412411689,999000013,263583000,90143213,416029363,413441090,261008070,235071779,412473587,412433799,224094160,271072382,412322696,412457011,247121880,412433643,228282000,466518320,265616100,247121820,412332286,412459953,412464495,412202682,338145405,824335820,412515898,412419197,235087027,412464331,410025515,412489777,412441905,412445383,412449247,412323921,412417063,412001628,412478686,412450085,412328918,304145000,247143580,900402635,270007565,412435094,265668860,130400923,412329271,272740000,412462038,231045000,100705209,412064497,412431119,412213461,412417065,412416059,412201603,412413956,412286805,251576540,900019534,412421998,412430411,412418804,412510026,800036107,200005718,224020790,412437981,412422289,412698540,412300862,259595000,413214763,440500247,900412851,412469752,412460866,800003792,412427022,431702990,200006419,412330746,416000831,412418459,412206498,412327101,235090864,412479526,900264110,412418411,988585757,228258000,900367122,200007915,412412192,271062117,412446733,412202537,345904243,412568997,800036705,367416270,412413602,412418986,412423422,247063630,412200527,412213273,699889966,413022596,900006043,251080110,210000009,205155000,412328001,900404892,412326262]
# files = ["100706176_2014_1","110701275_2014_10","110701275_2014_11","110701275_2014_9","110701275_2015_1","110701275_2015_2","110701275_2015_3","123450800_2014_1","123450800_2014_10","123450800_2014_11","123450800_2014_12","123450800_2014_2","123450800_2014_3","123450800_2014_4","123450800_2014_5","123450800_2014_6","123450800_2014_7","123450800_2014_8","123450800_2014_9","123450800_2015_1","123450800_2015_2","123450800_2015_3","123450800_2015_4","123450800_2015_5","123450800_2015_6","123450800_2015_7","130400923_2014_5","130400923_2014_8","130400923_2014_9","200000055_2014_10","200000055_2015_1","200000055_2015_2","200000055_2015_3","200000055_2015_5","200001801_2014_1","200005718_2014_12","200007915_2014_5","205155000_2014_1","205155000_2014_10","205155000_2014_11","205155000_2014_12","205155000_2014_2","205155000_2014_3","205155000_2014_4","205155000_2014_5","205155000_2014_6","205155000_2014_7","205155000_2014_8","205155000_2014_9","205155000_2015_1","205155000_2015_2","205155000_2015_3","205155000_2015_4","205155000_2015_5","205155000_2015_6","205155000_2015_7","210000009_2014_10","210000009_2014_11","210000009_2014_12","210000009_2014_7","210000009_2014_8","210000009_2014_9","210000009_2015_1","210000009_2015_2","210000009_2015_3","210000009_2015_4","210000009_2015_5","210000009_2015_6","219019804_2014_10","219019804_2014_11","219019804_2014_12","219019804_2014_7","219019804_2014_8","219019804_2014_9","219019804_2015_3","219019804_2015_4","219019804_2015_6","219019804_2015_7","224016620_2014_10","224016620_2014_4","224016620_2014_5","224016620_2014_6","224016620_2014_9","224016620_2015_3","224016620_2015_4","224016620_2015_5","224016620_2015_6","224020790_2014_1","224020790_2014_10","224020790_2014_11","224020790_2014_12","224020790_2014_2","224020790_2014_3","224020790_2014_6","224020790_2014_7","224020790_2014_8","224020790_2014_9","224020790_2015_1","224020790_2015_2","224020790_2015_3","224020790_2015_6","224020790_2015_7","224055250_2014_1","224055250_2014_2","224055250_2014_3","224055250_2014_4","224055250_2014_5","224055250_2014_6","224055250_2014_9","224055250_2015_5","224055250_2015_6","224094160_2014_10","224094160_2014_8","224094160_2014_9","224094160_2015_3","224094160_2015_5","224094160_2015_6","224094160_2015_7","227101600_2014_1","227101600_2014_10","227101600_2014_11","227101600_2014_12","227101600_2014_2","227101600_2014_3","227101600_2014_4","227101600_2014_5","227101600_2014_9","227101600_2015_1","227101600_2015_2","227101600_2015_3","227101600_2015_4","227101600_2015_5","228258000_2014_1","228258000_2014_10","228258000_2014_11","228258000_2014_12","228258000_2014_2","228258000_2014_3","228258000_2014_4","228258000_2014_5","228258000_2014_6","228258000_2014_7","228258000_2014_8","228258000_2014_9","228258000_2015_1","228258000_2015_2","228258000_2015_3","228258000_2015_4","228258000_2015_5","228258000_2015_6","228258000_2015_7","228282000_2014_10","228282000_2014_11","228282000_2014_12","228282000_2014_3","228282000_2014_4","228282000_2014_5","228282000_2014_6","228282000_2014_7","228282000_2014_8","228282000_2014_9","228282000_2015_1","228282000_2015_2","228282000_2015_3","228282000_2015_4","228282000_2015_5","228282000_2015_6","228282000_2015_7","231045000_2014_1","231045000_2014_10","231045000_2014_11","231045000_2014_12","231045000_2014_2","231045000_2014_3","231045000_2014_4","231045000_2014_5","231045000_2014_6","231045000_2014_7","231045000_2014_8","231045000_2014_9","231045000_2015_1","231045000_2015_2","231045000_2015_3","231045000_2015_4","231045000_2015_5","231045000_2015_6","231045000_2015_7","231184000_2014_1","231184000_2014_10","231184000_2014_11","231184000_2014_12","231184000_2014_2","231184000_2014_3","231184000_2014_4","231184000_2014_5","231184000_2014_6","231184000_2014_8","231184000_2014_9","231184000_2015_1","231184000_2015_2","231184000_2015_3","231184000_2015_4","231184000_2015_5","231184000_2015_6","231184000_2015_7","235071779_2014_1","235071779_2014_10","235071779_2014_11","235071779_2014_12","235071779_2014_2","235071779_2014_3","235071779_2014_4","235071779_2014_5","235071779_2014_6","235071779_2014_7","235071779_2014_8","235071779_2014_9","235071779_2015_1","235071779_2015_2","235071779_2015_3","235071779_2015_4","235071779_2015_5","235071779_2015_6","235071779_2015_7","235087027_2014_10","235087027_2014_11","235087027_2015_3","235087027_2015_4","235087027_2015_5","235087027_2015_7","235090864_2014_1","235090864_2014_11","235090864_2014_12","235090864_2014_3","235090864_2014_4","235090864_2014_5","235090864_2015_1","247051730_2014_1","247051730_2014_10","247051730_2014_11","247051730_2014_12","247051730_2014_2","247051730_2014_3","247051730_2014_4","247051730_2014_5","247051730_2014_6","247051730_2014_7","247051730_2014_9","247051730_2015_1","247051730_2015_2","247051730_2015_3","247051730_2015_4","247051730_2015_5","247051730_2015_6","247051730_2015_7","247063630_2014_1","247063630_2014_10","247063630_2014_11","247063630_2014_12","247063630_2014_2","247063630_2014_3","247063630_2014_4","247063630_2014_5","247063630_2014_6","247063630_2014_7","247063630_2014_8","247063630_2014_9","247063630_2015_1","247063630_2015_2","247063630_2015_3","247063630_2015_4","247063630_2015_5","247063630_2015_6","247063630_2015_7","247121820_2014_12","247121820_2015_1","247121820_2015_2","247121820_2015_3","247121820_2015_4","247121820_2015_5","247121820_2015_6","247121820_2015_7","247121880_2014_10","247121880_2014_5","247121880_2014_6","247121880_2014_7","247121880_2014_8","247121880_2014_9","247121880_2015_4","247121880_2015_5","247121880_2015_6","247121880_2015_7","247143580_2014_1","247143580_2014_10","247143580_2014_11","247143580_2014_2","247143580_2014_3","247143580_2014_4","247143580_2014_5","247143580_2014_6","247143580_2014_7","247143580_2014_8","247143580_2014_9","247143580_2015_2","247143580_2015_3","247143580_2015_4","247143580_2015_5","247143580_2015_6","247143580_2015_7","247155210_2014_7","247155210_2014_8","247155210_2015_6","247155210_2015_7","251080110_2014_10","251080110_2014_11","251080110_2014_12","251080110_2014_2","251080110_2014_3","251080110_2014_4","251080110_2014_5","251080110_2014_6","251080110_2014_7","251080110_2014_8","251080110_2014_9","251080110_2015_1","251080110_2015_2","251080110_2015_3","251080110_2015_4","251080110_2015_5","251080110_2015_6","251080110_2015_7","251194540_2014_6","251194540_2014_7","251194540_2014_8","251194540_2015_7","251415440_2014_5","251415440_2015_5","251415640_2014_10","251415640_2014_4","251415640_2014_5","251415640_2014_6","251415640_2014_7","251415640_2014_9","251415640_2015_5","251415640_2015_6","251415640_2015_7","251576540_2014_3","251576540_2014_4","251576540_2014_5","251576540_2014_6","251576540_2015_3","257001210_2015_3","257001210_2015_4","257001210_2015_5","257311740_2015_4","257488620_2014_2","257488620_2014_3","257488620_2014_4","257488620_2015_2","257488620_2015_3","257488620_2015_4","257705500_2014_1","257705500_2014_11","257705500_2014_12","257705500_2014_2","257705500_2014_3","257705500_2014_4","257705500_2014_5","257705500_2014_6","257705500_2014_7","257705500_2014_8","257705500_2014_9","257705500_2015_1","257705500_2015_2","257705500_2015_3","257705500_2015_4","257705500_2015_5","257705500_2015_6","257705500_2015_7","259595000_2014_1","259595000_2014_10","259595000_2014_11","259595000_2014_12","259595000_2014_2","259595000_2014_3","259595000_2014_4","259595000_2014_5","259595000_2014_6","259595000_2014_7","259595000_2014_8","259595000_2014_9","259595000_2015_1","259595000_2015_2","259595000_2015_3","259595000_2015_4","259595000_2015_5","259595000_2015_6","259595000_2015_7","261008070_2014_1","261008070_2014_10","261008070_2014_11","261008070_2014_12","261008070_2014_2","261008070_2014_3","261008070_2014_4","261008070_2014_5","261008070_2014_6","261008070_2014_7","261008070_2014_8","261008070_2014_9","261008070_2015_1","261008070_2015_2","261008070_2015_3","261008070_2015_4","261008070_2015_5","261008070_2015_6","261008070_2015_7","263583000_2014_1","263583000_2014_10","263583000_2014_11","263583000_2014_12","263583000_2014_2","263583000_2014_3","263583000_2014_4","263583000_2014_5","263583000_2014_6","263583000_2014_7","263583000_2014_8","263583000_2014_9","263583000_2015_1","263583000_2015_2","263583000_2015_3","263583000_2015_4","263583000_2015_5","263583000_2015_6","263583000_2015_7","265502370_2014_1","265502370_2014_10","265502370_2014_11","265502370_2014_12","265502370_2014_2","265502370_2014_3","265502370_2014_4","265502370_2014_5","265502370_2014_6","265502370_2014_7","265502370_2014_8","265502370_2014_9","265502370_2015_1","265502370_2015_2","265502370_2015_3","265502370_2015_4","265502370_2015_5","265502370_2015_6","265502370_2015_7","265616100_2014_10","265616100_2014_8","265616100_2015_7","265668860_2014_10","265668860_2014_11","265668860_2014_6","265668860_2014_7","265668860_2015_1","265668860_2015_3","270007565_2014_3","270007565_2014_4","270007565_2014_5","271062117_2014_10","271062117_2014_11","271062117_2014_12","271062117_2014_2","271062117_2014_3","271062117_2014_4","271062117_2014_9","271062117_2015_1","271062117_2015_2","271072382_2014_1","271072382_2014_10","271072382_2014_11","271072382_2014_12","271072382_2014_2","271072382_2014_3","271072382_2014_4","271072382_2014_6","271072382_2014_7","271072382_2014_8","271072382_2014_9","271072382_2015_1","271072382_2015_2","271072382_2015_3","271072382_2015_4","271072382_2015_5","271072382_2015_6","272740000_2014_10","272740000_2014_11","272740000_2014_12","272740000_2014_9","272740000_2015_1","272740000_2015_2","272740000_2015_3","304145000_2014_1","304145000_2014_10","304145000_2014_11","304145000_2014_12","304145000_2014_2","304145000_2014_3","304145000_2014_4","304145000_2014_5","304145000_2014_6","304145000_2014_7","304145000_2014_8","304145000_2014_9","304145000_2015_1","304145000_2015_2","304145000_2015_3","304145000_2015_4","304145000_2015_5","304145000_2015_6","304145000_2015_7","316008961_2014_1","316008961_2014_12","316008961_2014_4","316008961_2014_9","316008961_2015_1","338145405_2014_1","338145405_2014_10","338145405_2014_2","338145405_2014_3","338145405_2014_4","338145405_2014_5","338145405_2014_6","338145405_2014_7","338145405_2014_8","338145405_2014_9","345904243_2014_10","345904243_2014_9","356394000_2014_10","356394000_2014_11","356394000_2014_12","356394000_2014_8","356394000_2014_9","356394000_2015_1","356394000_2015_4","356394000_2015_5","356394000_2015_7","359001000_2014_10","359001000_2014_8","359001000_2015_2","359001000_2015_3","359001000_2015_6","359001000_2015_7","367338620_2014_12","367338620_2015_1","367338620_2015_2","367416270_2014_1","367416270_2014_10","367416270_2014_11","367416270_2014_2","367416270_2014_3","367416270_2014_4","367416270_2014_5","367416270_2014_6","367416270_2014_7","367416270_2014_8","367416270_2014_9","367416270_2015_1","367416270_2015_2","367416270_2015_3","367416270_2015_4","367416270_2015_5","367416270_2015_6","367416270_2015_7","410025515_2014_2","410025515_2014_3","410025515_2014_4","410025515_2014_5","410025515_2014_7","412001628_2014_8","412002777_2014_1","412002777_2014_10","412002777_2014_11","412002777_2014_12","412002777_2014_3","412002777_2014_4","412002777_2014_5","412002777_2014_7","412002777_2014_8","412002777_2014_9","412002777_2015_1","412002777_2015_3","412002777_2015_4","412002777_2015_5","412061922_2014_2","412061922_2014_3","412061922_2014_4","412061922_2014_5","412064497_2014_10","412064497_2014_5","412064497_2014_9","412064497_2015_5","412123411_2014_1","412123411_2014_2","412123411_2014_3","412123411_2014_4","412123411_2014_5","412200527_2014_9","412200527_2015_5","412201603_2014_10","412201603_2014_11","412201603_2014_12","412201603_2014_3","412201603_2014_4","412201603_2014_9","412202537_2014_10","412202537_2014_11","412202537_2014_9","412202682_2014_9","412206498_2014_10","412206498_2014_9","412213273_2014_10","412213273_2014_11","412213273_2014_9","412213273_2015_4","412213273_2015_5","412213461_2014_4","412213461_2014_5","412286699_2014_10","412286699_2014_11","412286699_2014_8","412286699_2014_9","412286805_2014_10","412286805_2014_11","412286805_2014_12","412286805_2014_3","412286805_2014_4","412286805_2014_5","412286805_2014_6","412286805_2014_7","412286805_2014_8","412286805_2014_9","412286805_2015_1","412286805_2015_2","412286805_2015_3","412286805_2015_4","412286805_2015_5","412286805_2015_6","412286805_2015_7","412300862_2014_10","412300862_2014_11","412300862_2014_12","412300862_2014_9","412323921_2014_10","412323921_2014_11","412323921_2014_9","412326262_2014_3","412326262_2014_4","412327101_2014_10","412328001_2014_2","412328001_2014_5","412328001_2014_7","412328565_2014_9","412328565_2015_4","412328565_2015_5","412328918_2014_9","412329271_2014_10","412329271_2014_5","412329271_2014_9","412330746_2014_10","412330746_2014_11","412330746_2014_5","412330746_2014_9","412330746_2015_5","412332286_2014_8","412332837_2014_9","412332837_2015_3","412360539_2014_10","412360539_2014_8","412360539_2014_9","412360539_2015_3","412360539_2015_4","412360539_2015_5","412411689_2014_1","412411689_2014_10","412411689_2014_11","412411689_2014_12","412411689_2014_2","412411689_2014_3","412411689_2014_4","412411689_2014_5","412411689_2014_8","412411689_2014_9","412411689_2015_1","412411689_2015_2","412411689_2015_3","412411689_2015_4","412411689_2015_5","412412192_2014_2","412412192_2014_4","412412192_2014_5","412412715_2014_10","412412715_2014_11","412412715_2014_12","412412715_2014_3","412412715_2014_4","412412715_2014_9","412412715_2015_3","412413220_2014_3","412413602_2014_10","412413602_2014_11","412413602_2014_12","412413602_2014_5","412413602_2014_9","412413602_2015_5","412413956_2014_10","412413956_2014_11","412413956_2014_12","412413956_2014_2","412413956_2014_3","412413956_2014_4","412413956_2014_8","412413956_2014_9","412413956_2015_2","412413956_2015_3","412413956_2015_4","412416059_2014_10","412416059_2014_9","412416059_2015_3","412416335_2014_3","412416335_2014_4","412416335_2014_5","412416586_2014_12","412417063_2014_1","412417063_2014_11","412417063_2014_12","412417063_2014_3","412417063_2014_4","412417063_2014_5","412417063_2014_9","412417063_2015_1","412417063_2015_2","412417063_2015_3","412417063_2015_4","412417063_2015_5","412417065_2014_10","412417065_2014_9","412418411_2014_11","412418411_2014_12","412418411_2014_4","412418411_2014_5","412418411_2014_8","412418411_2014_9","412418411_2015_2","412418411_2015_3","412418411_2015_4","412418459_2014_3","412418459_2014_4","412418459_2014_5","412418459_2015_1","412418459_2015_3","412418459_2015_4","412418459_2015_5","412418804_2014_1","412418804_2014_10","412418804_2014_11","412418804_2014_12","412418804_2014_8","412418804_2015_1","412418804_2015_3","412418804_2015_4","412418986_2014_1","412418986_2014_11","412418986_2014_12","412418986_2014_4","412418986_2014_5","412418996_2014_1","412418996_2014_11","412418996_2014_12","412418996_2014_4","412418996_2014_5","412418996_2014_8","412418996_2014_9","412418996_2015_1","412418996_2015_2","412418996_2015_3","412418996_2015_4","412418996_2015_5","412419197_2014_10","412419197_2014_11","412421803_2014_10","412421803_2014_11","412421803_2014_7","412421803_2014_9","412421803_2015_1","412421803_2015_2","412421803_2015_4","412421803_2015_5","412421803_2015_6","412421803_2015_7","412421998_2014_10","412421998_2014_11","412421998_2014_12","412421998_2014_9","412421998_2015_1","412421998_2015_3","412421998_2015_4","412421998_2015_5","412422289_2014_10","412422289_2014_11","412422289_2014_12","412422289_2014_2","412422289_2014_3","412422289_2014_4","412422289_2014_5","412422289_2014_7","412422289_2014_9","412422289_2015_1","412422289_2015_2","412422289_2015_3","412422289_2015_4","412422289_2015_5","412422289_2015_7","412423199_2014_10","412423199_2014_11","412423199_2014_12","412423199_2014_7","412423199_2014_8","412423199_2014_9","412423199_2015_1","412423199_2015_3","412423199_2015_7","412423422_2014_10","412423422_2014_11","412423422_2014_12","412423422_2014_9","412423422_2015_1","412423422_2015_3","412423422_2015_4","412423422_2015_5","412423422_2015_6","412425899_2014_11","412425899_2014_8","412427022_2014_10","412427022_2014_3","412427022_2014_5","412427022_2014_8","412427022_2014_9","412427022_2015_2","412427022_2015_5","412428092_2014_10","412428092_2014_11","412428092_2014_12","412428092_2015_1","412428092_2015_2","412428092_2015_3","412428092_2015_4","412428092_2015_5","412428092_2015_6","412430411_2014_10","412430411_2014_11","412430411_2014_12","412430411_2014_5","412430411_2014_9","412430411_2015_1","412430411_2015_5","412430414_2014_10","412430414_2014_11","412430414_2014_12","412430414_2014_5","412430414_2014_9","412430414_2015_1","412430414_2015_5","412431119_2014_10","412431119_2014_11","412431119_2014_12","412431119_2014_2","412431119_2014_3","412431119_2014_4","412431119_2014_8","412431119_2014_9","412431119_2015_3","412432048_2014_1","412432048_2014_10","412432048_2014_11","412432048_2014_12","412432048_2014_2","412432048_2014_3","412432048_2014_7","412432048_2014_9","412432048_2015_1","412432048_2015_2","412432048_2015_3","412432048_2015_7","412433643_2014_10","412433643_2014_11","412433643_2014_9","412433799_2014_1","412433799_2014_10","412433799_2014_11","412433799_2014_3","412433799_2014_4","412433799_2014_5","412433799_2014_8","412433799_2014_9","412433799_2015_4","412433799_2015_5","412435094_2014_7","412435094_2014_9","412435094_2015_7","412437435_2014_1","412437435_2014_10","412437435_2014_11","412437435_2014_12","412437435_2014_3","412437435_2014_4","412437435_2014_5","412437435_2014_9","412437981_2015_4","412437981_2015_5","412441214_2014_3","412441214_2014_4","412441214_2014_8","412441905_2014_11","412441905_2015_4","412441905_2015_5","412441905_2015_7","412443614_2014_2","412443614_2014_6","412444188_2014_1","412444188_2014_10","412444188_2014_11","412444188_2014_12","412444188_2014_2","412444188_2014_3","412444188_2014_4","412444188_2014_5","412444188_2014_8","412444188_2014_9","412444188_2015_1","412444188_2015_2","412444188_2015_3","412444188_2015_4","412444796_2014_1","412444796_2014_10","412444796_2014_11","412444796_2014_12","412444796_2014_4","412444796_2014_5","412444796_2014_8","412444796_2014_9","412444796_2015_1","412444796_2015_2","412444796_2015_4","412444796_2015_5","412445383_2014_11","412445383_2014_4","412445383_2014_5","412445383_2014_8","412445383_2014_9","412447295_2014_12","412447295_2015_1","412447295_2015_2","412448749_2014_11","412448749_2014_12","412448749_2015_4","412449247_2014_10","412449247_2014_11","412449247_2014_12","412449247_2014_2","412449247_2014_3","412449247_2014_4","412449247_2014_6","412449247_2014_7","412449247_2014_8","412449247_2014_9","412449247_2015_1","412449247_2015_2","412449247_2015_3","412449247_2015_4","412449247_2015_5","412449247_2015_6","412449247_2015_7","412449545_2014_11","412449545_2014_12","412449545_2014_4","412449545_2014_5","412449545_2014_6","412449545_2014_8","412449545_2015_1","412449545_2015_2","412450085_2014_1","412450085_2014_10","412450085_2014_11","412450085_2014_12","412450085_2014_2","412450085_2014_3","412450085_2014_5","412450085_2014_6","412450085_2014_7","412450085_2015_1","412450085_2015_2","412450085_2015_3","412450085_2015_4","412450746_2014_10","412450746_2014_11","412450746_2014_12","412450746_2014_3","412450746_2014_4","412450746_2014_8","412450746_2014_9","412450746_2015_1","412450746_2015_2","412457011_2014_1","412457011_2014_11","412457011_2014_2","412457011_2014_3","412457011_2014_5","412457011_2014_6","412457011_2014_7","412457011_2015_1","412457011_2015_3","412457011_2015_4","412460866_2014_1","412460866_2014_10","412460866_2014_11","412460866_2014_12","412460866_2014_2","412460866_2014_9","412460866_2015_1","412460866_2015_2","412460866_2015_3","412460866_2015_4","412460866_2015_5","412462038_2014_3","412462038_2014_4","412462038_2015_3","412462038_2015_4","412462038_2015_5","412462593_2014_10","412462593_2014_11","412462593_2014_12","412462593_2015_1","412464331_2014_10","412464331_2014_11","412464331_2014_12","412464331_2014_2","412464331_2014_3","412464331_2014_4","412464331_2014_7","412464331_2014_8","412464331_2014_9","412464331_2015_1","412464331_2015_3","412464331_2015_4","412464331_2015_7","412464376_2014_10","412464376_2014_11","412464376_2014_12","412464376_2014_4","412464376_2014_5","412464376_2014_8","412464376_2015_1","412464376_2015_2","412464376_2015_3","412464376_2015_4","412464495_2014_12","412464495_2014_9","412464495_2015_6","412464495_2015_7","412469752_2014_4","412469752_2014_8","412469752_2014_9","412470461_2014_8","412470461_2014_9","412473587_2014_8","412478686_2014_9","412478686_2015_1","412478686_2015_3","412478686_2015_4","412478686_2015_5","412479526_2014_8","412479526_2014_9","412479576_2014_1","412479576_2015_1","412479576_2015_2","412480156_2014_4","412489777_2014_10","412489777_2014_11","412489777_2014_12","412489777_2014_4","412489777_2014_7","412489777_2014_8","412489777_2014_9","412489777_2015_1","412489777_2015_2","412489777_2015_3","412489777_2015_4","412489777_2015_5","412489777_2015_7","412510026_2014_5","412510026_2014_7","412515898_2014_3","412515898_2014_4","412515898_2015_4","412568997_2014_1","412568997_2014_11","412568997_2014_12","412568997_2014_3","412568997_2014_4","412568997_2014_9","412568997_2015_1","412568997_2015_2","412568997_2015_4","412568997_2015_5","412596013_2014_10","412596013_2014_11","412596013_2014_12","412596013_2014_7","412596013_2014_8","412596013_2014_9","412596013_2015_1","412596013_2015_2","412596013_2015_3","412596013_2015_4","412596013_2015_7","412698540_2014_1","412698540_2014_12","412698540_2014_4","412698540_2014_5","412698540_2014_6","413000110_2014_2","413011032_2014_10","413011032_2014_9","413011032_2015_1","413011032_2015_2","413011032_2015_4","413011032_2015_5","413022596_2014_4","413022596_2014_5","413214763_2014_12","413214763_2014_3","413214763_2014_4","413214763_2014_5","413214763_2014_7","413214763_2014_8","413214763_2014_9","413214763_2015_3","413214763_2015_4","413214763_2015_7","413441090_2014_11","413441090_2014_4","413441090_2014_6","413441090_2015_3","413441090_2015_4","413441090_2015_6","413441090_2015_7","416004801_2014_10","416004801_2014_11","416004801_2014_12","416004801_2015_1","416004801_2015_2","416004801_2015_3","416004801_2015_4","416004801_2015_6","416004801_2015_7","416029363_2014_12","431702990_2014_1","431702990_2014_10","431702990_2014_11","431702990_2014_12","431702990_2014_2","431702990_2014_3","431702990_2014_4","431702990_2014_5","431702990_2014_6","431702990_2014_7","431702990_2014_8","431702990_2014_9","431702990_2015_1","431702990_2015_2","431702990_2015_3","431702990_2015_4","431702990_2015_5","431702990_2015_6","431702990_2015_7","432845000_2014_1","432845000_2014_10","432845000_2014_11","432845000_2014_12","432845000_2014_2","432845000_2014_3","432845000_2014_4","432845000_2014_5","432845000_2014_6","432845000_2014_7","432845000_2014_8","432845000_2014_9","432845000_2015_1","432845000_2015_2","432845000_2015_3","432845000_2015_4","432845000_2015_5","432845000_2015_6","432845000_2015_7","432927000_2014_1","432927000_2014_10","432927000_2014_11","432927000_2014_12","432927000_2014_2","432927000_2014_3","432927000_2014_4","432927000_2014_5","432927000_2014_6","432927000_2014_7","432927000_2014_8","432927000_2014_9","432927000_2015_1","432927000_2015_2","432927000_2015_3","432927000_2015_4","432927000_2015_5","432927000_2015_6","432927000_2015_7","440000690_2014_1","440000690_2014_10","440000690_2014_11","440000690_2014_12","440000690_2014_3","440000690_2014_5","440000690_2014_6","440000690_2014_7","440000690_2014_8","440000690_2014_9","440000690_2015_1","440000690_2015_2","440000690_2015_3","440000690_2015_4","440000690_2015_5","440000690_2015_6","440000690_2015_7","440500247_2015_5","466518320_2014_7","699889966_2014_1","699889966_2014_2","699889966_2014_3","699889966_2014_4","701000662_2014_10","701000662_2014_11","701000662_2014_4","701000662_2014_5","701000662_2014_7","701000662_2014_8","701000662_2014_9","701000662_2015_1","701000662_2015_2","701000662_2015_3","701000662_2015_4","701000662_2015_5","701000662_2015_6","701000662_2015_7","725009500_2014_1","725009500_2014_10","725009500_2014_11","725009500_2014_12","725009500_2014_2","725009500_2014_3","725009500_2014_4","725009500_2014_5","725009500_2014_6","725009500_2014_7","725009500_2014_8","725009500_2014_9","725009500_2015_1","725009500_2015_2","725009500_2015_3","725009500_2015_4","725009500_2015_5","725009500_2015_6","725009500_2015_7","775000000_2014_1","775000000_2014_10","775000000_2014_11","775000000_2014_12","775000000_2014_2","775000000_2014_3","775000000_2014_4","775000000_2014_5","775000000_2014_6","775000000_2014_7","775000000_2014_8","775000000_2014_9","775000000_2015_1","775000000_2015_2","775000000_2015_3","775000000_2015_4","775000000_2015_5","775000000_2015_6","775000000_2015_7","796917797_2015_4","800003792_2014_5","800003792_2014_9","800017081_2014_1","800017081_2014_10","800017081_2014_11","800017081_2014_12","800017081_2014_6","800017081_2014_8","800017081_2014_9","800017081_2015_1","800017081_2015_2","800017081_2015_3","800017081_2015_7","800021303_2014_1","800028837_2014_11","800028837_2015_5","800028837_2015_6","800036107_2014_3","800036107_2015_1","800036705_2014_10","800036705_2014_11","800036705_2014_5","800036705_2015_5","800036705_2015_6","900000328_2015_1","900000328_2015_7","900019534_2014_10","900019534_2014_11","900019534_2014_12","900019534_2014_2","900019534_2014_3","900019534_2014_4","900019534_2014_5","900019534_2014_8","900019534_2014_9","900019534_2015_1","900019534_2015_2","900019534_2015_3","900264110_2014_2","900264110_2014_3","900264110_2014_4","900264110_2014_5","900303106_2014_1","900303106_2014_2","900303106_2014_3","900303106_2014_4","900367122_2015_3","900402635_2014_1","900402635_2014_10","900402635_2014_12","900402635_2015_1","900402635_2015_2","900402635_2015_3","900402635_2015_4","900405802_2014_10","900405802_2014_11","900405802_2014_12","900405802_2014_8","900405802_2014_9","900405802_2015_1","900412851_2014_12","900412851_2015_1","900412851_2015_3","900412851_2015_4","900412851_2015_5","900658520_2014_3","900658520_2015_1","900658520_2015_2","900658520_2015_3","900658520_2015_4","90143213_2014_8","90143213_2015_3","90143213_2015_4","998508330_2015_4","998508330_2015_6","999000013_2014_7"]


for v in vessels:
    selects = []
    selects2 = []
    #v_months[v]=[]
    for f in files:
        if str(v) == f.split("_")[0]:
            m = int(f.split("_")[2])
            y = int(f.split("_")[1])
            if y == 2015:
                selects.append(m)
            if y == 2014:
                selects2.append(m)
    if len(selects)+len(selects2)>2:
        # selects = sorted(selects, key=itemgetter(0))
        selects = sorted(selects)#, key=itemgetter(1))
        selects2 = sorted(selects2)#, key=itemgetter(1))

        for i in range(len(selects)): 
            selects[i]=str(selects[i])
        
        for j in range(len(selects2)): 
            selects2[j]=str(selects2[j])

        #2014, then 2015
        print str(v)+"\t"+",".join(selects2)+"\t"+ (",".join(selects))
        # print (",".join(selects2))
        # two_files = random.sample(set(selects), 2)
        # for t in two_files:
        #     t = t.split("_")
        #     print t[0]+"\t"+t[1]+"\t"+t[2].split(".")[0]
    

