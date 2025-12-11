"""
基础生成器 - 所有数据生成器的基类
"""
from abc import ABC, abstractmethod
from typing import Dict, List
from utils.device_manager import DeviceManager
from utils.service_manager import ServiceManager


class BaseGenerator(ABC):
    """数据生成器基类"""
    
    def __init__(self):
        self.device_manager = DeviceManager()
        self.service_manager = ServiceManager()
    
    def create_system_prompt(self, include_all_devices: bool = True, required_devices: List[Dict] = None, 
                           exclusive_device_types: List[str] = None) -> str:
        """
        创建系统提示（模拟真实家庭环境，包含各类设备）
        
        Args:
            include_all_devices: 是否包含所有类型的设备（默认True，模拟真实家庭）
            required_devices: 必须包含的设备列表（这些设备一定会出现在系统提示中）
            exclusive_device_types: 排他性设备类型列表（这些类型只会包含required_devices中的设备，不会再随机添加）
            
        Returns:
            系统提示字符串
        """
        if include_all_devices:
            import random
            
            # 首先确保必需的设备被包含
            all_devices = []
            required_device_ids = set()
            exclusive_types = set(exclusive_device_types) if exclusive_device_types else set()
            
            if required_devices:
                all_devices.extend(required_devices)
                required_device_ids = {d['id'] for d in required_devices}
            
            # 从每种设备类型中随机选择一些设备，模拟真实家庭
            for device_type in self.device_manager.get_all_device_types():
                # 如果这个类型是排他性的，跳过（已经在required_devices中包含了所有需要的设备）
                if device_type in exclusive_types:
                    continue
                    
                devices_of_type = self.device_manager.get_all_devices_by_type(device_type)
                if devices_of_type:
                    # 过滤掉已经在必需设备列表中的设备
                    available_devices = [d for d in devices_of_type if d['id'] not in required_device_ids]
                    
                    if available_devices:
                        # 随机选择该类型的部分设备（至少1个，最多全部）
                        count = random.randint(min(1, len(available_devices)), len(available_devices))
                        selected = random.sample(available_devices, count)
                        all_devices.extend(selected)
            
            # 打乱设备顺序，更自然
            random.shuffle(all_devices)
            
            device_lines = []
            for device in all_devices:
                device_lines.append(f"{device['id']} '{device['name']}'")
            devices = "\n".join(device_lines)
            
            # 包含所有类型的服务
            services = self.device_manager.format_services_for_system_prompt()
        else:
            # 仅包含所有设备和服务（旧行为）
            devices = self.device_manager.format_devices_for_system_prompt()
            services = self.device_manager.format_services_for_system_prompt()
        
        return (
            "You are 'M5', a helpful AI Assistant that controls the devices in a house. "
            "Complete the following task as instructed or answer the following question "
            "with the information provided only.\n"
            f"Services: {services}\n"
            f"Devices:\n{devices}"
        )
    
    def create_message(self, system: str, user: str, assistant: str) -> Dict:
        """
        创建ShareGPT格式的消息
        
        Args:
            system: 系统提示
            user: 用户消息
            assistant: 助手回复
            
        Returns:
            消息字典
        """
        return {
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant}
            ]
        }
    
    def format_service_calls(self, service_calls: List[Dict]) -> str:
        """
        格式化服务调用为代码块
        
        Args:
            service_calls: 服务调用列表
            
        Returns:
            格式化的代码块字符串
        """
        lines = []
        for call in service_calls:
            # 构建基础调用
            line = f'{{"service": "{call["service"]}", "target_device": "{call["target_device"]}"'
            
            # 添加额外参数
            for key, value in call.items():
                if key not in ["service", "target_device"]:
                    if isinstance(value, str):
                        line += f', "{key}": "{value}"'
                    else:
                        line += f', "{key}": {value}'
            
            line += "}"
            lines.append(line)
        
        return "\n".join(lines)
    
    @abstractmethod
    def generate(self, count: int = 1) -> List[Dict]:
        """
        生成数据
        
        Args:
            count: 生成数量
            
        Returns:
            生成的数据列表
        """
        pass
