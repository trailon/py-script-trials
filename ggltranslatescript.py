from google_trans_new import google_translator  

translator = google_translator()  

file1 = open('2.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    translate_text = translator.translate(str(line), lang_src='en', lang_tgt='tr')  
    with open('output.txt', 'a') as the_file:
        the_file.write(translate_text+"\n")