from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.translation import gettext_lazy as _


class MenuItem(models.Model):
    """Модель элемента меню."""

    name = models.CharField(_('Название'), max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('Родительский пункт')
    )
    menu_name = models.CharField(_('Имя меню'), max_length=100)
    url = models.CharField(
        _('URL или именованный URL'),
        max_length=200,
        help_text=_(
            'Можно указать как прямой URL (/about/), так и именованный (about)'
        )
    )

    class Meta:
        verbose_name = _('Пункт меню')
        verbose_name_plural = _('Пункты меню')
        ordering = ['id']
        indexes = [
            models.Index(fields=['menu_name']),
            models.Index(fields=['parent']),
        ]

    def __str__(self):
        return f"{self.name} ({self.menu_name})"

    def get_url(self):
        """Возвращает URL, обрабатывая как именованные URL, так и прямые."""
        try:
            return reverse(self.url)
        except NoReverseMatch:
            return self.url
