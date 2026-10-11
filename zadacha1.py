text = input("Vavedi niz: ")
result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result += text[i - 1] + str(count)
        count = 1

result += text[-1] + str(count)
print("RLE:", result)

code = input("Vavedi RLE kod: ")
result = ""

for i in range(0, len(code), 2):
    result += code[i] * int(code[i + 1])

print("Originalen niz:", result)