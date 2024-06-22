import os

def init():
    print('Welcome to helpcmd')
    helpcmd = input('What command do you need help with? ').strip()
    if helpcmd:
        try:
            os.system(f'man {helpcmd}')
        except Exception as e:
            print(f"Error retrieving man page for {helpcmd}: {e}")
    else:
        print("No command entered.")
