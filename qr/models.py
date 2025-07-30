from django.db import models


class QR(models.Model):
    url = models.URLField()
    image = models.ImageField(upload_to='qr_codes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
