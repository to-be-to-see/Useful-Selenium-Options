from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



options = Options()
options.page_load_strategy = 'none'                             # Never wait for page to load
options.add_experimental_option("detach", True)     # Keep window opened when Error raised
options.add_argument('--blink-settings=imagesEnabled=false')    # Don't load image
options.add_argument("--start-maximized")                       # Window maximized to load login btn in home page

# Reduce cpu usage
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_argument("--disable-client-side-phishing-detection")
options.add_argument("--disable-crash-reporter")
options.add_argument("--disable-oopr-debug-crash-dump")
options.add_argument("--no-crash-upload")
options.add_argument("--disable-low-res-tiling")
options.add_argument("--silent")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--FontRenderHinting[none]")
options.add_argument("--ash-no-nudges")
options.add_argument("--propagate-iph-for-testing")
options.add_argument("--disable-features=CalculateNativeWinOcclusion")
options.add_argument("--disable-ipc-flooding-protection")
options.add_argument("--disable-features=BackForwardCache")


driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

















