import projectpack

def test_hello():
    assert projectpack.hello('Guys')=='Hi there Guys'
def get_info(kinetics):
    assert projectpack.get_info('kinetics')==200
    
