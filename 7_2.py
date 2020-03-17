class Student:
    name = None
    points_lab = None
    points_exam = None

    def __init__(self, name, conf = {'exam_max': 30,
                                    'lab_max':   7,
                                    'lab_num':  10,
                                    'k':      0.61, }):
        self.name = name
        
    def make_lab(self, m, n):#TODO d.get(key, default)
        list_lab = [0] * 10
        if m > self.conf.get('lab_max'):
            m = 7
            
        self.points_lab = 
        return self

    def make_exam(self, m):
        if m > 30:
            self.points_exam = 30
        else:
            self.points_exam = m
        return self
    
    def is_certified(self):
        points = self.points_lab + self.points_exam
        if points > 61.0:
            return (points, True)
        else:
            return (points, False)
