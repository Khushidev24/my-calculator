 def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -4) == -6

        
    def test_multiply_by_zero(self):
        """Test multiplying by zero """
        assert multiply(5,0) == 0
        assert multiply(0,10) == 0
 def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -4) == -6

        
    def test_multiply_by_zero(self):
        """Test multiplying by zero """
        assert multiply(5,0) == 0
        assert multiply(0,10) == 0

    def test_multiply_negative_numbers(self):
        """Test adding positive numbers"""
        assert multiply(-2, 3) == 6
        assert multiply(-4, -5) == 20
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 3) == 5
        assert divide(15, 3) == 5

   def test_divide_negative_numbers(self):
        """Test dividing negtive numbers"""
        assert divide(-10, 3) == -5
        assert divide(-12, -3) == 4
