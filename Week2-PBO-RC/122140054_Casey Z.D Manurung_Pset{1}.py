import random

class Father:
    def __init__(self):
        self.allele_type = input("Enter Father's allele type: ").upper()

class Mother:
    def __init__(self):
        self.allele_type = input("Enter Mother's allele type: ").upper()

class Child(Father, Mother):
    def __init__(self, father, mother):
        Father.__init__(self)
        Mother.__init__(self)
        self.father_allele = father.allele_type
        self.mother_allele = mother.allele_type
        self.child_blood_type = self.calculate_child_blood_type()

    def calculate_child_blood_type(self):
        father_allele = random.choice([self.father_allele[0], self.father_allele[1]])
        mother_allele = random.choice([self.mother_allele[0], self.mother_allele[1]])

        child_allele = random.choice([father_allele, mother_allele])

        if child_allele == 'O':
            return 'O'
        elif child_allele == 'A' and ('A' in self.father_allele or 'A' in self.mother_allele):
            return 'A'
        elif child_allele == 'B' and ('B' in self.father_allele or 'B' in self.mother_allele):
            return 'B'
        elif child_allele == 'AB' and (('A' in self.father_allele and 'B' in self.mother_allele) or ('B' in self.father_allele and 'A' in self.mother_allele)):
            return 'AB'
        else:
            return 'O'

    def display_child_blood_type(self):
        print("Father's Allele: ", self.father_allele)
        print("Mother's Allele: ", self.mother_allele)
        print("Child's Allele: ", self.child_blood_type)
        print("Child's Blood Type: ", self.calculate_child_blood_type())

#contoh penggunaan 
father = Father()
mother = Mother()
child = Child(father, mother)

child.display_child_blood_type()
