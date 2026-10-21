#Show me the values that were passed to my_function()
from unittest.mock import Mock
my_function = Mock()
my_function(1, "senin", "abc123")
print(my_function.call_args.args)