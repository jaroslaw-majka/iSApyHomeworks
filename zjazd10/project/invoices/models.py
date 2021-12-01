from django.db import models


class Address(models.Model):
    local_no = models.CharField(
        'no lokalu',
        max_length=10,
        blank=True,
        null=True,
    )
    building = models.CharField(
        'nr budynku',
        max_length=10,
    )
    street = models.CharField(
        'ulica',
        max_length=100,
    )
    city = models.CharField(
        'masto',
        max_length=50,
    )
    zip_code = models.CharField(
        'kod pocztowy',
        max_length=10,
    )

    def __str__(self):
        local = f'/{self.local_no}' if self.local_no else ''
        return f'{self.street} {self.building}{local}, {self.zip_code} {self.city}'


class Issuer(models.Model):
    company_name = models.CharField(
        'nazwa firmy',
        max_length=100,
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        verbose_name='adres',
    )

    def __str__(self):
        return self.company_name


class Service(models.Model):
    service_name = models.CharField(
        'nazwa usługi',
        max_length=50,
    )
    price = models.DecimalField(
        'cena',
        decimal_places=2,
        max_digits=5,
    )

    def __str__(self):
        return self.service_name


class Invoice(models.Model):
    number = models.CharField(
        'numer faktury',
        max_length=20,
    )
    issuer = models.ForeignKey(
        Issuer,
        on_delete=models.CASCADE,
        verbose_name='sprzedawca'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        verbose_name='usługa',
    )
    payment_date = models.DateField(
        'data płatności',
    )
    payment_status = models.BooleanField(
        'status płatności',
    )

    def __str__(self):
        return self.number
