#!/usr/bin/env python3

# one whitespace in front of "class info" :)
classinfo = {'all': [
         {'name': 'Cat',
          'skill level': 'amazing',
          'spirit animal': 'Chinchilla',
          'super power': 'Body Part Substitution'},
         {'name': 'Chris',
          'skill level': 'astonishing',
          'spirit animal': 'Chipmunk',
          'super power': 'Camouflage'},
         {'name': 'Dao',
          'skill level': 'astounding',
          'spirit animal': 'Clam',
          'super power': 'Bone Manipulation'},
         {'name': 'David',
          'skill level': 'awe-inspiring',
          'spirit animal': 'Clownfish',
          'super power': 'Claw Retraction'},
         {'name': 'Henwin',
          'skill level': 'breathtaking',
          'spirit animal': 'Cobra',
          'super power': 'Deflection'},
         {'name': 'Herman',
          'skill level': 'imposing',
          'spirit animal': 'Condor',
          'super power': 'Fang Retraction'},
         {'name': 'Jose',
          'skill level': 'inspiring',
          'spirit animal': 'Constrictor',
          'super power': 'Helicopter Propulsion'},
         {'name': 'Justin',
          'skill level': 'magnificent',
          'spirit animal': 'Coral',
          'super power': 'Invisibility'},
         {'name': 'Kris',
          'skill level': 'majestic',
          'spirit animal': 'Cougar',
          'super power': 'Immobility'},
         {'name': 'Mannie',
          'skill level': 'miraculous',
          'spirit animal': 'Coyote',
          'super power': 'Immutability'},
         {'name': 'Marcos',
          'skill level': 'spectacular',
          'spirit animal': 'Crab',
          'super power': 'Invulnerability'},
         {'name': 'Marshall',
          'skill level': 'staggering',
          'spirit animal': 'Crane',
          'super power': 'Jet Propulsion'},
         {'name': 'Michael',
          'skill level': 'stunning',
          'spirit animal': 'Crawdad',
          'super power': 'Invulnerability'},
         {'name': 'Mike',
          'skill level': 'stupefying',
          'spirit animal': 'Crocodile',
          'super power': 'Muscle Manipulation'},
         {'name': 'Nikko',
          'skill level': 'sublime',
          'spirit animal': 'Crow',
          'super power': 'Needle Projection'},
         {'name': 'Phil',
          'skill level': 'wonderful',
          'spirit animal': 'Cuckoo',
          'super power': 'Prehensile Tongue'},
         {'name': 'Ryan',
          'skill level': 'wondrous',
          'spirit animal': 'Cicada',
          'super power': 'Regenerative Healing Factor'},
         {'name': 'Sachin',
          'skill level': 'affecting',
          'spirit animal': 'Damselfly',
          'super power': 'Replication'},
         {'name': 'Samekh',
          'skill level': 'arresting',
          'spirit animal': 'Deer',
          'super power': 'Self-Detonation'},
         {'name': 'Will',
          'skill level': 'august',
          'spirit animal': 'Dingo',
          'super power': 'Super Strength'}]}

print(len(classinfo["all"]))
print(classinfo["all"][18]["name"])

samekh = classinfo["all"][18]

def powerSentence():
    print(f"my name is {samekh['name']} and my power is {samekh['super power']} ")
                                                                        # missing '

def showEveryOne():
    for x in classinfo["all"]:
        print(f"{x['name']}, an {x['skill level']} {x['spirit animal']} of a programmer, possesses a {x['super power']} factor for moonlighting as a superhero!")

powerSentence()
showEveryOne()