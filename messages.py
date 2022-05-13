from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import tools

def process_old_message(driver, message_id, action_chain, tray_message, jump_button, emoji_list, wait):
    # select an exact message by its id in the actual chat
    while len(driver.find_elements(By.CSS_SELECTOR, f"#chat-messages-{message_id}")) == 0:
        action_chain.move_to_element(tray_message)
        action_chain.perform()
        action_chain.reset_actions()
        jump_button.click()
    current_message = driver.find_element(By.CSS_SELECTOR, f"#chat-messages-{message_id}")
    # right click a message. If there was an animation bug - repeat
    action_chain.context_click(current_message)
    action_chain.perform()
    action_chain.reset_actions()
    while len(driver.find_elements(By.CSS_SELECTOR, f"[data-name=\"{emoji_list[0]}\"]")) == 0:
        while len(driver.find_elements(By.CSS_SELECTOR, "#message-add-reaction")) == 0:
            action_chain.move_to_element(tray_message)
            action_chain.perform()
            action_chain.reset_actions()
            jump_button.click()
            tools.wait_and_right_click(action_chain, current_message)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#message-add-reaction"))).click()
        tools.put_emojies(action_chain, emoji_list, wait)

def process_new_message(driver, message_id, action_chain, emoji_list, wait, first_channel):
    current_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"#chat-messages-{message_id}")))
    action_chain.context_click(current_message)
    action_chain.perform()
    action_chain.reset_actions()
    while len(driver.find_elements(By.CSS_SELECTOR, f"[data-name=\"{emoji_list[0]}\"]")) == 0:
        while len(driver.find_elements(By.CSS_SELECTOR, "#message-add-reaction")) == 0:
            tools.wait_and_right_click(action_chain, current_message)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#message-add-reaction"))).click()
        tools.put_emojies(action_chain, emoji_list, wait)
    first_channel.click()