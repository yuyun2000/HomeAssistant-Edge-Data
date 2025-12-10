"""
灯光控制生成器 - 专门生成调整灯光颜色和亮度的数据
"""
import random
from typing import List, Dict
from generators.base_generator import BaseGenerator
from config import COLORS_EN


class LightControlGenerator(BaseGenerator):
    """灯光控制数据生成器"""
    
    def __init__(self):
        super().__init__()
    
    def generate_color_change(self, language: str = None) -> Dict:
        """
        生成灯光颜色调整数据
        
        Args:
            language: 语言 ('zh' 或 'en')，如果为None则随机选择
            
        Returns:
            生成的数据字典
        """
        if language is None:
            language = random.choice(["zh", "en"])
        
        # 获取所有灯光设备
        all_lights = self.device_manager.get_all_devices_by_type("light")
        
        # 随机选择单个灯或多个灯
        is_multiple = random.choice([True, False])
        
        if is_multiple:
            # 选择多个灯（2-4个）
            light_count = random.randint(2, min(4, len(all_lights)))
            selected_lights = random.sample(all_lights, light_count)
        else:
            # 选择单个灯
            selected_lights = [random.choice(all_lights)]
        
        # 随机选择颜色
        color_name, rgb = self.service_manager.get_random_color()
        
        # 构建服务调用
        service_calls = []
        for light in selected_lights:
            params = {"rgb_color": self.service_manager.format_rgb_color(rgb)}
            service_call = self.service_manager.build_service_call(
                "light.turn_on", light["id"], params
            )
            service_calls.append(service_call)
        
        # 生成用户输入
        if language == "zh":
            if is_multiple:
                if len(selected_lights) == len(all_lights):
                    # 所有灯
                    templates = [
                        f"把所有灯都调成{color_name}",
                        f"所有灯换成{color_name}吧",
                        f"帮我把灯都变成{color_name}",
                        f"把灯光都改成{color_name}",
                        f"所有灯光调成{color_name}",
                        f"全部的灯换成{color_name}",
                    ]
                else:
                    # 指定几个灯 - 使用中文名称
                    light_names = "、".join([light.get("name_zh", light["name"]) for light in selected_lights])
                    templates = [
                        f"把{light_names}调成{color_name}",
                        f"{light_names}换成{color_name}",
                        f"帮我把{light_names}改成{color_name}",
                        f"{light_names}都调成{color_name}吧",
                    ]
            else:
                # 单个灯 - 使用中文名称
                light_name = selected_lights[0].get("name_zh", selected_lights[0]["name"])
                templates = [
                    f"把{light_name}调成{color_name}",
                    f"{light_name}换成{color_name}",
                    f"帮我把{light_name}变成{color_name}",
                    f"把{light_name}改成{color_name}吧",
                    f"{light_name}调成{color_name}",
                    f"想把{light_name}换成{color_name}",
                ]
            user_input = random.choice(templates)
            
            # 生成回复
            response_templates = [
                f"好的，已经调成{color_name}了！",
                f"没问题，{color_name}已设置好！",
                f"收到，灯光已切换为{color_name}！",
                f"搞定，现在是{color_name}了！",
                f"已经帮你换成{color_name}了！",
            ]
            response_text = random.choice(response_templates)
        else:  # en
            color_en = COLORS_EN.get(color_name, color_name)
            if is_multiple:
                if len(selected_lights) == len(all_lights):
                    templates = [
                        f"change all lights to {color_en}",
                        f"set all lights to {color_en}",
                        f"turn all lights {color_en}",
                        f"make all lights {color_en}",
                        f"switch all lights to {color_en}",
                    ]
                else:
                    light_names = " and ".join([light["name"] for light in selected_lights])
                    templates = [
                        f"change {light_names} to {color_en}",
                        f"set {light_names} to {color_en}",
                        f"turn {light_names} {color_en}",
                        f"make {light_names} {color_en}",
                    ]
            else:
                light_name = selected_lights[0]["name"]
                templates = [
                    f"change the {light_name} to {color_en}",
                    f"set the {light_name} to {color_en}",
                    f"turn the {light_name} {color_en}",
                    f"make the {light_name} {color_en}",
                    f"switch the {light_name} to {color_en}",
                ]
            user_input = random.choice(templates)
            
            response_templates = [
                f"Done! Changed to {color_en}.",
                f"All set to {color_en}!",
                f"Lights are now {color_en}!",
                f"Got it, switched to {color_en}!",
                f"Changed to {color_en} successfully!",
            ]
            response_text = random.choice(response_templates)
        
        formatted_calls = self.format_service_calls(service_calls)
        assistant_response = f"{response_text}\n```homeassistant\n{formatted_calls}\n```"
        
        system_prompt = self.create_system_prompt(include_all_devices=True)
        return self.create_message(system_prompt, user_input, assistant_response)
    
    def generate_brightness_change(self, language: str = None) -> Dict:
        """
        生成灯光亮度调整数据
        
        Args:
            language: 语言 ('zh' 或 'en')，如果为None则随机选择
            
        Returns:
            生成的数据字典
        """
        if language is None:
            language = random.choice(["zh", "en"])
        
        # 获取所有灯光设备
        all_lights = self.device_manager.get_all_devices_by_type("light")
        
        # 随机选择单个灯或多个灯
        is_multiple = random.choice([True, False])
        
        if is_multiple:
            light_count = random.randint(2, min(4, len(all_lights)))
            selected_lights = random.sample(all_lights, light_count)
        else:
            selected_lights = [random.choice(all_lights)]
        
        # 随机选择亮度值或描述性亮度
        use_percentage = random.choice([True, False])
        
        if use_percentage:
            # 使用百分比（0-100）
            brightness_percent = random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
            brightness_value = round(brightness_percent / 100.0, 2)  # 转换为0-1的百分比
        else:
            # 使用描述性的亮度级别
            brightness_value = self.service_manager.get_random_brightness()
            brightness_percent = int(brightness_value * 100)
        
        # 构建服务调用
        service_calls = []
        for light in selected_lights:
            params = {"brightness": brightness_value}
            service_call = self.service_manager.build_service_call(
                "light.turn_on", light["id"], params
            )
            service_calls.append(service_call)
        
        # 生成用户输入
        if language == "zh":
            if is_multiple:
                if len(selected_lights) == len(all_lights):
                    if use_percentage:
                        templates = [
                            f"把所有灯的亮度调到{brightness_percent}%",
                            f"所有灯亮度设为{brightness_percent}%",
                            f"帮我把灯光亮度都调成{brightness_percent}%",
                            f"全部灯光调到{brightness_percent}%",
                        ]
                    else:
                        # 使用描述性语言
                        if brightness_value < 0.3:
                            level = "暗一点"
                        elif brightness_value < 0.6:
                            level = "稍微暗一点"
                        elif brightness_value < 0.8:
                            level = "中等亮度"
                        else:
                            level = "亮一点"
                        templates = [
                            f"把所有灯调{level}",
                            f"所有灯{level}",
                            f"灯光都{level}吧",
                            f"把灯光调{level}",
                        ]
                else:
                    # 指定几个灯 - 使用中文名称
                    light_names = "、".join([light.get("name_zh", light["name"]) for light in selected_lights])
                    if use_percentage:
                        templates = [
                            f"把{light_names}亮度调到{brightness_percent}%",
                            f"{light_names}调成{brightness_percent}%亮度",
                            f"帮我把{light_names}设为{brightness_percent}%",
                        ]
                    else:
                        if brightness_value < 0.3:
                            level = "调暗"
                        elif brightness_value < 0.6:
                            level = "稍微调暗"
                        elif brightness_value < 0.8:
                            level = "调到中等"
                        else:
                            level = "调亮"
                        templates = [
                            f"把{light_names}{level}",
                            f"{light_names}{level}一点",
                            f"帮我把{light_names}{level}",
                        ]
            else:
                # 单个灯 - 使用中文名称
                light_name = selected_lights[0].get("name_zh", selected_lights[0]["name"])
                if use_percentage:
                    templates = [
                        f"把{light_name}调到{brightness_percent}%",
                        f"{light_name}亮度调成{brightness_percent}%",
                        f"帮我把{light_name}设为{brightness_percent}%亮度",
                        f"{light_name}调到{brightness_percent}%",
                    ]
                else:
                    if brightness_value < 0.3:
                        level = "暗一点"
                    elif brightness_value < 0.6:
                        level = "稍微暗点"
                    elif brightness_value < 0.8:
                        level = "中等"
                    else:
                        level = "亮一点"
                    templates = [
                        f"把{light_name}调{level}",
                        f"{light_name}{level}",
                        f"帮我把{light_name}调{level}",
                        f"{light_name}弄{level}吧",
                    ]
            user_input = random.choice(templates)
            
            response_templates = [
                f"好的，亮度已调整！",
                f"收到，亮度已设置为{brightness_percent}%！",
            ]
            response_text = random.choice(response_templates)
        else:  # en
            if is_multiple:
                if len(selected_lights) == len(all_lights):
                    templates = [
                        f"set all lights brightness to {brightness_percent}%",
                        f"change all lights to {brightness_percent}% brightness",
                        f"dim all lights to {brightness_percent}%",
                        f"adjust all lights to {brightness_percent}%",
                    ]
                else:
                    light_names = " and ".join([light["name"] for light in selected_lights])
                    templates = [
                        f"set {light_names} to {brightness_percent}%",
                        f"adjust {light_names} to {brightness_percent}% brightness",
                        f"change {light_names} brightness to {brightness_percent}%",
                    ]
            else:
                light_name = selected_lights[0]["name"]
                templates = [
                    f"set the {light_name} to {brightness_percent}%",
                    f"adjust the {light_name} to {brightness_percent}% brightness",
                    f"dim the {light_name} to {brightness_percent}%",
                    f"change the {light_name} brightness to {brightness_percent}%",
                ]
            user_input = random.choice(templates)
            
            response_templates = [
                f"Done! Brightness set to {brightness_percent}%.",
                f"All set! Adjusted to {brightness_percent}%.",
                f"Brightness changed to {brightness_percent}%!",
                f"Got it, lights are now at {brightness_percent}%!",
            ]
            response_text = random.choice(response_templates)
        
        formatted_calls = self.format_service_calls(service_calls)
        assistant_response = f"{response_text}\n```homeassistant\n{formatted_calls}\n```"
        
        system_prompt = self.create_system_prompt(include_all_devices=True)
        return self.create_message(system_prompt, user_input, assistant_response)
    
    def generate_color_and_brightness(self, language: str = None) -> Dict:
        """
        生成同时调整灯光颜色和亮度的数据
        
        Args:
            language: 语言 ('zh' 或 'en')，如果为None则随机选择
            
        Returns:
            生成的数据字典
        """
        if language is None:
            language = random.choice(["zh", "en"])
        
        all_lights = self.device_manager.get_all_devices_by_type("light")
        
        # 随机选择灯
        is_multiple = random.choice([True, False])
        if is_multiple:
            light_count = random.randint(2, min(3, len(all_lights)))
            selected_lights = random.sample(all_lights, light_count)
        else:
            selected_lights = [random.choice(all_lights)]
        
        # 选择颜色和亮度
        color_name, rgb = self.service_manager.get_random_color()
        brightness_percent = random.choice([30, 50, 70, 80, 100])
        brightness_value = round(brightness_percent / 100.0, 2)
        
        # 构建服务调用
        service_calls = []
        for light in selected_lights:
            params = {
                "rgb_color": self.service_manager.format_rgb_color(rgb),
                "brightness": brightness_value
            }
            service_call = self.service_manager.build_service_call(
                "light.turn_on", light["id"], params
            )
            service_calls.append(service_call)
        
        # 生成用户输入
        if language == "zh":
            if is_multiple:
                # 多个灯 - 使用中文名称
                light_names = "、".join([light.get("name_zh", light["name"]) for light in selected_lights])
                templates = [
                    f"把{light_names}调成{color_name}，亮度{brightness_percent}%",
                    f"{light_names}换成{color_name}，{brightness_percent}%亮度",
                    f"帮我把{light_names}设为{color_name}，亮度调到{brightness_percent}%",
                ]
            else:
                # 单个灯 - 使用中文名称
                light_name = selected_lights[0].get("name_zh", selected_lights[0]["name"])
                templates = [
                    f"把{light_name}调成{color_name}，亮度{brightness_percent}%",
                    f"{light_name}换成{color_name}，{brightness_percent}%的亮度",
                    f"帮我把{light_name}设为{color_name}，亮度{brightness_percent}%",
                    f"{light_name}改成{color_name}，亮度调到{brightness_percent}%",
                ]
            user_input = random.choice(templates)
            
            response_templates = [
                f"好的，已设置为{color_name}，亮度{brightness_percent}%！",
                f"完成！{color_name}，{brightness_percent}%亮度！",
                f"搞定，现在是{color_name}，{brightness_percent}%的亮度！",
            ]
            response_text = random.choice(response_templates)
        else:  # en
            color_en = COLORS_EN.get(color_name, color_name)
            if is_multiple:
                light_names = " and ".join([light["name"] for light in selected_lights])
                templates = [
                    f"set {light_names} to {color_en} at {brightness_percent}%",
                    f"change {light_names} to {color_en}, {brightness_percent}% brightness",
                    f"make {light_names} {color_en} with {brightness_percent}% brightness",
                ]
            else:
                light_name = selected_lights[0]["name"]
                templates = [
                    f"set the {light_name} to {color_en} at {brightness_percent}%",
                    f"change the {light_name} to {color_en}, {brightness_percent}% brightness",
                    f"make the {light_name} {color_en} with {brightness_percent}% brightness",
                ]
            user_input = random.choice(templates)
            
            response_templates = [
                f"Done! Set to {color_en} at {brightness_percent}%.",
                f"All set! {color_en} with {brightness_percent}% brightness.",
                f"Changed to {color_en}, {brightness_percent}% brightness!",
            ]
            response_text = random.choice(response_templates)
        
        formatted_calls = self.format_service_calls(service_calls)
        assistant_response = f"{response_text}\n```homeassistant\n{formatted_calls}\n```"
        
        system_prompt = self.create_system_prompt(include_all_devices=True)
        return self.create_message(system_prompt, user_input, assistant_response)
    
    def generate_mixed_control(self, language: str = None) -> Dict:
        """
        生成对多个灯进行不同控制的数据（每个灯的控制不同）
        
        Args:
            language: 语言 ('zh' 或 'en')，如果为None则随机选择
            
        Returns:
            生成的数据字典
        """
        if language is None:
            language = random.choice(["zh", "en"])
        
        all_lights = self.device_manager.get_all_devices_by_type("light")
        
        # 选择2-3个灯
        light_count = random.randint(2, min(3, len(all_lights)))
        selected_lights = random.sample(all_lights, light_count)
        
        # 为每个灯生成不同的控制
        light_controls = []
        service_calls = []
        
        for light in selected_lights:
            # 随机决定这个灯的控制类型
            control_type = random.choice(['color_only', 'brightness_only', 'color_and_brightness'])
            
            params = {}
            control_desc = {}
            
            if control_type == 'color_only':
                # 只改变颜色
                color_name, rgb = self.service_manager.get_random_color()
                params["rgb_color"] = self.service_manager.format_rgb_color(rgb)
                control_desc['type'] = 'color'
                control_desc['color'] = color_name
                control_desc['color_en'] = COLORS_EN.get(color_name, color_name)
                
            elif control_type == 'brightness_only':
                # 只改变亮度
                brightness_percent = random.choice([20, 30, 40, 50, 60, 70, 80])
                brightness_value = round(brightness_percent / 100.0, 2)
                params["brightness"] = brightness_value
                control_desc['type'] = 'brightness'
                control_desc['brightness'] = brightness_percent
                
            else:  # color_and_brightness
                # 同时改变颜色和亮度
                color_name, rgb = self.service_manager.get_random_color()
                brightness_percent = random.choice([30, 50, 70])
                brightness_value = round(brightness_percent / 100.0, 2)
                params["rgb_color"] = self.service_manager.format_rgb_color(rgb)
                params["brightness"] = brightness_value
                control_desc['type'] = 'both'
                control_desc['color'] = color_name
                control_desc['color_en'] = COLORS_EN.get(color_name, color_name)
                control_desc['brightness'] = brightness_percent
            
            light_controls.append({
                'light': light,
                'control': control_desc
            })
            
            service_call = self.service_manager.build_service_call(
                "light.turn_on", light["id"], params
            )
            service_calls.append(service_call)
        
        # 生成用户输入
        if language == "zh":
            parts = []
            for lc in light_controls:
                light_name = lc['light'].get("name_zh", lc['light']["name"])
                ctrl = lc['control']
                
                if ctrl['type'] == 'color':
                    part = f"{light_name}调成{ctrl['color']}"
                elif ctrl['type'] == 'brightness':
                    part = f"{light_name}亮度{ctrl['brightness']}%"
                else:  # both
                    part = f"{light_name}{ctrl['color']}{ctrl['brightness']}%"
                parts.append(part)
            
            # 随机选择连接方式
            if len(parts) == 2:
                user_input = random.choice([
                    f"把{parts[0]}，{parts[1]}",
                    f"{parts[0]}，{parts[1]}",
                    f"帮我把{parts[0]}，{parts[1]}",
                ])
            else:  # 3个灯
                user_input = random.choice([
                    f"把{parts[0]}，{parts[1]}，{parts[2]}",
                    f"{parts[0]}，{parts[1]}，{parts[2]}",
                ])
            
            response_templates = [
                "好的，设置完成！",
                "收到，调整完毕！",
            ]
            response_text = random.choice(response_templates)
            
        else:  # en
            parts = []
            for lc in light_controls:
                light_name = lc['light']["name"]
                ctrl = lc['control']
                
                if ctrl['type'] == 'color':
                    part = f"{light_name} to {ctrl['color_en']}"
                elif ctrl['type'] == 'brightness':
                    part = f"{light_name} to {ctrl['brightness']}%"
                else:  # both
                    part = f"{light_name} to {ctrl['color_en']}, {ctrl['brightness']}%"
                parts.append(part)
            
            if len(parts) == 2:
                user_input = random.choice([
                    f"set {parts[0]} and {parts[1]}",
                    f"change {parts[0]} and {parts[1]}",
                    f"adjust {parts[0]} and {parts[1]}",
                ])
            else:  # 3个灯
                user_input = random.choice([
                    f"set {parts[0]}, {parts[1]}, and {parts[2]}",
                    f"change {parts[0]}, {parts[1]}, and {parts[2]}",
                ])
            
            response_templates = [
                "All set!",
                "Got it! All changes applied.",
            ]
            response_text = random.choice(response_templates)
        
        formatted_calls = self.format_service_calls(service_calls)
        assistant_response = f"{response_text}\n```homeassistant\n{formatted_calls}\n```"
        
        system_prompt = self.create_system_prompt(include_all_devices=True)
        return self.create_message(system_prompt, user_input, assistant_response)
    
    def generate_single(self, change_type: str = None, language: str = None) -> Dict:
        """
        生成单条灯光控制数据
        
        Args:
            change_type: 改变类型 ('color', 'brightness', 'both', 'mixed')，如果为None则随机选择
            language: 语言 ('zh' 或 'en')，如果为None则随机选择
            
        Returns:
            生成的数据字典
        """
        if change_type is None:
            change_type = random.choice(['color', 'brightness', 'both', 'mixed'])
        
        if change_type == 'color':
            return self.generate_color_change(language)
        elif change_type == 'brightness':
            return self.generate_brightness_change(language)
        elif change_type == 'both':
            return self.generate_color_and_brightness(language)
        else:  # mixed
            return self.generate_mixed_control(language)
    
    def generate(self, count: int = 1, change_type: str = None, 
                language: str = None) -> List[Dict]:
        """
        生成多条灯光控制数据
        
        Args:
            count: 生成数据条数
            change_type: 改变类型 ('color', 'brightness', 'both', 'mixed')
            language: 语言 ('zh' 或 'en')
            
        Returns:
            生成的数据列表
        """
        return [self.generate_single(change_type, language) for _ in range(count)]
