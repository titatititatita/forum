from django.db import models


class Thread(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(default='Forgot to write smth')

    def __str__(self):
        return self.text
