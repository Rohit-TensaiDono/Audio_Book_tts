import pyttsx3
import PyPDF2

# book = open("c:\\Users\\hp\\Downloads\\Electronic_Devices_and_Circuit_Theory_11th_Ed.pdf", "rb")
in_book = input("\nEnter Book : ")
print(in_book)
book = open(in_book, "rb")
pdf = PyPDF2.PdfFileReader(book)
pages = pdf.numPages
print("\nTotal pagre : ", pages)
begin = eval(input("\nEnter beginning of page : "))
end = eval(input("Enter the Ending page : "))

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
engine.setProperty("rate",250)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

for page in range(begin, end+1):
    page = pdf.getPage(page)
    t = page.extractText()
    speak(t)