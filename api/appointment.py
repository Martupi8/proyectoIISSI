from flask import Blueprint, jsonify, request
from bll.AppointmentBLL import AppointmentBLL
from bll.BLLException import BLLException

from datetime import date, time

appointment_bll = AppointmentBLL()
appointment_api = Blueprint('appointment_api', __name__)

@appointment_api.route("/appointments", methods=["GET"])
def get_all():
    appointments = appointment_bll.get_all()
    for appointment in appointments:
        appointment["hourAppointment"] = str(appointment["hourAppointment"])
    code = 200
    body = jsonify(appointments)
    return body, code

@appointment_api.route("/appointments/<int:oid>", methods=["GET"])
def get_by_OID(oid):
    appointment = appointment_bll.get_by_OID(oid)
    appointment["hourAppointment"] = str(appointment["hourAppointment"])
    body = jsonify(appointment)
    code = 200

    if appointment is None:
        code = 404
    
    return body, code

@appointment_api.route("/appointments/students/<int:studentId>", methods=["GET"])
def get_by_studentId(studentId):
    appointments = appointment_bll.get_BY_studentId(studentId)
    for appointment in appointments:
        appointment["hourAppointment"] = str(appointment["hourAppointment"])
    body = jsonify(appointments)
    code = 200

    if appointments is None:
        code = 404
    
    return body, code
    
@appointment_api.route("/appointments/teachers/<int:teacherId>", methods=["GET"])
def get_by_teacherId(teacherId):
    appointments = appointment_bll.get_BY_teacherId(teacherId)
    for appointment in appointments:
        appointment["hourAppointment"] = str(appointment["hourAppointment"])
    body = jsonify(appointments)
    code = 200

    if appointments is None:
        code = 404
    
    return body, code

@appointment_api.route("/appointments", methods=["POST"])
def insert():
    res = None
    form = request.form

    dateAppointment = form.get("dateAppointment", default=None)
    hourAppointment = form.get("hourAppointment", default=None)
    tutorialId = form.get("tutorialId", default=None)
    studentId = form.get("studentId", default=None)

    try:
        oid = appointment_bll.insert(dateAppointment, hourAppointment, tutorialId, studentId)
        res = jsonify({'oid': oid}), 200
    except BLLException as exc:
         res = jsonify({'error': str(exc)}), 400
    
    return res

@appointment_api.route("/appointments/<int:oid>", methods=["PUT"])
def update(oid):
    res = None
    form = request.form

    dateAppointment = form.get("dateAppointment", default=None)
    hourAppointment2 = form.get("hourAppointment", default=None)
    tutorialId = form.get("tutorialId", default=None)
    studentId = form.get("studentId", default=None)
    
    try:
        new_oid = appointment_bll.update(oid, dateAppointment, hourAppointment2, tutorialId, studentId)
        res = jsonify({'oid': new_oid}), 200
    except BLLException as exc:
        res = jsonify({'error': str(exc)}), 400
    
    return res

@appointment_api.route("/appointments/<int:oid>", methods=["DELETE"])
def delete(oid):

    res = None

    try:
        delete_id = appointment_bll.delete(oid)
        res = jsonify({'oid': delete_id}), 200
    except BLLException as exc:
        res = jsonify({'error': str(exc)}), 400
    
    return res