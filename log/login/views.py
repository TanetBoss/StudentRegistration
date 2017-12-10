from django.contrib.auth import login, authenticate
from django.views.generic import View
from login.forms import UserForm
from django.shortcuts import render, redirect


class UserFormView(View):
    form_class = UserForm
    template_name = 'signup.html'
    # display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('home')
        return render(request,self.template_name,{'form':form})
