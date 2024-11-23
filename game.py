# DEPRECATED, DO NOT USE, FOR ARCHIVAL PURPOSES ONLY

import random
class Entity:
    def __init__(self, name, hp,  defense):
        self.name = name
        self.hp = hp
        self.defense = defense
    
    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, amount):
        self.hp += amount

    def talk(self, words):
        print(f"{self.name}: {words}")
    

class Enemy(Entity):
    def __init__(self, name, hp, defense, attack):
        super().__init__(name, hp, defense)
        self.attack = attack
    
    def action_attack(self, target, weapon):
        if self.hp > 0:
            weapon.attack_weapon(target, self)
    
    def say_info(self):
        print(f"{self.name} has {self.hp} hp, {self.defense} defense and {self.attack} attack")


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def attack_weapon(self, target, user):
        target.take_damage(self.damage+user.attack)
        if target.hp <= 0:
            print(f"{target.name} died")
        else:
            print(f"{self.name} hit {target.name} for {self.damage+user.attack} damage.")
            print(f"{target.name} has {target.hp} hp left.")

# NPC class
class NPC(Entity):
    def greet(self):
        print(f"Hello, my name is {self.name}")

# Player class
class Player(Enemy):
    def __init__(self, name, hp, defense, attack):
        # Create an empty inventory list
        inventory = []

        # Assign the inventory list to self.inventory attribute
        self.inventory = inventory

        # Call the parent class __init__ method to initialize name, hp, defense, and attack attributes
        super().__init__(name, hp, defense, attack)
    
    def obtain_item(self, item):
        # Add item to the inventory
        self.inventory.append(item.name)
        print(f"You obtained {item.name}")
    
    def drop_item(self, item):
        # Remove item from the inventory
        self.inventory.remove(item.name)
        print(f"You dropped {item.name}")
    
    def list_inventory(self):
        # Print the inventory
        print("Inventory:")
        iterations = 0
        # Loop through the inventory
        for item in self.inventory:
            print(item)
            iterations += 1
        # Check if the inventory is empty
        if iterations == 0: print("Inventory is empty")        

    def ask_weapon(self, target):
        while True:
            self.list_inventory()
            print("Type 'exit' to exit")
            choice = input("Enter the weapon you want to use: ")
            if choice.lower() == "exit": # Handles exit logic
                exit()
            elif choice in self.inventory:
                weapon = player_weapons[choice]
                weapon.attack_weapon(target, self)
            else:
                print("You don't have that item")





player_weapons = {
    
} # Put all weapons here in the format "weapon name": weapon object (ex. "sword": sword) (required for functionality)
