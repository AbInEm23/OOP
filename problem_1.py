class Retailitem: 


    def __init__(self,item_description,units_in_inventory,price):
        self.__item_description = item_description
        self.__units_in_inventory = units_in_inventory
        self.__price = price 
    
    '''
    def set_description(self,item_description):
        self.__item_description = item_description
    
    def set_units(self,unit_in_inventory):
        self.__units_in_inventory = unit_in_inventory
    
    def set_price(self,price):
        self.__price = price
    '''
    def get_description(self):
        return self.__item_description

    def get_units(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price
    




