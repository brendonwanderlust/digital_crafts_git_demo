# In this simple RPG game, the hero fights the goblin. He has the options to:
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def main():
    barry_the_hero = Hero()
    steve_the_goblin = Goblin()

    while steve_the_goblin.health > 0 and barry_the_hero.health > 0:
        print "You have %d health and %d power." % (barry_the_hero.health, barry_the_hero.power)
        print "The goblin has %d health and %d power." % (steve_the_goblin.health, steve_the_goblin.power)
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            steve_the_goblin.health -= barry_the_hero.power
            print "You do %d damage to the goblin." % barry_the_hero.power
            if steve_the_goblin.health <= 0:
                print "The goblin is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if steve_the_goblin.health > 0:
            # Goblin attacks hero
            barry_the_hero.health -= steve_the_goblin.power
            print "The goblin does %d damage to you." % steve_the_goblin.power
            if barry_the_hero.health <= 0:
                print "You are dead."


main()
