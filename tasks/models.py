from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):

    STATUS =(
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) #Atrela o model do usuário a essa tarefa
    created_at = models.DateTimeField(auto_now_add=True) #Sempre que o registro for criado, ele vai criar esse valor de data no banco
    updated_ate = models.DateTimeField(auto_now=True) #Sempre que a tarefa for atualizada, ele muda

    def __str__(self):
        return self.title

