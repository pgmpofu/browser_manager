import webbrowser
import sys
import time


def manage_browser():
    print ('Opening favorite sites')

    browser_list_file = 'websites.txt'
    browser = 'chrome'

    if len(sys.argv) >= 2:
        browser_list_file = sys.argv[1].lower()
    if len(sys.argv) >= 3:
        browser_list_file = sys.argv[2].lower()

    wbbrowser = webbrowser.get(browser)
    with open(browser_list_file) as read_obj:
        try:
            for num, url in enumerate(read_obj):
                wbbrowser.open_new_tab(url.strip())
                time.sleep(1)
        except Exception as e:
            print ('Error occurred ', e)

    if __name__ == '__main__':
        print ('Running main')
        manage_browser()
