#
# Lutris Win Installer script
# by OdzioM
#

import subprocess

print("Lutris EXE Installer")
print("Sprawdzam, czy Lutris działa w tle... ", end="")
try:
    checker = subprocess.check_output("pgrep lutris", shell=True).decode()
    print("Lutris jest uruchomiony. Wyłączam!")
    line = checker.split()
    subprocess.call("kill " + line[0], shell=True)
except subprocess.CalledProcessError:
    print("OK.")
name = input("Podaj nazwę oprogramowania: ")
print("Wybierz architekturę:")
print("1. Win32")
print("2. Win64")
arch = input("Twój wybór: ")
print("Instalacja z:")
print("1. Pliku exe")
print("2. Płyty CD/DVD/Virtual Drive")
device = input("Twój wybór: ")
if name != "" and (arch == "1" or arch == "2"):
    slug = name.replace(":", "-").replace("'", "").replace(" ", "-").lower()
    #slug = slug.replace(" ", "-")
    if arch == "1": win = "win32"
    if arch == "2": win = "win64"
    output_file = open(slug + ".yml", "w")
    output_file.write("name: \"" + name + "\"\n")
    output_file.write("game_slug: " + slug + "\n")
    output_file.write("version: Standalone\n")
    output_file.write("slug: " + slug + "\n")
    output_file.write("runner: wine\n\n")
    output_file.write("script:\n")
    if device == "1":
        output_file.write("  files:\n")
        output_file.write("  - installer: 'N/A:Select the Setup executable:'\n")
    output_file.write("  game:\n")
    output_file.write("    arch: " + win + "\n")
    output_file.write("    exe: $GAMEDIR/drive_c/.\n")
    output_file.write("    prefix: $GAMEDIR\n")
    if device == "1":
        output_file.write("  installer:\n")
        output_file.write("    - task:\n")
        output_file.write("        arch: " + win + "\n")
        output_file.write("        description: Creating prefix\n")
        output_file.write("        name: create_prefix\n")
        output_file.write("        prefix: $GAMEDIR\n")
        output_file.write("    - task:\n")
        output_file.write("        arch: " + win + "\n")
        output_file.write("        executable: installer\n")
        output_file.write("        name: wineexec\n")
        output_file.write("        prefix: $GAMEDIR\n")
        output_file.write("    - task:\n")
        output_file.write("        name: winekill\n")
        output_file.write("        prefix: $GAMEDIR\n")
    if device == "2":
        output_file.write("  installer:\n")
        output_file.write("    - task:\n")
        output_file.write("        arch: " + win + "\n")
        output_file.write("        description: Creating prefix\n")
        output_file.write("        name: create_prefix\n")
        output_file.write("        prefix: $GAMEDIR\n")
        output_file.write("    - task:\n")
        output_file.write("        arch: " + win + "\n")
        output_file.write("        executable: taskmgr.exe\n")
        output_file.write("        name: wineexec\n")
        output_file.write("        prefix: $GAMEDIR\n")
        output_file.write("    - task:\n")
        output_file.write("        name: winekill\n")
        output_file.write("        prefix: $GAMEDIR\n")
    output_file.close()
    subprocess.call("lutris -i ./" + slug + ".yml", shell=True)
    subprocess.call("rm ./" + slug + ".yml", shell=True) 
else:
    print("Błędny wybór opcji. Spróbuj ponownie!")