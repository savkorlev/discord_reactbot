from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException
import tools
import messages
import prereact


# USER INPUT
email = input("1/7. Enter your account's email:")
password = input("2/7. Enter your account's password:")
target_person = "from: " + input("3/7. Enter the target person's identifier (example: SampleUser#1234):") + " "
target_server = input("4/7. Enter the target server (example: Sample Server):")
number_of_emojis = input("5/7. Enter the number of emojis to put (example: 4):")
emoji_list = []
for i in range(int(number_of_emojis)):
    if i == 0:
        emoji_list.append(input(f"6/7. Enter the name of the {i + 1} emoji (example: regional_indicator_s. WARNING: order does matter):"))
    else:
        emoji_list.append(input(f"Enter the name of the {i + 1} emoji:"))
number_of_pages = input("7/7. Enter the number of pages to parse (example: 4. To enter all messages type: max. Each page contains 25 messages):")

# set up
chrome_options = webdriver.ChromeOptions()
# hide the automated browser notification
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# activating headless mode
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  
# TODO: hide headless
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
driver.maximize_window()
driver.get("https://discord.com/channels/@me")
wait = WebDriverWait(driver, 300)
ac_versatile = ActionChains(driver)

# authorization
prereact.authorize(wait, email, password)

# turn off motion animations
prereact.turn_off_animations(wait, ac_versatile)

# navigate to the target server and get permissions
first_channel = prereact.navigation_and_permissions(wait, target_server, driver)

# search for the target person
prereact.search_for_person(wait, target_person)

# get the total number of pages to parse
number_of_pages = prereact.get_number_of_pages(wait, number_of_pages)

# delete the redundant variables
del(chrome_options)
del(email)
del(number_of_emojis)
del(password)
del(target_person)
del(target_server)

for i in range(number_of_pages):
    # get all messages of the target person in the current page
    tray_of_messages = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.container-rZM65Y")))
    
    # find a message from the tray of messages in the actual chat by its id
    for tray_message in tray_of_messages:
        message_id = tray_message.find_element(By.CSS_SELECTOR, "div > div > div").get_attribute("id")[14:]
        
        is_jump_button_clicked = False
        while not is_jump_button_clicked:
            try:
                jump_button = tools.find_jump_button(ac_versatile, tray_message)
                jump_button.click()
                is_jump_button_clicked = True
            except ElementNotInteractableException:
                continue
        
        # voice chat message
        if len(driver.find_elements(By.CSS_SELECTOR, "button.joinButton-2KP9ZZ")) != 0:
            messages.process_new_message(driver, message_id, ac_versatile, emoji_list, wait, first_channel)
        # any other message
        else:
            messages.process_old_message(driver, message_id, ac_versatile, tray_message, jump_button, emoji_list)
    
    # go to the next page
    driver.find_element(By.CSS_SELECTOR, 'button[rel=\'next\']').click()

# driver.quit()

# TODO: since jump is a getter the frequency of clicking it can also be detectable by discord. Set random waiting times before clicking