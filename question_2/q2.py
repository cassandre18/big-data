'importation des librairires'
from mrjob.job import MRJob

class TagsParUtilisateur(MRJob):

'fonction map'
    def mapper(self, _, line):
        if line.startswith('userId'):
            return
        parts = line.split(',')
        userId = parts[0]
        yield userId, 1

'fonction reduce'
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagsParUtilisateur.run()
