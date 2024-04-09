def dollar_to_rupee(amount):

    if amount == '':
        raise ValueError("Input cannot be blank")

    if not isinstance(amount, (int, float)):
        raise ValueError("Input must be numeric")	

    if amount < 0:
        raise ValueError("Negative input not allowed")	
    
    return amount * 74


def rupee_to_dollar(amount):

    return amount / 74
