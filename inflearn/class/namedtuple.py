##### data model
##### Tuple vs. namedtuple
from math import sqrt
q1 = (2.0, 3.0)
q2 = (3.0, 5.0)

q_length = sqrt((q1[0] - q2[0]) ** 2 + (q1[1] - q2[1]) ** 2)
print(q_length)

from collections import namedtuple
Point = namedtuple('Points', 'x y')

p1 = Point(2.0, 3.0)
p2 = Point(3.0, 5.0)
p_length1 = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
p_length2 = sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
print(p_length1)
print(p_length2)

##### namedtuple types
Point1 = namedtuple('Point', 'x y')
Point2 = namedtuple('Point', ['x', 'y'])
Point3 = namedtuple('Point', 'x, y')
# Point4_1 = namedtuple('Point', 'x y x') # ValueError: Encountered duplicate field name: 'x'
# Point4_2 = namedtuple('Point', 'x y class') # ValueError: Type names and field names cannot be a keyword: 'class'
Point4 = namedtuple('Point', 'x y x class', rename = True) #  Point(x=20, y=30, _2=40, _3=50)
print(Point1, Point2, Point3, Point4)
##### unpacking
temp_dict = {'x': 75, 'y': 55}
## usage
pq1 = Point1(20, 30)
pq2 = Point2(x = 20, y = 30)
pq3 = Point3(20, y = 30)
pq4 = Point4(20, 30, 40, 50)
# qp5_1 = Point1(**temp_dict)
# qp5_2 = Point2(**temp_dict)
qp5 = Point3(**temp_dict)
print(pq1, pq2, pq3, pq4, qp5)
print(pq1.x + pq2.y)
x, y = pq2
print(x, y)

##### namedtuple method
## _make()
temp = [52, 38]
p4 = Point1._make(temp)
print(p4)
## _fields
print(pq1._fields, pq2._fields, pq3._fields)
## _asdict() == OrderedDcit
print(pq1._asdict())
print(p4._asdict())