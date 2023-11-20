Rockwell_hardness=float(input("enter the value of Rockwell_hardness:"))
Carbon_content=float(input("enter th value of Carbon_content:"))
Tensile_strength =float(input("enter the value of Tensile_strength:"))

if (Rockwell_hardness > 50 and Carbon_content > 0.7 and Tensile_strength > 5600 ):
    print (" this is Grade 10,  all the conditions are satisfied ")
elif (Rockwell_hardness > 50 and Carbon_content > 0.7):
    print (" this is Grade 9, Rockwell hardness and Carbon content are satisfied ")
elif (Carbon_content>0.7and Tensile_strength > 5600 ):
    print (" this is Grade 8  Carbon content and Tensile strength are satisfied ")
elif(Rockwell_hardness > 50 and Tensile_strength > 5600):
    print(" this is Grade 7,  Rockwell hardness  and Tensile strength  are satisfied ")
else:
    print(" this is Grade 0 ,non of the conditions are satisfied")