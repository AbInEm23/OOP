import problem_1 as a

def main():
    item1 = a.Retailitem('Jacket',12,59.95)
    item2 = a.Retailitem('Designer Jeans',40,34.95)
    item3 = a.Retailitem('Shirt',20,24.95)
    

    print('Item 1')
    print('Description: ', item1.get_description())
    print('units: ', item1.get_units())
    print('price: ', item1.get_price())

    print('Item 2')
    print('Description: ', item2.get_description())
    print('units: ', item2.get_units())
    print('price: ', item2.get_price())

    print('Item 3')
    print('Description: ', item3.get_description())
    print('units: ', item3.get_units())
    print('price: ', item3.get_price())


# or i could set everything for item2 and 3 






main()