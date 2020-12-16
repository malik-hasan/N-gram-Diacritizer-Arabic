import pyarabic.araby as araby
input_file = open ("/Users/rana/Desktop/L165_diacritized_processed_complete.txt", "r")
words = input_file.read()
input_file.close()
output_words = araby.strip_tashkeel(words)
output_file = open ("L165_undiacritized.txt", "w")
output_file.write(output_words)
output_file.close()
print ("done")
                    
