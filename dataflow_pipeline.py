import apache_beam as beam

class Parse(beam.DoFn):
    def process(self, element):
        yield element
