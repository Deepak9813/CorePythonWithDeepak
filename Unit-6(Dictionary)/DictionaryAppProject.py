""""
Q.2. Write a to take word from user and gives their meaning.

ie. make a dictionary(real word dictionary app)


"""

# mydictionary = {
#     "father":"Buwa",
#     "mother":"Aama",
#     "Hello":"Namaste",
    
# }

mydictionary = {
    "father": "बुबा",
    "mother": "आमा",
    "hello": "नमस्ते",
    "thank you": "धन्यवाद",
    "sorry": "माफ गर्नुहोस्",
    "water": "पानी",
    "food": "खाना",
    "friend": "साथी",
    "home": "घर",
    "love": "माया",
    "school": "विद्यालय",
    "teacher": "शिक्षक",
    "student": "विद्यार्थी",
    "book": "पुस्तक",
    "pen": "कलम",
    "sun": "घाम",
    "moon": "चन्द्रमा",
    "star": "तारा",
    "sky": "आकाश",
    "earth": "धरती",
    "fire": "अागो",
    "air": "हावा",
    "mountain": "पहाड",
    "river": "नदी",
    "child": "बालक",
    "girl": "केटी",
    "boy": "केटा",
    "brother": "दाजु",
    "sister": "दिदी",
    "grandfather": "हजुरबुबा",
    "grandmother": "हजुरआमा",
    "family": "परिवार",
    "house": "घर",
    "room": "कोठा",
    "door": "ढोका",
    "window": "झ्याल",
    "chair": "कुर्सी",
    "table": "टेबल",
    "bed": "खाट",
    "road": "बाटो",
    "car": "गाडी",
    "bus": "बस",
    "train": "रेल",
    "city": "सहर",
    "village": "गाउँ",
    "market": "बजार",
    "shop": "दोकान",
    "money": "पैसा",
    "work": "काम",
    "time": "समय",
    "day": "दिन",
    "night": "रात",
    "morning": "बिहान",
    "evening": "साँझ",
    "yesterday": "हिजो",
    "today": "आज",
    "tomorrow": "भोलि",
    "happy": "खुसी",
    "sad": "दुःखी",
    "angry": "रिसाएको",
    "big": "ठूलो",
    "small": "सानो",
    "hot": "तातो",
    "cold": "चिसो",
    "good": "राम्रो",
    "bad": "नराम्रो",
    "new": "नयाँ",
    "old": "पुरानो",
    "beautiful": "सुन्दर",
    "ugly": "कुरुप",
    "strong": "बलियो",
    "weak": "दुर्बल",
    "open": "खोल्नु",
    "close": "बन्द गर्नु",
    "eat": "खानु",
    "drink": "पिउनु",
    "sleep": "सुत्नु",
    "walk": "हिँड्नु",
    "run": "दौडनु",
    "sit": "बस्नु",
    "stand": "उभिनु",
    "read": "पढ्नु",
    "write": "लेख्नु",
    "speak": "बोल्नु",
    "listen": "सुन्नु",
    "see": "देख्नु",
    "think": "सोच्नु",
    "know": "थाहा पाउनु",
    "understand": "बुझ्नु",
    "help": "सहयोग गर्नु",
    "play": "खेल्नु",
    "work": "काम गर्नु",
    "clean": "सफाई गर्नु",
    "dirty": "फोहोर",
    "light": "उज्यालो",
    "dark": "अँध्यारो",
    "happy birthday": "जन्मदिन शुभकामना"
}




# word = "xydhhdh"
# word = input("Enter word: ")
word = input("Enter word: ").lower()

# mydictionary.get(word)
# mydictionary.get(word,"word does not found in the dictionary")
print(mydictionary.get(word,"word does not found in the dictionary"))