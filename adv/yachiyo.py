import adv.adv_test
from core.advbase import *
from slot.a import *
from slot.d import *
from slot.w import *

class w530(WeaponBase):
    ele = ['water','light']
    wt = 'blade'
    att = 468


def module():
    return Yachiyo

class Yachiyo(Adv):
    a3 = ('k_paralysis', 0.2)
    conf = {}
    conf['slots.a'] = MF()+SotS()
    conf['slots.d'] = Corsaint_Phoenix()
    conf['acl'] = """
        `fs, self.fsa_charge and seq=5
        `s2
        `s1
        `s3
        """
    conf['afflict_res.paralysis'] = 0

    def prerun(self):
        self.fsa_charge = 0        

    def s1_proc(self, e):
        self.dmg_make('s1',4.32)
        self.afflics.paralysis('s1',100,0.66)
        Selfbuff('a1',0.15*self.afflics.paralysis.get(),10).on()
        self.dmg_make('s1',4.32)


    def s2_proc(self, e):
        # self.fso_dmg = self.conf.fs.dmg
        self.fso_sp = self.conf.fs.sp
        # self.conf.fs.dmg = 7.82
        self.conf.fs.sp = 200
        self.fsa_charge = 1

    def fs_proc(self, e):
        if self.fsa_charge:
            # self.conf.fs.dmg = self.fso_dmg
            self.dmg_make("o_fs_boost",6.90)
            self.conf.fs.sp = self.fso_sp
            self.fsa_charge = 0



if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

