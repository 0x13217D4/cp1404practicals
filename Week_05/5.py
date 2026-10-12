my_subject = {"CP1404","CP1401","CP5639"}
your_subject = {"CP1401","CP5639","CP2406"}
print(f"Union : {my_subject | your_subject}")
print(f"Differences : {my_subject - your_subject}")
print(f"Intersection : {my_subject & your_subject}")
print(f"Symmetric : {my_subject ^ your_subject}")