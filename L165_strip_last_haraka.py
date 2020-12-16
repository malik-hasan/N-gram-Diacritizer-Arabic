import pyarabic.araby as araby
from pyarabic.araby import strip_lastharaka
from pyarabic.araby import strip_harakat


s = "المَدْرَسةُ"
d = strip_lastharaka(s)
print(d)

f = open ("/Users/rana/Desktop/L165_diacritized_processed_complete.txt", "r")
words = f.read()
f.close()
output_words = strip_lastharaka(words)
output_f = open ("L165_last_haraka.txt", "w")
output_f.write(output_words)
output_f.close()
print ("done")
