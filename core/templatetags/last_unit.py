from django import template
from django.template import resolve_variable

register = template.Library()


@register.tag()
def last_unit(parser, token):
    return LastUnit()


class LastUnit(template.Node):
    def render(self, context):
        user = resolve_variable('user', context)
        course = resolve_variable('course', context)
        course_student = CourseStudent.objects.get(user=user, course=course)
        last_unit = course_student.resume_last_unit()
        return last_unit.lesson.slug + '#' + str(last_unit.position + 1)
