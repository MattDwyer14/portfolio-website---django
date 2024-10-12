from django.db import models

class contactMessage(models.Model):
    type_of_message = [
        ('general', 'General Enquiry'),
        ('feedback', 'Feedback'),
        ('permanent', 'Hire Me!'),
        ('contact', 'Contract Work Oppurtunity'),
        ('tutoring', 'Tutoring')
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    reason = models.CharField(max_length=100, choices=type_of_message)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class HomePageContent(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title