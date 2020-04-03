class Student(object):
    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.exam = 0
        self.labs = map(float, [i for i in '0' * self.conf['lab_num']])
    def make_lab(self, m, n = None):
        if n < self.conf['lab_num']:
            if m > self.conf['lab_max']:
                m = self.conf['lab_max']
            if n == None:
                for i in range(0, len(self.labs)):
                    if self.labs[i] == 0.0:
                        n = i
                        self.labs[n] = m
                        return self 

            self.labs = map(float, self.labs)
            if self.labs[n] != 0.0:
                    if type(self.labs[n]) == str:
                        return self
                    self.labs[n] = str(m)
                    return self 
            elif self.labs[n] == 0.0:   
                self.labs[n] = m
                return self
    def make_exam(self, m):
        if m > self.conf['exam_max']:
            m = self.conf['exam_max']
        self.exam = m
        return self
    def is_certified(self):
        self.labs = map(float, self.labs)
        summa = sum(self.labs) + self.exam 
        m_k = summa / (self.conf['lab_num'] * self.conf['lab_max'] + self.conf['exam_max'])
        if m_k >= self.conf['k']:
            ans = True
        else:
            ans = False
        return (summa, ans)

conf3 = {'exam_max': 10,'lab_max': 1,'lab_num': 90,'k': 0.5,}
o6 = Student('Oleg', conf3)
for i in range(51): o6.make_lab(1)
print o6.is_certified()
