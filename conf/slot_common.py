#unused now
import slot
from slot.a import *
import slot.w

def set(slots):
    ele = slots.c.ele
    wt = slots.c.wt
    stars = slots.c.stars
    name = slots.c.name


    if ele == 'flame':
        slots.d = slot.d.flame.Cerberus()
    elif ele == 'water':
        slots.d = slot.d.water.Leviathan()
    elif ele == 'wind':
        slots.d = slot.d.wind.Zephyr()
    elif ele == 'light':
        slots.d = slot.d.light.Cupid()
    elif ele == 'shadow':
        slots.d = slot.d.shadow.Marishiten()


    slots.a = RR()+CE()

    if wt == 'sword':
        slots.a = RR()+FP()
    if wt == 'blade':
        slots.a = RR()+CE()
    if wt == 'dagger':
        slots.a = RR()+FG()
    if wt == 'axe':
        #slots.a = RR()+KFM()
        slots.a = KFM()+Flower_in_the_Fray()
    if wt == 'lance':
        slots.a = RR()+CE()
        #slots.a = LC()+Dragon_and_Tamer()
    if wt == 'wand':
        slots.a = RR()+CE()
    if wt == 'bow':
        slots.a = RR()+FG()

    typeweapon = getattr(slot.w, wt)
    weapon = getattr(typeweapon, ele)

    slots.w = weapon()

    return
