import adv.adv_test
from core.advbase import *

def module():
    return Fritz

class Fritz(Adv):
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    def prerun(self):
        self.stance = 0
        self.s2fscharge = 0

    def s2_proc(self, e):
        self.s2fscharge = 3

    def fs_proc(self, e):
        if self.s2fscharge > 0:
            self.s2fscharge -= 1
            self.dmg_make("o_fs_boost",0.57*3+0.29)



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
