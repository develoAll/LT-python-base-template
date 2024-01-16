from app.models.course import Course


def get_all_course():
    last_item = []
    data = Course.query.all()
    complain_json = list(
        map(
            lambda item: {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "image": item.image
            },
            data,
        )
    )
    if not complain_json:
        last_item = complain_json
    else:
        last_item = complain_json
    return {"success": True, "code": 200, "data": last_item}
