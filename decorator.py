def check(f):
    def wrapper(self, a, b):
        try:
            return f(self, a, b)
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception as e:
            return f"Error: {str(e)}"
    return wrapper

class Operations:
    @check
    def div(self, a, b):
        return a / b

# Testing the Operations class
print(f"Res is {Operations().div(1, 2)}")  # Should print 0.5
print(f"Res is {Operations().div(1, 0)}")  # Should handle division by zero
