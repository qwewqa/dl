import adv.adv_test
from core.advbase import *
from slot.d import *

def module():
    return Veronica

class Veronica(Adv):
    a3 = ('prep','100%')
    conf = {}
    conf['slot.d'] = Shinobi()
    conf['acl'] = """
        `s1
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        `fs, seq=5 and s1.charged >= 2500
        """

    def prerun(self):
        Teambuff('last',2.28,1).on()
        self.hp = 80

    def s1_proc(self, e):
        with CrisisModifier('s1', 1.25, self.hp):
            self.dmg_make('s1', 10.84)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

