
fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples
            
    Returns cost of order
    """          
	
    " YOUR CODE HERE "

orderList = [ ('apples', 2), ('pears', 3), ('limes', 4) ]
print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))