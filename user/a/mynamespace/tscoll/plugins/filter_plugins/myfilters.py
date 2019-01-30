def afilter(data):
    return "user filter, original data was {0}".format(data)

class FilterModule(object):

    def filters(self):
        return {
            'afilter': afilter
        }
