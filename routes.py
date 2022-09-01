from ast import Return
from app import application

@application.route('/')
def root():
    return "XYZ"

@application.route('/colleges')
def college_list(): 
    return "XYZ" 

@application.route('/colleges/<int:id>')
def root(id):
    return "XYZ"       

