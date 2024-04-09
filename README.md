""Currency convertor through TDD""

This currency convertor has two type of functions.'def dollar_to_rupee(amount):' function used to convert the currency from dollar to rupee and function 'def rupee_to_dollar(amount):' is used to convert the currency from rupee to dollar.

Test cases for dollar_to_rupee(amount) :

1)converting the currency correctly (dollar_to_rupee(10) should return 740)
2)input cannot be empty. ( dollar_to_rupee('') must raise a value error)
3)input must be numerical (dollar_to_rupee('value') must raise a value error)
4)input cannot be negative (dollar_to_rupee('value') must raise a value error)


Test cases for rupee_to_dollar(amount) :

1)converting the currency correctly ((rupee_to_dollar(740) should return 10)
2)input cannot be empty. ( rupee_to_dollar('') must raise a value error)
3)input must be numerical (rupee_to_dollar('value') must raise a value error)
4)input cannot be negative (rupee_to_dollar('value') must raise a value error)
