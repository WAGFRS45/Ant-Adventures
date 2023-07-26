import time
import random

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class Ant:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return self.name

class Player(Ant):
    def __init__(self, name):
        super().__init__(name, 100, 20)
        self.level = 1
        self.exp = 0
        self.inventory = {}

    def add_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name] += quantity
        else:
            self.inventory[item.name] = quantity

    def remove_item(self, item, quantity=1):
        if item.name in self.inventory:
            if self.inventory[item.name] >= quantity:
                self.inventory[item.name] -= quantity
                return True
            else:
                return False
        else:
            return False

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def delay_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.3)

def show_inventory(player):
    print("\n你的背包：")
    for item_name, quantity in player.inventory.items():
        print(f"{item_name}: {quantity}个")

def choose_action():
    print("\n你可以做以下操作：")
    print("1. 查看角色状态")
    print("2. 查看背包")
    print("3. 探险")
    print("4. 升级")
    print("5. 退出游戏")
    while True:
        try:
            choice = int(input("请输入你的选择（1/2/3/4/5）："))
            if 1 <= choice <= 5:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def show_character_status(player):
    print(f"\n{name}等级：{player.level}")
    print(f"生命值：{player.health}")
    print(f"攻击力：{player.attack}")
    print(f"经验值：{player.exp}/{player.level * 100}")

def explore(player):
    delay_print("\n你踏上了蚂蚁历险的旅程。")
    encounter = random.choice(["danger", "resource", "nothing"])
    
    if encounter == "danger":
        monster_attack(player)
    elif encounter == "resource":
        collect_resource(player)
    else:
        delay_print("这片区域看起来平静无事。")

def monster_attack(player):
    delay_print("\n突然，一只蜘蛛出现在你面前！")
    while player.health > 0 and player_attack_choice(player):
        delay_print(f"\n你的生命值：{player.health}  蜘蛛的生命值：{player.attack}")
        player.attack_spider()
        if player.health > 0:
            delay_print("蜘蛛反击了！")
            player.spider_attack()

def player_attack_choice(player):
    while True:
        choice = input("你要攻击（A）还是逃跑（E）？").lower()
        if choice == "a":
            return True
        elif choice == "e":
            delay_print("你逃跑了。")
            break
        else:
            delay_print("无效的选择，请重新输入。")
    return False

def collect_resource(player):
    resource = random.choice(resource_list)
    quantity = random.randint(1, 5)
    player.add_item(resource, quantity)
    delay_print(f"你发现了{resource.name} x {quantity}。")

def upgrade(player):
    if player.exp >= player.level * 100:
        player.exp -= player.level * 100
        player.level += 1
        player.health = 100
        player.attack += 5
        delay_print("恭喜你升级了！")
    else:
        delay_print("经验值不足，无法升级。")

def play_game():
    player_name = input("请输入你的蚂蚁名字：")
    player = Player(player_name)
    
    resource_list = [
        Item("果实", "新鲜的水果"),
        Item("叶子", "绿油油的叶子"),
        Item("露水", "清晨的露水"),
        Item("蚂蚁食物", "蚂蚁的食物来源")
    ]

    delay_print(f"欢迎来到《蚂蚁历险记》游戏，{player_name}！")
    delay_print("你将在这片神奇的世界中历险。")

    while True:
        show_character_status(player)
        action = choose_action()

        if action == 1:
            show_character_status(player)
        elif action == 2:
            show_inventory(player)
        elif action == 3:
            explore(player)
        elif action == 4:
            upgrade(player)
        elif action == 5:
            delay_print("谢谢你玩《蚂蚁历险记》游戏，再见！")
            exit()

if __name__ == "__main__":
    play_game()
