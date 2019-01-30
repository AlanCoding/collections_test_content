def atest(data):
	return data == 'fromuser'

class TestModule(object):

    def tests(self):
        return {
            'atest': atest
        }
