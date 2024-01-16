from app.models.career import Career
from app.models.student import Student
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
        return {
            "success": True,
            "message": "Solicitud de Carrera registrado con exito",
            "code": "100"
        }
    except Exception as err:
        return {
            "success": False,
            "code": 500,
            "error": str(err)
        }


def get_all_carrer_card():
    try:
        last_items = []
        data = Career.query.all()
        for cardCarrer in data:
            itemCarrer = {
                "id": cardCarrer.id,
                "image": cardCarrer.image,
                "title": cardCarrer.title,
                "description": cardCarrer.description,
            }
            listCourses = []
            for course in cardCarrer.courses:
                itemCourse = {
                    "id": course.id,
                    "title": course.title
                }
                listCourses.append(itemCourse)
            itemCarrer['courses'] = listCourses
            queryStudents = Student.query.filter(Student.id_career == cardCarrer.id).all()
            listStudents = []
            for studen in queryStudents:
                itemStudent = {
                    "id": studen.id,
                    "name": f"{studen.name} {studen.father_last_name} {studen.mother_last_name}"
                }
                listStudents.append(itemStudent)
            itemCarrer['students'] = listStudents

            last_items.append(itemCarrer)
        return {"success": True, "code": 200, "data": last_items}
    except Exception as err:
        return {
            "success": False,
            "code": 500,
            "error": str(err)
        }


def get_all_id_name_carrer():
    try:
        last_items = []
        data = Career.query.all()
        for cardCarrer in data:
            itemCarrer = {
                "id": cardCarrer.id,
                "title": cardCarrer.title,
            }
            last_items.append(itemCarrer)
        return {"success": True, "code": 200, "data": last_items}
    except Exception as err:
        return {
            "success": False,
            "code": 500,
            "error": str(err)
        }
