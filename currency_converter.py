def dollar_to_rupee(amount):

    if amount == '':
        raise ValueError("Input cannot be blank")

    if not isinstance(amount, (int, float)):
        raise ValueError("Input must be numeric")	
    
    return amount * 74

