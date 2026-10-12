module_to_number = {"CP1404":109,"CP1401":65,"CP5639":35}
modules = ["CP1404","CP5639"]

for module in modules:
    module_to_number[module]=module_to_number.get(module,0)+1
    print(module,module_to_number[module])