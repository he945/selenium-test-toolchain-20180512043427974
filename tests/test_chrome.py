import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from transfersh_client.app import send_to_transfersh, create_zip, remove_file
import time

class ChromeTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/google-chrome-stable"
        options.add_experimental_option( "prefs", {'plugin.state.flash': 1, "profile.default_content_setting_values.plugins":1, "profile.content_settings.plugin_whitelist.adobe-flash-player": 1, "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1, "PluginsAllowedForUrls": "http://abc.go.com/watch-live"})
        options.add_argument('--always-authorize-plugins')
        options.add_argument("--no-sandbox")
        options.add_argument('--allow-outdated-plugins')
        options.add_argument('--ppapi-flash-path=/usr/lib/pepperflashplugin-nonfree/libpepflashplayer.so')
        self.driver = webdriver.Chrome(chrome_options=options)

    def test_page(self):
        self.driver.get("https://www.luckyseat.com/hamilton-ny/")
        new_elem = self.driver.find_element_by_tag_name("body");
        assert "RODGERS " in new_elem.text
        driver.save_screenshot('/tmp/sc.png')
        time.sleep(1)
        send_to_transfersh('/tmp/sc.png')
        


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

