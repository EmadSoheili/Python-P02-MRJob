from mrjob.job import MRJob

class bacon_count(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1

    def reducer(self, key, value):
        yield key, sum(value)

if __name__ == "__main__":
    bacon_count.run()
