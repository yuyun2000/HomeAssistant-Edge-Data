"""
混合操作生成器 - 生成统一操作和个别操作混合的数据
例如：打开所有的灯并把窗帘拉上
"""
import random
from typing import List, Dict
from generators.base_generator import BaseGenerator
from config import COLORS_EN


class MixedGenerator(BaseGenerator):
    """混合操作数据生成器"""
    
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
    
    def generate_batch_operation(self, device_type: str, language: str) -> tuple:
        """
        生成统一操作部分
        
        Returns:
            (操作描述, 设备列表, 服务调用列表, 参数字典)
        """
        # 获取该类型的所有设备
        all_devices_in_db = self.device_manager.get_all_devices_by_type(device_type)
        
        if not all_devices_in_db:
            return None
        
        # 随机选择2-5个该类型的设备
        max_count = min(5, len(all_devices_in_db))
        min_count = min(2, len(all_devices_in_db))
        device_count = random.randint(min_count, max_count)
        selected_devices = random.sample(all_devices_in_db, device_count)
        
        # 选择操作
        service, action = self.service_manager.get_random_action(device_type, language)
        if not service:
            return None
        
        # 构建参数
        params = {}
        color_name = None
        brightness = None
        
        # 灯光操作可能添加颜色或亮度
        if device_type == "light" and service == "light.turn_on":
            rand_val = random.random()
            if rand_val < 0.3:  # 30%概率添加颜色
                color_name, rgb = self.service_manager.get_random_color()
                params["rgb_color"] = self.service_manager.format_rgb_color(rgb)
            elif rand_val < 0.5:  # 20%概率添加亮度
                brightness = self.service_manager.get_random_brightness()
                params["brightness"] = brightness
        
        # 生成服务调用
        service_calls = []
        for device in selected_devices:
            service_call = self.service_manager.build_service_call(
                service, device["id"], params.copy()
            )
            service_calls.append(service_call)
        
        # 生成操作描述
        if language == "zh":
            device_type_name = self.device_type_names.get(device_type, device_type)
            if color_name:
                templates = [
                    f"把所有的{device_type_name}变成{color_name}",
                    f"所有{device_type_name}都调成{color_name}",
                    f"所有{device_type_name}改成{color_name}",
                ]
            elif brightness:
                templates = [
                    f"把所有的{device_type_name}亮度调到{brightness}",
                    f"所有{device_type_name}调到{brightness}亮度",
                ]
            else:
                templates = [
                    f"{action}所有的{device_type_name}",
                    f"把所有{device_type_name}都{action}",
                    f"所有{device_type_name}{action}",
                    f"{action}全部{device_type_name}",
                ]
            operation_desc = random.choice(templates)
        else:  # en
            device_type_name_en = self.device_type_names_en.get(device_type, device_type + "s")
            if color_name:
                color_en = COLORS_EN.get(color_name, color_name)
                templates = [
                    f"turn all {device_type_name_en} to {color_en}",
                    f"change all {device_type_name_en} to {color_en}",
                    f"set all {device_type_name_en} to {color_en}",
                ]
            elif brightness:
                templates = [
                    f"set all {device_type_name_en} brightness to {brightness}",
                    f"adjust all {device_type_name_en} to {brightness}",
                ]
            else:
                templates = [
                    f"{action} all {device_type_name_en}",
                    f"{action} all the {device_type_name_en}",
                ]
            operation_desc = random.choice(templates)
        
        return (operation_desc, selected_devices, service_calls, params)
    
    def generate_individual_operation(self, device_type: str, language: str, 
                                     exclude_devices: List[str] = None) -> tuple:
        """
        生成单个设备操作部分
        
        Args:
            device_type: 设备类型
            language: 语言
            exclude_devices: 要排除的设备ID列表
            
        Returns:
            (操作描述, 设备, 服务调用)
        """
        device = self.device_manager.get_random_device(device_type)
        if not device:
            return None
        
        # 如果设备在排除列表中，重新选择
        attempts = 0
        while exclude_devices and device['id'] in exclude_devices and attempts < 10:
            device = self.device_manager.get_random_device(device_type)
            attempts += 1
        
        if attempts >= 10:
            return None
        
        service, action = self.service_manager.get_random_action(device_type, language)
        if not service:
            return None
        
        # 构建参数
        params = {}
        color_name = None
        brightness = None
        
        # 灯光操作可能添加颜色或亮度
        if device_type == "light" and service == "light.turn_on":
            rand_val = random.random()
            if rand_val < 0.3:
                color_name, rgb = self.service_manager.get_random_color()
                params["rgb_color"] = self.service_manager.format_rgb_color(rgb)
            elif rand_val < 0.5:
                brightness = self.service_manager.get_random_brightness()
                params["brightness"] = brightness
        
        # 生成操作描述
        if language == "zh":
            device_name = device.get('name_zh', device['name'])
            if color_name:
                templates = [
                    f"把{device_name}变成{color_name}",
                    f"{device_name}调成{color_name}",
                    f"帮我把{device_name}换成{color_name}",
                ]
            elif brightness:
                templates = [
                    f"把{device_name}亮度调到{brightness}",
                    f"{device_name}亮度{brightness}",
                ]
            else:
                templates = [
                    f"{action}{device_name}",
                    f"把{device_name}{action}",
                    f"{action}一下{device_name}",
                ]
            operation_desc = random.choice(templates)
        else:  # en
            if color_name:
                color_en = COLORS_EN.get(color_name, color_name)
                templates = [
                    f"change the {device['name']} to {color_en}",
                    f"set the {device['name']} to {color_en}",
                    f"turn the {device['name']} {color_en}",
                ]
            elif brightness:
                templates = [
                    f"set the {device['name']} brightness to {brightness}",
                    f"adjust the {device['name']} to {brightness}",
                ]
            else:
                templates = [
                    f"{action} the {device['name']}",
                    f"{action} {device['name']}",
                ]
            operation_desc = random.choice(templates)
        
        service_call = self.service_manager.build_service_call(
            service, device["id"], params
        )
        
        return (operation_desc, device, service_call)
    
    def generate_single(self, language: str = None) -> Dict:
        """
        生成单条混合操作数据
        
        Args:
            language: 语言 ('zh' 或 'en')，如果为None则随机选择
            
        Returns:
            生成的数据字典
        """
        if language is None:
            language = random.choice(["zh", "en"])
        
        # 随机决定混合方式
        # 1. 统一操作 + 1-2个单独操作（不同类型）
        # 2. 多个统一操作（不同类型）
        # 3. 1-2个统一操作 + 1-3个单独操作
        
        mix_type = random.choice([1, 2, 3])
        
        operations = []
        service_calls = []
        all_devices = []
        
        if mix_type == 1:
            # 统一操作 + 1-2个单独操作（不同类型）
            available_types = self.device_manager.get_all_device_types()
            
            # 选择统一操作的设备类型
            batch_type = random.choice([t for t in available_types 
                                       if len(self.device_manager.get_all_devices_by_type(t)) > 1])
            
            batch_result = self.generate_batch_operation(batch_type, language)
            if batch_result:
                desc, devices, calls, params = batch_result
                operations.append(desc)
                service_calls.extend(calls)
                all_devices.extend(devices)
            
            # 选择1-2个不同类型的单独操作
            individual_count = random.randint(1, 2)
            other_types = [t for t in available_types if t != batch_type]
            random.shuffle(other_types)
            
            for device_type in other_types[:individual_count]:
                result = self.generate_individual_operation(device_type, language)
                if result:
                    desc, device, call = result
                    operations.append(desc)
                    service_calls.append(call)
                    all_devices.append(device)
        
        elif mix_type == 2:
            # 2个不同类型的统一操作
            available_types = [t for t in self.device_manager.get_all_device_types() 
                             if len(self.device_manager.get_all_devices_by_type(t)) > 1]
            
            if len(available_types) >= 2:
                selected_types = random.sample(available_types, 2)
                
                for device_type in selected_types:
                    batch_result = self.generate_batch_operation(device_type, language)
                    if batch_result:
                        desc, devices, calls, params = batch_result
                        operations.append(desc)
                        service_calls.extend(calls)
                        all_devices.extend(devices)
            else:
                # 如果没有足够的类型，退化为类型1
                return self.generate_single(language)
        
        else:  # mix_type == 3
            # 1个统一操作 + 2-3个单独操作
            available_types = self.device_manager.get_all_device_types()
            
            # 统一操作
            batch_type = random.choice([t for t in available_types 
                                       if len(self.device_manager.get_all_devices_by_type(t)) > 1])
            
            batch_result = self.generate_batch_operation(batch_type, language)
            if batch_result:
                desc, devices, calls, params = batch_result
                operations.append(desc)
                service_calls.extend(calls)
                all_devices.extend(devices)
            
            # 2-3个单独操作（可以是相同类型也可以不同）
            individual_count = random.randint(2, 3)
            for _ in range(individual_count):
                device_type = random.choice(available_types)
                result = self.generate_individual_operation(device_type, language)
                if result:
                    desc, device, call = result
                    operations.append(desc)
                    service_calls.append(call)
                    all_devices.append(device)
        
        # 如果没有生成任何操作，重试
        if not operations:
            return self.generate_single(language)
        
        # 重要：不要打乱顺序！
        # 因为统一操作（batch）可能对应多个service_calls
        # 打乱会导致操作描述和service_calls不匹配
        # 而且真实场景中，用户说话的顺序和执行顺序应该是一致的
        
        # 生成用户输入
        if language == "zh":
            if len(operations) == 2:
                connectors = [
                    "并", "并且", "还有", "，然后", "，再", "，顺便", "和"
                ]
                user_input = f"{operations[0]}{random.choice(connectors)}{operations[1]}"
            elif len(operations) == 3:
                # 第一个连接词
                connectors1 = ["，", "并", "，然后"]
                # 第二个连接词
                connectors2 = ["，还有", "并", "，再", "和"]
                user_input = f"{operations[0]}{random.choice(connectors1)}{operations[1]}{random.choice(connectors2)}{operations[2]}"
            else:
                # 4个或更多
                parts = [operations[0]]
                for i in range(1, len(operations) - 1):
                    connectors = ["，", "，然后", "，再", "并"]
                    parts.append(random.choice(connectors) + operations[i])
                connectors_last = ["，还有", "并", "和", "，最后"]
                parts.append(random.choice(connectors_last) + operations[-1])
                user_input = "".join(parts)
        else:  # en
            if len(operations) == 2:
                connectors = [" and ", " and also ", ", and "]
                user_input = random.choice(connectors).join(operations)
            else:
                parts = [operations[0]]
                for i in range(1, len(operations) - 1):
                    parts.append(random.choice([", ", ", then ", " and "]) + operations[i])
                parts.append(random.choice([", and ", " and also "]) + operations[-1])
                user_input = "".join(parts)
        
        # 生成助手回复
        if language == "zh":
            response_templates = [
                "好的，全部完成！",
                "收到，都搞定了！",
                "没问题，处理完毕！",
            ]
        else:
            response_templates = [
                "All done!",
                "Got it, all set!",
                "Sure thing, completed!",
            ]
        response_text = random.choice(response_templates)
        
        formatted_calls = self.format_service_calls(service_calls)
        assistant_response = f"{response_text}\n```homeassistant\n{formatted_calls}\n```"
        
        # 创建系统提示
        exclusive_types = list(set([d['id'].split('.')[0] for d in all_devices]))
        system_prompt = self.create_system_prompt(
            include_all_devices=True,
            required_devices=all_devices,
            exclusive_device_types=exclusive_types
        )
        
        return self.create_message(system_prompt, user_input, assistant_response)
    
    def generate(self, count: int = 1, language: str = None) -> List[Dict]:
        """
        生成多条混合操作数据
        
        Args:
            count: 生成数据条数
            language: 语言 ('zh' 或 'en')，如果为None则每条随机
            
        Returns:
            生成的数据列表
        """
        return [self.generate_single(language) for _ in range(count)]
