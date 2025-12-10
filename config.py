"""
配置文件 - 定义所有可用的服务和设备
"""

# 可用的服务定义
SERVICES = {
    "cover": [
        "cover.close_cover()",
        "cover.open_cover()",
        "cover.stop_cover()",
        "cover.toggle()"
    ],
    "fan": [
        "fan.decrease_speed()",
        "fan.increase_speed()",
        "fan.toggle()",
        "fan.turn_off()",
        "fan.turn_on()"
    ],
    "light": [
        "light.toggle()",
        "light.turn_off()",
        "light.turn_on(rgb_color,brightness)"
    ],
    "lock": [
        "lock.lock()",
        "lock.unlock()"
    ],
    "media_player": [
        "media_player.media_next_track()",
        "media_player.media_pause()",
        "media_player.media_play()",
        "media_player.media_play_pause()",
        "media_player.media_previous_track()",
        "media_player.media_stop()",
        "media_player.toggle()",
        "media_player.turn_off()",
        "media_player.turn_on()",
        "media_player.volume_down()",
        "media_player.volume_mute()",
        "media_player.volume_up()"
    ],
    "timer": [
        "timer.cancel()",
        "timer.pause()",
        "timer.start(duration)"
    ],
    "vacuum": [
        "vacuum.pause()",
        "vacuum.return_to_base()",
        "vacuum.start()",
        "vacuum.stop()"
    ]
}

# 设备列表
DEVICES = {
    "light": [
        {"id": "light.living_room_main", "name": "Living Room Main Light", "name_zh": "客厅主灯"},
        {"id": "light.bedroom_ceiling", "name": "Bedroom Ceiling Light", "name_zh": "卧室吸顶灯"},
        {"id": "light.kitchen_spot_1", "name": "Kitchen Spot Light 1", "name_zh": "厨房射灯1"},
        {"id": "light.kitchen_spot_2", "name": "Kitchen Spot Light 2", "name_zh": "厨房射灯2"},
        {"id": "light.bathroom_mirror", "name": "Bathroom Mirror Light", "name_zh": "浴室镜前灯"},
        {"id": "light.hallway_pendant", "name": "Hallway Pendant", "name_zh": "走廊吊灯"},
        {"id": "light.garage_workshop", "name": "Garage Workshop Light", "name_zh": "车库工作灯"},
        {"id": "light.backyard_floodlight", "name": "Backyard Floodlight", "name_zh": "后院泛光灯"},
        {"id": "light.front_porch", "name": "Front Porch Light", "name_zh": "前廊灯"},
        {"id": "light.study_desk_lamp", "name": "Study Desk Lamp", "name_zh": "书房台灯"},
        {"id": "light.dining_chandelier", "name": "Dining Room Chandelier", "name_zh": "餐厅吊灯"},
        {"id": "light.basement_stairway", "name": "Basement Stairway Light", "name_zh": "地下室楼梯灯"},
        {"id": "light.guest_room_bedside", "name": "Guest Room Bedside Lamp", "name_zh": "客房床头灯"},
        {"id": "light.master_bedroom_reading", "name": "Master Bedroom Reading Light", "name_zh": "主卧阅读灯"},
        {"id": "light.kids_room_nightlight", "name": "Kids Room Nightlight", "name_zh": "儿童房夜灯"},
    ],
    "cover": [
        {"id": "cover.living_room_curtain", "name": "Living Room Curtain", "name_zh": "客厅窗帘"},
        {"id": "cover.bedroom_blinds", "name": "Bedroom Blinds", "name_zh": "卧室百叶窗"},
        {"id": "cover.kitchen_roller_shade", "name": "Kitchen Roller Shade", "name_zh": "厨房卷帘"},
        {"id": "cover.garage_door_main", "name": "Main Garage Door", "name_zh": "车库主门"},
        {"id": "cover.garage_door_side", "name": "Side Garage Door", "name_zh": "车库侧门"},
        {"id": "cover.sunroom_awning", "name": "Sunroom Awning", "name_zh": "阳光房遮阳篷"},
        {"id": "cover.patio_screen", "name": "Patio Screen", "name_zh": "露台屏风"},
        {"id": "cover.skylight_roof", "name": "Roof Skylight", "name_zh": "屋顶天窗"},
    ],
    "lock": [
        {"id": "lock.front_door", "name": "Front Door Lock", "name_zh": "前门锁"},
        {"id": "lock.back_door", "name": "Back Door Lock", "name_zh": "后门锁"},
        {"id": "lock.garage_entry", "name": "Garage Entry Lock", "name_zh": "车库入口锁"},
        {"id": "lock.side_gate", "name": "Side Gate Lock", "name_zh": "侧门锁"},
        {"id": "lock.basement_door", "name": "Basement Door Lock", "name_zh": "地下室门锁"},
        {"id": "lock.shed_padlock", "name": "Shed Padlock", "name_zh": "储物间挂锁"},
        {"id": "lock.wine_cellar", "name": "Wine Cellar Lock", "name_zh": "酒窖锁"},
    ],
    "fan": [
        {"id": "fan.living_room_ceiling", "name": "Living Room Ceiling Fan", "name_zh": "客厅吊扇"},
        {"id": "fan.bedroom_master", "name": "Master Bedroom Fan", "name_zh": "主卧风扇"},
        {"id": "fan.bedroom_guest", "name": "Guest Bedroom Fan", "name_zh": "客房风扇"},
        {"id": "fan.dining_room", "name": "Dining Room Fan", "name_zh": "餐厅风扇"},
        {"id": "fan.patio_outdoor", "name": "Outdoor Patio Fan", "name_zh": "露台风扇"},
        {"id": "fan.office_desk", "name": "Office Desk Fan", "name_zh": "办公桌风扇"},
    ],
    "timer": [
        {"id": "timer.cooking", "name": "Cooking Timer", "name_zh": "烹饪计时器"},
        {"id": "timer.laundry", "name": "Laundry Timer", "name_zh": "洗衣计时器"},
        {"id": "timer.workout", "name": "Workout Timer", "name_zh": "健身计时器"},
        {"id": "timer.meditation", "name": "Meditation Timer", "name_zh": "冥想计时器"},
    ],
    "vacuum": [
        {"id": "vacuum.living_room_robot", "name": "Living Room Robot Vacuum", "name_zh": "客厅扫地机器人"},
        {"id": "vacuum.upstairs_cleaner", "name": "Upstairs Robot Cleaner", "name_zh": "楼上扫地机"},
        {"id": "vacuum.basement_bot", "name": "Basement Cleaning Bot", "name_zh": "地下室清洁机器人"},
    ],
    "media_player": [
        {"id": "media_player.living_room_tv", "name": "Living Room TV", "name_zh": "客厅电视"},
        {"id": "media_player.bedroom_tv", "name": "Bedroom TV", "name_zh": "卧室电视"},
        {"id": "media_player.kitchen_speaker", "name": "Kitchen Smart Speaker", "name_zh": "厨房智能音箱"},
        {"id": "media_player.bathroom_speaker", "name": "Bathroom Speaker", "name_zh": "浴室音箱"},
        {"id": "media_player.garage_radio", "name": "Garage Radio", "name_zh": "车库收音机"},
    ]
}

# 颜色映射（RGB）
COLORS = {
    # 基础色
    "红色": [255, 0, 0],
    "绿色": [0, 255, 0],
    "蓝色": [0, 0, 255],
    "黄色": [255, 255, 0],
    "紫色": [128, 0, 128],
    "白色": [255, 255, 255],
    "橙色": [255, 165, 0],
    "粉色": [255, 192, 203],
    "青色": [0, 255, 255],
    "黑色": [0, 0, 0],
    "灰色": [128, 128, 128],
    # 常见扩展色
    "青色": [0, 255, 255],        # cyan
    "青绿": [0, 128, 128],
    "天蓝色": [135, 206, 250],    # light sky blue
    "深蓝色": [0, 0, 139],        # dark blue
    "浅蓝色": [173, 216, 230],    # light blue

    "深绿色": [0, 100, 0],        # dark green
    "浅绿色": [144, 238, 144],    # light green

    "金色": [255, 215, 0],        # gold
    "银色": [192, 192, 192],      # silver
    "灰色": [128, 128, 128],      # gray
    "黑色": [0, 0, 0],            # black

    "棕色": [165, 42, 42],        # brown
    "咖啡色": [111, 78, 55],      # coffee

    "深红色": [139, 0, 0],        # dark red
    "酒红色": [128, 0, 32],       # wine red
    "玫红色": [255, 0, 127],      # rose

    "淡黄色": [255, 255, 224],    # light yellow
    "米黄色": [245, 245, 220],    # beige

    "紫罗兰色": [238, 130, 238],  # violet
    "靛蓝色": [75, 0, 130],       # indigo

    # 一些好听的描述色
    "晚霞的颜色": [255, 120, 80],      # 橙红偏粉的暖色
    "夕阳的颜色": [255, 100, 50],
    "日出时的颜色": [255, 160, 90],
    "黎明的颜色": [200, 220, 255],     # 冷一点的淡蓝
    "海边的颜色": [70, 130, 180],      # steel blue
    "大海的颜色": [0, 105, 148],
    "天空的颜色": [135, 206, 235],     # 天蓝
    "夏天的天空": [135, 206, 250],
    "森林的颜色": [34, 139, 34],
    "春天的颜色": [144, 238, 144],     # 浅绿
    "秋天的颜色": [210, 105, 30],      # 巧克力色偏橙
    "冬天的颜色": [240, 248, 255],     # 很浅的冷白

    "樱花的颜色": [255, 182, 193],    # light pink
    "薰衣草的颜色": [150, 123, 182],
    "玫瑰的颜色": [220, 20, 60],
    "薄荷的颜色": [152, 255, 152],
    "冰蓝色": [173, 216, 230],
    "暖白色": [255, 244, 229],
    "冷白色": [230, 240, 255],

    # 混合色描述（简单用大致“加权平均”的效果）
    "红色和蓝色的混合色": [180, 0, 180],    # 近似洋红/紫红
    "红色和绿色的混合色": [200, 200, 0],    # 偏黄
    "红色和黄色的混合色": [255, 140, 0],    # 橙色偏红
    "黄色和蓝色的混合色": [128, 255, 128],  # 亮黄绿色
    "黄色和绿色的混合色": [180, 255, 100],  # 柠檬绿
    "蓝色和绿色的混合色": [0, 200, 180],    # 青绿
    "蓝色和紫色的混合色": [100, 0, 200],
    "红色和粉色的混合色": [255, 100, 150],

    # 一些口语化的形容
    "柔和的粉色": [255, 182, 193],
    "淡淡的蓝色": [180, 220, 255],
    "柔和的蓝色": [160, 200, 255],
    "淡淡的绿色": [195, 255, 195],
    "柔和的黄色": [255, 250, 205],
    "浪漫的紫色": [186, 85, 211],
    "梦幻的紫色": [218, 112, 214],
    "温暖的橙色": [255, 140, 0],
    "温馨的橙色": [255, 160, 90],
    "温暖的黄色": [255, 230, 150],

    "酷一点的蓝色": [0, 102, 204],
    "深一点的蓝色": [0, 0, 139],
    "暗一点的红色": [139, 0, 0],
    "亮一点的红色": [255, 80, 80],
}
# 颜色的英文翻译
COLORS_EN = {
    "红色": "red",
    "绿色": "green",
    "蓝色": "blue",
    "黄色": "yellow",
    "紫色": "purple",
    "白色": "white",
    "橙色": "orange",
    "粉色": "pink",
    "青色": "cyan",
    "黑色": "black",
    "灰色": "gray",

    "青色": "cyan",
    "青绿": "teal",
    "天蓝色": "sky blue",
    "深蓝色": "dark blue",
    "浅蓝色": "light blue",

    "深绿色": "dark green",
    "浅绿色": "light green",

    "金色": "gold",
    "银色": "silver",
    "灰色": "gray",
    "黑色": "black",

    "棕色": "brown",
    "咖啡色": "coffee",

    "深红色": "dark red",
    "酒红色": "wine red",
    "玫红色": "rose",

    "淡黄色": "light yellow",
    "米黄色": "beige",

    "紫罗兰色": "violet",
    "靛蓝色": "indigo",

    "晚霞的颜色": "sunset glow",
    "夕阳的颜色": "sunset",
    "日出时的颜色": "sunrise",
    "黎明的颜色": "dawn",
    "海边的颜色": "seaside blue",
    "大海的颜色": "sea blue",
    "天空的颜色": "sky blue",
    "夏天的天空": "summer sky",
    "森林的颜色": "forest green",
    "春天的颜色": "spring green",
    "秋天的颜色": "autumn orange",
    "冬天的颜色": "winter white",

    "樱花的颜色": "sakura pink",
    "薰衣草的颜色": "lavender",
    "玫瑰的颜色": "rose red",
    "薄荷的颜色": "mint",
    "冰蓝色": "ice blue",
    "暖白色": "warm white",
    "冷白色": "cool white",

    "红色和蓝色的混合色": "red and blue mixed",
    "红色和绿色的混合色": "red and green mixed",
    "红色和黄色的混合色": "red and yellow mixed",
    "黄色和蓝色的混合色": "yellow and blue mixed",
    "黄色和绿色的混合色": "yellow and green mixed",
    "蓝色和绿色的混合色": "blue and green mixed",
    "蓝色和紫色的混合色": "blue and purple mixed",
    "红色和粉色的混合色": "red and pink mixed",

    "柔和的粉色": "soft pink",
    "淡淡的蓝色": "light blue",
    "柔和的蓝色": "soft blue",
    "淡淡的绿色": "light green",
    "柔和的黄色": "soft yellow",
    "浪漫的紫色": "romantic purple",
    "梦幻的紫色": "dreamy purple",
    "温暖的橙色": "warm orange",
    "温馨的橙色": "cozy orange",
    "温暖的黄色": "warm yellow",

    "酷一点的蓝色": "cool blue",
    "深一点的蓝色": "darker blue",
    "暗一点的红色": "darker red",
    "亮一点的红色": "brighter red",

}

# 亮度范围（百分比）
BRIGHTNESS_RANGE = (10, 100)

# 输出配置
OUTPUT_FILE = "generated_data.json"

# 语言配置
LANGUAGES = ["zh", "en"]  # 支持的语言：中文、英文

