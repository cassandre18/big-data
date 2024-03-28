'importation des libraires'
from mrjob.job import MRJob

class TagsParFilm(MRJob):

'fonction map'
    def mapper(self, _, line):
        # Ignorer len-tete
        if line.startswith('userId'):
            return
        parts = line.split(',')
        movieId = parts[1]
        yield movieId, 1

'fonction reduce'
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagsParFilm.run()
