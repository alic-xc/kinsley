from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from .forms import *
import os
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
import json


# # Load model
# with  open('./models/labels.json', 'r') as f:
#     labelInfo = f.read()
#
# labelInfo = json.loads(labelInfo)
# model = load_model('./models/PNP.h5')

#
# def display_img(request):
#     path='homepage/static/homepage/image/'
#     filename=os.listdir(path)
#     os.rename(os.path.join(path,filename[0]),os.path.join(path,'image.jpg'))
#
#     img = image.load_img(os.path.join(path,'image.jpg'),grayscale=True ,target_size=(180,180))
#     x = image.img_to_array(img)
#     x = x/255
#     x = x.reshape(1, 180, 180, 1 )
#     pred = model.predict(x)
#
#     if pred[0][0]<0.5:
#         predictedlabel='Normal'
#     else:
#         predictedlabel='Pneumonia'
#
#     context = {
#         'label': predictedlabel,
#         'prob': pred[0][0],
#     }
#     return render(request, 'homepage/display.html', context)
#


class LoginView(generic.FormView):
    template_name = 'account/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('dashboard')

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            messages.success(self.request, "login successful")
        else:
            messages.error(self.request, "No account found. Please check login credentials and try again")
            return super().form_invalid(form)

        return super().form_valid(form)


class DashboardView(LoginRequiredMixin, generic.ListView):
    template_name = 'account/dashboard.html'
    model = Question
    paginate_by = 20
    context_object_name = 'questions'


class DiagnosView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/diagnose.html'


class QuestionView(LoginRequiredMixin, generic.FormView):
    template_name = 'account/question.html'
    form_class = QuestionForm
    model = Question

    def get_success_url(self):

        return reverse('question')

    def form_valid(self, form):
        try:
            q = Question(**form.cleaned_data)
            q.save()
            return redirect(q.get_absolute_url())
        except Exception as err:
            messages.error(self.request, err)
            return super().form_invalid(form)


class QuestionDetailView(LoginRequiredMixin, generic.FormView):
    template_name = 'account/question_details.html'
    model = Question
    context_object_name = 'question'
    form_class = UploadForm

    def get_success_url(self):
        return reverse('question_details', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['question'] = Question.objects.get(id=self.kwargs['pk'])
        return context

    # def form_valid(self, form):
    #     xray_img = self.request.FILES['img']
    #     file_ext = str(xray_img.name).split('.')[-1]
    #     new_name = "%s.%s" % (self.request.user.username, file_ext)
    #     fs = FileSystemStorage()
    #
    #     # Delete already exist file
    #     if os.path.exists("media/images/%s" % new_name):
    #         os.remove("media/images/%s" % new_name)
    #
    #     filename = fs.save("media/images/%s" % new_name, xray_img)
    #     # Detection
    #
    #     img = image.load_img(filename, grayscale=True , target_size=(180, 180))
    #     x = image.img_to_array(img)
    #     x = x/255
    #     x = x.reshape(1, 180, 180, 1 )
    #     pred = model.predict(x)
    #     try:
    #         question_obj = Question.objects.get(pk=self.kwargs['pk'])
    #         if pred[0][0] < 0.5:
    #             question_obj.is_pneumonia_patient = False
    #         else:
    #             question_obj.is_pneumonia_patient = True
    #
    #         question_obj.xray_scan = True
    #         question_obj.pneumonia_point = pred[0][0]
    #         question_obj.save()
    #         messages.success(self.request, "Xray diagnosed successfully")
    #     except Question.DoesNotExist:
    #         messages.error(self.request, "Medical test not found")
    #         return super().form_invalid(form)
    #
    #     return super().form_valid(form)


class ReportView(LoginRequiredMixin, generic.ListView):
    template_name = 'account/report.html'
    model = Question
    context_object_name = 'questions'

