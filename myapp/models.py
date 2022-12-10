from django.db import models

# Create your models here.
class AIAnalysisLog(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    image_path = models.CharField(max_length=255,null=True)
    success = models.CharField(max_length=255,null=True)
    message = models.CharField(max_length=255,null=True)
    classes = models.IntegerField(null=True)
    confidence = models.DecimalField(max_digits=5,decimal_places=4,null=True)
    request_timestamp = models.PositiveIntegerField(null=True)
    response_timestamp = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.image_path
