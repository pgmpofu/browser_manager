import os
import webbrowser


class BrowserManager:

    def __init__(self):
        pass


def open_website(file_to_open : str, error_msg: str):
    if os.path.exists(file_to_open) and os.path.getsize(file_to_open) > 0:
        try:
            with open('websites.txt') as read_obj:
                for num, url in enumerate(read_obj):
                    webbrowser.open_new_tab(url.strip())
        except IOError as e:
            print (error_msg, e)
    else:
        raise Exception(error_msg)


if __name__ == '__main__':
    open_website('websites.txt', 'File does not exist or is empty, please add and retry')
