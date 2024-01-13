from app.models.student import Student
from app import db


def get_by_course():
    last_item = []
    data = Student.query.all()
    complain_json = list(
        map(
            lambda item: {
                "id": item.id,
                "name": item.name,
                "secondName": item.second_name,
                "motherLastName": item.mother_last_name,
                "fatherLastName": item.father_last_name,
                "nickname": item.nick_name,
                "edad": item.edad,
                "codigo": item.codigo,
                "birthdate": item.birthdate,
                "photo": item.photo,
                "sex": item.sex,
                "mail": item.mail,
                "createdAt": item.created_at,
            },
            data,
        )
    )
    if not complain_json:
        last_item = complain_json
    else:
        last_item = complain_json
    return {"status": 200, "data": last_item}


def create_student(request):
    try:
        body = request
        if not validStudent(body['codigo']):
            new_transaccion = Student(
                name=body['name'],
                second_name=body['secondName'],
                mother_last_name=body['motherLastName'],
                father_last_name=body['fatherLastName'],
                nick_name=body['nickname'],
                edad=body['edad'],
                codigo=body['codigo'],
                birthdate=body['birthdate'],
                photo=body['photo'],
                sex=body['sex'],
                mail=body['mail']
            )
            db.session.add(new_transaccion)
            db.session.flush()
            db.session.commit()
            return ({
                "success": True,
                "message": "Solicitud registrado con exito",
                "code": "100"
            }, 200)
        else:
            return ({
                "success": False,
                "message": "El estudiante ya se encuentra registrado",
                "code": "100"
            }, 400)
    except Exception as err:
        return ({
            "result": False,
            "status": 500,
            "error": str(err)
        }, 500)


def validStudent(codigo):
    student = Student.query.filter(
        Student.codigo == codigo
    ).first()
    if student:
        return True
    else:
        return False
