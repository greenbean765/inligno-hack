# (down, over)
import time, replit
from random import randint
from termcolor import colored, cprint
monsters = False
replit.clear()
Key = 0
Level = 1
XP = 0
ReqXP = 50
maxHP = 100
etype = 2
l = None
HP = maxHP
maxBP = 8
BP = maxBP
coin = 0
DEF = 0
wins = 0
eHP = 1
k = 1
Fb = 8
He = 15
Df = 0
map01 = [list("AAAAAAAAAAAAAAAAAAAA"), list("AAAAAAA####XWWWWAAAA"), list("AAAAAA##O##XWWWWWAAA"), list("AAAAAi####XWWWWWWWAA"), list("AAAAAAAXXXXWWWWWWWWA"), list("AAAAAWWWWWWWWWWWWWXA"), list("AAAA@XWWWWWWWWXXXX@A"), list("AA@@@@XXWWWWWX@@@@@A"), list("A@@@@@@@XXWWWX@@@@>A"), list("A@@@@@@@@@XWWWXX@@@A"), list("A@@@###@@@@XXWWWX##A"), list("A@s@#i##@@g@@XWWWX#A"), list("A@@@@##@@@@@@XWWWWXA"), list("AAAAAAAAAAAAAAAWWWWA"), [2,11,True,"@","s"], [10,11,True,"@","g"], [8,2,"#",True]]
map02 = [list("AAAAAAAAAAAAAAAAAAAA"), list("AXXXXXXXXAAAXXX^XXXA"), list("AXXXXXXXXXXAAXXXXXXA"), list("AXXXXXXXXXXAAAXXXXXA"), list("AXXXXXXXXXXAAAXXXXXA"), list("AXXXXXXXXXXAAXXXXXXA"), list("A#XXXXXXXXXXAAXXXXXA"), list("A###XXXXXXX!AAXXXXXA"), list("AO###XXXXXXXAAXXXXXA"), list("A####XXXXXXAAXXXXXXA"), list("A##XXXXXXXX>AAAXXXXA"), list("A##XXXXXXXAAAAAXXXXA"), list("A#XXXXXXAAAAAXXXXXXA"), list("AAAAAAAAAAAAAAAAAAAA"), [1,8,"<",True]]
map03 = [list("AAAAAAAAAAAAAAAAAAAA"), list("AAAAAAAAAAAAAAAAAAAA"), list("AAAAAAAAAAAAAAAAAAAA"), list("AAA______________AAA"), list("AAA______________AAA"), list("AAA______________AAA"), list("AAO______n_______AAA"), list("AAA______________AAA"), list("AAA______________AAA"), list("AAA______________AAA"), list("AAA______________AAA"), list("AAAAAAAAAAAAAAAAAAAA"), list("AAAAAAAAAAAAAAAAAAAA"), list("AAAAAAAAAAAAAAAAAAAA"), [2,6,"<",True]]
map04 = [list("AAAAAAAAAAAAAAAAAAAA"), list("AXXXXXXXXXXXXXXAXXXA"), list("AXiXXXXXXXXXXXXAXXXA"), list("AXXXXXXXXXXXXXXAXXXA"), list("AAAAAAAAAAAXXXXAXXXA"), list("AAAAAAAAAXXXXXXAXXXA"), list("AAAAAAAXXXXXXAAAXXXA"), list("AAAAAXXXXXXAAAAAXXXA"), list("AAAXXXXXXAAAAAAAXXXA"), list("AXXXXXXAAAAAAAAAXXXA"), list("AXXXXXXXXXXXXXXXXXXA"), list("AXXXXXXXXXXXXXXXXXXA"), list("AXXXXXXXXXXXXXXOXXXA"), list("AAAAAAAAAAAAAAAAAAAA"), [15,12,"v",True]]
map05 = [list("AAAAAAAAAAAAAAAAAAAA"), list("A##www/###\wwwww###A"), list("A#wwww/####\wwww###A"),  list("Awwwww/####\#wwww##A"), list("Awwwww/###\##www###A"), list("AwwwwWW/A\WWWw#####A"), list("AAAAAAAXXXXXXAAAXXXA"), list("AAAAAXXXXXXAAAAAXXXA"), list("AAAXXXXXXAAAAAAAXXXA"), list("AXXXXXXAAAAAAAAAXXXA"), list("AXXXXXXXXXXXXXXXXXXA"), list("AXXXXXXXXXXXXXXXXXXA"), list("AXXXXXXXXXXXXXXOXXXA"), list("AAAAAAAAAAAAAAAAAAAA"), [15,12,"v",True]]
mapNo = map01
def getitem(Fb, He, Df):
  rec_fb = randint(0, 3)
  rec_he = randint(0, 2)
  rec_df = randint(0, 9)
  if rec_fb == 3:
    quantity = randint(1, 2)
    Fb += quantity
    print("Get %s " % quantity, end='')
    if quantity == 1:
      cprint("fireball!", 'red')
    else:
      cprint("fireballs!", 'red')
  if rec_he == 2:
    quantity = randint(1, 3)
    He += quantity
    print("Get %s " % quantity, end='')
    if quantity == 1:
      cprint("heal!", 'blue')
    else:
      cprint("heals!", 'blue')
  if rec_df == 9:
    Df += 1
    print("Get 1 ", end='')
    cprint("DEF+!", 'green')
  return Fb, He, Df
reqexp = 50
def levelup(choice, maxHP, maxBP, DEF, HP, BP):
  cprint("Level Up!", 'cyan')
  print("Choose:")
  cprint("HP", 'yellow')
  cprint("BP", 'green')
  cprint("DEF", 'blue')
  choice = input("(Type your choice)")
  if str(choice).lower() == "hp":
    replit.clear()
    maxHP += 10
    HP = maxHP
    BP = maxBP
    cprint("HP +10!", 'yellow')
    return choice, maxHP, maxBP, DEF, HP, BP
  elif str(choice).lower() == "bp":
    replit.clear()
    maxBP += 2
    BP = maxBP
    HP = maxHP
    cprint("BP +2!", 'green')
    return choice, maxHP, maxBP, DEF, HP, BP
  elif str(choice).lower() == "def":
    replit.clear()
    DEF += 5
    HP = maxHP
    BP = maxBP
    cprint("DEF +5!", 'blue')
    return choice, maxHP, maxBP, DEF, HP, BP
  else:
    replit.clear()
    print("Invalid Choice")
    return choice, maxHP, maxBP, DEF, HP, BP
def enemy_art():
  if etype == 1:
    shock()
  elif etype == 2:
    garble()
def garble():
  print("                  ", end='')
  cprint("@@", 'grey', end='')
  print("    ", end='')
  cprint("@@@@@@@@", 'grey')
  print("                ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@@@@@@@@@@@@@", 'grey')
  print("    ", end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  print("      ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@@@@@@@@@@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'white', end='')
  cprint("@@@@@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'red', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'red', end='')
  cprint("@@", 'grey')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'white', end='')
  cprint("@@@@@@", 'grey', end='')
  cprint("@@@@", 'red', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  cprint("@@@@@@", 'grey', end='')
  cprint("@@@@", 'white', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@", 'white', end='')
  cprint("@@@@@@@@@@@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("  ", end='')
  cprint("@@@@@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@", 'white', end='')
  cprint("@@@@@@@@@@@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("    ", end='')
  cprint("@@@@@@", 'grey', end='')
  cprint("@@@@", 'red', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'white', end='')
  cprint("@@@@@@@@@@@@", 'grey', end='')
  cprint("@@@@@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("      ", end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@", 'red', end='')
  cprint("@@@@@@@@@@@@@@@@@@@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("      ", end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@@@@@@@@@", 'red', end='')
  cprint("@@@@@@", 'grey', end='')
  cprint("@@", 'red', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@@@@@", 'grey')
  print("        ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@@@@@@@@@@@@@@@", 'red', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey')
  print("        ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@@@@@@@@@@@@@@@", 'red', end='')
  cprint("@@@@", 'grey')
  print("        ", end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@@@@@@@@@@@@@@@", 'red', end='')
  cprint("@@", 'grey')
  print("        ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@@@@@@@@@@@", 'red', end='')
  cprint("@@", 'grey')
  print("        ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@@@@@@@@@", 'red', end='')
  cprint("@@", 'grey')
  print("        ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@@@@@@@", 'red', end='')
  cprint("@@@@", 'grey')
  print("        ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@@@@@@@@@@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("          ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("            ", end='')
  cprint("@@@@@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("                ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("                ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("                  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("                    ", end='')
  cprint("@@@@@@", 'grey', end='')
  print("    ", end='')
  cprint("@@@@@@", 'grey')
def shock():
  print("                    ", end='')
  cprint("@@", 'grey')
  print("                  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@@@@@", 'grey')
  print("                ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("            ", end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("          ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@", 'yellow', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("        ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey')
  print("      ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  # Gosh this is taking a long time
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'white', end='')
  cprint("@@", 'grey')
  print("    ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@@@@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@", 'white', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@@@", 'grey')
  print("  ", end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@@@@@", 'yellow', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'white', end='')
  cprint("@@@@", 'grey')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@@@@@@@@@@@@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@@@", 'white', end='')
  cprint("@@@@", 'grey')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey', end='')
  print("        ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@@@", 'white', end='')
  cprint("@@", 'grey')
  print("    ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey', end='')
  print("    ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@@@@@", 'white', end='')
  cprint("@@", 'grey')
  print("      ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@@@@@@@", 'white', end='')
  cprint("@@", 'grey')
  print("        ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@", 'white', end='')
  cprint("@@@@", 'grey')
  print("          ", end='')
  cprint("@@@@@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@@@@@@@@@", 'grey')
  print("                ", end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@", 'white', end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("              ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'white', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("              ", end='')
  cprint("@@@@@@@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("              ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("            ", end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("        ", end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("      ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@@@", 'yellow', end='')
  cprint("@@@@", 'grey', end='')
  print("  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("      ", end='')
  cprint("@@@@@@@@", 'grey', end='')
  print("    ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("                  ", end='')
  cprint("@@", 'grey', end='')
  cprint("@@", 'yellow', end='')
  cprint("@@", 'grey')
  print("                    ", end='')
  cprint("@@@@", 'grey')
currentTile = mapNo[len(mapNo)-1][2]
def battle(Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins):
  DEFadd = 0
  Dfcounter = 0
  sword = 40
  while HP > 0:
    punch = 25 + (wins * 1.7)
    if etype == 1:
      eHP = 50 + (wins * 2)
      exp = 12 + (wins * 2)
      ecoin = randint(wins + 1, wins + 4)
      ename = "Shock "
      ecolor = 'yellow'
      eDEF = 6 + wins
    elif etype == 2:
      eHP = 40 + (wins * 1.5)
      exp = (wins * 2) + 9
      ecoin = randint(wins + 2, wins + 3)
      ename = "Garble "
      ecolor = 'red'
      eDEF = 10 + wins
    else:
      print("This message should not appear")
    print("Enemy ", end='')
    cprint("%s" % ename, '%s' % ecolor, end='')
    print("Appears!")
    
    while eHP > 0:
      if etype == 1:
        ePOW = randint(wins + 15, wins * 2 + 15)
      elif etype == 2:
        ePOW = randint(wins + 10, wins * 2 + 10)
      dHP = str(HP) + "/" + str(maxHP)
      dBP = str(BP) + "/" + str(maxBP)
      dXP = str(XP) + "/" + str(reqexp)
      enemy_art()
      Dfcounter -= 1
      if Dfcounter > 0:
        cprint("DEF +%s" % DEFadd, 'blue', end='')
        print(" ~ ", end='')
        cprint("%s turns" % Dfcounter, 'blue')
      else:
        DEF -= DEFadd
        DEFadd = 0
      cprint("$ - %s/999" % coin, 'magenta')
      cprint("XP - %s" % dXP, 'cyan')
      cprint("HP - %s" % dHP, 'yellow')
      cprint("BP - %s" % dBP, 'green')
      specialA = randint(60,120)
      specialB = randint(50,90)
      fireball = randint(45,100)
      heal = randint(65,100)
      
      print("Choose:")
      cprint("\tAttack", 'red')
      cprint("\tItem", 'cyan')
      cprint("\tSpecial", 'magenta')
      cprint("\tRun", 'white')
      choice = input("(Type your choice)")
      
      if str(choice).lower() == "attack":
        replit.clear()
        enemy_art()
        print("Level " + str(wins + 1))
        cprint("$ - %s/999" % coin, 'magenta')
        cprint("XP - %s" % dXP, 'cyan')
        cprint("HP - %s" % dHP, 'yellow')
        cprint("BP - %s" % dBP, 'green')
        cprint("Attacks:", 'red')
        cprint("\tSword", 'white')
        cprint("\tPunch", 'yellow')
        # don't make THAT mistake
        choice = input("(Type your choice)")
        
        if str(choice).lower() == "sword":
          replit.clear()
          critical = randint(0, 10)
          if critical >= 8:
            damage = (sword * 2) - eDEF
            cprint("Critical Hit!", 'cyan')
          else:
            damage = sword - eDEF
          if damage < 0:
            damage = 0
          else:
            u = 0
          eHP -= damage
          cprint("Enemy ", 'blue', end='')
          cprint("%s" % ename, '%s' % ecolor, end='')
          cprint("Takes %s Damage!" % damage, 'blue')
          if eHP <= 0:
            wins += 1
            XP += exp
            coin += ecoin
            cprint("+ %s $!" % ecoin, 'magenta')
            if coin > 999:
              coin = 999
            cprint("+ %s XP" % exp, 'cyan')
            cprint("Enemy ", 'magenta', end='')
            cprint("%s" % ename, '%s' % ecolor, end='')
            cprint("is Defeated", 'magenta')
            Fb, He, Df = getitem(Fb, He, Df)
            while XP >= ReqXP:
              choice, maxHP, maxBP, DEF, HP, BP = levelup(choice, maxHP, maxBP, DEF, HP, BP)
              if str(choice).lower() == "hp":
                XP -= ReqXP
                ReqXP += (wins + 24)
                break
              elif str(choice).lower() == "bp":
                XP -= ReqXP
                ReqXP += (wins + 24)
                break
              elif str(choice).lower() == "def":
                XP -= ReqXP
                ReqXP += (wins + 24)
                break
            return Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins
          else:
            damage = ePOW - DEF
            if damage < 0:
              damage = 0
            else:
              u = 0
            HP -= damage
            cprint("Take %s Damage!" % damage, 'red')
            if HP <= 0:
              time.sleep(1)
              replit.clear()
              cprint('''
  
  
        Game Over
        
        
        ''','red')
              quit()
            else:
              print("")
        
        elif str(choice).lower() == "punch":
          replit.clear()
          critical = randint(0, 10)
          if critical >= 9:
            damage = (punch * 2) - eDEF
            cprint("Critical Hit!", 'cyan')
          else:
            damage = punch - eDEF
          if damage < 0:
              damage = 0
          else:
            u = 0
          eHP -= damage
          cprint("Enemy ", 'blue', end='')
          cprint("%s" % ename, '%s' % ecolor, end='')
          cprint("Takes %s Damage!" % damage, 'blue')
          if eHP <= 0:
            wins += 1
            XP += exp
            coin += ecoin
            cprint("+ %s $!" % ecoin, 'magenta')
            if coin > 999:
              coin = 999
            cprint("+ %s xp" % exp, 'cyan')
            cprint("Enemy ", 'magenta', end='')
            cprint("%s" % ename, '%s' % ecolor, end='')
            cprint("is Defeated", 'magenta')
            Fb, He, Df = getitem(Fb, He, Df)
            while XP >= ReqXP:
              choice, maxHP, maxBP, DEF, HP, BP = levelup(choice, maxHP, maxBP, DEF, HP, BP)
              if str(choice).lower() == "hp":
                XP -= ReqXP
                ReqXP += (wins + 24)
                break
              elif str(choice).lower() == "bp":
                XP -= ReqXP
                ReqXP += (wins + 24)
                break
              elif str(choice).lower() == "def":
                XP -= ReqXP
                ReqXP += (wins + 24)
                break
            return Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins
          else:
            damage = ePOW - DEF
            if damage < 0:
              damage = 0
            else:
              u = 0
            HP -= damage
            cprint("Take %s Damage!" % damage, 'red')
            if HP <= 0:
              time.sleep(1)
              replit.clear()
              cprint('''
  
  
        Game Over
        
        
        ''','red')
              quit()
            else:
              print("")
        
        else:
          replit.clear()
          Dfcounter += 1
          print("Invalid Choice")
          
      elif str(choice).lower() == "item":
        replit.clear()
        enemy_art()
        print("Level " + str(wins + 1))
        cprint("$ - %s/999" % coin, 'magenta')
        cprint("XP - %s" % dXP, 'cyan')
        cprint("HP - %s" % dHP, 'yellow')
        cprint("BP - %s" % dBP, 'green')
        cprint("Items:", 'cyan')
        cprint("\tHeal * %s" % He, 'blue')
        cprint("\tFireball * %s" % Fb, 'red')
        cprint("\tDEF+ * %s" % Df, 'green')
        choice = input("(Type your choice)")
        
        if str(choice).lower() == "heal":
          replit.clear()
          if He <= 0:
            replit.clear()
            Dfcounter += 1
            print("No More Heals")
          else:
            He -= 1
            damage = heal
            HP += damage
            cprint("+ %sHP" % damage, 'cyan')
            if HP > maxHP:
              HP = maxHP
              damage = ePOW - DEF
              HP -= damage
              cprint("Take %s Damage!" % damage, 'red')
            else:
              damage = ePOW - DEF
              if damage < 0:
                damage = 0
              else:
                u = 0
              HP -= damage
              cprint("Take %s Damage!" % damage, 'red')
              if HP <= 0:
                time.sleep(1)
                replit.clear()
                cprint('''


        Game Over
        
        
        ''','red')
                quit()
              else:
                print("")
      
        elif str(choice).lower() == "fireball":
          replit.clear()
          if Fb <= 0:
            replit.clear()
            Dfcounter += 1
            print("No More Fireballs")
          else:
            Fb -= 1
            damage = fireball
            eHP -= damage
            cprint("Enemy ", 'blue', end='')
            cprint("%s" % ename, '%s' % ecolor, end='')
            cprint("Takes %s Damage!" % damage, 'blue')
            if eHP <= 0:
              wins += 1
              XP += exp
              coin += ecoin
              cprint("+ %s $!" % ecoin, 'magenta')
              if coin > 999:
                coin = 999
              cprint("+ %sXP" % exp, 'cyan')
              cprint("Enemy ", 'magenta', end='')
              cprint("%s" % ename, '%s' % ecolor, end='')
              cprint("is Defeated", 'magenta')
              Fb, He, Df = getitem(Fb, He, Df)
              while XP >= ReqXP:
                choice, maxHP, maxBP, DEF, HP, BP = levelup(choice, maxHP, maxBP, DEF, HP, BP)
                if str(choice).lower() == "hp":
                  XP -= ReqXP
                  ReqXP += (wins + 24)
                  break
                elif str(choice).lower() == "bp":
                  XP -= ReqXP
                  ReqXP += (wins + 24)
                  break
                elif str(choice).lower() == "def":
                  XP -= ReqXP
                  ReqXP += (wins + 24)
                  break
              return Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins
            else:
              damage = ePOW - DEF
              if damage < 0:
                damage = 0
              else:
                u = 0
              HP -= damage
              cprint("Take %s Damage!" % damage, 'red')
              if HP <= 0:
                time.sleep(1)
                replit.clear()
                cprint('''


        Game Over
        
        
        ''','red')
                quit()
              else:
                print("")
        elif str(choice).lower() == "def+":
          replit.clear()
          if Df <= 0:
            Dfcounter += 1
            print("No More DEF+")
          elif Dfcounter > 0:
            Dfcounter += 1
            print("You are already using one of these")
          else:
            Df -= 1
            DEFadd = randint(8, 12)
            DEF += DEFadd
            Dfcounter = 4
            cprint("DEF +%s" % DEFadd, 'blue')
            damage = ePOW - DEF
            if damage < 0:
              damage = 0
            else:
              u = 0
            HP -= damage
            cprint("Take %s Damage!" % damage, 'red')
            if HP <= 0:
              time.sleep(1)
              replit.clear()
              cprint('''
              
              
                      Game Over
                      
                      
                      ''','red')
              quit()
            else:
              print("")
      
        else:
          replit.clear()
          Dfcounter += 1
          print("Invalid Choice")
      
      elif str(choice).lower() == "special":
        replit.clear()
        enemy_art()
        print("Level " + str(wins + 1))
        cprint("$ - %s/999" % coin, 'magenta')
        cprint("XP - %s" % dXP, 'cyan')
        cprint("HP - %s" % dHP, 'yellow')
        cprint("BP - %s" % dBP, 'green')
        cprint("Special:", 'magenta')
        cprint("\tShockwave - 5 BP", 'yellow')
        cprint("\tTri Sword - 3 BP", 'white')
        cprint("\tBP heal", 'green')
        choice = input("(Type your choice)")
        if str(choice).lower() == "shockwave":
          replit.clear()
          if BP >= 5:
            BP -= 5
            critical = randint(0, 10)
            if critical >= 10:
              damage = (specialA * 2) - eDEF
              cprint("Critical Hit!", 'cyan')
            else:
              damage = specialA - eDEF
            if damage < 0:
              damage = 0
            else:
              u = 0
            eHP -= damage
            cprint("Enemy ", 'blue', end='')
            cprint("%s" % ename, '%s' % ecolor, end='')
            cprint("Takes %s Damage!" % damage, 'blue')
            if eHP <= 0:
              wins += 1
              XP += exp
              coin += ecoin
              cprint("+ %s $!" % ecoin, 'magenta')
              if coin > 999:
                coin = 999
              cprint("+ %sXP" % exp, 'cyan')
              cprint("Enemy ", 'magenta', end='')
              cprint("%s" % ename, '%s' % ecolor, end='')
              cprint("is Defeated", 'magenta')
              Fb, He, Df = getitem(Fb, He, Df)
              while XP >= ReqXP:
                choice, maxHP, maxBP, DEF, HP, BP = levelup(choice, maxHP, maxBP, DEF, HP, BP)
                if str(choice).lower() == "hp":
                  XP -= ReqXP
                  ReqXP += (wins + 24)
                  break
                elif str(choice).lower() == "bp":
                  XP -= ReqXP
                  ReqXP += (wins + 24)
                  break
                elif str(choice).lower() == "def":
                  XP -= ReqXP
                  ReqXP += (wins + 24)
                  break
              return Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins
            else:
              damage = ePOW - DEF
              if damage < 0:
                damage = 0
              else:
                u = 0
              HP -= damage
              cprint("Take %s Damage!" % damage, 'red')
              if HP <= 0:
                time.sleep(1)
                replit.clear()
                cprint('''
  
  
        Game Over
        
        
        ''','red')
                quit()
              else:
                print("")
          else:
            Dfcounter += 1
            print("Not Enough BP")
            
        elif str(choice).lower() == "bp heal":
          replit.clear()
          damage = randint(2, 4)
          BP += damage
          cprint("+ %sBP" % damage, 'blue')
          if BP > maxBP:
            BP = maxBP
          damage = ePOW - DEF
          HP -= damage
          cprint("Take %s Damage!" % damage, 'red')
          if HP <= 0:
            time.sleep(1)
            replit.clear()
            cprint('''


        Game Over
        
        
        ''','red')
            quit()
          else:
            print("")
            
        elif str(choice).lower() == "tri sword":
          replit.clear()
          if BP >= 3:
            BP -= 3
            critical = randint(0, 10)
            if critical >= 9:
              damage = (specialB * 2) - eDEF
              cprint("Critical Hit!", 'cyan')
            else:
              damage = specialB - eDEF
            if damage < 0:
              damage = 0
            else:
              u = 0
            eHP -= damage
            cprint("Enemy ", 'blue', end='')
            cprint("%s" % ename, '%s' % ecolor, end='')
            cprint("Takes %s Damage!" % damage, 'blue')
            if eHP <= 0:
              wins += 1
              XP += exp
              coin += ecoin
              cprint("+ %s $!" % ecoin, 'magenta')
              if coin > 999:
                coin = 999
              cprint("+ %sXP" % exp, 'cyan')
              cprint("Enemy ", 'magenta', end='')
              cprint("%s" % ename, '%s' % ecolor, end='')
              cprint("is Defeated", 'magenta')
              Fb, He, Df = getitem(Fb, He, Df)
              while XP >= ReqXP:
                choice, maxHP, maxBP, DEF, HP, BP = levelup(choice, maxHP, maxBP, DEF, HP, BP)
                if str(choice).lower() == "hp":
                  XP -= ReqXP
                  ReqXP += (wins + 24)
                  break
                elif str(choice).lower() == "bp":
                  XP -= ReqXP
                  ReqXP += (wins + 24)
                  break
                elif str(choice).lower() == "def":
                  XP -= ReqXP
                  ReqXP += (wins + 24)
                  break
              return Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins 
            else:
              damage = ePOW - DEF
              if damage < 0:
                damage = 0
              else:
                u = 0
              HP -= damage
              cprint("Take %s Damage!" % damage, 'red')
              if HP <= 0:
                time.sleep(1)
                replit.clear()
                cprint('''


        Game Over
        
        
        ''','red')
                quit()
              else:
                print("")
          else:
            Dfcounter += 1
            print("Not Enough BP")
            
        else:
          replit.clear()
          Dfcounter += 1
          print("Invalid Choice")
          
      elif str(choice).lower() == "run":
        replit.clear()
        print("You Ran!")
        return Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins
      # don't make THAT mistake
      else:        
        replit.clear()
        Dfcounter += 1
        print("Invalid Choice")
  
def useKey2(mapObj,Key,l):
  x = mapObj[len(mapObj)-1][0]
  y = mapObj[len(mapObj)-1][1]
  if x == 11 and y == 7:
    if mapObj[-1][2] == "!":
      if Key <= 0:
        l = "you have no key."
        Key = 0
        return mapObj,Key,l
      Key -= 1
      mapObj[7][12] = "_"
      mapObj[7][13] = "_"
      mapObj[-1][2] = "X"
      l = None
  else:
    l = "nothing to unlock."
  return mapObj,Key,l
def monster(mapObj,monster):
  x = monster[0]
  y = monster[1]
  currentTile = monster[-2]
  mapObj[y][x] = currentTile
  xadd = 0
  yadd = 0
  if mapObj[-1][0] > x - 5 and mapObj[-1][0] < x + 5 and mapObj[-1][1] > y - 5 and mapObj[-1][1] < y + 5:
    if mapObj[-1][0] > x:
      xadd = 1
    elif mapObj[-1][0] < x:
      xadd = -1
    if mapObj[-1][1] > y:
      yadd = 1
    elif mapObj[-1][1] < y:
      yadd = -1
  else:
    direction = randint(1,8)
    if direction == 1:
      xadd = 1
    elif direction == 2:
      xadd = -1
    elif direction == 3:
      yadd = 1
    elif direction == 4:
      yadd = -1
    elif direction == 5:
      xadd = 1
      yadd = 1
    elif direction == 6:
      xadd = -1
      yadd = 1
    elif direction == 7:
      xadd = -1
      yadd = -1
    elif direction == 8:
      xadd = 1
      yadd = -1
  x += xadd
  y += yadd
  if mapObj[y][x] == "A":
    x -= xadd
    y -= yadd
  elif mapObj[y][x] == "W":
    x -= xadd
    y -= yadd
  elif mapObj[y][x] == "\\" or mapObj[y][x] == "/":
    x -= xadd
    y -= yadd
  elif mapObj[y][x] == "M":
    x -= xadd
    y -= yadd
  currentTile = mapObj[y][x]
  mapObj[y][x] = monster[-1]
  monster[-2] = currentTile
  monster[0] = x
  monster[1] = y

def mapPrint(mapObj):
    for i in mapObj:
        for x in i:
            if x == "W":
              x = x+" "
              cprint(x,'blue',end='')
            elif x == "@":
              x = x+" "
              cprint(x,'green',attrs=['bold'],end='')
            elif x == "A":
              x = x+" "
              cprint(x,'grey',end='')
            elif x == "#":
              x = x+" "
              cprint(x,'green',end='')
            elif x == "i":
              x = x+" "
              cprint(x,'grey',attrs=['bold'],end='')
            elif x == "_":
              x = x+" "
              cprint(x,'white',end='')
            elif x == "X":
              x = x+" "
              cprint(x,'yellow',end='')
            elif x == "M":
              x = x+" "
              cprint(x,'red',end='')
            elif x == "H":
              x = x+" "
              cprint(x,'grey',end='')
            elif x == "=":
              x = x+" "
              cprint(x,'yellow',attrs=['bold'],end='')
            elif x == "w":
              x = x+" "
              cprint(x,'cyan',end='')
            elif x == "!":
              x = x+" "
              cprint(x,'blue',end='')
            elif x == "n":
              x = x+" "
              cprint(x,'red',attrs=['bold'],end='')
            elif x == "u":
              x = x+" "
              cprint(x,'red',attrs=['bold'],end='')
            elif x == "/":
              x = x+" "
              cprint(x,'grey',end='')
            elif x == str("\\"):
              x = x+" "
              cprint(x,'grey',end='')
            elif x == "s":
              x = x+" "
              cprint(x,'yellow',attrs=['bold'],end='')
            elif x == "g":
              x = x+" "
              cprint(x,'red',attrs=['bold'],end='')
            else:
              x = str(x)+" "
              print(x,end='')
        print()
def interact1(mapObj):
  x = mapObj[len(mapObj)-1][0]
  y = mapObj[len(mapObj)-1][1]
  if x == 5 and y == 3:
    mapObj[5][9] = "="
    mapObj[6][9] = "="
    mapObj[7][9] = "="
    replit.clear()
  elif x == 5 and y == 11:
    mapObj[11][14] = "="
    mapObj[11][15] = "="
    mapObj[11][16] = "="
    replit.clear()
  else:
    print("No object to interact with.")
    time.sleep(1)
  return mapObj
def interact3(mapObj,Key):
  if mapObj[-1][2] == "n":
    Key += 1
    mapObj[-1][2] = "u"
    replit.clear()
    return mapObj,Key
  elif mapObj[-1][2] == "u":
    print("Chest already opened")
    time.sleep(1)
    replit.clear()
  else:
    print("No object to interact with.")
    time.sleep(1)
    replit.clear
  return mapObj,Key
def interact4(mapObj,map01):
  x = mapObj[len(mapObj)-1][0]
  y = mapObj[len(mapObj)-1][1]
  if x == 2 and y == 2:
    map01[6][3] = "_"
    map01[6][2] = "_"
    map01[6][1] = "_"
    map01[5][3] = "_"
    map01[5][2] = "_"
    map01[5][1] = "<"
    map01[4][3] = "_"
    map01[4][2] = "_"
    map01[4][1] = "_"
    replit.clear()
    print("Something happened somewhere!")
    time.sleep(1)
    replit.clear()
  else:
    print("No object to interact with.")
    time.sleep(1)
    replit.clear()
  return mapObj,map01
def move(mapObj,xAdd,yAdd):
    x = mapObj[-1][0]
    y = mapObj[-1][1]
    currentTile = mapObj[-1][2]
    mapObj[y][x] = currentTile
    x += xAdd
    y += yAdd
    if mapObj[y][x] == "A":
      replit.clear()
      print("The mountain is too high! Try looking for a tunnel.")
      x -= xAdd
      y -= yAdd
      mapObj[y][x] = "O"
      return "interference"
    elif mapObj[y][x] == "W":
      replit.clear()
      print("The water is too deep! Try looking for a bridge.")
      x -= xAdd
      y -= yAdd
      mapObj[y][x] = "O"
      return "interference"
    elif mapObj[y][x] == "M":
      replit.clear()
      print("The city walls are too high! Try looking for a gate.")
      x -= xAdd
      y -= yAdd
      mapObj[y][x] = "O"
      return "interference"
    elif mapObj[y][x] == "/" or mapObj[y][x] == "\\":
      replit.clear()
      print("The slope is too steep! Try somewhere else.")
      x -= xAdd
      y -= yAdd
      mapObj[y][x] = "O"
      return "interference"
    else:
      currentTile = mapObj[y][x]
      mapObj[-1][2] = currentTile
      mapObj[y][x] = "O"
      mapObj[-1][0] = x
      mapObj[-1][1] = y
      time.sleep(0.25)
def walk(mapObj,command):
  if command.lower() == "up":
    u = move(mapObj,0,-1)
  elif command.lower() == "down":
    u = move(mapObj,0,1)
  elif command.lower() == "left":
    u = move(mapObj,-1,0)
  elif command.lower() == "right":
    u = move(mapObj,1,0)
  if u == "interference":
    return "interference"
def enter(mapObj,l):
  x = mapObj[len(mapObj)-1][0]
  y = mapObj[len(mapObj)-1][1]
  if l == 1:
    if x == 18 and y == 8:
      l = 2
      return mapObj,l
    elif x == 1 and y == 5:
      l = 5
      return mapObj,l
    else:
      print("no entry point")
      return mapObj,l
  elif l == 2:
    if x == 1 and y == 8:
      l = 1
      return mapObj,l
    elif x == 11 and y == 10:
      l = 3
      return mapObj,l
    elif x == 15 and y == 1:
      l = 4
      return mapObj,l
    else:
      print("no entry point")
      return mapObj,l
  elif l == 3:
    if x == 2 and y == 6:
      l = 2
      return mapObj,l
    else:
      print("no entry point")
      return mapObj,l
  elif l == 4:
    if x == 15 and y == 12:
      l = 2
      return mapObj,l
    else:
      print("no entry point")
      return mapObj,l
  elif l == 5:
    if x == 15 and y == 12:
      l = 1
      return mapObj,l
    else:
      print("no entry point")
      return mapObj,l
def open_bag():
  print(bag)
# Main program
    
print('''
    
         WELCOME TO ''',end='')
cprint("INOGI",'cyan',end='')
print('''!
    inligno hack by ''', end='')
cprint("greenbean",'green',end='')
cprint("7",'blue',end='')
cprint("6",'magenta',end='')
cprint('''5

''','red')
print("      Press ",end='')
cprint("ENTER",'cyan',end='')
go = input(" to continue")
replit.clear()
time.sleep(0.1)
mapPrint(mapNo)
print("YOUR GOAL:")
while mapNo[-1][3] == True:
    print("Type 'i' to view controls")
    x = mapNo[-1][0]
    y = mapNo[-1][1]
    command = input()
    if command.lower() == "i":
      replit.clear()
      print('''
      CONTROLS
      
      -walk up/down/left/right (number of spaces)
        move your character
      -open bag
        opens your bag
      -interact
        interacts with an object at your location
      -enter
        enter a gate
      -use (item)
        use an item you have collected
      
      # = grass,
      @ = forest,
      _ = snow/rock floor
      = = bridge,
      X = sand,
      i = switch,
      A = mountain,
      W = deep water,
      w = shallow water,
      ! = keyhole,
      n = chest,
      u = opened chest,
      O = you
      s = shock
      g = garble
      </>/^/v = gate
      
      ITEMS:
        Key
        Book of Hints
        Heal
        Fireball
        DEF+
        
      GRID GUIDE
      
        x -->
      y 1 2 3
      | 2 # #
      V 3 # #
      
      ''')
      print("Press ",end='')
      cprint("ENTER",'cyan',end='')
      go = input("")
      replit.clear()
      mapPrint(mapNo)
    elif "walk" in command.lower():
      if "sudo" in command.lower():
          location = command.lower().split(" ")[3]
          x = int(location.split(",")[0])
          y = int(location.split(",")[1])
          move(mapNo,x-mapNo[len(mapNo)-1][0],y-mapNo[len(mapNo)-1][1])
          replit.clear()
          mapPrint(mapNo)
          continue
      if "up" in command.lower():
        try:
          amount = int(command.lower().split(" ")[2])
          n = 0
        except ValueError:
          replit.clear()
          print("you typed something wrong.")
          amount = 0
          n = 0
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
        except IndexError:
          replit.clear()
          print("you typed something wrong.")
          amount = 0
          n = 0
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
        while n != amount:
          walkStatus = walk(mapNo,command.lower().split(" ")[1])
          if walkStatus == "interference":
            time.sleep(1)
            replit.clear()
            mapPrint(mapNo)
            break
          n += 1
          for i in mapNo:
            x = mapNo[-1][0]
            y = mapNo[-1][1]
            if i[2] == True:
              monster(mapNo,i)
              if i[-1] == "s":
                etype = 1
              elif i[-1] == "g":
                etype = 2
              if i[0] == mapNo[-1][0] and i[1] == mapNo[-1][1]:
                replit.clear()
                time.sleep(1)
                Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins = battle(Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins)
              if eHP <= 0:
                i[2] = False
                if i[-2] == "O":
                  i[-2] = mapNo[-1][-2]
                mapNo[-1][-2] = i[-2]
                mapNo[y][x] = "O"
                eHP = 1
          replit.clear()
          time.sleep(0.1)
          mapPrint(mapNo)
          time.sleep(0.3)
      elif "down" in command.lower():
        try:
          amount = int(command.lower().split(" ")[2])
          n = 0
        except ValueError:
          replit.clear()
          print("you typed something wrong.")
          amount = 0
          n = 0
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
        except IndexError:
          replit.clear()
          print("you typed something wrong.")
          amount = 0
          n = 0
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
        while n != amount:
          walkStatus = walk(mapNo,command.lower().split(" ")[1])
          if walkStatus == "interference":
            time.sleep(1)
            replit.clear()
            mapPrint(mapNo)
            break
          n += 1
          for i in mapNo:
            x = mapNo[-1][0]
            y = mapNo[-1][1]
            if i[2] == True:
              monster(mapNo,i)
              if i[-1] == "s":
                etype = 1
              elif i[-1] == "g":
                etype = 2
              if i[0] == mapNo[-1][0] and i[1] == mapNo[-1][1]:
                replit.clear()
                time.sleep(1)
                Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins = battle(Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins)
              if eHP <= 0:
                i[2] = False
                if i[-2] == "O":
                  i[-2] = mapNo[-1][-2]
                mapNo[-1][-2] = i[-2]
                mapNo[y][x] = "O"
                eHP = 1
          replit.clear()
          time.sleep(0.1)
          mapPrint(mapNo)
          time.sleep(0.3)
      elif "left" in command.lower():
        try:
          amount = int(command.lower().split(" ")[2])
          n = 0
        except ValueError:
          replit.clear()
          print("you typed something wrong.")
          amount = 0
          n = 0
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
        except IndexError:
          replit.clear()
          print("you typed something wrong.")
          amount = 0
          n = 0
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
        while n != amount:
          walkStatus = walk(mapNo,command.lower().split(" ")[1])
          if walkStatus == "interference":
            time.sleep(1)
            replit.clear()
            mapPrint(mapNo)
            break
          n += 1
          for i in mapNo:
            x = mapNo[-1][0]
            y = mapNo[-1][1]
            if i[2] == True:
              monster(mapNo,i)
              if i[-1] == "s":
                etype = 1
              elif i[-1] == "g":
                etype = 2
              if i[0] == mapNo[-1][0] and i[1] == mapNo[-1][1]:
                replit.clear()
                time.sleep(1)
                Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins = battle(Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins)
              if eHP <= 0:
                i[2] = False
                if i[-2] == "O":
                  i[-2] = mapNo[-1][-2]
                mapNo[-1][-2] = i[-2]
                mapNo[y][x] = "O"
                eHP = 1
          replit.clear()
          time.sleep(0.1)
          mapPrint(mapNo)
          time.sleep(0.3)
      elif "right" in command.lower():
        try:
          amount = int(command.lower().split(" ")[2])
          n = 0
        except ValueError:
          replit.clear()
          print("you typed something wrong.")
          amount = 0
          n = 0
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
        except IndexError:
          replit.clear()
          print("you typed something wrong.")
          amount = 0
          n = 0
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
        while n != amount:
          walkStatus = walk(mapNo,command.lower().split(" ")[1])
          x = mapNo[-1][0]
          y = mapNo[-1][1]
          if walkStatus == "interference":
            time.sleep(1)
            replit.clear()
            mapPrint(mapNo)
            break
          n += 1
          for i in mapNo:
            x = mapNo[-1][0]
            y = mapNo[-1][1]
            if i[2] == True:
              monster(mapNo,i)
              if i[-1] == "s":
                etype = 1
              elif i[-1] == "g":
                etype = 2
              if i[0] == mapNo[-1][0] and i[1] == mapNo[-1][1]:
                replit.clear()
                time.sleep(1)
                Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins = battle(Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins)
              if eHP <= 0:
                i[2] = False
                if i[-2] == "O":
                  i[-2] = mapNo[-1][-2]
                mapNo[-1][-2] = i[-2]
                mapNo[y][x] = "O"
                eHP = 1
          replit.clear()
          time.sleep(0.1)
          mapPrint(mapNo)
          time.sleep(0.3)
    elif command.lower() == "open bag":
      bag = ["Book of Hints","Key - %s" % Key,"Heal - %s" % He,"Fireball - %s" % Fb,"DEF+ - %s" % Df]
      open_bag()
    elif command.lower() == "interact":
      t = Key
      if mapNo == map01:
        monsters = interact1(mapNo)
      elif mapNo == map03:
        mapNo,Key = interact3(mapNo,Key)
      elif mapNo == map04:
        monsters,map01 = interact4(mapNo,map01)
      else:
        replit.clear()
        print("No object to interact with.")
        time.sleep(1)
        replit.clear()
      for i in mapNo:
        if i[2] == True:
          monster(mapNo,i)
          if i[-1] == "s":
            etype = 1
          elif i[-1] == "g":
            etype = 2
          if i[0] == mapNo[-1][0] and i[1] == mapNo[-1][1]:
            replit.clear()
            time.sleep(1)
            Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins = battle(Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins)
          if eHP <= 0:
            i[2] = False
            if i[-2] == "O":
              i[-2] = mapNo[-1][-2]
            mapNo[-1][-2] = i[-2]
            mapNo[y][x] = "O"
            eHP = 1
      replit.clear()
      time.sleep(0.1)
      mapPrint(mapNo)
      if Key > t:
        print("Got a key!")
    elif command.lower() == "enter":
      replit.clear()
      mapNo,k = enter(mapNo,k)
      if k == 1:
        if mapNo == map02:
          map02 = mapNo
        elif mapNo == map05:
          map05 = mapNo
        mapNo = map01
        mapPrint(mapNo)
      elif k == 2:
        if mapNo == map01:
          map01 = mapNo
        elif mapNo == map03:
          map03 = mapNo
        elif mapNo == map04:
          map04 = mapNo
        mapNo = map02
        mapPrint(mapNo)
      elif k == 3:
        if mapNo == map02:
          map02 = mapNo
        mapNo = map03
        mapPrint(mapNo)
      elif k == 4:
        if mapNo == map02:
          map02 = mapNo
        mapNo = map04
        mapPrint(mapNo)
      elif k == 5:
        if mapNo == map01:
          map01 = mapNo
        mapNo = map05
        mapPrint(mapNo)
    elif "use" in command.lower():
      if "key" in command.lower():
        mapNo,Key,l = useKey2(mapNo,Key,l)
        if l == "nothing to unlock.":
          replit.clear()
          print(l)
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
          continue
        elif l == "you have no key.":
          replit.clear()
          print(l)
          time.sleep(1)
          replit.clear()
          mapPrint(mapNo)
          continue
      else:
        replit.clear()
        print("no item by that name.")
        time.sleep(1)
        replit.clear()
        mapPrint(mapNo)
        continue
      for i in mapNo:
        if i[2] == True:
          monster(mapNo,i)
          if i[-1] == "s":
            etype = 1
          elif i[-1] == "g":
            etype = 2
          if i[0] == mapNo[-1][0] and i[1] == mapNo[-1][1]:
            replit.clear()
            time.sleep(1)
            Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins = battle(Fb,He,Df,Level,XP,ReqXP,HP,maxHP,BP,maxBP,DEF,etype,eHP,coin,wins)
          if eHP <= 0:
            i[2] = False
            if i[-2] == "O":
              i[-2] = mapNo[-1][-2]
            mapNo[-1][-2] = i[-2]
            mapNo[y][x] = "O"
            eHP = 1
      replit.clear()
      time.sleep(0.1)
      mapPrint(mapNo)
    else:
      print("Sorry, there's no command by that name.")
