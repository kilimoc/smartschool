from django import forms

class SchoolForm(forms.Form):
    school_name=forms.CharField(label='NAME OF SCHOOL',max_length=100)
    reg_number = forms.CharField(max_length=100,label='SCHOOL REGISTRATION NUMBER')
    teacher_no = forms.IntegerField()
