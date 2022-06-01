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
        fields = ['address', 'positions']

    def create(self, validated_data):

        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        for pos in positions:
            StockProduct.objects.create(stock=stock, product=pos['product'], quantity=pos['quantity'],price=pos['price'])
            # StockProduct.objects.create(stock=stock, **pos)




        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock


    def update(self, instance, validated_data):
        # print(instance)
        # print(self)
        # print(validated_data)

        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(positions)
        for pos in positions:
            print(pos['product'])
            print(pos['quantity'])
            print(pos['price'])

        # print(validated_data)
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # print(stock)
        # self.data.update(positions)
        # print(StockSerializer.validated_data[:])
        # self.data.update(['positions'='new'])
        # new_dict = dict(positions=positions)
        # print(new_dict)

        # st = StockProduct.objects.filter(stock=stock)
        # print(st.values())
        # for ss in st.values():
        #     print(ss)
        #     for pos in positions:
        #         StockProduct.objects.update(product=pos['product'])
        #         StockProduct.objects.update(quantity=pos['quantity'])
        #         StockProduct.objects.update(price=pos['price'])






        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
