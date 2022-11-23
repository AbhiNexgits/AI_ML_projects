from ThaiPersonalCardExtract import PersonalCard

reader = PersonalCard(lang="mix", tesseract_cmd="/home/nexgits/tesseract-4.1.1/INSTALL")

result = reader.extract_front_info("Thai_card.jpg")

# result2 = reader.extract_back_info("Thai_card.jpg")

print(result)

