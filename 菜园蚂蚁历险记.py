import random

# 定义玩家属性
player = {
    "name": "小蚂蚁",
    "health": 100,
    "food": 100,
    "seeds": 0
}

# 定义游戏中可能遇到的事件和场景
events = [
    "你在地下发现了一颗美味的蚂蚁食物，恢复了健康。",
    "你收集了一些种子，可以用来种植食物。",
    "你遇到了一只敌对蚂蚁部落，发生了一场激烈的战斗。",
    "你发现了一个人类野餐，有很多食物可以偷。",
    "你成功种植了一片蔬菜园，获得了食物。",
    "你被一只蜘蛛咬伤，失去了一些健康。"
]

def game_over():
    print("\n游戏结束，小蚂蚁的历险之旅结束了。")
    print(f"最终状态：")
    print(f"健康：{player['health']}")
    print(f"食物：{player['food']}")
    print(f"种子：{player['seeds']}")

def main():
    print("欢迎来到菜园蚂蚁历险记游戏！")
    print("你是一只小蚂蚁，生活在一个巨大的菜园中。")
    print("你必须管理你的健康、食物和种子来生存。")

    while player["health"] > 0:
        print("\n选择一个行动：")
        print("1. 探索地下")
        print("2. 收集种子")
        print("3. 建造蚂蚁部落")
        print("4. 查看状态")
        print("5. 退出游戏")

        choice = input("请输入选项的数字：")

        if choice == "1":
            event = random.choice(events)
            print(event)
            if "健康" in event:
                player["health"] += random.randint(10, 20)
            elif "食物" in event:
                player["food"] += random.randint(10, 20)
        elif choice == "2":
            player["seeds"] += random.randint(1, 5)
            print(f"你收集了一些种子，当前总数：{player['seeds']}")
        elif choice == "3":
            if player["seeds"] >= 10:
                player["seeds"] -= 10
                print("你建造了一个蚂蚁部落，获得了食物！")
                player["food"] += random.randint(30, 50)
            else:
                print("种子不足，无法建造蚂蚁部落。")
        elif choice == "4":
            print(f"\n状态：")
            print(f"健康：{player['health']}")
            print(f"食物：{player['food']}")
            print(f"种子：{player['seeds']}")
        elif choice == "5":
            game_over()
            break
        else:
            print("无效的选项，请重新选择。")

        # 更新玩家状态
        player["health"] -= random.randint(5, 15)
        player["food"] -= random.randint(5, 15)

        # 检查玩家是否死亡
        if player["food"] <= 0:
            print("你死亡了，小蚂蚁的历险之旅结束了。")
            game_over()
            break

if __name__ == "__main__":
    main()
