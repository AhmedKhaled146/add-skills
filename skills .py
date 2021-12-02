skills = []
name = str(input("Enter Your Name : "))
num_of_skill = int(input("Enter The Number of Skills You Have : "))
a = 0
while a < num_of_skill:
    skill = input(f"what is Your skill {a + 1} : ")
    a += 1
    skills.append(skill)


def say(name, skills):
    print(f"Welcome {name} You Have {num_of_skill} Skills, is {skills}")


say(name, skills)
