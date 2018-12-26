from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

__all___ = (
    'Card',
)


class Card(models.Model):
    contents = models.TextField(
        verbose_name="Card's content",
        help_text="Compose card"
    )
    created_date = models.DateField(
        verbose_name='Created date',
        auto_now_add=True,
    )
    modified_date = models.DateField(
        verbose_name='Modified date',
        auto_now=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    is_checked = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.pk} {self.contents}'
