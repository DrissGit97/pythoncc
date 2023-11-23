from employee import Employee

def test_default_raise():
    """Tests the default raise of five thousand (5000) dollars."""
    employee = Employee ('fname1', 'lname1', 1000)
    employee.give_raise()
    assert employee.salary == 6000
                         
def test_default_raise():
    """Tests the default raise of five thousand (5000) dollars."""
    employee = Employee ('fname2', 'lname2', 1200)
    employee.give_raise(800)
    assert employee.salary == 2000
