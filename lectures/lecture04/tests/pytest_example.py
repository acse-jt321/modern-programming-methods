import foo

def test_solve_quadratic_part_one():
    
    assert foo.solve_quadratic(1,0,-1)==(-1.0,1.0)
    assert foo.solve_quadratic(1,0,0)==0.0

def test_solve_quadratic_part_two():
    assert foo.solve_quadratic(1,0,1) is None