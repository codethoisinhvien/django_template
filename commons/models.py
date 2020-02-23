from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=20)


class CasbinRule(models.Model):
    ptype = models.CharField(max_length=255)
    v0 = models.CharField(max_length=255)
    v1 = models.CharField(max_length=255)
    v2 = models.CharField(max_length=255)
    v3 = models.CharField(max_length=255)
    v4 = models.CharField(max_length=255)
    v5 = models.CharField(max_length=255)

    def __str__(self):
        arr = [self.ptype]
        for v in (self.v0, self.v1, self.v2, self.v3, self.v4, self.v5):
            if v is None:
                break
            arr.append(v)
        return ', '.join(arr)

    def __repr__(self):
        return '<CasbinRule {}: "{}">'.format(self.id, str(self))
