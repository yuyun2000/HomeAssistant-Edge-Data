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
    ],
    "switch": [
        "switch.turn_on()",
        "switch.turn_off()",
    ]
}

# 设备列表
DEVICES = {
    "light": [
        {"id": "light.living", "name": "Living Room Light", "name_zh": "客厅灯"},
        {"id": "light.living2", "name": "Living Room 2 Light", "name_zh": "客厅2号灯"},
        {"id": "light.living_strip", "name": "Living Room Strip Light", "name_zh": "客厅灯带"},
        {"id": "light.living_tv", "name": "Living Room TV Light", "name_zh": "客厅电视墙灯"},
        {"id": "light.living_corner", "name": "Living Room Corner Lamp", "name_zh": "客厅角落灯"},

        {"id": "light.bed", "name": "Bedroom Light", "name_zh": "卧室灯"},
        {"id": "light.bed_main", "name": "Bedroom Main Light", "name_zh": "卧室主灯"},
        {"id": "light.bed_strip", "name": "Bedroom Strip Light", "name_zh": "卧室灯带"},
        {"id": "light.bed_read", "name": "Bedroom Reading Light", "name_zh": "卧室阅读灯"},
        {"id": "light.bedside", "name": "Bedside Lamp", "name_zh": "床头灯"},

        {"id": "light.kitchen", "name": "Kitchen Light", "name_zh": "厨房灯"},
        {"id": "light.kitchen_main", "name": "Kitchen Main Light", "name_zh": "厨房主灯"},
        {"id": "light.kitchen_bar", "name": "Kitchen Bar Light", "name_zh": "厨房吧台灯"},
        {"id": "light.kitchen_under", "name": "Kitchen Under Cabinet Light", "name_zh": "橱柜下灯"},
        {"id": "light.kitchen_strip", "name": "Kitchen Strip Light", "name_zh": "厨房灯带"},

        {"id": "light.dining", "name": "Dining Room Light", "name_zh": "餐厅灯"},
        {"id": "light.dining_main", "name": "Dining Main Light", "name_zh": "餐厅主灯"},
        {"id": "light.dining_bar", "name": "Dining Bar Light", "name_zh": "餐边吧台灯"},
        {"id": "light.dining_wall", "name": "Dining Wall Light", "name_zh": "餐厅墙灯"},

        {"id": "light.bath", "name": "Bathroom Light", "name_zh": "卫生间灯"},
        {"id": "light.bath_main", "name": "Bathroom Main Light", "name_zh": "卫生间主灯"},
        {"id": "light.bath_mirror", "name": "Bathroom Mirror Light", "name_zh": "卫浴镜前灯"},
        {"id": "light.bath_shower", "name": "Shower Light", "name_zh": "淋浴灯"},

        {"id": "light.hall", "name": "Hallway Light", "name_zh": "走廊灯"},
        {"id": "light.hall_main", "name": "Hallway Main Light", "name_zh": "走廊主灯"},
        {"id": "light.hall_night", "name": "Hallway Night Light", "name_zh": "走廊夜灯"},

        {"id": "light.study", "name": "Study Light", "name_zh": "书房灯"},
        {"id": "light.study_main", "name": "Study Main Light", "name_zh": "书房主灯"},
        {"id": "light.study_desk", "name": "Study Desk Light", "name_zh": "书桌灯"},
        {"id": "light.study_wall", "name": "Study Wall Light", "name_zh": "书房壁灯"},

        {"id": "light.kids", "name": "Kids Room Light", "name_zh": "儿童房灯"},
        {"id": "light.kids_main", "name": "Kids Main Light", "name_zh": "儿童房主灯"},
        {"id": "light.kids_night", "name": "Kids Night Light", "name_zh": "儿童夜灯"},

        {"id": "light.master", "name": "Master Bedroom Light", "name_zh": "主卧灯"},
        {"id": "light.guest", "name": "Guest Room Light", "name_zh": "客房灯"},
        {"id": "light.guest_main", "name": "Guest Main Light", "name_zh": "客房主灯"},
        {"id": "light.guest_bedside", "name": "Guest Bedside Lamp", "name_zh": "客房床头灯"},

        {"id": "light.balcony", "name": "Balcony Light", "name_zh": "阳台灯"},
        {"id": "light.balcony_main", "name": "Balcony Main Light", "name_zh": "阳台主灯"},
        {"id": "light.balcony_plant", "name": "Balcony Plant Light", "name_zh": "阳台植物灯"},

        {"id": "light.porch", "name": "Porch Light", "name_zh": "门廊灯"},
        {"id": "light.entry", "name": "Entry Light", "name_zh": "玄关灯"},
        {"id": "light.entry_main", "name": "Entry Main Light", "name_zh": "玄关主灯"},

        {"id": "light.garage", "name": "Garage Light", "name_zh": "车库灯"},
        {"id": "light.garage_main", "name": "Garage Main Light", "name_zh": "车库主灯"},
        {"id": "light.garage_side", "name": "Garage Side Light", "name_zh": "车库侧灯"},

        {"id": "light.stairs", "name": "Stairs Light", "name_zh": "楼梯灯"},
        {"id": "light.stairs_step", "name": "Stairs Step Light", "name_zh": "踏步灯"},
        {"id": "light.stairs_wall", "name": "Stairs Wall Light", "name_zh": "楼梯墙灯"},
        # ---------- very short ids ----------
        {"id": "light.a", "name": "A Light", "name_zh": "A灯"},
        {"id": "light.b", "name": "B Light", "name_zh": "B灯"},
        {"id": "light.c1", "name": "C1 Light", "name_zh": "C1灯"},
        {"id": "light.x", "name": "X Light", "name_zh": "X灯"},
        {"id": "light.y1", "name": "Y1 Light", "name_zh": "Y1灯"},
        {"id": "light.z9", "name": "Z9 Light", "name_zh": "Z9灯"},
        {"id": "light.lr", "name": "LR Light", "name_zh": "LR灯"},
        {"id": "light.br", "name": "BR Light", "name_zh": "BR灯"},
        {"id": "light.k1", "name": "K1 Light", "name_zh": "K1灯"},
        {"id": "light.wc", "name": "WC Light", "name_zh": "卫生间灯"},
        {"id": "light.s1", "name": "S1 Light", "name_zh": "S1灯"},
        {"id": "light.l1", "name": "L1 Light", "name_zh": "L1灯"},
        {"id": "light.aa", "name": "AA Light", "name_zh": "AA灯"},
        {"id": "light.bb2", "name": "BB2 Light", "name_zh": "BB2灯"},
        {"id": "light.p", "name": "P Light", "name_zh": "P灯"},

        # ---------- typical short-ish user style ----------
        {"id": "light.lr1", "name": "Living Room 1 Light", "name_zh": "客厅1号灯"},
        {"id": "light.lr2", "name": "Living Room 2 Light", "name_zh": "客厅2号灯"},
        {"id": "light.br1", "name": "Bedroom 1 Light", "name_zh": "卧室1号灯"},
        {"id": "light.br2", "name": "Bedroom 2 Light", "name_zh": "卧室2号灯"},
        {"id": "light.k", "name": "Kitchen Light", "name_zh": "厨房灯"},
        {"id": "light.k2", "name": "Kitchen 2 Light", "name_zh": "厨房2号灯"},
        {"id": "light.bth", "name": "Bath Light", "name_zh": "浴室灯"},
        {"id": "light.din", "name": "Dining Light", "name_zh": "餐厅灯"},
        {"id": "light.stu", "name": "Study Light", "name_zh": "书房灯"},
        {"id": "light.yt", "name": "Balcony Light", "name_zh": "阳台灯"},
        {"id": "light.dr", "name": "Doorway Light", "name_zh": "门口灯"},
        {"id": "light.entr", "name": "Entrance Light", "name_zh": "玄关灯"},
        {"id": "light.tv", "name": "TV Wall Light", "name_zh": "电视墙灯"},
        {"id": "light.ws", "name": "Workstation Light", "name_zh": "工位灯"},
        {"id": "light.pc", "name": "PC Desk Light", "name_zh": "电脑桌灯"},
        {"id": "light.mb", "name": "Master Bed Light", "name_zh": "主卧灯"},
        {"id": "light.k3", "name": "Kitchen 3 Light", "name_zh": "厨房3号灯"},
        {"id": "light.bal", "name": "Balcony Main Light", "name_zh": "阳台主灯"},
        {"id": "light.clo", "name": "Closet Light", "name_zh": "衣柜灯"},
        {"id": "light.st", "name": "Stair Light", "name_zh": "楼梯灯"},
        {"id": "light.gr", "name": "Garden Light", "name_zh": "花园灯"},
        {"id": "light.pt", "name": "Patio Light", "name_zh": "庭院灯"},
        {"id": "light.rd", "name": "Reading Light", "name_zh": "阅读灯"},
        {"id": "light.bedl", "name": "Bedside Light", "name_zh": "床边灯"},
        {"id": "light.ac", "name": "Accent Light", "name_zh": "氛围灯"},
        {"id": "light.tb", "name": "Table Light", "name_zh": "桌面灯"},
        {"id": "light.w1", "name": "Wall 1 Light", "name_zh": "墙灯1"},
        {"id": "light.w2", "name": "Wall 2 Light", "name_zh": "墙灯2"},
        {"id": "light.roof", "name": "Roof Light", "name_zh": "屋顶灯"},
        {"id": "light.floor", "name": "Floor Light", "name_zh": "地灯"},
        # ---------- long ids (4–5 words-ish) ----------
        {"id": "light.living_room_corner_floor_lamp", "name": "Living Room Corner Floor Lamp", "name_zh": "客厅角落落地灯"},
        {"id": "light.bedroom_window_side_reading_lamp", "name": "Bedroom Window Side Reading Lamp", "name_zh": "卧室窗边阅读灯"},
        {"id": "light.kitchen_island_pendant_cluster", "name": "Kitchen Island Pendant Cluster", "name_zh": "厨房岛台吊灯组"},
        {"id": "light.hallway_motion_activated_spot", "name": "Hallway Motion Activated Spot", "name_zh": "走廊感应射灯"},
        {"id": "light.bathroom_shower_ceiling_spot", "name": "Bathroom Shower Ceiling Spot", "name_zh": "浴室淋浴顶灯"},
        {"id": "light.garage_ceiling_center_main", "name": "Garage Ceiling Center Main", "name_zh": "车库中部主灯"},
        {"id": "light.backyard_patio_string_lights", "name": "Backyard Patio String Lights", "name_zh": "后院天台串灯"},
        {"id": "light.front_yard_garden_path_lights", "name": "Front Yard Garden Path Lights", "name_zh": "前院花园小径灯"},
        {"id": "light.study_bookshelf_ambient_strip", "name": "Study Bookshelf Ambient Strip", "name_zh": "书房书架氛围灯带"},
        {"id": "light.dining_table_center_pendant", "name": "Dining Table Center Pendant", "name_zh": "餐桌中部吊灯"},
        {"id": "light.master_bedroom_ceiling_spot_array", "name": "Master Bedroom Ceiling Spot Array", "name_zh": "主卧顶射灯阵列"},
        {"id": "light.kids_room_ceiling_star_projector", "name": "Kids Room Ceiling Star Projector", "name_zh": "儿童房星空投影灯"},
        {"id": "light.balcony_wall_mount_sconce_pair", "name": "Balcony Wall Mount Sconce Pair", "name_zh": "阳台壁挂双头灯"},
        {"id": "light.staircase_step_safety_lights", "name": "Staircase Step Safety Lights", "name_zh": "楼梯踏步安全灯"},
        {"id": "light.home_office_monitor_backlight", "name": "Home Office Monitor Backlight", "name_zh": "家庭办公室显示器背光"},
        {"id": "light.living_room_tv_backlight_strip", "name": "Living Room TV Backlight Strip", "name_zh": "客厅电视背景灯带"},
        {"id": "light.living_room_window_sill_lamp", "name": "Living Room Window Sill Lamp", "name_zh": "客厅窗台灯"},
        {"id": "light.living_room_sofa_side_lamp", "name": "Living Room Sofa Side Lamp", "name_zh": "客厅沙发边灯"},
        {"id": "light.bedroom_headboard_ambient_strip", "name": "Bedroom Headboard Ambient Strip", "name_zh": "卧室床头氛围灯带"},
        {"id": "light.bedroom_closet_ceiling_spots", "name": "Bedroom Closet Ceiling Spots", "name_zh": "卧室衣柜顶射灯"},
        {"id": "light.bedroom_dressing_table_mirror", "name": "Bedroom Dressing Table Mirror Light", "name_zh": "卧室梳妆镜灯"},
        {"id": "light.kitchen_under_cabinet_led_strip", "name": "Kitchen Under Cabinet LED Strip", "name_zh": "厨房橱柜下灯带"},
        {"id": "light.kitchen_sink_task_spot_light", "name": "Kitchen Sink Task Spot Light", "name_zh": "厨房水槽照明射灯"},
        {"id": "light.kitchen_pantry_ceiling_center", "name": "Kitchen Pantry Ceiling Center Light", "name_zh": "厨房储物间顶灯"},
        {"id": "light.bathroom_vanity_side_wall_sconces", "name": "Bathroom Vanity Side Wall Sconces", "name_zh": "浴室洗手台壁灯"},
        {"id": "light.bathroom_toilet_area_ceiling", "name": "Bathroom Toilet Area Ceiling Light", "name_zh": "浴室马桶区顶灯"},
        {"id": "light.entryway_ceiling_flush_mount", "name": "Entryway Ceiling Flush Mount", "name_zh": "玄关吸顶灯"},
        {"id": "light.hallway_night_motion_guides", "name": "Hallway Night Motion Guides", "name_zh": "走廊夜间感应灯"},
        {"id": "light.garage_workbench_overhead_strip", "name": "Garage Workbench Overhead Strip", "name_zh": "车库工作台顶灯带"},
        {"id": "light.garage_side_door_exterior_lamp", "name": "Garage Side Door Exterior Lamp", "name_zh": "车库侧门外灯"},
        {"id": "light.backyard_wooden_deck_step_lights", "name": "Backyard Wooden Deck Step Lights", "name_zh": "后院木平台踏步灯"},
        {"id": "light.backyard_tree_uplight_spot", "name": "Backyard Tree Uplight Spot", "name_zh": "后院树下上照灯"},
        {"id": "light.front_porch_ceiling_fan_light", "name": "Front Porch Ceiling Fan Light", "name_zh": "前廊风扇灯"},
        {"id": "light.front_gate_pillar_lanterns", "name": "Front Gate Pillar Lanterns", "name_zh": "大门门柱灯"},
        {"id": "light.study_corner_floor_reading_lamp", "name": "Study Corner Floor Reading Lamp", "name_zh": "书房角落阅读落地灯"},
        {"id": "light.study_desk_overhead_panel_light", "name": "Study Desk Overhead Panel Light", "name_zh": "书桌上方面板灯"},
        {"id": "light.dining_room_wall_washer_strip", "name": "Dining Room Wall Washer Strip", "name_zh": "餐厅洗墙灯带"},
        {"id": "light.dining_room_cabinet_display_lights", "name": "Dining Room Cabinet Display Lights", "name_zh": "餐边柜展示灯"},
        {"id": "light.staircase_handrail_led_strip", "name": "Staircase Handrail LED Strip", "name_zh": "楼梯扶手灯带"},
        {"id": "light.staircase_mid_landing_ceiling_light", "name": "Staircase Mid Landing Ceiling Light", "name_zh": "楼梯中平台顶灯"},
        {"id": "light.home_office_ceiling_panel_main", "name": "Home Office Ceiling Panel Main", "name_zh": "家庭办公室主面板灯"},
        {"id": "light.home_office_bookshelf_spot_array", "name": "Home Office Bookshelf Spot Array", "name_zh": "家庭办公室书架射灯阵列"},
        {"id": "light.kids_room_bed_under_glow_strip", "name": "Kids Room Bed Under Glow Strip", "name_zh": "儿童床底氛围灯带"},
        {"id": "light.kids_room_desk_task_lamp", "name": "Kids Room Desk Task Lamp", "name_zh": "儿童学习桌台灯"},
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

        {"id": "cover.master_bedroom_curtain", "name": "Master Bedroom Curtain", "name_zh": "主卧窗帘"},
        {"id": "cover.guest_bedroom_blinds", "name": "Guest Bedroom Blinds", "name_zh": "次卧百叶窗"},
        {"id": "cover.study_room_shade", "name": "Study Room Shade", "name_zh": "书房遮光帘"},
        {"id": "cover.dining_room_curtain", "name": "Dining Room Curtain", "name_zh": "餐厅窗帘"},
        {"id": "cover.balcony_sunshade", "name": "Balcony Sunshade", "name_zh": "阳台遮阳帘"},
        {"id": "cover.bathroom_blinds", "name": "Bathroom Blinds", "name_zh": "浴室百叶窗"},
        {"id": "cover.staircase_window_shade", "name": "Staircase Window Shade", "name_zh": "楼梯窗遮光帘"},
        {"id": "cover.attic_skylight", "name": "Attic Skylight", "name_zh": "阁楼天窗"},
        {"id": "cover.kids_room_curtain", "name": "Kids Room Curtain", "name_zh": "儿童房窗帘"},
        {"id": "cover.media_room_blackout", "name": "Media Room Blackout Shade", "name_zh": "影音室遮光帘"},
        {"id": "cover.front_porch_awning", "name": "Front Porch Awning", "name_zh": "前门门廊遮阳篷"},
        {"id": "cover.backyard_patio_awning", "name": "Backyard Patio Awning", "name_zh": "后院露台遮阳篷"},
        {"id": "cover.greenhouse_shade", "name": "Greenhouse Shade", "name_zh": "温室遮阳帘"},
        {"id": "cover.office_blinds", "name": "Home Office Blinds", "name_zh": "家庭办公室百叶窗"},
        {"id": "cover.laundry_room_blinds", "name": "Laundry Room Blinds", "name_zh": "洗衣房百叶窗"},
        {"id": "cover.hallway_window_shade", "name": "Hallway Window Shade", "name_zh": "走廊窗帘"},
        {"id": "cover.poolside_pergola_shade", "name": "Poolside Pergola Shade", "name_zh": "泳池凉亭遮阳帘"},
        {"id": "cover.terrace_screen", "name": "Terrace Screen", "name_zh": "露台卷帘门"},
        {"id": "cover.workshop_garage_door", "name": "Workshop Garage Door", "name_zh": "车间车库门"},
    ],
    "lock": [
        {"id": "lock.front_door", "name": "Front Door Lock", "name_zh": "前门锁"},
        {"id": "lock.back_door", "name": "Back Door Lock", "name_zh": "后门锁"},
        {"id": "lock.garage_entry", "name": "Garage Entry Lock", "name_zh": "车库入口锁"},
        {"id": "lock.side_gate", "name": "Side Gate Lock", "name_zh": "侧门锁"},
        {"id": "lock.basement_door", "name": "Basement Door Lock", "name_zh": "地下室门锁"},
        {"id": "lock.shed_padlock", "name": "Shed Padlock", "name_zh": "储物间挂锁"},
        {"id": "lock.wine_cellar", "name": "Wine Cellar Lock", "name_zh": "酒窖锁"},
        {"id": "lock.master_bedroom_door", "name": "Master Bedroom Door Lock", "name_zh": "主卧门锁"},
        {"id": "lock.guest_bedroom_door", "name": "Guest Bedroom Door Lock", "name_zh": "客卧门锁"},
        {"id": "lock.study_room_door", "name": "Study Room Door Lock", "name_zh": "书房门锁"},
        {"id": "lock.home_office_door", "name": "Home Office Door Lock", "name_zh": "家庭办公室门锁"},
        {"id": "lock.kids_room_door", "name": "Kids Room Door Lock", "name_zh": "儿童房门锁"},
        {"id": "lock.balcony_door", "name": "Balcony Door Lock", "name_zh": "阳台门锁"},
        {"id": "lock.rooftop_access", "name": "Rooftop Access Lock", "name_zh": "屋顶通道锁"},
        {"id": "lock.pool_gate", "name": "Pool Gate Lock", "name_zh": "泳池门锁"},
        {"id": "lock.backyard_gate", "name": "Backyard Gate Lock", "name_zh": "后院门锁"},
        {"id": "lock.mailbox", "name": "Mailbox Lock", "name_zh": "信箱锁"},
        {"id": "lock.safe", "name": "Safe Lock", "name_zh": "保险箱锁"},
        {"id": "lock.attic_door", "name": "Attic Door Lock", "name_zh": "阁楼门锁"},
        {"id": "lock.server_cabinet", "name": "Server Cabinet Lock", "name_zh": "服务器柜锁"},
        {"id": "lock.tool_cabinet", "name": "Tool Cabinet Lock", "name_zh": "工具柜锁"},
        {"id": "lock.medicine_cabinet", "name": "Medicine Cabinet Lock", "name_zh": "药柜锁"},
        {"id": "lock.garage_side_door", "name": "Garage Side Door Lock", "name_zh": "车库侧门锁"},
        {"id": "lock.patio_door", "name": "Patio Door Lock", "name_zh": "露台门锁"},
        {"id": "lock.storage_room_door", "name": "Storage Room Door Lock", "name_zh": "储藏室门锁"},
        {"id": "lock.workshop_door", "name": "Workshop Door Lock", "name_zh": "工坊门锁"},
        {"id": "lock.garden_shed_door", "name": "Garden Shed Door Lock", "name_zh": "花园小屋门锁"},
    ],
    "fan": [
        {"id": "fan.living_room_ceiling", "name": "Living Room Ceiling Fan", "name_zh": "客厅吊扇"},
        {"id": "fan.bedroom_master", "name": "Master Bedroom Fan", "name_zh": "主卧风扇"},
        {"id": "fan.bedroom_guest", "name": "Guest Bedroom Fan", "name_zh": "客房风扇"},
        {"id": "fan.dining_room", "name": "Dining Room Fan", "name_zh": "餐厅风扇"},
        {"id": "fan.patio_outdoor", "name": "Outdoor Patio Fan", "name_zh": "露台风扇"},
        {"id": "fan.office_desk", "name": "Office Desk Fan", "name_zh": "办公桌风扇"},
        {"id": "fan.kitchen_ceiling", "name": "Kitchen Ceiling Fan", "name_zh": "厨房吊扇"},
        {"id": "fan.living_room_standing", "name": "Living Room Standing Fan", "name_zh": "客厅立式风扇"},
        {"id": "fan.bedroom_kids", "name": "Kids Bedroom Fan", "name_zh": "儿童房风扇"},
        {"id": "fan.study_room", "name": "Study Room Fan", "name_zh": "书房风扇"},
        {"id": "fan.balcony_wall", "name": "Balcony Wall Fan", "name_zh": "阳台壁扇"},
        {"id": "fan.garage_ventilation", "name": "Garage Ventilation Fan", "name_zh": "车库排风扇"},
        {"id": "fan.bathroom_exhaust", "name": "Bathroom Exhaust Fan", "name_zh": "浴室排风扇"},
        {"id": "fan.laundry_room", "name": "Laundry Room Fan", "name_zh": "洗衣房风扇"},
        {"id": "fan.attic_vent", "name": "Attic Vent Fan", "name_zh": "阁楼通风扇"},
        {"id": "fan.basement_circulation", "name": "Basement Circulation Fan", "name_zh": "地下室循环风扇"},
        {"id": "fan.kitchen_range_hood", "name": "Kitchen Range Hood Fan", "name_zh": "厨房油烟机风扇"},
        {"id": "fan.server_room_cooling", "name": "Server Room Cooling Fan", "name_zh": "机房冷却风扇"},
        {"id": "fan.home_theater", "name": "Home Theater Fan", "name_zh": "影音室风扇"},
        {"id": "fan.gym_room", "name": "Home Gym Fan", "name_zh": "家庭健身房风扇"},
        {"id": "fan.dressing_room", "name": "Dressing Room Fan", "name_zh": "更衣室风扇"},
    ],
    "timer": [
        {"id": "timer.cooking", "name": "Cooking Timer", "name_zh": "烹饪计时器"},
        {"id": "timer.laundry", "name": "Laundry Timer", "name_zh": "洗衣计时器"},
        {"id": "timer.workout", "name": "Workout Timer", "name_zh": "健身计时器"},
        {"id": "timer.meditation", "name": "Meditation Timer", "name_zh": "冥想计时器"},
        {"id": "timer.cleaning", "name": "Cleaning Timer", "name_zh": "打扫计时器"},
        {"id": "timer.study", "name": "Study Timer", "name_zh": "学习计时器"},
        {"id": "timer.pomodoro", "name": "Pomodoro Timer", "name_zh": "番茄钟计时器"},
        {"id": "timer.nap", "name": "Nap Timer", "name_zh": "小憩计时器"},
        {"id": "timer.outdoor_watering", "name": "Outdoor Watering Timer", "name_zh": "室外浇水计时器"},
        {"id": "timer.plant_grow_light", "name": "Plant Grow Light Timer", "name_zh": "植物生长灯计时器"},
        {"id": "timer.screen_time", "name": "Screen Time Timer", "name_zh": "屏幕时间计时器"},
        {"id": "timer.kids_bedtime", "name": "Kids Bedtime Timer", "name_zh": "儿童睡前计时器"},
        {"id": "timer.tea_brewing", "name": "Tea Brewing Timer", "name_zh": "泡茶计时器"},
        {"id": "timer.coffee_brewing", "name": "Coffee Brewing Timer", "name_zh": "咖啡冲煮计时器"},
        {"id": "timer.sauna_session", "name": "Sauna Session Timer", "name_zh": "桑拿计时器"},
        {"id": "timer.yoga_session", "name": "Yoga Session Timer", "name_zh": "瑜伽计时器"},
    ],
    "vacuum": [
        {"id": "vacuum.living_room_robot", "name": "Living Room Robot Vacuum", "name_zh": "客厅扫地机器人"},
        {"id": "vacuum.upstairs_cleaner", "name": "Upstairs Robot Cleaner", "name_zh": "楼上扫地机"},
        {"id": "vacuum.basement_bot", "name": "Basement Cleaning Bot", "name_zh": "地下室清洁机器人"},
        {"id": "vacuum.kitchen_robot", "name": "Kitchen Robot Vacuum", "name_zh": "厨房扫地机器人"},
        {"id": "vacuum.bedroom_robot", "name": "Bedroom Robot Vacuum", "name_zh": "卧室扫地机器人"},
        {"id": "vacuum.hallway_robot", "name": "Hallway Robot Vacuum", "name_zh": "走廊扫地机器人"},
        {"id": "vacuum.garage_robot", "name": "Garage Robot Vacuum", "name_zh": "车库扫地机器人"},
        {"id": "vacuum.dining_room_robot", "name": "Dining Room Robot Vacuum", "name_zh": "餐厅扫地机器人"},
        {"id": "vacuum.kids_room_robot", "name": "Kids Room Robot Vacuum", "name_zh": "儿童房扫地机器人"},
        {"id": "vacuum.patio_robot", "name": "Patio Robot Cleaner", "name_zh": "露台清洁机器人"},
        {"id": "vacuum.stairs_spot_cleaner", "name": "Stairs Spot Cleaner", "name_zh": "楼梯局部清洁机"},
    ],
    "media_player": [
        {"id": "media_player.living_room_tv", "name": "Living Room TV", "name_zh": "客厅电视"},
        {"id": "media_player.bedroom_tv", "name": "Bedroom TV", "name_zh": "卧室电视"},
        {"id": "media_player.kitchen_speaker", "name": "Kitchen Smart Speaker", "name_zh": "厨房智能音箱"},
        {"id": "media_player.bathroom_speaker", "name": "Bathroom Speaker", "name_zh": "浴室音箱"},
        {"id": "media_player.garage_radio", "name": "Garage Radio", "name_zh": "车库收音机"},
        {"id": "media_player.dining_room_speaker", "name": "Dining Room Speaker", "name_zh": "餐厅音箱"},
        {"id": "media_player.living_room_soundbar", "name": "Living Room Soundbar", "name_zh": "客厅回音壁"},
        {"id": "media_player.home_theater_receiver", "name": "Home Theater Receiver", "name_zh": "家庭影院功放"},
        {"id": "media_player.study_room_speaker", "name": "Study Room Speaker", "name_zh": "书房音箱"},
        {"id": "media_player.office_speaker", "name": "Office Speaker", "name_zh": "办公室音箱"},
        {"id": "media_player.patio_speaker", "name": "Patio Speaker", "name_zh": "露台音箱"},
        {"id": "media_player.bedroom_smart_display", "name": "Bedroom Smart Display", "name_zh": "卧室智能屏"},
        {"id": "media_player.kids_room_speaker", "name": "Kids Room Speaker", "name_zh": "儿童房音箱"},
        {"id": "media_player.gym_room_speaker", "name": "Home Gym Speaker", "name_zh": "家庭健身房音箱"},
        {"id": "media_player.study_headphones", "name": "Study Headphones", "name_zh": "书房耳机"},
        {"id": "media_player.game_console", "name": "Game Console", "name_zh": "游戏主机"},
        {"id": "media_player.projector", "name": "Home Projector", "name_zh": "家庭投影仪"},
    ],
    "switch": [
        # --- 加热设备 (Heaters) ---
        {"id": "switch.living_room_heater", "name": "Living Room Space Heater", "name_zh": "客厅取暖器"},
        {"id": "switch.bedroom_floor_heating", "name": "Master Bedroom Floor Heating", "name_zh": "主卧地暖"},
        {"id": "switch.bathroom_wall_heater", "name": "Bathroom Wall-Mounted Heater", "name_zh": "浴室壁挂暖风机"},
        {"id": "switch.patio_heater", "name": "Outdoor Patio Heater", "name_zh": "户外露台加热器"},
        {"id": "switch.office_foot_warmer", "name": "Office Foot Warmer Mat", "name_zh": "办公室暖脚垫"},
        {"id": "switch.towel_warmer", "name": "Plug-in Towel Warmer", "name_zh": "电热毛巾架"},
        {"id": "switch.baseboard_heater", "name": "Baseboard Convection Heater", "name_zh": "踢脚线加热器"},
        {"id": "switch.garage_heater", "name": "Garage Workshop Heater", "name_zh": "车库工作间加热器"},
        {"id": "switch.heater", "name": "Heater", "name_zh": "加热器"},

        # --- 厨房电器 (Kitchen Appliances) ---
        {"id": "switch.rice_cooker", "name": "Smart Rice Cooker", "name_zh": "智能电饭煲"},
        {"id": "switch.toaster", "name": "Kitchen Toaster", "name_zh": "烤面包机"},
        {"id": "switch.slow_cooker", "name": "Electric Slow Cooker", "name_zh": "电炖锅"},
        {"id": "switch.wine_cooler", "name": "Wine Cellar Cooler", "name_zh": "酒柜制冷器"},
        {"id": "switch.sandwich_maker", "name": "Breakfast Sandwich Maker", "name_zh": "三明治机"},
        {"id": "switch.dishwasher_power", "name": "Dishwasher Main Power", "name_zh": "洗碗机总电源"},
        {"id": "switch.water_dispenser", "name": "Instant Water Dispenser", "name_zh": "即热饮水机"},

        # --- 清洁与机器人 (Cleaning & Robotics) ---
        {"id": "switch.robot_mop", "name": "Robotic Mop Power", "name_zh": "拖地机器人电源"},
        {"id": "switch.shoe_dryer", "name": "Electric Shoe Dryer", "name_zh": "烘鞋器"},
        {"id": "switch.ultrasonic_cleaner", "name": "Ultrasonic Jewelry Cleaner", "name_zh": "超声波清洗机"},
        {"id": "switch.pool_cleaner", "name": "Automatic Pool Cleaner", "name_zh": "自动泳池清洗机"},

        # --- 生活环境与健康 (Environment & Health) ---
        {"id": "switch.massage_chair", "name": "Living Room Massage Chair", "name_zh": "客厅按摩椅"},
        {"id": "switch.oxygen_concentrator", "name": "Home Oxygen Concentrator", "name_zh": "家用制氧机"},
        {"id": "switch.uv_sanitizer", "name": "Entrance UV Sanitizer", "name_zh": "玄关紫外线消毒灯"},
        {"id": "switch.electric_toothbrush_charger", "name": "Toothbrush Sanitizer Case", "name_zh": "牙刷消毒盒"},
        {"id": "switch.eye_massager", "name": "Eye Massager Charger", "name_zh": "眼部按摩仪"},

        # --- 户外与园艺 (Outdoor & Garden) ---
        {"id": "switch.pond_fountain", "name": "Garden Pond Fountain", "name_zh": "花园喷泉"},
        {"id": "switch.insect_trap", "name": "Outdoor Insect Trap", "name_zh": "户外捕虫灯"},
        {"id": "switch.greenhouse_fan", "name": "Greenhouse Exhaust Fan", "name_zh": "温室排风扇"},
        {"id": "switch.irrigation_pump", "name": "Lawn Irrigation Pump", "name_zh": "草坪灌溉泵"},

        # --- 娱乐与办公 (Entertainment & Office) ---
        {"id": "switch.christmas_tree_lights", "name": "Christmas Tree Lights", "name_zh": "圣诞树装饰灯"},
        {"id": "switch.projector_screen", "name": "Projector Screen Motor", "name_zh": "投影幕布电机"},
        {"id": "switch.three_d_printer", "name": "3D Printer Power", "name_zh": "3D打印机电源"},
        {"id": "switch.paper_shredder", "name": "Office Paper Shredder", "name_zh": "碎纸机"},
        {"id": "switch.soldering_station", "name": "Hobby Soldering Station", "name_zh": "焊台电源"},

        # --- 其他 (Misc) ---
        {"id": "switch.door_bell_chime", "name": "Doorbell Chime Mute", "name_zh": "门铃响铃开关"},
        {"id": "switch.garage_door_opener", "name": "Garage Door Remote Switch", "name_zh": "车库门遥控开关"},
        {"id": "switch.scented_oil_warmer", "name": "Scented Oil Warmer", "name_zh": "香薰油加热器"},
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

