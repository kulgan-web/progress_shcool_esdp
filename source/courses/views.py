from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from courses.models import Course, Lesson
from pages.models import PageModel



class IndexPageView(TemplateView):
    template_name = 'courses/index.html'


class AboutUsView(ListView):
    model = get_user_model()
    template_name = 'courses/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = get_user_model().objects.all().filter(role='teacher')
        try:
            context['page'] = PageModel.objects.get(path=self.request.path)
        except:
            pass
        return context


class CoursesView(ListView):
    model = Course
    template_name = 'courses/courses_view.html'
    context_object_name = 'courses'

class LessonsView(ListView):
    model = Lesson
    template_name = 'courses/lesson_view.html'
    context_object_name = 'lessons'
    paginate_by = 16
    paginate_orphans = 3
    ordering = ('-datetime',)

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('courses', None)
        if search_query:
                queryset = queryset.filter(course__course_name__iexact=search_query)
        else:
            queryset = queryset.none()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["courses"] = Course.objects.all()
        return context