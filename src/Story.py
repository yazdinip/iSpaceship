import Ability
import Mission
import AbilityBuff
import Spaceship

# 4 Missions

# Ability(damage, abilityBuff, coolDown, abilityName, hitChance, price)

# Spaceship(maxHealth, attackDmg, abilityList)

# 400 -> 600 -> 800 -> 1000 -> 1500 HEALTH
# 10 -> 20 -> 50 -> 100 ATTACK DAMAGE

# Abilities
# Healing

heal1 = (0, (AbilityBuff.Buff.HEAL, 50), 2, "Quick Repair Mk. 1", 0, 100)
heal2 = (0, (AbilityBuff.Buff.HEAL, 70), 3, "Quick Repair Mk. 2", 0, 200)
heal3 = (0, (AbilityBuff.Buff.HEAL, 80), 2, "Quick Repair Mk. 3", 0, 300)
heal4 = (0, (AbilityBuff.Buff.HEAL, 150), 4, "Ultra repair", 0, 1000)

# On Fire

fire1 = (50, (AbilityBuff.Buff.ONFIRE, 10), 4, "Flamethrower Mk. 1", 0, 100)
fire2 = (70, (AbilityBuff.Buff.ONFIRE, 20), 4, "Flamethrower Mk. 2", 0, 200)
fire3 = (100, (AbilityBuff.Buff.ONFIRE, 30), 3, "Flamethrower Mk. 3", 0, 300)

fire4 = (10, (AbilityBuff.Buff.ONFIRE, 50), 5, "Fire Charge Mk. 1", 0, 200)
fire5 = (10, (AbilityBuff.Buff.ONFIRE, 80), 5, "Fire Charge Mk. 2", 0, 400)
fire6 = (10, (AbilityBuff.Buff.ONFIRE, 100), 4, "Fire Charge Mk. 3", 0, 500)

# Stun 

stun1 = (10, (AbilityBuff.Buff.STUN, 0), 5, "Sun Flash Mk. 1", 0, 300)
stun2 = (20, (AbilityBuff.Buff.STUN, 0), 5, "Sun Flash Mk. 2", 0, 400)
stun3 = (30, (AbilityBuff.Buff.STUN, 0), 3, "Sun Flash Mk. 3", 0, 500)

# Damage

damage1 = (40, (AbilityBuff.Buff.NOBUFF, 0), 2, "Rocket Launcher Mk. 1", 0, 100)
damage2 = (50, (AbilityBuff.Buff.NOBUFF, 0), 2, "Rocket Launcher Mk. 2", 0, 200)
damage3 = (60, (AbilityBuff.Buff.NOBUFF, 0), 2, "Rocket Launcher Mk. 3", 0, 300)

damage4 = (200, (AbilityBuff.Buff.NOBUFF, 0), 7, "Cannon Barrage Mk. 1", 0, 200)
damage5 = (300, (AbilityBuff.Buff.NOBUFF, 0), 7, "Cannon Barrage Mk. 2", 0, 300)
damage6 = (400, (AbilityBuff.Buff.NOBUFF, 0), 6, "Cannon Barrage Mk. 3", 0, 500)

damage7 = (600, (AbilityBuff.Buff.NOBUFF, 0), 10, "Hyper Cannon", 0, 500)

# Enemy One: Basic Enemy

e1a1 = (40, (AbilityBuff.Buff.NOBUFF, 0), 2, "Rocket Launcher Mk. 1", 0, 1)
e1a2 = (50, (AbilityBuff.Buff.ONFIRE, 10), 4, "Flamethrower Mk. 1", 0, 100)
e1a3 = (10, (AbilityBuff.Buff.ONFIRE, 50), 5, "Fire Charge Mk. 1", 0, 200)
e1a4 = (10, (AbilityBuff.Buff.STUN, 0), 5, "Sun Flash Mk. 1", 0, 300)

abilityList1 = [e1a1, e1a2, e1a3, e1a4]

# Enemy Two: Healing Enemy

e2a1 = (50, (AbilityBuff.Buff.NOBUFF, 0), 2, "Rocket Launcher Mk. 2", 0, 200)
e2a2 = (70, (AbilityBuff.Buff.ONFIRE, 20), 4, "Flamethrower Mk. 2", 0, 200)
e2a3 = (0, (AbilityBuff.Buff.HEAL, 80), 2, "Quick Repair Mk. 3", 0, 300)
e2a4 = (10, (AbilityBuff.Buff.STUN, 0), 5, "Sun Flash Mk. 1", 0, 300)

abilityList2 = [e2a1, e2a2, e2a3, e2a4]

# Enemy Three: Tanky Giant

e3a1 = (60, (AbilityBuff.Buff.NOBUFF, 0), 2, "Rocket Launcher Mk. 3", 0, 300)
e3a2 = (70, (AbilityBuff.Buff.ONFIRE, 20), 4, "Flamethrower Mk. 2", 0, 200)
e3a3 = (0, (AbilityBuff.Buff.HEAL, 80), 2, "Quick Repair Mk. 3", 0, 300)
e3a4 = (30, (AbilityBuff.Buff.STUN, 0), 3, "Sun Flash Mk. 3", 0, 500)

abilityList3 = [e3a1, e3a2, e3a3, e3a4]

# Enemy Four: Glass Cannon

e4a1 = (600, (AbilityBuff.Buff.NOBUFF, 0), 10, "Hyper Cannon", 0, 500)
e4a2 = (30, (AbilityBuff.Buff.STUN, 0), 3, "Sun Flash Mk. 3", 0, 500)
e4a3 = (200, (AbilityBuff.Buff.NOBUFF, 0), 7, "Cannon Barrage Mk. 1", 0, 200)
e4a4 = (10, (AbilityBuff.Buff.ONFIRE, 100), 4, "Fire Charge Mk. 3", 0, 500)

abilityList4 = [e4a1, e4a2, e4a3, e4a4]

enemy1 = Spaceship.Spaceship(400, 10, abilityList1)
enemy2 = Spaceship.Spaceship(600, 20, abilityList2)
enemy3 = Spaceship.Spaceship(800, 30, abilityList3)
enemy4 = Spaceship.Spaceship(800, 40, abilityList4)

playerAbilityList = [damage1, heal1, stun1, fire1]

player = Spaceship.Spaceship(400, 10, playerAbilityList)

abilityA = [damage2, damage3, damage4, damage5, damage6, damage7, stun2, stun3, heal2, heal3, heal4, fire2, fire3, fire4, fire5, fire6]
abilityB = []

mission1 = Mission.Mission(enemy1)
mission2 = Mission.Mission(enemy2)
mission3 = Mission.Mission(enemy3)
mission4 = Mission.Mission(enemy4)