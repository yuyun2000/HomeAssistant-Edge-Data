下面是测试的设备列表：
```
devices:
- id: light.livingroom
  name: Livingroom

- id: light.bedroom
  name: Bedroom

- id: light.bathroom
  name: Bathroom

- id: light.diningroom
  name: Diningroom

- id: light.kitchen
  name: Kitchen

- id: cover.livingroom_curtain
  name: Livingroom Curtain

- id: cover.bedroom_curtain
  name: Bedroom Curtain

- id: fan.bedroom_fan
  name: Bedroom Fan

- id: lock.front_door
  name: Front Door

- id: switch.coffee_machine
  name: Coffee Machine
```

下面是一些失败的测试用例：

# 厨房灯口误后错误输出
```
'Tururn on the bedroom light, and the chicken light.' (0.29s)

LLM Response (2.08s):
   turning on bedroom light and turning on chicken light
```homeassistant
{"service": "light.turn_on", "target_device": "light.bedroom"}
{"service": "light.turn_on", "target_device": "light.chicken"}
```


# fan识别为fine，输出错误
```
 'increase the fine speed' (0.24s)
    Sent ASR_RESULT response (ID: 2d52a07c)
[192.168.20.32:51495][2d52a07c]  Processing with LLM...
[192.168.20.32:51495][2d52a07c]  LLM Response (1.45s):
   speeding up coffee machine for you
```homeassistant
{"service": "switch.increase_speed", "target_device": "switch.coffee_machine"}
```

# 别名没有正确识别
```
'tururn off the dining light' (0.20s)

LLM Response (0.63s):
   sorry, i couldn't find that device....

'turnurn off the dining roomlight' (0.21s)
LLM Response (0.62s):
   sorry, i couldn't find that device....
```

