from flask import Blueprint, render_template, redirect, request, abort
from services.student.student_service import StudentService
from services.student.student_model import StudentModel

student_v1 = Blueprint('student-v1', __name__, template_folder='templates', static_folder='static')


@student_v1.route('/student/create', methods=['GET', 'POST'])
def create_student():
    if request.method == 'GET':
        return render_template('/student/form.html', student=StudentModel(), post_link='/v1/student/create')
    else:
        students_service = StudentService()
        student_to_create = StudentModel(**request.form)
        students_service.insert(student_to_create)
    return redirect('/student')


@student_v1.route('/student/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    students_service = StudentService()
    if request.method == 'GET':
        students = students_service.get_by_id(id)
        if len(students) != 1:
            abort(404)
        return render_template('/student/form.html', student=students[0], post_link='/v1/student/update/'+str(id))
    else:
        student_to_update = StudentModel(**request.form)
        student_to_update.id = id
        students_service.update(student_to_update)
    return redirect('/student')
