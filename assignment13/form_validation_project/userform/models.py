from django.db import models


class UserSubmission(models.Model):
    # CharField ნაგულისხმევად არის blank=False, რაც ნიშნავს, რომ ველი სავალდებულოა ფორმაში. შესაბამისად, სახელის ველი უკვე Required-ია.
    username = models.CharField(max_length=40, verbose_name='username')
    # EmailField ავტომატურად აკეთებს ვალიდაციას, ველი შეიცავს თუ არა ვალიდურ იმეილს (RFC სტანდარტით). თუ მომხმარებელი შეიყვანს რაიმე არავალიდურს, Django თვითონ აჩვენებს შეცდომას.
    email = models.EmailField()

    class Meta:
        verbose_name = 'User Submission'
        verbose_name_plural = 'User Submission'

    def __str__(self):
        return f'{self.username} {self.email}'


