from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from pages.page_choice import PageChoices
# Create your models here.


class PageModel(models.Model):
    title = models.CharField(verbose_name='Название страницы', 
                             null=True, 
                             unique=True, 
                             max_length=150
                             )
    path = models.CharField(verbose_name='Путь до страницы', 
                            choices=PageChoices,
                            default=PageChoices.HOME
                            )
    text_primary = CKEditor5Field(verbose_name='Основной блок', 
                                  config_name='extends', 
                                  blank=True, 
                                  null=True
                                  )
    text_secondary = CKEditor5Field(verbose_name='Дополнительный блок', 
                                    config_name='extends', 
                                    blank=True, 
                                    null=True
                                    )
    


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тексты для страниц"
        verbose_name_plural = "Тексты для страниц"


