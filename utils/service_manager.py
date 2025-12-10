"""
服务管理模块 - 处理服务调用相关的操作
"""
import random
from typing import Dict, List, Optional, Any
from config import COLORS, BRIGHTNESS_RANGE


class ServiceManager:
    """服务管理器"""
    
    # 服务与中文动作的映射
    SERVICE_ACTION_MAP = {
        "light.turn_on": ["打开", "开启", "点亮", "开", "打开灯", "亮起", "启动"],
        "light.turn_off": ["关闭", "关掉", "熄灭", "关", "关灯", "关闭灯", "熄掉"],
        "light.toggle": ["切换", "反转", "切换状态"],
        "cover.open_cover": ["打开", "拉开", "开启", "升起", "打开窗帘", "拉开窗帘", "展开"],
        "cover.close_cover": ["关闭", "拉上", "关上", "降下", "关闭窗帘", "拉上窗帘", "收起"],
        "cover.stop_cover": ["停止", "暂停", "停下"],
        "cover.toggle": ["切换", "反转"],
        "lock.lock": ["锁上", "上锁", "锁定", "锁门", "加锁", "闭锁"],
        "lock.unlock": ["解锁", "开锁", "打开", "开门", "解开", "开启"],
        "fan.turn_on": ["打开", "开启", "启动", "打开风扇", "开风扇"],
        "fan.turn_off": ["关闭", "关掉", "停止", "关风扇", "关闭风扇"],
        "fan.increase_speed": ["加速", "提高速度", "加快", "转快点", "风大一点"],
        "fan.decrease_speed": ["减速", "降低速度", "减慢", "转慢点", "风小一点"],
        "fan.toggle": ["切换", "反转"],
        "vacuum.start": ["开始", "启动", "打扫", "开始清扫", "开始工作", "启动扫地"],
        "vacuum.stop": ["停止", "停下", "停止清扫"],
        "vacuum.pause": ["暂停", "暂停清扫"],
        "vacuum.return_to_base": ["回充", "回家", "返回", "返回充电", "回去充电", "回基站"],
        "media_player.turn_on": ["打开", "开启", "启动"],
        "media_player.turn_off": ["关闭", "关掉", "关机"],
        "media_player.media_play": ["播放", "开始播放", "继续播放"],
        "media_player.media_pause": ["暂停", "暂停播放"],
        "media_player.media_stop": ["停止", "停止播放"],
        "media_player.media_next_track": ["下一曲", "下一首", "切歌", "下一个", "跳过"],
        "media_player.media_previous_track": ["上一曲", "上一首", "上一个", "回到上一首"],
        "media_player.volume_up": ["音量增大", "调大音量", "大声", "声音大点", "增大音量"],
        "media_player.volume_down": ["音量减小", "调小音量", "小声", "声音小点", "降低音量"],
        "media_player.volume_mute": ["静音", "关闭声音", "消音"],
        "timer.start": ["启动", "开始", "设置", "开启计时", "启动计时器"],
        "timer.pause": ["暂停", "暂停计时"],
        "timer.cancel": ["取消", "停止", "取消计时", "停止计时"],
    }
    
    # 服务与英文动作的映射
    SERVICE_ACTION_MAP_EN = {
        "light.turn_on": ["turn on", "switch on", "power on", "activate", "light up", "illuminate"],
        "light.turn_off": ["turn off", "switch off", "power off", "deactivate", "shut off", "turn out"],
        "light.toggle": ["toggle", "switch", "flip"],
        "cover.open_cover": ["open", "raise", "lift", "pull up", "unfold", "extend"],
        "cover.close_cover": ["close", "lower", "pull down", "shut", "fold", "retract"],
        "cover.stop_cover": ["stop", "halt", "pause"],
        "cover.toggle": ["toggle", "switch"],
        "lock.lock": ["lock", "secure", "bolt", "fasten", "engage"],
        "lock.unlock": ["unlock", "open", "unbolt", "release", "disengage"],
        "fan.turn_on": ["turn on", "start", "power on", "activate", "switch on"],
        "fan.turn_off": ["turn off", "stop", "power off", "shut off", "switch off"],
        "fan.increase_speed": ["speed up", "increase speed", "go faster", "turn up"],
        "fan.decrease_speed": ["slow down", "decrease speed", "go slower", "turn down"],
        "fan.toggle": ["toggle", "switch"],
        "vacuum.start": ["start", "begin cleaning", "start cleaning", "activate", "run"],
        "vacuum.stop": ["stop", "halt", "stop cleaning"],
        "vacuum.pause": ["pause", "pause cleaning"],
        "vacuum.return_to_base": ["return to base", "go home", "dock", "return for charging", "go back"],
        "media_player.turn_on": ["turn on", "power on", "switch on"],
        "media_player.turn_off": ["turn off", "power off", "shut down"],
        "media_player.media_play": ["play", "start playing", "resume"],
        "media_player.media_pause": ["pause", "pause playback"],
        "media_player.media_stop": ["stop", "stop playback", "halt"],
        "media_player.media_next_track": ["next track", "skip", "next song", "skip forward", "next"],
        "media_player.media_previous_track": ["previous track", "go back", "previous song", "last track", "previous"],
        "media_player.volume_up": ["volume up", "louder", "increase volume", "turn up", "raise volume"],
        "media_player.volume_down": ["volume down", "quieter", "decrease volume", "turn down", "lower volume"],
        "media_player.volume_mute": ["mute", "silence", "mute audio"],
        "timer.start": ["start", "set", "begin", "activate", "start timer"],
        "timer.pause": ["pause", "pause timer"],
        "timer.cancel": ["cancel", "stop", "abort", "end timer"],
    }
    
    # 反向映射：中文动作到服务
    ACTION_SERVICE_MAP = {}
    for service, actions in SERVICE_ACTION_MAP.items():
        for action in actions:
            if action not in ACTION_SERVICE_MAP:
                ACTION_SERVICE_MAP[action] = []
            ACTION_SERVICE_MAP[action].append(service)
    
    # 反向映射：英文动作到服务
    ACTION_SERVICE_MAP_EN = {}
    for service, actions in SERVICE_ACTION_MAP_EN.items():
        for action in actions:
            if action not in ACTION_SERVICE_MAP_EN:
                ACTION_SERVICE_MAP_EN[action] = []
            ACTION_SERVICE_MAP_EN[action].append(service)
    
    def get_service_for_action(self, device_type: str, action: str) -> Optional[str]:
        """
        根据设备类型和动作获取对应的服务
        
        Args:
            device_type: 设备类型
            action: 动作描述
            
        Returns:
            服务名称
        """
        # 先尝试精确匹配
        possible_services = self.ACTION_SERVICE_MAP.get(action, [])
        
        # 过滤出与设备类型匹配的服务
        for service in possible_services:
            if service.startswith(device_type + "."):
                return service
        
        # 如果没有精确匹配，返回None
        return None
    
    def get_random_action(self, device_type: str, language: str = "zh") -> tuple:
        """
        为指定设备类型随机生成一个动作
        
        Args:
            device_type: 设备类型
            language: 语言 ('zh' 或 'en')
            
        Returns:
            (服务名, 动作描述)
        """
        # 获取该设备类型的所有可能服务
        action_map = self.SERVICE_ACTION_MAP if language == "zh" else self.SERVICE_ACTION_MAP_EN
        possible_services = [s for s in action_map.keys() 
                           if s.startswith(device_type + ".")]
        
        if not possible_services:
            return None, None
        
        service = random.choice(possible_services)
        action = random.choice(action_map[service])
        
        return service, action
    
    def build_service_call(self, service: str, device_id: str, 
                          params: Optional[Dict[str, Any]] = None) -> Dict:
        """
        构建服务调用字典
        
        Args:
            service: 服务名称
            device_id: 设备ID
            params: 额外参数
            
        Returns:
            服务调用字典
        """
        call = {
            "service": service,
            "target_device": device_id
        }
        
        if params:
            call.update(params)
        
        return call
    
    def get_random_color(self) -> tuple:
        """
        获取随机颜色
        
        Returns:
            (颜色名称, RGB值列表)
        """
        color_name = random.choice(list(COLORS.keys()))
        return color_name, COLORS[color_name]
    
    def get_color_by_name(self, color_name: str) -> Optional[List[int]]:
        """
        根据颜色名称获取RGB值
        
        Args:
            color_name: 颜色名称
            
        Returns:
            RGB值列表
        """
        return COLORS.get(color_name)
    
    def get_random_brightness(self) -> float:
        """
        获取随机亮度值
        
        Returns:
            亮度值 (0-1 的百分比)
        """
        return round(random.randint(BRIGHTNESS_RANGE[0], BRIGHTNESS_RANGE[1]) / 100.0, 2)
    
    def format_rgb_color(self, rgb: List[int]) -> str:
        """
        格式化RGB颜色为字符串
        
        Args:
            rgb: RGB值列表
            
        Returns:
            格式化的字符串 "(R, G, B)"
        """
        return f"({rgb[0]}, {rgb[1]}, {rgb[2]})"
