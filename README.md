# battlesim

## How to Run

1. Ensure Python3 is installed. This program was developed with Python 3.12.3

2. Click the green button and select Download Zip. Extract the contents somewhere you can find them easily

3. Run main.py. This can be ran directly by double cliking the file in the folder or by launching it via Command Prompt

### About the Program

**A program to simulate battles between two Fire Emblem Sacred Stones units.**

This program allows you to choose two units from the game "Fire Emblem Sacred Stones" and simulate a battle between them. The battle will continue until one of the units is defeated.

Once a unit has been selected you will be able to choose a weapon for them to use, as well as increase their level up to 20, increasing their stats. If a unit is level 10 or above, they can be promoted into one of their advanced classes, providing a boost to stats and resetting their level to 1 allowing them to be levelled up further.

Optionally, the units base class can be changed. This will completely reset them to their base stats, so is bets done before levelling & promoting them. The option is more for fun than anything. Any unit can be put into any class meaning certain charcaters may end up incredibly strong or incredibly weak if using this feature.

All units, weapons, class and terrain stats are imported into the program from the relevant .csv files fouind in the stat_sheets directory. This allows stats to be tweaked as desired and allows the addition of custom content.

Magic and Strength are considered one stat (named str). Magic units still target resistance over defence as expected

Base stats for unpromoted units are their joining stats minus the class base stats.
Base stats for promoted units are their joining stats minus the promotion bonus of promoting into that class
Similarly, unpromoted classes use the base stats for their stats, whereas promoted classes use the promotion bonuses
This allows for more customisation as can more easily play with units in classes they don't usually have access to.

Class skills are defined in jobs.csv under class_skills. Weapon skills are defined in weapons.csv under other_effects

#### Implemented Skills

The following skills are currently functional:

**Class Skills**
* Crit - +15% chance to critical hit
* Great Shield - EnemyLevel% chance to make next attack do 0
* Pierce - SelfLevel% chance to make next attack ignore defence
* Silencer - 50% chance to instantly reduce targets HP to 0 when scoring a critical hit regardless of damage dealt
* Slayer - Gain effective damage against Monsters
* Sure Strike - SelfLevel% chance to make attack 100% hit

**Weapon Skills**
* Brave - Attacks twice
* Devil - 31 - Luck% to damage self
* Halve HP - Deals damage equal to 50% targets current HP
* Ignore Def - Ignores targets Def stat
* Ignore Res - Ignore targets Res stat
* Lifesteal - Recover HP equal to damage dealt
* Stat Ups - Various stat increases


#### TBD
Things I would like to address in the future:
* Personal Weapon
* Tweaks to UI. Would like to improve the design. Perhaps add portraits of the units
* Changes to stat increase skills. Currently hardcoded and inflexible. Would like to add more flexibility to how they work
* General tidy up & improvement