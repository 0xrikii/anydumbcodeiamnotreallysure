#this is for solve hackthissite level 6 challange 

def encrypt(text):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + i-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      elif (char.islower()):
         result += chr((ord(char) + i - 97) % 26 + 97)
      else:
         result += chr((ord(char) + i - 33) % 26 + 33)
    
    return result

def decrypt(text):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) - i-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      elif (char.islower()):
         result += chr((ord(char) - i - 97) % 26 + 97)
      else:
         result += chr((ord(char) - i - 33) % 26 + 33)
    
    return result
#check the above function
text = "5::7=9<7"

print ("Plain Text : " + text)
print ("Result: " + decrypt(text,s))
