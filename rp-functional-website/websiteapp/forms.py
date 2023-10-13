from django.forms import ModelForm 
from .app.models import * 
from django. contrib.auth.forms import UserCreationForm
from django. contrib.auth.models import user 

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']

class addAttendanceform(ModelForm):
    class Meta:
        model=Attendance 
        fields= "_all_" 
        
class addMarksform(ModelForm):
       class Meta:
            model=Marks
            fields="_all_"

class addNoticeform(ModelForm) :
     class Meta:
          model= Notice
          fiedls="_all_"


