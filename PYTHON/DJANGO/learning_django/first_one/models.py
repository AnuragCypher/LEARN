from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    # property decorator exampel
    @property
    def calculate_discounted_price(self):
        return f"{(50 / 100) * self.price}"


# fiels and field options
class ExampleTable(models.Model):
    f1 = models.CharField(max_length=100, null=True, unique=False)
    f2 = models.TextField(max_length=200, default="currently not available")
    f3 = models.BooleanField(null=True, choices=[(True, "Yes"), (False, "No")])


# relations
class Author(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    colloborator = models.ManyToManyField(Author, related_name="collaborator_link")

    class Meta:
        # Meta class is most commonly used to specify the uniques fields when set together, used to set indexes, to set permissions, defininig order, in whcih rows will be treated  and many more.
        # see the example from net.
        db_table = "Post_by_Authors"


class example_changing_manager_name(models.Model):

    field_1 = models.TextField(max_length=200)
    manager = models.Manager()


class Custom_Manager(models.Manager):

    def get_filtered_data(self) -> models.QuerySet:
        return self.filter(name__startswith="a")

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(name__startswith="a")


# here we are maintaining multiple managers.
class Person(models.Model):
    name = models.TextField(max_length=200, null=True)
    custom = Custom_Manager()
    objects = models.Manager()
