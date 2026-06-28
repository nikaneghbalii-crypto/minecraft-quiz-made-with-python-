repeat = True
while repeat == True:
    print("""
    welcome.
    this game is a quiz game that you have to answer based on the questions...
      

1. **How can you get coal without mining coal ore? (Without cheats)**



   * A) Wood 

   * B) Dirt

   * C) Stone

   * D) Pickaxe



2. **What is the preferred height to mine diamonds?**



   * A) 65

   * B) -60 

   * C) 60

   * D) -65



3. **How do you get Netherite armor?**



   * A) Upgrade diamond armor with a Smithing Table 

   * B) Craft it directly with Netherite Ingots

   * C) Use Netherite Scrap only

   * D) None of the above



4. **What material is required to build a Nether Portal frame?**



   * A) Stone

   * B) Obsidian 

   * C) Basalt

   * D) Blackstone



5. **Which mob drops Ender Pearls when defeated?**



   * A) Creeper

   * B) Enderman 

   * C) Witch

   * D) Blaze



6. **What item do you need to tame a wolf?**



   * A) Fish

   * B) Apple
      
   * C) Bone 

   * D) Wheat



7. **What is the name of the dimension where you fight the Ender Dragon?**



   * A) The Nether

   * B) The End 

   * C) The Overworld

   * D) The Void



8. **Which ore is required to craft a diamond pickaxe?**



   * A) Iron Ore

   * B) Gold Ore

   * C) Diamond 

   * D) Emerald



9. **What happens when you sleep in a bed in the Nether or the End?**



   * A) You set your spawn point

   * B) Nothing happens

   * C) The bed explodes 

   * D) You teleport home



10. **Which block is needed to activate a beacon's powers?**



* A) Glowstone

* B) Diamond Block 

* C) Obsidian

* D) Quartz Block
 
      

""")
    one = str(input("q.1: ")).lower()
    two = str(input("q.2: ")).lower()
    three = str(input("q.3: ").lower())
    four = str(input("q.4: ").lower())
    five = str(input("q.5: ").lower())
    six = str(input("q.6: ").lower())
    seven = str(input("q.7: ").lower())
    eight = str(input("q.8: ").lower())
    nine = str(input("q.9: ").lower())
    ten = str(input("q.10: ").lower())
    score = 0
    if one == "a":
        score += 2
    else:
        pass
    if two == "d":
        score += 2
    else:
        pass
    if three == "a":
        score += 2
    else:
        pass
    if four == "b":
        score += 2
    else:
        pass
    if five == "b":
        score += 2
    else:
        pass
    if six == "c":
        score += 2
    else:
        pass
    if seven == "b":
        score += 2
    else:
        pass
    if eight == "c":
        score += 2
    else:
        pass
    if nine == "c":
        score += 2
    else:
        pass
    if ten == "b":
        score += 2
    else:
        pass

    print("here is your score: " + str(score))
    ansr = str(input("""
    do you want to play again?
      yes/no
"""))
    if ansr == "no" :
        break
    print("bye!")
    if ansr == "yes" :
        continue
