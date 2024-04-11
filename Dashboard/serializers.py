from rest_framework import serializers
from .models import MachineData

class MachineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineData
        fields = ['id', 'MACHINEID', 'DATE', 'OPERATORID', 'STARTTIME', 'ENDTIME', 
                  'MODE', 'RAWSTITCHCOUNT', 'INLSTITCHCOUNT', 'INLRUNTIME', 
                  'INLSTOPTIME', 'PICKDISPOSETIME', 'MANUALSTITCHESPERPIECE', 
                  'MANUALPIECECOUNT', 'AUTOSTITCHESPERPIECE', 'AUTOPIECECOUNT', 
                  'CUTTERCOUNT', 'DUMMYDATA1', 'DUMMYDATA2']
