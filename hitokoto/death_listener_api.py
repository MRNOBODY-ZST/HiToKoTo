import re

death1 = re.compile(".*? was shot.*?")
death2 = re.compile(".*?lost connection: Killed")
death3 = re.compile(".*? was pummeled.*?")
death4 = re.compile(".*? was pricked to death")
death5 = re.compile(".*? walked into a cactus whilst trying to escape .*?")
death6 = re.compile(".*? drowned")
death7 = re.compile(".*? drowned.*?")
death8 = re.compile(".*? experienced kinetic.*?")
death9 = re.compile(".*? blew up")
death10 = re.compile(".*? was blown up by .*?")
death11 = re.compile(".*? was killed by [Intentional Game Design]")
death12 = re.compile(".*? hit the ground too hard.*?")
death13 = re.compile(".*? fell.*?")
death14 = re.compile(".*? was impaled on a.*?")
death15 = re.compile(".*? went up in flames")
death16 = re.compile(".*? walked into fire whilst fighting .*?")
death17 = re.compile(".*? burned to death")
death18 = re.compile(".*? was burnt to a crisp whilst fighting .*?")
death19 = re.compile(".*? went off with a bang.*?")
death20 = re.compile(".*? tried to swim in lava.*?")
death21 = re.compile(".*? was struck by lightning.*?")
death22 = re.compile(".*? discovered the floor was lava")
death23 = re.compile(".*? walked into danger zone due to .*?")
death24 = re.compile(".*? was killed by.*?")
death25 = re.compile(".*? froze to death")
death26 = re.compile(".*? was frozen to death by .*?")
death27 = re.compile(".*? was slain by.*?")
death28 = re.compile(".*? was fireballed by .*?")
death29 = re.compile(".*? was stung to death")
death30 = re.compile(".*? was shot by a skull from .*?")
death31 = re.compile(".*? starved to.*?")
death32 = re.compile(".*? suffocated.*?")
death33 = re.compile(".*? was squished.*?")
death34 = re.compile(".*? was poked to death by a sweet berry bush")
death35 = re.compile(".*? was killed.*?")
death36 = re.compile(".*? was impaled by .*? with .*?")
death37 = re.compile(".*? fell out of the world")
death38 = re.compile(".*? didn't want to live in the same world as .*?")
death39 = re.compile(".*? withered.*?")

class death:

    def __init__(self) -> None:
        pass
    def detect(server_message):
        if death1.fullmatch(server_message) or death2.fullmatch(server_message) or death3.fullmatch(server_message) or death4.fullmatch(server_message) or death5.fullmatch(server_message) or death6.fullmatch(server_message) or death7.fullmatch(server_message) or death8.fullmatch(server_message) or death9.fullmatch(server_message) or death10.fullmatch(server_message) or death11.fullmatch(server_message) or death12.fullmatch(server_message) or death13.fullmatch(server_message) or death14.fullmatch(server_message) or death15.fullmatch(server_message) or death16.fullmatch(server_message) or death17.fullmatch(server_message) or death18.fullmatch(server_message) or death19.fullmatch(server_message) or death20.fullmatch(server_message) or death21.fullmatch(server_message) or death22.fullmatch(server_message) or death23.fullmatch(server_message) or death24.fullmatch(server_message) or death25.fullmatch(server_message) or death26.fullmatch(server_message) or death27.fullmatch(server_message) or death28.fullmatch(server_message) or death29.fullmatch(server_message) or death30.fullmatch(server_message) or death31.fullmatch(server_message) or death32.fullmatch(server_message) or death33.fullmatch(server_message) or death34.fullmatch(server_message) or death35.fullmatch(server_message) or death36.fullmatch(server_message) or death37.fullmatch(server_message) or death38.fullmatch(server_message) or death39.fullmatch(server_message):
            return True

