# from GGDC.views import faculty
from django.db import models
from django.utils.html import format_html
import datetime
from dateutil.relativedelta import relativedelta

# from datetime import year

# Create your models here.



class Firstyearform(models.Model):
    religion_choices = (
        ('Islam','Islam'),
        ('Hindu', 'Hindu'),
        ('Christen', 'Christen'),
        ('Other', 'Other')
    )
    mrtlstatus_choices = (
        ('Single','Single'),
        ('Married', 'Married')
    )
    status_choices = (
        ('Annual','Annual'),
        ('Supply', 'supply')
    )
    grade_choices = (
        ('A','A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    board_choices = (
        ('BISE Sukkur Board','BISE Sukkur Board'),
        ('Panjab Board', 'Panjab Board'),
        ('Agha Khan Board', 'Agha Khan Board'),
        ('Cambridge', 'Cambridge')
    )
    sid = models.AutoField(primary_key=True)
    picture = models.ImageField(upload_to = 'std_doc/')
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    religion = models.CharField(max_length=50, blank=False, null=False, choices= religion_choices)
    nationality= models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50, blank=False, null=False, choices= mrtlstatus_choices)
    DOB = models.DateField()
    email = models.EmailField(max_length=254)
    permanent_address = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    talukka= models.CharField(max_length=100)
    postal_address = models.IntegerField()
    contact_number = models.IntegerField()
    guardian_cnumber = models.IntegerField()
    guardian_profession = models.CharField(max_length=100)
    family_members = models.IntegerField()
    Guardian_mlyincome = models.IntegerField()
    native_place = models.CharField(max_length=100)
    cnic_no = models.IntegerField()
    cnic_img = models.ImageField(upload_to = 'std_doc/')
    vaccination_img = models.ImageField(upload_to = 'std_doc/')
    slip_img = models.ImageField(upload_to = 'std_doc/')
    ssc_max_marks = models.IntegerField()
    ssc_obt_marks = models.IntegerField()
    ssc_grade = models.CharField(max_length=50, blank=False, null=False, choices= grade_choices)
    ssc_passing_year = models.IntegerField()
    ssc_seat_number = models.IntegerField()
    ssc_status = models.CharField(max_length=50, blank=False, null=False, choices= status_choices)
    ssc_board = models.CharField(max_length=50, blank=False, null=False, choices= board_choices)
    hsc1_max_marks = models.IntegerField(blank=True, null=True)
    hsc1_obt_marks = models.IntegerField(blank=True, null=True)
    hsc1_grade = models.CharField(max_length=50, blank=True, null=True, choices= grade_choices)
    hsc1_passing_year = models.IntegerField(blank=True, null=True)
    hsc1_seat_number = models.IntegerField(blank=True, null=True)
    hsc1_status = models.CharField(max_length=50, blank=True, null=True, choices= status_choices)
    hsc1_board = models.CharField(max_length=50, blank=True, null=True, choices= board_choices)
    def Picture_tag(self):
        return format_html('<img src= "/media/{}" style="width:40px; height:40px; border-radius:50%;" />'.format(self.picture))
#     def roll_number():
#         return
#     submission_date = models.DateField()
    
    
    def __str__(self):
        return self.name


    

class Faculty(models.Model):
    hod_choices = (
        ('HOD','HOD'),
        ('Staff', 'Staff')
    )
    department_choices = (
        ('BBA','BBA'),
        ('Botany','Botany'),
        ('BSIT','BSIT'),
        ('Commerce','Commerce'),
        ('Chemistry', 'Chemistry'),
        ('Economics','Economics'),
        ('English', 'English'),
        ('Home Economics','Home Economics'),
        ('Islamiat','Islamiat'),
        ('Mathematics', 'Mathematics'),
        ('Pakistan Studies','Pakistan Studies'),
        ('Physical Education','Physical Education'),
        ('Physics', 'Physics'),
        ('Sindhi','Sindhi'),
        ('Urdu', 'Urdu'),
        ('Zoology', 'Zoology')
    )
    designation_choices = (
        ('Associate professor', 'Associate professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer'),
        ('Visiting', 'Visiting'),
        ('Lab Assistant', 'Lab Assistant'),
        )
    status_choices = (
        ('Active', 'Active'),
        ('Retired', 'Retired'),
        ('Transferred', 'Transferred')
    )
    fid = models.AutoField(primary_key=True)
    picture = models.ImageField(upload_to = 'faculty/')
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    joining_date = models.DateField()
    leaving_date = models.DateField(blank=True, null=True)
    hod= models.CharField(max_length=20, blank=True, null=True, choices=hod_choices)
    department = models.CharField(max_length=50, blank=False, null=False, choices=department_choices)
    designation = models.CharField(max_length=50, blank=False, null=False, choices=designation_choices)
    status = models.CharField(max_length=30, blank=False, null=False, choices=status_choices)
    def Picture_tag(self):
        return format_html('<img src= "/media/{}" style="width:40px; height:40px; border-radius:50%;" />'.format(self.picture))
    def Experience(self):
        if self.status=='Active':
            current_date = datetime.date.today()
            count = relativedelta (current_date, self.joining_date)
            if count.years < 1:
                return 'New'
            else:
                return str(count.years) + ' years'
        else:
            count = relativedelta(self.leaving_date, self.joining_date)
            return str(count.years) + ' years'
    def __str__ (self):
        return self.name
        

class Principal(models.Model):
    status_choices = (
        ('Current', 'Current'),
        ('Former', 'Former')
    )
    pid = models.AutoField(primary_key=True)
    picture = models.ImageField(upload_to = 'principal/')
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    joining_date = models.DateField()
    leaving_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=False, null=False, choices=status_choices)
    def Picture_tag(self):
        return format_html('<img src= "/media/{}" style="width:40px; height:40px; border-radius:50%;" />'.format(self.picture))
    def duration(self):
        if self.status=='Former':
            count = relativedelta(self.leaving_date, self.joining_date)
            return str(count.years) + ' years'
        else:
            return '-'

    def __str__ (self):
        return self.name
        



class Books(models.Model):
    program_choices = (
        ('BSIT', 'BSIT'),
        ('BBA', 'BBA')
    )
    admin_upload = models.FileField(upload_to='books/')
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=50, blank=False, null=False, choices=program_choices)

    def __str__ (self):
        return self.title


class News(models.Model):
    Nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    dec = models.CharField(max_length=500)
    date_uploaded = models.DateField()

    def __str__ (self):
        return self.title

class Gallery(models.Model):
    gid = models.AutoField(primary_key=True)
    picture = models.ImageField(upload_to = 'gallery/')
    title = models.CharField(max_length=100)
    date = models.DateField()
    date_uploaded = models.DateField()


    def Picture_tag(self):
        return format_html('<img src= "/media/{}" style="width:40px; height:40px; border-radius:50%;" />'.format(self.picture))

    def __str__ (self):
        return self.title


class NewsBanner(models.Model):
    bid= models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    picture = models.ImageField(upload_to = 'Newsbanner/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def Picture_tag(self):
        return format_html('<img src= "/media/{}" style="width:40px; height:40px; border-radius:50%;" />'.format(self.picture))

    def __str__ (self):
        return self.title



