from django.contrib import admin
from .models import Physician
from .models import Technician
from .models import Test
from .models import Patient
from .models import Sample
from .models import PerformedBy
from .models import AssignedTo
from .models import ReceivedBy

admin.site.register(Physician)
admin.site.register(Test)
admin.site.register(Technician)
admin.site.register(Patient)
admin.site.register(Sample)
admin.site.register(PerformedBy)
admin.site.register(AssignedTo)
admin.site.register(ReceivedBy)