from flask_smorest import Blueprint

from .cours_service import CoursService
from .dto.response import CourseResponse

cours = Blueprint('cours', 'cours', url_prefix='/api/cours', description='Operations on courses')

cours_service = CoursService()

@cours.route('/')
@cours.response(status_code=200, schema=CourseResponse(many=True))
def get_all():
    return cours_service.get_all_courses()