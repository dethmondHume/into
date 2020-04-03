class Student(object):
    name = None
    points_lab = None
    points_exam = None
    conf = None
    list_lab = None

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.list_lab =  [ 0 for index in range(conf['lab_num'])]
        self.points_exam = 0
        self.points_lab = 0
        
    def make_lab(self, m, n=None):
        if m > conf.get('lab_max'):
            m = conf.get('lab_max')
        if n == None:
            for i in range(10):
                if self.list_lab[i] == 0:
                    self.list_lab[i] = m
                    break
        else:
            self.list_lab[n] = m
        self.points_lab = 0
        for i in self.list_lab:
            self.points_lab += i 
        return self

    def make_exam(self, m):
        if m > conf.get('exam_max'):
            self.points_exam = conf.get('exam_max')
        else:
            self.points_exam = m
        return self
    
    def is_certified(self):
        points = self.points_lab + self.points_exam
        if points > conf.get('k') * 100:
            return (points, True)
        else:
            return (points, False)


conf = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}

o = Student('first', {'exam_max' : 30, 'lab_max' : 10, 'lab_num' : 7, 'k' : 0.61 })
o.make_lab(10, 0).make_lab(10).make_lab(10).make_exam(30)
print o.is_certified()
o1 = Student('second', {'exam_max' : 30, 'lab_max' : 10, 'lab_num' : 7, 'k' : 0.61 })
o1.make_lab(10)
print o1.is_certified()
