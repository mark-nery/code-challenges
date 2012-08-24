from minimum_scalar_product import *

def process_file(file_name):
    f = open(file_name)
    data = f.read()
    f.close()

    file_name_without_extension = ''.join(takewhile(lambda c: c != '.',file_name))

    ans_file = open('{0}.out'.format(file_name_without_extension),'w+')

    for i,v in enumerate(get_vectors(data)):
        ans_file.write("Case #{0}: {1}\n".format(i + 1,min_scalar_ordering(v)))

    ans_file.close()

input_files = ['A-small-practice.in','A-large-practice.in']

for f in input_files:
    process_file(f)
