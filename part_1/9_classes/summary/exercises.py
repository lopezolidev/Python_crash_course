"""
======================================================================
OOP PRACTICE CHALLENGE (BASED ON CHAPTER 9 OF PYTHON CRASH COURSE)
======================================================================
"""

# ====================================================================
# EXERCISE 1: Class Composition and Attribute Management
# Concepts: __init__, update methods, composition (instance as an attribute)
# Ref: Pages 162-166, 170-173[cite: 1]
# ====================================================================
"""
CHALLENGE 1: Spaceship System

1. Create a class named 'Engine':
   - Attribute: 'fuel_level' with a default value of 100.
   - Method 'burn_fuel(amount)': subtracts 'amount' from fuel_level. If fuel goes below 0, 
     set it to 0 and print "Fuel depleted!".
   - Method 'refuel(amount)': adds 'amount' to fuel_level, capped at a maximum of 100.

2. Create a class named 'Spaceship':
   - Required attributes in __init__: 'name' and 'model'.
   - Default attribute: 'speed' (initial speed = 0).
   - Composition: In __init__, assign a new instance of 'Engine' to 'self.engine'.
   - Method 'accelerate(increase)': 
     * Only increases 'self.speed' if the engine's fuel_level is greater than 0.
     * When accelerating, consume 10 units of fuel by calling the engine's method.
   - Method 'get_status()': prints the spaceship's name, current speed, and remaining fuel.

3. TEST: Instantiate a spaceship, accelerate several times until fuel runs out, 
   try to accelerate again with no fuel, refuel, and display the status.
"""

# --- CODE FOR EXERCISE 1 HERE ---
# 1. Engine
class Engine:
    '''
    Modeling an Engine class for a model of a spaceship
    Attributes:
        - fuel_level
    Methods:
        - burn_fuel(amount): decreases fuel amount, capped at 0%
        - refuel(amount): increases fuel amount, capped at 100%
    '''
    def __init__(self):
        self.fuel_level = 100

    def burn_fuel(self, amount):
        """
        Method to diminish amount of fuel for the spaceship's engine
        Cannot decrease below 0.
        """
        if self.fuel_level == 0 or self.fuel_level - amount <= 0:
            print(f"There's only {self.fuel_level}% of fuel")
            return
        self.fuel_level = self.fuel_level - amount
        print("Burning some fuel...")
        print(f"Current fuel level: {self.fuel_level}")
        return

    def refuel(self, amount):
        """
        Method to increment fuel level for the engine.
        Capped value at 100.
        """
        self.fuel_level = self.fuel_level + amount
        print("Refueling tank...")
        if self.fuel_level >= 100:  
            print(f"The tank is overloading with {self.fuel_level + amount}% of fuel!")
            print("Storing excess fuel...")
            self.fuel_level = 100
        print(f"Current fuel level: {self.fuel_level}%")
        return

    def get_fuel_level(self):
        print(f"Engine's fuel level is {self.fuel_level}%")

# 2. Spaceship

    class Spaceship:
        """
        Modeling a spaceship, composing it with an Engine instance.
        Attributes:
            - name
            - model
            - speed
            - engine
        Methods:   
            - accelerate(increase): burns fuel and increases speed
            - get_status(): prints spaceship's name, current speed and remaining fuel
        """
        def __init__(self, name, model):
            self.name = name
            self.model = model
            self.speed = 0
            self.engine = Engine()

        


# ====================================================================
# EXERCISE 2: Inheritance and Method Overriding
# Concepts: Inheritance (Parent/Child), super().__init__(), overriding
# Ref: Pages 167-170[cite: 1]
# ====================================================================
"""
CHALLENGE 2: Bank Account Management

1. Create the base class 'BankAccount':
   - Attributes in __init__: 'owner' and 'balance' (initial balance, float).
   - Method 'deposit(amount)': adds the amount to the balance and prints the new balance.
   - Method 'withdraw(amount)': subtracts the amount from the balance as long as there are sufficient funds.
     If funds are insufficient, print "Insufficient funds".

2. Create the child class 'SavingsAccount' inheriting from 'BankAccount':
   - Must use 'super().__init__()' to initialize 'owner' and 'balance'.
   - Specific attribute: 'interest_rate' (e.g., 0.05 for 5%).
   - Specific method 'apply_interest()': calculates interest on the current balance, 
     deposits it into the account, and prints the earned interest amount.

3. Create another child class 'CryptoAccount' inheriting from 'BankAccount':
   - Override the 'withdraw(amount)' method:
     Crypto withdrawals have a fixed fee (e.g., $5.00). 
     The method must deduct 'amount + fee'. If the balance cannot cover 
     the withdrawal PLUS the fee, reject the transaction.

4. TEST: Create a 'SavingsAccount' and apply interest. Create a 'CryptoAccount', 
   attempt a withdrawal that exceeds the balance considering the fee, and then make a valid withdrawal.
"""

# --- CODE FOR EXERCISE 2 HERE ---




# ====================================================================
# EXERCISE 3: Simulation with Standard Library (`random`)
# Concepts: Using `random.randint` or `random.choice` inside Class Methods
# Ref: Pages 180-181[cite: 1]
# ====================================================================
"""
CHALLENGE 3: RPG Combat Simulator

1. Import 'randint' or 'choice' from the 'random' module.

2. Create a 'Character' class:
   - Attributes in __init__: 'name', 'health' (e.g., 100), 'max_attack' (maximum attack damage).
   - Method 'attack(target)': 
     * Generates random damage between 5 and 'self.max_attack'.
     * Subtracts that damage from the target's 'health'.
     * Prints a message stating how much damage was dealt to whom.
   - Method 'is_alive()': returns True if 'health' > 0, otherwise False.

3. Combat logic outside the classes:
   - Create two characters (e.g., "Warrior" with 100 HP / 20 attack, and "Mage" with 80 HP / 25 attack).
   - Use a 'while' loop to simulate turn-based combat where they attack each other 
     until one character's health reaches 0.
   - Announce the winner of the battle.
"""

# --- CODE FOR EXERCISE 3 HERE ---