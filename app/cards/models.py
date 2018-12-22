from django.db import models

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

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.pk} {self.contents}'
