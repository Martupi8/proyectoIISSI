from flask import Blueprint, jsonify, request
from bll.StudentBLL import StudentBLL
from bll.BLLException import BLLException

student_bll = StudentBLL()
student_api = Blueprint('student_api', __name__)

@student_api.route("/students", methods=["GET"])
def get_all():
    students = student_bll.get_all()
    code = 200
    body = jsonify(students)
    return body, code

@student_api.route("/students/<int:oid>", methods=["GET"])
def get_by_OID(oid):
    student = student_bll.get_by_OID(oid)
    body = jsonify(student)
    code = 200

    if student is None:
        code = 404
    
    return body, code

@student_api.route("/students", methods=["POST"])
def insert():
    res = None
    form = request.form

    accessMethod = form.get("accessMethod", default = None)
    dniSt = form.get("dniSt", default = None)
    firstNameSt = form.get("firstNameSt", default = None)
    surnameSt = form.get("surnameSt", default = None)
    birthDateSt = form.get("birthDateSt", default = None)
    emailSt = form.get("emailSt", default = None)

    try:
        oid = student_bll.insert(accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt)
        res = jsonify({'oid': oid}), 200
    except BLLException as exc:
        res = jsonify({'error': str(exc)}), 400

    return res

@student_api.route("/students/<int:oid>", methods=["PUT"])
def update(oid):
    res = None
    form = request.form

    accessMethod = form.get("accessMethod", default = None)
    dniSt = form.get("dniSt", default = None)
    firstNameSt = form.get("firstNameSt", default = None)
    surnameSt = form.get("surnameSt", default = None)
    birthDateSt = form.get("birthDateSt", default = None)
    emailSt = form.get("emailSt", default = None)

    try:
        modified_id = student_bll.update(oid, accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt)
        res = jsonify({'oid': modified_id}), 200
    except BLLException as exc:
        res = jsonify({'error': str(exc)}), 400

    return res

@student_api.route("/students/<int:oid>", methods=["DELETE"])
def delete(oid):
    res = None

    try:
        delete_id = student_bll.delete(oid)
        res = jsonify({'oid': delete_id}), 200
    except BLLException as exc:
        res = jsonify({'error': str(exc)}), 400
    
    return res