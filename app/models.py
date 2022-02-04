from django.db import models

class LinkTree(models.Model):
    tree_title = models.CharField(max_length=50)
    tree_description = models.TextField()

    COLORS = [
        ("AQ", "aqua"),
        ("BL", "blue"),
        ("BR", "brown"),
        ("GO", "gold"),
        ("GE", "green"),
        ("OR", "orange"),
        ("PI", "pink"),
        ("PU", "purple"),
        ("RE", "red"),
        ("VI", "violet"),
    ]
    tree_color = models.CharField(max_length=30, choices=COLORS, default="BL")

    def __str__(self):
        return self.tree_title

class Links(models.Model):
    link_title = models.CharField(max_length=50)
    link_url = models.TextField()
    tree = models.ForeignKey(LinkTree, related_name="trees", on_delete=models.CASCADE)

    def __str__(self):
        return self.link_title