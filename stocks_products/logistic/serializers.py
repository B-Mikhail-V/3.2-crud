from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    # product = ProductSerializer()
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        print(self)
        print(validated_data)
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(positions)
        print(validated_data)
        print(Stock.objects.all())
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        print(stock)

        StockProduct.objects.create()

        # for pos in positions:


        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

    def update(self, instance, validated_data):
        print(self)
        print(validated_data)
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(validated_data)
        print(positions)
        print(Stock.objects.all())
        # обновляем склад по его параметрам
        st = Stock.objects.all()

        stock = super().update(instance, validated_data)

        print(stock)
        # print(StockProduct.objects.filter(stock=stock))
        stock_upp = StockProduct.objects.filter(stock=stock)

        # instance.positions.set = validated_data.get('positions', instance.positions)
        # instance.save
        # print(instance.positions.set)





        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
