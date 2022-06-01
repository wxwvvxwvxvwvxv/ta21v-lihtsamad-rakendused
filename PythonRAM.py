import psutil

# Teha Pythoni programm, mis vaatab:



#2. Palju on vaba salvestusruumi ja kokku
path = "C:"
sdiskusage = psutil.disk_usage(path)

#1. Palju on vaba RAMi ja kokku RAMi
Vmemory = psutil.virtual_memory()

#3. Kui RAM või Salvestusruum võtab üle 20%, siis kuvab hoiatusteadet
# (hoiatusteate täituvus % peab olema seadistatav)
if Vmemory[2] > 20.0:
    print("RAM votab yle 20%")
if sdiskusage[3] > 20.0:
    print("Salvestusruum votab yle 20%")

#4. Ajalugu programmi käivitusest, vabast ruumist,
# hoiatuvusteatest peab olema salvestatud logisse (txt fail näiteks)
with open("Ajalugu.txt", "a") as file1:
    file1.write("\nVaba RAMi on " + str(Vmemory[4]))
    file1.write("\nKokku RAMi on " + str(Vmemory[0]))
    file1.write("\nVaba salvestusruumi on " + str(sdiskusage[2]))
    file1.write("\nKokku salvestusruumi on " + str(sdiskusage[0]))


#5. Vaadata internetist mõnelt veebelehelt või APIst,
# mis on temperatuur Tallinnas ja see lisada tekstifaili.

print("RAM", Vmemory)
print("salvestusruum",sdiskusage)
print("Vaba RAMi on", Vmemory[4])
print("Kokku RAMi on", Vmemory[0])
print("Vaba salvestusruumi on", sdiskusage[2])
print("Kokku salvestusruumi on", sdiskusage[0])