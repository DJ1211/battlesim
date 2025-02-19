# battlesim

A program to simulate battles between 2 Fire Emblem Sacred Stones units.

Goals are to implement levelling up with growth rates, different weapons & promotion.

Small number of units & weapons to begin with.

Magic has been named strength to make the variable name simpler. Magic units still target res over def as expected

Base stats for unpromoted units are their joining stats - the class base stats.
Base stats for promoted units are their joining stats - the promotion bonus of promoting into that class
Similarly, unpromoted classes use the base stats for their stats, whereas promoted classes use the promotion bonuses
This allows for more customisation as can more easily play with units in classes they don't usually have access to.

TBD:
Class skills e.g. Swordmaster crit bonus
Weapon skills (brave, devil)
Swordslayer effective against sword user
Add check for csv files exisiting