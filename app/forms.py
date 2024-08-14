from django import forms

class StudentForm(forms.Form):
    sname=forms.CharField(max_length=50)
    sage=forms.IntegerField()
    semail=forms.EmailField()
    surl=forms.URLField()
    DOB=forms.DateField()
    gender=forms.ChoiceField(choices=[('MALE','male'),('FEMALE','female')],widget=forms.RadioSelect)
    #gender=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
    subjects=forms.MultipleChoiceField(choices=[('PYTHON','python'),('SQL','sql'),('WEB TECH','web tech')],widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':5}))