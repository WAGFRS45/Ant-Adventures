import time

class Ant:
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy

    def eat(self):
        self.energy += 10
        if self.energy > 100:
            self.energy = 100

    def rest(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def explore_yard(ant):
    delay_print(f"欢迎来到种菜院子，{ant.name}！")
    delay_print("你将在这个游戏中扮演一只蚂蚁，探索院子，种植蔬菜，与其他昆虫互动。")

    while ant.health > 0:
        print("\n你可以进行以下操作：")
        print("1. 探索院子")
        print("2. 种植蔬菜")
        print("3. 进食")
        print("4. 休息")

        choice = input("请选择要进行的操作（输入操作编号）：")
        if choice == "1":
            delay_print(f"{ant.name}在院子中发现了一只蚱蜢。")
            ant.take_damage(10)
            delay_print(f"{ant.name}受到了蚱蜢的攻击，剩余生命值：{ant.health}")
        elif choice == "2":
            delay_print(f"{ant.name}正在种植蔬菜。")
            ant.energy -= 20
            delay_print(f"{ant.name}种植了蔬菜，剩余能量：{ant.energy}")
        elif choice == "3":
            ant.eat()
            delay_print(f"{ant.name}正在进食，能量恢复到：{ant.energy}")
        elif choice == "4":
            ant.rest()
            delay_print(f"{ant.name}正在休息，能量恢复到：{ant.energy}")
        else:
            delay_print("无效的选择。")

        continue_choice = input("是否继续冒险？(是/否): ").strip().lower()
        if continue_choice != "是":
            delay_print(f"谢谢参与蚂蚁在种菜院子冒险游戏！再见。")
            exit()

def main():
    ant_name = input("请输入蚂蚁的名字：")
    ant = Ant(ant_name, health=100, energy=50)

    explore_yard(ant)

if __name__ == "__main__":
    main()
