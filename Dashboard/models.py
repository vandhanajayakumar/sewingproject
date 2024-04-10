from django.db import models

class MachineData(models.Model):
    MACHINEID = models.CharField(max_length=255)
    DATE = models.DateTimeField()
    OPERATORID = models.CharField(max_length=255)
    STARTTIME = models.TimeField()
    ENDTIME = models.TimeField()
    MODE = models.CharField(max_length=255)
    RAWSTITCHCOUNT = models.IntegerField()
    INLSTITCHCOUNT = models.IntegerField()
    INLRUNTIME = models.IntegerField()
    INLSTOPTIME = models.IntegerField()
    PICKDISPOSETIME = models.IntegerField()
    MANUALSTITCHESPERPIECE = models.IntegerField()
    MANUALPIECECOUNT = models.IntegerField()
    AUTOSTITCHESPERPIECE = models.IntegerField()
    AUTOPIECECOUNT = models.IntegerField()
    CUTTERCOUNT = models.IntegerField()
    DUMMYDATA1 = models.CharField(max_length=255)
    DUMMYDATA2 = models.CharField(max_length=255)

    def __str__(self):
      return f'Machine Data ID: {self.id}'
