import adv.adv_test
from core.advbase import *
import slot
from slot.d import *

def module():
    return Student_Maribelle

class Student_Maribelle(Adv):
    a1 = ('s', 0.4, 'hp100')
    a3 = ('bk',0.3)
    conf = {}
    conf['slot.d'] = Sakuya()
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2
        `fs, (s1.charged>=s1.sp-self.sp_val('fs')) or (s2.charged>=s2.sp-self.sp_val('fs'))
    """


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)

