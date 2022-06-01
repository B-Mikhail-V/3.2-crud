from rest_framework import serializers


from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


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
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):

        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # создаем данные
        for pos in positions:
            # StockProduct.objects.create(stock=stock, product=pos['product'], quantity=pos['quantity'],price=pos['price'])
            StockProduct.objects.create(stock=stock, **pos)

        return stock


    def update(self, instance, validated_data):


        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # достаем все данные для склада и удаляем
        pos_del = StockProduct.objects.filter(stock=stock)
        pos_del.delete()

        # создаем данные
        for pos in positions:
            # StockProduct.objects.create(stock=stock, product=pos['product'], quantity=pos['quantity'],price=pos['price'])
            StockProduct.objects.create(stock=stock, **pos)

        return stock
