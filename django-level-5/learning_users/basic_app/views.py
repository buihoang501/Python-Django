from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered =False
    if request.method == 'POST':
        #get form values type from user
        user_form = UserForm(data= request.POST)
        profile_form = UserProfileInfoForm(data= request.POST)

        #check user from and profile form value is valid
        if user_form.is_valid() and profile_form.is_valid():
            #create user in database
            user = user_form.save()
            #hasing password
            user.set_password(user.password)
            #update user after hasing password to database
            user.save()

            # Don't save to the database yet
            profile= profile_form.save(commit=False)
            # So One To One Relationship =
            profile.user = user

            #upload picture
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            #save to database
            profile.save()

            #Register successfully
            registered= True
        else:
        #Display errors
            print(user_form.errors, profile_form.errors)
    else:
        #get form blank (form before an user types values) (Not HTTP POST request)
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'basic_app/registration.html',
                      {'user_form':user_form,'profile_form':profile_form,'registered':registered})