import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import time
import os
import sys

currentdir = os.path.realpath(__file__)
downloadsdir = currentdir[:-len(__file__)]

parameters = {
    "Support": 
        'You want to help people directly, either individually or in groups.',
    "Availability": 
        'You attempt to meet with students regularly, setting aside adequate and comfortable time for students.',
    "Interest and Enthusiasm": 
        'You are interested and enthusiastic about your own and the student\'s work.',
    "Knowledge and Expertise in the Field": 
        'You feel some mastery in your field and use your knowledge to understand and demonstrate how the student\'s research topic fits within the wider field.',
    "Interest in the Student's Career":
        'You provide ample support for establishing the student\'s career in various ways.',
    "Good Communication":
        'You have good listening skills, communicate in an honest and fair manner about issues that arise, and make expectations clear.',
    "Constructive Feedback":
        'You provide feedback and criticism of student\'s work that is constructive and prompt.',
    "Provides Direction and Structure":
        'You provide an appropriate amount of direction and structure to the student\'s research project.',
    "Approachabillity and Rapport":
        'You are approachable and work to establish a good rapport with your students',
    }

for key in parameters:
    print("\n\n\nPLEASE ENTER HOW MUCH YOU AGREE WITH THESE STATEMENTS (IN NUMBER):\n")
    print("-----------------------------------------------------------------------------------")
    print(key, ":\n", parameters[key])
    print("-----------------------------------------------------------------------------------")
    
    num_value = input("\nVery High(1), High(2), Moderate(3), Not at all(4)\n")

print ("\n\nCALCULATING RESULTS\n\n")
toolbar_width = 80
for i in range(toolbar_width):
    time.sleep(0.1)
    sys.stdout.write("*")
    sys.stdout.flush()

sys.stdout.write("\n")

img=mpimg.imread('output/results1.png')
imgplot = plt.imshow(img)
plt.axis('off')
plt.show()
