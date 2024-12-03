import os
import time
import shutil
import pandas as pd

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException



def crear_driver():
    PATH_CHROME_DRIVER = '/home/ubuntu/CL-SII_Juridicos/include/chromedriver'
    options = ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-logging')
    options.add_argument('--log-level=3')

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    options.add_argument(f'--user-agent={user_agent}')

    nombre = 'Descargas'
    carpeta_descarga = os.path.join(os.getcwd(), nombre)
    if not os.path.exists(carpeta_descarga):
        os.makedirs(carpeta_descarga)
    prefs = {"download.default_directory": carpeta_descarga
             }
    options.add_experimental_option("prefs", prefs)
    carpeta_base =  '/home/ubuntu/CL-SII_Juridicos/'
    carpeta_csv = os.path.join(carpeta_base, 'Descargas')
    carpeta_descarga = os.path.join(os.getcwd(), carpeta_csv)
    if not os.path.exists(carpeta_descarga):
        os.makedirs(carpeta_descarga)
    prefs = {"download.default_directory": carpeta_descarga
             }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(PATH_CHROME_DRIVER, options=options)
    driver.get('https://www.sii.cl/sobre_el_sii/nominapersonasjuridicas.html')
    return driver

def espera_descarga_carpeta(carpeta_descargas):

    while not any(fname.endswith('.crdownload') for fname in os.listdir(carpeta_descargas)):
        time.sleep(1)
    
    while any(fname.endswith('.crdownload') for fname in os.listdir(carpeta_descargas)):
        time.sleep(1)

def extaer_actividades_contribuyentes():
    driver = crear_driver()
    actividades_contribuyentes = driver.find_element_by_xpath('//*[@id="my-wrapper"]/div[2]/div[1]/div/div/div[2]/ul[1]/li[1]/a')
    actividades_contribuyentes.click()
    time.sleep(1)
    ruta_archivo = '/home/ubuntu/CL-SII_Juridicos/Descargas/'
    espera_descarga_carpeta(ruta_archivo)
    archivos_zip = [archivo for archivo in os.listdir(ruta_archivo) if archivo.endswith('.zip')]
    archivo_zip = archivos_zip[0]
    shutil.unpack_archive(os.path.join(ruta_archivo, archivo_zip), ruta_archivo)

    os.remove(os.path.join(ruta_archivo, archivo_zip))
    
    df = pd.read_csv(ruta_archivo + 'PUB_NOM_ACTECOS.txt', delimiter='\t', header=0)
    columnas_a_conservar = ['RUT', 'DV', 'CODIGO ACTIVIDAD', 'DESC. ACTIVIDAD ECONOMICA']
    df = df[columnas_a_conservar]
    df.to_csv(ruta_archivo + 'PUB_NOM_ACTECOS(1).txt', sep='\t', index=False)

def extaer_direcciones_contribuyentes():
    driver = crear_driver()
    direcciones_contribuyentes = driver.find_element_by_xpath('//*[@id="my-wrapper"]/div[2]/div[1]/div/div/div[2]/ul[1]/li[2]/a')
    direcciones_contribuyentes.click()
    time.sleep(1)
    ruta_archivo = '/home/ubuntu/CL-SII_Juridicos/Descargas/'
    espera_descarga_carpeta(ruta_archivo)
    archivos_zip = [archivo for archivo in os.listdir(ruta_archivo) if archivo.endswith('.zip')]
    archivo_zip = archivos_zip[0]
    shutil.unpack_archive(os.path.join(ruta_archivo, archivo_zip), ruta_archivo)

    os.remove(os.path.join(ruta_archivo, archivo_zip))
    
    df = pd.read_csv(ruta_archivo + 'PUB_NOM_DOMICILIO.txt', delimiter='\t', header=0)
    df.to_csv(ruta_archivo + 'PUB_NOM_DOMICILIO.csv', sep='\t', index=False)
    
    df = pd.read_csv(ruta_archivo + 'PUB_NOM_SUCURSAL.txt', delimiter='\t', header=0)
    df.to_csv(ruta_archivo + 'PUB_NOM_SUCURSAL.csv', sep='\t', index=False)

def extraer_razon_social_contribuyentes():
    driver = crear_driver()
    razon_contribuyentes = driver.find_element_by_xpath('//*[@id="my-wrapper"]/div[2]/div[1]/div/div/div[2]/ul[1]/li[3]/a')
    razon_contribuyentes.click()
    time.sleep(1)
    ruta_archivo = '/home/ubuntu/CL-SII_Juridicos/Descargas/'
    espera_descarga_carpeta(ruta_archivo)
    archivos_zip = [archivo for archivo in os.listdir(ruta_archivo) if archivo.endswith('.zip')]
    archivo_zip = archivos_zip[0]
    shutil.unpack_archive(os.path.join(ruta_archivo, archivo_zip), ruta_archivo)

    os.remove(os.path.join(ruta_archivo, archivo_zip))
    
    df = pd.read_csv(ruta_archivo + 'CODIGO_TIPO_SUBTIPO.txt', delimiter='\t', header=0)
    df.to_csv(ruta_archivo + 'CODIGO_TIPO_SUBTIPO.csv', sep='\t', index=False)
    
    df = pd.read_csv(ruta_archivo + 'PUB_NOMBRES_PJ.txt', delimiter='\t', header=0)
    df.to_csv(ruta_archivo + 'PUB_NOMBRES_PJ.csv', sep='\t', index=False)

def empresas_juridicas():
    driver = crear_driver()
    aempresas_juridicas = driver.find_element_by_xpath('//*[@id="my-wrapper"]/div[2]/div[1]/div/div/div[2]/ul[1]/li[4]/a')
    aempresas_juridicas.click()
    time.sleep(1)
    ruta_archivo = '/home/ubuntu/CL-SII_Juridicos/Descargas/'
    espera_descarga_carpeta(ruta_archivo)
    archivos_zip = [archivo for archivo in os.listdir(ruta_archivo) if archivo.endswith('.zip')]
    archivo_zip = archivos_zip[0]
    shutil.unpack_archive(os.path.join(ruta_archivo, archivo_zip), ruta_archivo)

    os.remove(os.path.join(ruta_archivo, archivo_zip))
    
    df = pd.read_csv(ruta_archivo + 'PUB_EMPRESAS_PJ_2020_A_2024.txt', delimiter='\t', header=0)
    columnas_a_conservar = ['Año comercial', 'RUT', 'DV', 'Razón social', 'Tramo según ventas', 'Número de trabajadores dependie', 'Fecha inicio de actividades vige', 'Fecha término de giro', 'Fecha primera inscripción de ac']
    df = df[columnas_a_conservar]
    df.to_csv(ruta_archivo + 'PUB_EMPRESAS_PJ_2020_A_2024.csv', sep='\t', index=False)

def main():
    extaer_actividades_contribuyentes()
    extaer_direcciones_contribuyentes()
    extraer_razon_social_contribuyentes()
    empresas_juridicas()

if __name__ == "__main__":
    main()