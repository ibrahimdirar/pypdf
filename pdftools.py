import pdfmerge
import pdfrotate

action = None
print()
print("PDF Tools:")
print("1. Merge")
print("2. Rotate")
print("3. Exit")
while True:
    try:
        action = int(input('Select number of desired tool: '))
    except ValueError:
        print("Please select a number")
        continue
    else:
        if (action == 1):
            print("PDF Merge selected.")
            pdfmerge.main()
        if (action == 2):
            print("PDF Rotate selected.")
            pdfrotate.main()
        if (action == 3):
            break
        print()
        print("PDF Tools:")
        print("1. Merge")
        print("2. Rotate")
        print("3. Exit")
