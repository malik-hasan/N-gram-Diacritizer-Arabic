import re
f = open ("/Users/rana/Desktop/L165_corpus1.txt", "r")
file = f.read()
z = file.lstrip()
trim_space = re.sub(' +',' ', z)
output_file = open ("/Users/rana/Desktop/L165_diacritized_corpus2.txt", 'w')
output_file.write(trim_space)
output_file.close()

