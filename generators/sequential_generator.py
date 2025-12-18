"""
连续操作生成器 - 生成多个连续操作的数据
"""
import random
from typing import List, Dict
from generators.base_generator import BaseGenerator


class SequentialGenerator(BaseGenerator):
    """连续操作数据生成器"""
    
    def __init__(self):
        super().__init__()
        self.device_type_names = {
            "light": "灯",
            "cover": "窗帘",
            "lock": "锁",
            "fan": "风扇",
            "vacuum": "扫地机器人",
            "media_player": "媒体播放器",
            "timer": "定时器",
            "switch": "开关"
        }
        self.device_type_names_en = {
            "light": "light",
            "cover": "cover",
            "lock": "lock",
            "fan": "fan",
            "vacuum": "vacuum",
            "media_player": "media player",
            "timer": "timer",
            "switch": "switch"
        }
    
    def generate_single(self, operation_count: int = None, language: str = None) -> Dict:
        """
        生成单条连续操作数据
        
        Args:
            operation_count: 操作数量，如果为None则随机2-5个
            language: 语言 ('zh' 或 'en')，如果为None则随机选择
            
        Returns:
            生成的数据字典
        """
        if operation_count is None:
            operation_count = random.randint(2, 5)
        
        if language is None:
            language = random.choice(["zh", "en"])
        
        # 随机选择不同的设备类型
        available_types = self.device_manager.get_all_device_types()
        selected_types = random.sample(available_types, 
                                     min(operation_count, len(available_types)))
        
        # 如果操作数多于设备类型，重复使用某些类型
        while len(selected_types) < operation_count:
            selected_types.append(random.choice(available_types))
        
        random.shuffle(selected_types)
        
        # 生成操作
        operations = []
        service_calls = []
        selected_devices = []  # 保存选中的设备，用于系统提示
        
        for device_type in selected_types:
            device = self.device_manager.get_random_device(device_type)
            if not device:
                continue
            
            selected_devices.append(device)  # 记录选中的设备
            
            service, action = self.service_manager.get_random_action(device_type, language)
            if not service:
                continue
            
            # 构建服务调用参数
            params = {}
            color_name = None
            brightness = None
            
            # 如果是灯光打开操作，可能添加颜色或亮度（但要在用户输入中体现）
            if device_type == "light" and service == "light.turn_on":
                rand_val = random.random()
                if rand_val < 0.4:  # 30%概率添加颜色
                    color_name, rgb = self.service_manager.get_random_color()
                    params["rgb_color"] = self.service_manager.format_rgb_color(rgb)
                elif rand_val < 0.7:  # 20%概率添加亮度
                    brightness = self.service_manager.get_random_brightness()
                    params["brightness"] = brightness
            
            # 构建操作描述 - 更口语化，并包含颜色/亮度信息
            if language == "zh":
                device_name = device.get('name_zh', device['name'])  # 使用中文名称
                device_type_name = self.device_type_names.get(device_type, device_type)
                
                # 如果有颜色或亮度参数，需要在操作描述中体现
                if color_name:
                    templates = [
                        f"把{device_name}变成{color_name}",
                        f"{device_name}调成{color_name}",
                        f"帮我把{device_name}换成{color_name}",
                        f"给{device_name}改成{color_name}",
                    ]
                elif brightness:
                    templates = [
                        f"把{device_name}亮度调到{brightness}",
                        f"{device_name}亮度{brightness}",
                        f"帮我把{device_name}设为{brightness}亮度",
                        f"给{device_name}调到{brightness}",
                    ]
                else:
                    # 普通操作，不带颜色和亮度
                    templates = [
                        f"{action}{device_name}",
                        f"帮我{action}{device_name}",
                        f"把{device_name}{action}",
                        f"给我{action}{device_name}",
                        f"{action}一下{device_name}",
                    ]
                operation_desc = random.choice(templates)
            else:  # en
                if color_name:
                    # 获取英文颜色名
                    from config import COLORS_EN
                    color_en = COLORS_EN.get(color_name, color_name)
                    templates = [
                        f"change the {device['name']} to {color_en}",
                        f"set the {device['name']} to {color_en}",
                        f"make the {device['name']} {color_en}",
                        f"turn the {device['name']} {color_en}",
                    ]
                elif brightness:
                    templates = [
                        f"set the {device['name']} brightness to {brightness}",
                        f"adjust the {device['name']} to {brightness} brightness",
                        f"make the {device['name']} brightness {brightness}",
                    ]
                else:
                    templates = [
                        f"{action} the {device['name']}",
                        f"can you {action} the {device['name']}",
                        f"please {action} the {device['name']}",
                        f"{action} {device['name']}",
                    ]
                operation_desc = random.choice(templates)
            operations.append(operation_desc)
            
            service_call = self.service_manager.build_service_call(
                service, device["id"], params
            )

            service_calls.append(service_call)
        
        # 生成用户输入 - 使用更自然的连接词
        if language == "zh":
            # 使用不同的连接方式，更口语化
            if len(operations) == 2:
                user_input = random.choice([
                    f"{operations[0]}，{operations[1]}",
                    f"{operations[0]}，还有{operations[1]}",
                    f"{operations[0]}，顺便{operations[1]}",
                    f"{operations[0]}和{operations[1]}",
                ])
            elif len(operations) == 3:
                user_input = random.choice([
                    f"{operations[0]}，{operations[1]}，{operations[2]}",
                    f"{operations[0]}，然后{operations[1]}，最后{operations[2]}",
                    f"{operations[0]}，再{operations[1]}，还有{operations[2]}",
                    f"{operations[0]}，顺便{operations[1]}，还要{operations[2]}",
                ])
            else:
                # 4个或更多操作
                connectors_mid = ["，然后", "，再", "，接着", "，顺便", "，"]
                connectors_last = ["，最后", "，还有", "，另外", ""]
                parts = [operations[0]]
                for i in range(1, len(operations) - 1):
                    parts.append(random.choice(connectors_mid) + operations[i])
                parts.append(random.choice(connectors_last) + operations[-1])
                user_input = "".join(parts)
        else:  # en
            # 英文也使用更自然的连接
            if len(operations) == 2:
                user_input = random.choice([" and ", ", and also ", ", plus "]).join(operations)
            else:
                connectors = [", ", ", then ", ", and ", ", also "]
                parts = [operations[0]]
                for i in range(1, len(operations)):
                    connector = random.choice(connectors) if i < len(operations) - 1 else ", and "
                    parts.append(connector + operations[i])
                user_input = "".join(parts)
        
        # 生成助手回复 - 更多样化的回复
        if language == "zh":
            response_templates = [
                "没问题，全部搞定",
                "收到，处理完毕",
            ]
            response_text = random.choice(response_templates)
        else:  # en
            response_templates = [
                "All done",
                "All set",
                "Completed all tasks",
            ]
            response_text = random.choice(response_templates)
        
        formatted_calls = self.format_service_calls(service_calls)
        assistant_response = f"{response_text}\n```homeassistant\n{formatted_calls}\n```"
        
        # 创建系统提示（包含所有类型的设备，模拟真实家庭环境）
        # 确保操作的设备一定会出现在系统提示中
        # 获取所有选中设备的类型（去重）
        exclusive_types = list(set([d['id'].split('.')[0] for d in selected_devices]))
        system_prompt = self.create_system_prompt(
            include_all_devices=True,
            required_devices=selected_devices,
            exclusive_device_types=exclusive_types
        )
        
        return self.create_message(system_prompt, user_input, assistant_response)
    
    def generate(self, count: int = 1, operation_count: int = None, 
                language: str = None) -> List[Dict]:
        """
        生成多条连续操作数据
        
        Args:
            count: 生成数据条数
            operation_count: 每条数据的操作数量
            language: 语言 ('zh' 或 'en')，如果为None则每条随机
            
        Returns:
            生成的数据列表
        """
        return [self.generate_single(operation_count, language) for _ in range(count)]
