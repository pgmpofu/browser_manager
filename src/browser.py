import os
import webbrowser


def open_website():
    if os.path.exists('websites.txt'):
        try:
            with open('websites.txt') as read_obj:
                for num, url in enumerate(read_obj):
                    webbrowser.open_new_tab(url.strip())
        except Exception as e:
            print ('An error occurred ', e)
    else:
        print ('File does not exist, please add and retry')


if __name__ == '__main__':
    open_website()
