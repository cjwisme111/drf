from django.db import models
from django.db.models.functions import Lower

# V2

class BaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Book(BaseModel):

    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to="img",default="img/default.jpg")
    publish = models.ForeignKey("Publish",
                                related_name="books",
                                on_delete=models.DO_NOTHING)

    @property
    def publish_name(self):
        return self.publish.name

    authors = models.ManyToManyField("Author",
                                     related_name="books")

    @property
    def author_list(self):
        # return self.authors.values("name",mobile = Lower("detail__work_phone"))
        return self.authors.values("name","detail__work_phone")

    class Meta:
        db_table = "tb_book"
        verbose_name = "书籍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Publish(BaseModel):

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = "tb_publish"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Author(BaseModel):

    name = models.CharField(max_length=30)
    age = models.SmallIntegerField()

    class Meta:
        db_table = "tb_author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AuthorDetail(BaseModel):

    work_phone = models.CharField(max_length=11)
    author = models.OneToOneField("Author",
                                  on_delete=models.CASCADE,
                                  related_name="detail")

    class Meta:
        db_table = "tb_author_detail"
        verbose_name = "作者详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author.name



class Car(models.Model):

    name = models.CharField(max_length=30,null=True, verbose_name="名称")
    price = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="价格")
    brand = models.CharField(max_length=20, verbose_name="品牌")

    class Meta:
        db_table = "tb_car"
        verbose_name = "汽车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name