class Student:
    
   def __init__(self, name, roll_number, cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa
        
def sort_students(student_list):
        
     sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
                      
     return sorted_students 
        
students = [
        Student("Hari", "A123", 7.8),
        Student("ashwin", "A234" ,9.0),
        Student("madhu", "A234" ,4.5)
 ]
 
sorted_students = sort_students(students)

for student in sorted_students:
      print("name: {}, Roll Number: {},CGPR{}".format(student.name,student.roll_number, student.cgpa))
  