preproinsulin = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy  " \
"tpktrreaed lqvgqvelggg pgagslqpl alegslqkrg iveqcctsic slyqlenycn"

print(preproinsulin)

preproinsulin = preproinsulin.replace(" ", "")
print(preproinsulin)

lsinsulin = preproinsulin[0:24]
binsulin  = preproinsulin[24:54]
cinsulin  = preproinsulin[54:89]
ainsulin  = preproinsulin[89:110]

print()
print(lsinsulin)
print(binsulin)
print(cinsulin)
print(ainsulin)

#lihat hasilnya di Lab nomor 11