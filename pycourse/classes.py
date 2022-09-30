"""
马云飞
2020118092
"""


# class Student.
# __init__ initialises four variables p_surname, p_given_name, p_id and p_course.
#
# course_count is a method to calculate the number of courses of a student.

class Student:
    def __init__(self, p_surname, p_given_name, p_id, p_course):
        self.surname = p_surname
        self.given_name = p_given_name
        self.id = p_id
        self.course = p_course
        self._course_count = 0

    @property  # '@property' changes this method to a property
    # method course_count() will find the length of self.courses and set self._course_count to the
    # length. It will then return the value of self._course_count.
    def course_count(self):
        self._course_count = len(self.course)
        return self._course_count


"""
>>> from classes import *
>>> student1 = Student('Ma','Yunfei',2020118092,['Python','Java'])
>>> student1.course_count
2
"""
