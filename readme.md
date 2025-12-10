该项目用来生成较高难度的智能家居控制的数据，生成的数据格式为‘sharegpt’，示例内容如下：

{
    "messages": [
      {
        "role": "system",
        "content": "You are 'M5', a helpful AI Assistant that controls the devices in a house. Complete the following task as instructed or answer the following question with the information provided only.\nServices: cover.close_cover(), cover.open_cover(), cover.stop_cover(), cover.toggle(), fan.decrease_speed(), fan.increase_speed(), fan.toggle(), fan.turn_off(), fan.turn_on(), cover.close_cover(), cover.open_cover(), cover.stop_cover(), cover.toggle(), light.toggle(), light.turn_off(), light.turn_on(rgb_color,brightness), lock.lock(), lock.unlock(), media_player.media_next_track(), media_player.media_pause(), media_player.media_play(), media_player.media_play_pause(), media_player.media_previous_track(), media_player.media_stop(), media_player.toggle(), media_player.turn_off(), media_player.turn_on(), media_player.volume_down(), media_player.volume_mute(), media_player.volume_up(), timer.cancel(), timer.pause(), timer.start(duration), vacuum.pause(), vacuum.return_to_base(), vacuum.start(), vacuum.stop()\nDevices:\nlight.downstairs_study_mqtt 'Downstairs Study Light'\nlight.back_closet_warm 'Back Closet Warm Light'\ntimer.timer0 'General purpose timer' \nvacuum.front_hall_samsung 'Front hall sweeping bot'\nmedia_player.ipad_kitchen 'Kitchen iPad'\nlight.deck_left 'Left deck light'\ncover.dining_room 'Dining Room Blinds' = \nlock.shed_2 'Second shed lock'\ncover.ikea_smart 'Ikea Smart Blinds'\nlight.downstairs_guest_bedroom_zigbee 'Downstairs Guest Bedroom Light'\nlock.safety_deposit 'Safety deposit box'\nfan.patio 'Patio Fan'\nlock.back_door 'Backyard entry lock'\nlight.upstairs_corridor_zigbee 'Upstairs Corridor Light'\nfan.kids_room 'Kids' room fan'\nlock.bike_storage 'Bike Storage Lock'\ncover.skylight 'Skylight Blinds'\nfan.dining_area 'Dining Area Fan'\nlight.front_corridor_homekit 'Front Corridor Light'\ntimer.entryway_chandelier 'Entryway chandelier timer'\ncover.left_door 'Left Garage Door'\nlight.front_yard_osram 'Front Yard Osram'\nlight.bathroom_1 'Bathroom 1'"
      },
      {
        "role": "user",
        "content": "can you turn on the bathroom light"
      },
      {
        "role": "assistant",
        "content": "sure, i'll turn on the light now.\n```homeassistant\n{\"service\": \"light.turn_on\", \"target_device\": \"light.bathroom_1\"}\n```"
      }
    ]
}
系统指令中列举了配置的设备和对应的便名以及对应的可用服务，然后用户一条随机的指令，系统以人性化回复和固定格式进行回复，上面的示例只是最简单的形式，本项目主要实现以下几种数据：

1、连续操作：
输入：
开灯1，关灯2，开窗帘1等连续N个指令
输出：
All completed\n```homeassistant\n{\"service\": \"light.turn_on\", \"target_device\": \"light.xxxx1\"\n\"service\": \"light.turn_off\", \"target_device\": \"light.xxxx2\"...}\n```
两个指令的时候人性化回复可以是“已经xx和xx”，当指令大于两个的时候，统一回复“All completed！”，后面的结构化数据按照所给的格式一行生成一个调用

2、统一操作：
输入:
打开/关闭/xx操作 所有的 灯
比如：把所有的灯变成红色
输出：
All the lights have turned red\n```homeassistant\n{\"service\": \"light.turn_on\", \"target_device\": \"light.xxxx1\", \"rgb_color\": \"(255, 0, 0)\"\n\"service\": \"light.turn_off\", \"target_device\": \"light.xxxx2\", \"rgb_color\": \"(255, 0, 0)\"...}\n```
注意：操作的灯必须是系统指令中配置的设备，不能输出没有配置的设备




