"""
统一操作生成器 - 生成对同类设备的批量操作数据
"""
import random
from typing import List, Dict, Optional
from generators.base_generator import BaseGenerator
from config import COLORS_EN


class BatchGenerator(BaseGenerator):
    """统一操作数据生成器"""
    
    def __init__(self):
        super().__init__()
        self.device_type_names = {
            "light": "灯",
            "cover": "窗帘",
            "lock": "锁",
            "fan": "风扇",
            "vacuum": "扫地机器人",
            "media_player": "媒体播放器",
            "timer": "定时器"
        }
        self.device_type_names_en = {
            "light": "lights",
            "cover": "covers",
            "lock": "locks",
            "fan": "fans",
            "vacuum": "vacuums",
            "media_player": "media players",
            "timer": "timers"
        }
        
        # 统一操作的描述模板
        self.operation_templates = {
            "all": "所有的{device_type}",
            "all_action": "{action}所有的{device_type}"
        }
    
    def generate_single(self, device_type: str = None, 
                       device_count: int = None, language: str = None) -> Dict:
        """
        生成单条统一操作数据
        
        Args:
            device_type: 设备类型，如果为None则随机选择
            device_count: 操作的设备数量，如果为None则使用该类型的所有设备
            language: 语言 ('zh' 或 'en')，如果为None则随机选择
            
        Returns:
            生成的数据字典
        """
        if language is None:
            language = random.choice(["zh", "en"])
        # 选择设备类型
        if device_type is None:
            available_types = [t for t in self.device_manager.get_all_device_types() 
                             if len(self.device_manager.get_all_devices_by_type(t)) > 1]
            device_type = random.choice(available_types)
        
        # 获取该类型的所有设备
        all_devices = self.device_manager.get_all_devices_by_type(device_type)
        
        if not all_devices:
            raise ValueError(f"No devices found for type: {device_type}")
        
        # 确定操作的设备数量
        if device_count is None:
            device_count = len(all_devices)
        else:
            device_count = min(device_count, len(all_devices))
        
        # 随机选择设备
        if device_count == len(all_devices):
            selected_devices = all_devices
        else:
            selected_devices = random.sample(all_devices, device_count)
        
        # 随机选择一个操作
        service, action = self.service_manager.get_random_action(device_type, language)
        if not service:
            raise ValueError(f"No service found for device type: {device_type}")
        
        # 生成服务调用
        service_calls = []
        params = {}
        color_name = None
        brightness = None
        
        # 如果是灯光操作，可能添加统一的颜色或亮度
        if device_type == "light" and service == "light.turn_on":
            rand_val = random.random()
            if rand_val < 0.4:  # 40%概率添加颜色
                color_name, rgb = self.service_manager.get_random_color()
                params["rgb_color"] = self.service_manager.format_rgb_color(rgb)
            elif rand_val < 0.6:  # 20%概率添加亮度
                brightness = self.service_manager.get_random_brightness()
                params["brightness"] = brightness
        
        for device in selected_devices:
            service_call = self.service_manager.build_service_call(
                service, device["id"], params.copy()
            )
            service_calls.append(service_call)
        
        # 生成用户输入和助手回复
        if language == "zh":
            device_type_name = self.device_type_names.get(device_type, device_type)
            
            if color_name and device_type == "light":
                templates = [
                    f"把所有的{device_type_name}变成{color_name}",
                    f"所有{device_type_name}都调成{color_name}",
                    f"帮我把{device_type_name}都换成{color_name}",
                    f"所有灯光改成{color_name}吧",
                    f"把灯都调成{color_name}",
                ]
                user_input = random.choice(templates)
                response_text = f"好的，所有{device_type_name}已变成{color_name}！"
            elif brightness and device_type == "light":
                templates = [
                    f"把所有的{device_type_name}亮度调到{brightness}",
                    f"所有{device_type_name}调到{brightness}亮度",
                    f"帮我把灯光亮度都设为{brightness}",
                    f"所有灯亮度{brightness}",
                ]
                user_input = random.choice(templates)
                response_text = f"好的，所有{device_type_name}亮度已调到{brightness}！"
            else:
                if device_count == len(all_devices):
                    templates = [
                        f"{action}所有的{device_type_name}",
                        f"帮我{action}所有{device_type_name}",
                        f"把所有{device_type_name}都{action}",
                        f"所有{device_type_name}{action}",
                        f"{action}全部{device_type_name}",
                    ]
                else:
                    templates = [
                        f"{action}所有{device_type_name}",
                        f"帮我{action}所有{device_type_name}",
                        f"把{device_type_name}都{action}",
                    ]
                user_input = random.choice(templates)
                response_templates = [
                    "全部完成！",
                    "好的，都搞定了！",
                ]
                response_text = random.choice(response_templates)
        else:  # en
            device_type_name_en = self.device_type_names_en.get(device_type, device_type + "s")
            
            if color_name and device_type == "light":
                color_en = COLORS_EN.get(color_name, color_name)
                templates = [
                    f"turn all {device_type_name_en} to {color_en}",
                    f"change all {device_type_name_en} to {color_en}",
                    f"set all {device_type_name_en} to {color_en}",
                    f"make all {device_type_name_en} {color_en}",
                ]
                user_input = random.choice(templates)
                response_text = f"Done! All the lights are now {color_en}."
            elif brightness and device_type == "light":
                templates = [
                    f"set all {device_type_name_en} brightness to {brightness}",
                    f"adjust all {device_type_name_en} to {brightness} brightness",
                    f"change all lights brightness to {brightness}",
                ]
                user_input = random.choice(templates)
                response_text = f"All set! Lights brightness is now {brightness}."
            else:
                templates = [
                    f"{action} all {device_type_name_en}",
                    f"{action} all the {device_type_name_en}",
                    f"can you {action} all {device_type_name_en}",
                    f"please {action} all the {device_type_name_en}",
                ]
                user_input = random.choice(templates)
                response_templates = [
                    "All completed!",
                    "Done! Everything is set.",
                    "Got it, all done!",
                    "Sure thing, all finished!",
                ]
                response_text = random.choice(response_templates)
        
        formatted_calls = self.format_service_calls(service_calls)
        assistant_response = f"{response_text}\n```homeassistant\n{formatted_calls}\n```"
        
        # 创建系统提示（包含所有类型的设备，模拟真实家庭环境）
        system_prompt = self.create_system_prompt(include_all_devices=True)
        
        return self.create_message(system_prompt, user_input, assistant_response)
    
    def generate(self, count: int = 1, device_type: str = None,
                language: str = None) -> List[Dict]:
        """
        生成多条统一操作数据
        
        Args:
            count: 生成数据条数
            device_type: 设备类型，如果为None则每次随机选择
            language: 语言 ('zh' 或 'en')，如果为None则每条随机
            
        Returns:
            生成的数据列表
        """
        return [self.generate_single(device_type, language=language) for _ in range(count)]
