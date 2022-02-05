import code_918_maximum_sum_circular_subarray as c

def test_example_1():
    s = c.Solution()
    assert s.maxSubarraySumCircular([1,-2,3,-2]) == 3

def test_example_2():
    s = c.Solution()
    assert s.maxSubarraySumCircular([5,-3,5]) == 10

def test_example_3():
    s = c.Solution()
    assert s.maxSubarraySumCircular([-3,-2,-3]) == -2

def test_first_fail():
    s = c.Solution()
    assert s.maxSubarraySumCircular([-5,3,5]) == 8

def test_fail_73():
    s = c.Solution()
    assert s.maxSubarraySumCircular([2,-2,2,7,8,0]) == 19