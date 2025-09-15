
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd


def has_recaaptcha(driver) -> bool:
    try:
        driver.find_element(By.CLASS_NAME, "g-recaptcha")
        return True
    except:
        try:
            driver.find_elemet(By.XPATH, "//iframe[contains(@src, 'google.com/recaptcha')]")
            return True
        except:
            return False
        

def solve_recaptcha_manual(driver, timeout=100):
    """Manuel reCAPTCHA çözümü"""
    try:
        print("👤 Manuel reCAPTCHA çözümü bekleniyor...")
        print("🔔 Lütfen tarayıcıda reCAPTCHA'yı çözün!")
        
        wait = WebDriverWait(driver, timeout)
        
        # reCAPTCHA'nın çözülmesini bekle
        wait.until(lambda d: d.execute_script(
            """
            var response = document.getElementById('g-recaptcha-response');
            return response && response.value.length > 0;
            """
        ))
        
        print("✅ reCAPTCHA manuel olarak çözüldü!")
        return True
        
    except Exception as e:
        print(f"❌ Manuel reCAPTCHA çözüm timeout: {e}")
        return False