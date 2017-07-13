from django.db import models

class Physician(models.Model):
    physicianID = models.CharField("Doctor ID", db_column='doctorID', primary_key=True, max_length=7)  # Field name made lowercase.
    physicianLastName = models.CharField("Doctor Last Name", db_column='doctorLastName', max_length=30)  # Field name made lowercase.
    physicianFirstName = models.CharField("Doctor First Name", db_column='doctorFirstName', max_length=30)  # Field name made lowercase.
    doctorspec = models.CharField("Doctor Specialization", db_column='doctorSpec', max_length=30)  # Field name made lowercase.
    physicianPhone = models.CharField(max_length=10, db_column='doctorPhone')
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    username = models.CharField("Username", unique=True, max_length=20)
    pPassword = models.CharField("Password", db_column='password', max_length=20)

    class Meta:
        managed = False
        db_table = 'Doctor'

class Technician(models.Model):
    technicianID = models.CharField(max_length=5, primary_key=True)
    technicianName = models.CharField(max_length=30)
    schedule = models.CharField(max_length=10)
    tPassword = models.CharField(max_length=20)

class Test(models.Model):
    testID = models.CharField(max_length=10, primary_key=True)
    testRuns = models.IntegerField()
    kindsOfTests = models.CharField(max_length=100)
    testSchedule = models.TimeField(default='00:00:00')
    testResult = models.CharField(max_length=30, default='Normal')
    equipmentNeeded = models.CharField(max_length=200, default='e')

class Patient(models.Model):
    patientID = models.CharField("Patient ID", db_column='patientID', primary_key=True, null=False, max_length=10)
    patientname = models.CharField("Patient Name", db_column='patientName', null=False, max_length=30)
    username = models.CharField("User Name", unique=True, null=False, max_length=20)
    password = models.CharField("Password", null=False, max_length=20)
    gender = models.CharField("Gender", null=False, max_length=1)
    patientactive = models.BooleanField("Patient Active", db_column='patientActive', null=False, default=True)
    email = models.CharField("Email Address", null=False, max_length=30)
    phone = models.CharField("Phone", null=False, max_length=10)
    address = models.CharField("Address Line", null=False, max_length=100)
    city = models.CharField("City", null=False, max_length=30)
    state = models.CharField("State", null=False, max_length=2)
    zip = models.CharField("Zip Code", null=False, max_length=5)
    insprovider = models.CharField("Insurance Provider", db_column='insProvider', max_length=100)
    insdeductible = models.DecimalField("Insurance Deductible", db_column='insDeductible', max_digits=6, decimal_places=2)
    inscopay = models.DecimalField("Insurance Copay", db_column='insCopay', max_digits=3, decimal_places=2)
    inspolicyno = models.CharField("Insurance Policy No", db_column='insPolicyNo', max_length=10)
    insphone = models.CharField("Insurance Phone Number", db_column='insPhone', max_length=10)

    class Meta:
        managed = False
        db_table = 'Patient'

class Sample(models.Model):
    sampleID = models.CharField(max_length=10, primary_key=True)
    sampleDisposition = models.CharField(max_length=20)
    sampleCategory = models.CharField(max_length=20)
    dateReceived = models.DateField()
    dateTestDone = models.DateField()
    patientID = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, db_constraint=False)
    physicianID = models.ForeignKey(Physician, db_column='doctorID_id', on_delete=models.DO_NOTHING, db_constraint=False)

    class Meta:
        managed = False
        db_table = 'dashboard_sample'

class PerformedBy(models.Model):
    technicianID = models.ForeignKey(Technician, on_delete=models.DO_NOTHING, db_constraint=False)
    testID = models.ForeignKey(Test, on_delete=models.DO_NOTHING, db_constraint=False)

class AssignedTo(models.Model):
    sampleID = models.ForeignKey(Sample, on_delete=models.DO_NOTHING, db_constraint=False)
    testID = models.ForeignKey(Test, on_delete= models.DO_NOTHING, db_constraint=False)

class ReceivedBy(models.Model):
    sampleID = models.ForeignKey(Sample, on_delete=models.DO_NOTHING, db_constraint=False)
    technicianID = models.ForeignKey(Technician, on_delete=models.DO_NOTHING, db_constraint=False)