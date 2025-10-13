from django.core.management import BaseCommand

from products.models import Product


class Command(BaseCommand):
    # help არის აღწერა, რომელიც CLI-ში სხვა დეველოპერებს (მეც სამომავლოდ) ეხმარება გაიგონ, რას აკეთებს custom ბრძანება.
    help = 'This command counts the number of products'


    def handle(self, *args, **kwargs):
        count = Product.objects.count()
        # self.stdout.write(...) არის (ტერმინალში) ტექსტის გამოტანის მეთოდი, რომელიც უსაფრთხოა Django-ს მენეჯმენტის კონტექსტში.
        # self.style.SUCCESS(...) არის სტილიზატორი, რომ ტექსტი გამოაჩინოს მწვანე ფერად (როგორც წარმატებული მოქმედება).
        self.stdout.write(self.style.SUCCESS(f'Total Products: {count}'))
