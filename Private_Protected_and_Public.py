class Employee:
    name_1 = "Diwakar"  # Public variable
    name_2 = "Rohit"      # Public variable
    _working_hour_of_an_employee_1 = 9   # Protected variable starts with single underscore
    _working_hour_of_an_employee_2 = 7   # Protected variable starts with single underscore
    __salary_1 = 1000000000    # Private variable starts with double underscore
    __salary_2 = 500000            # Private variable starts with double underscore


emp1 = Employee()
print(Employee.name_1)  # Public variable
print(Employee._working_hour_of_an_employee_1) # Protected variable
print(emp1._Employee__salary_1)  # We cannot use the Private variables just like Public variables to use the Private variable use need to write in the following
                                                        # syntax i.e., object-name._class-name__Private-variable-name . We use this type of syntax because we may by mistake
                                                        # use the Private variable to make ensure it is a Private variable we use this type of syntax so we cannot use Private variable
                                                        # by mistake
