from app.models.career import Career
from app.models.career_course import CareerCourse
from app import db


def create_career_detail(request):
    try:
        body = request
        new_transaccion = Career(
            title=body['title'],
            description=body['description'],
            image=body['image'],
            state=True
        )
        db.session.add(new_transaccion)
        db.session.flush()
        db.session.commit()
        return create_career_courses(new_transaccion.id, body['courses'])
    except Exception as err:
        return ({
            "result": False,
            "status": 500,
            "error": str(err)
        }, 500)


def create_career_courses(id, courses):
    try:
        for course in courses:
            new_transaccion = CareerCourse(
                id_career=id,
                id_course=course['id']
            )
            db.session.add(new_transaccion)
            db.session.flush()
            db.session.commit()
        return ({
            "success": True,
            "message": "Solicitud de Carrera registrado con exito",
            "code": "100"
        }, 200)
    except Exception as err:
        return ({
            "result": False,
            "status": 500,
            "error": str(err)
        }, 500)
