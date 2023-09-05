class MyTable(tables.Table):

   

    class Meta:
        fields = ['name', 'description',]
        model = Product