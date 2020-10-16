############################################################################

#   language detection configuration
#   reference: https://github.com/detectlanguage/detectlanguage-python

import detectlanguage

detectlanguage.configuration.api_key = "YOUR_API_KEY"   #get yours from https://detectlanguage.com/

############################################################################

input = open("input.txt", "r")
lines = input.readlines()

output = open("culprits.txt", "w")

for line in lines:

    line = line.strip()
    line = line.replace(',', '')
    line = line.replace('.', '')

    words = line.split()
    for word in words:

        result = detectlanguage.detect(word)
        print(word)
        print(result)

        languages = ""
        for detection in result:

            languages += detection["language"] + " "
            if detection["language"] == "fr":
                languages= ""
                break

        else:
            output.write(f"{word}, languages = {languages}\n")
            print(f"{word}, languages = {languages}\n")
            languages = ""

        result = None

output.write("\n\nOutput ends here")
input.close()
output.close()