class Student :
    def __init__(self, nom, prenom, num_etudiant, credit, level):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credit = credit
        self.__level = level
        self.__level = self.__student_eval()
        

    #I will alse add a getter to print the name of the student
    def  get_student_nom(self):
        return self.__nom
    
    def  get_student_prenom(self):
        return self.__prenom

    def add_credit(self, nombre) :   #it is a setter
        if nombre > 0 :
            self.__credit  += nombre
            #I have to call student_eval in order to update the level of the student
            self.__level = self.__student_eval()
        return self.__credit
    
    def __student_eval(self) :   #a  private method
        if self.__credit >= 90 :
            note = 'Excelent'
        elif 80 <= self.__credit < 90 :
            note = 'Très bien'
        elif 70 <= self.__credit < 80 :
            note = 'Bien'
        elif 60 <= self.__credit < 70 :
            note = 'Passable'
        elif 0 <= self.__credit < 60 :
            note = 'Insuffisant'
        return note
    
    def student_info(self) :
        return f"Les information de l'étudiant :\nNom = {self.__nom}\nPrenom = {self.__prenom}\nIdentifiant = {self.__num_etudiant}\nNiveau = {self.__level}"

    #I have to create a getter method for num_etudiant
    def get_num_etud(self) :
        return self.__num_etudiant
#create an object :
student1 = Student('Doe', 'John', '145', 0, '')
#print(f"Le nombre de {student1.get_student_nom()} {student1.get_student_prenom()} est de {student1.add_credit(30)} points")

print(f"Le nombre de {student1.get_student_nom()} {student1.get_student_prenom()} est de {student1.add_credit(145)} points")
print(student1.student_info())