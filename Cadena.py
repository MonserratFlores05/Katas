text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

txt_partes = text.split(". ")

txt_clave = ["average", "temperature", "distance"] #Arreglo

for txt in txt_partes:
    for clave in txt_clave:
        if clave in txt:
            print(txt)
            break

for txt in txt_partes:
    for clave in txt_clave:
        if clave in txt:
            print(txt.replace(' C', ' Celsius'))    
            break
         