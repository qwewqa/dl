import adv.adv_test
from core.advbase import *
from core.advbase import *
from slot.a import *

def module():
    return Naveed

class Naveed(Adv):
    a1 = ('a',0.08,'hit15')
    a3 = ('prep','100%')
    conf = {}
    conf['acl'] = """
        `s3, not self.s3_buff
        `s2, self.s1level < 5
        `s1
        `fs, seq=3 and cancel
        """
    conf['slot.a'] = TSO()+Primal_Crisis()
            
    def prerun(self):
        self.s1level = 0

    def s1_proc(self, e):
        for _ in range(self.s1level):
            for _ in range(3):
                self.dmg_make("o_s1_boost",0.7,'s')
                self.hits += 1

    def s2_proc(self, e):
        self.s1level += 1
        if self.s1level >= 5:
            self.s1level = 5
        adv.Event('defchain')()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

