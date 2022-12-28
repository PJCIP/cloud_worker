from selenium import webdriver
import os
from APIKEY import * 
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tqdm import tqdm
import warnings
import json
from datetime import datetime
warnings.simplefilter(action='ignore', category=FutureWarning)
from sys import argv



def scrape(ll,ul,sstate,data_2022):
    print("The lower limit is {} and upperlimit is {} the state id is {}. so far data shapee is {}".format(ll,ul,sstate,data_2022.shape))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    
    path = "./chromedriver.exe"
    # driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    driver = webdriver.Chrome(path)
    
    cs = {1: 30, 2: 68, 3: 76, 4: 16, 5: 59, 6: 65, 7: 9, 8: 2, 9: 4, 10: 68, 11: 160, 12: 6, 13: 100, 14: 45, 15: 102, 16: 93, 17: 106, 18: 121, 19: 65, 20: 15, 21: 25, 22: 17, 23: 84, 24: 88, 25: 116, 26: 83, 27: 57, 28: 101, 29: 54, 30: 94, 31: 11, 32: 22, 33: 34, 34: 18, 35: 63, 36: 89, 37: 78, 38: 37, 39: 68, 40: 79, 41: 6, 42: 47, 43: 67, 44: 96, 45: 255, 46: 30, 47: 134, 48: 15, 49: 40, 50: 73, 51: 56, 52: 24}
    # path = "chromedriver.exe"
    global hipps
    global state

    # driver = webdriver.Chrome(path)

    driver.get(
        "https://www.palmettogba.com/palmetto/hhapps.nsf/main?Openform&lob=J11HHH&tname=HHA%20PPS%20Claims%20Calculator")

    window_before = driver.window_handles[0]


    episode_selection = driver.find_element(By.NAME, "EpisodeSelection")

    # calculation_type=driver.find_element(By.NAME,"CalculationType")

    episode_box = Select(episode_selection)
    # calculation_box=Select(calculation_type)
    # 0 - 2022,1 - 2021,2 - 2020
    episode_box.select_by_index(0)
    state_dict = {1: 'AK', 2: 'AL', 3: 'AR', 4: 'AZ', 5: 'CA', 6: 'CO', 7: 'CT', 8: 'DC', 9: 'DE', 10: 'FL', 11: 'GA', 12: 'HI', 13: 'IA', 14: 'ID', 15: 'IL', 16: 'IN', 17: 'KS', 18: 'KY', 19: 'LA', 20: 'MA', 21: 'MD', 22: 'ME', 23: 'MI', 24: 'MN', 25: 'MO', 26: 'MS', 27: 'MT', 28: 'NC', 29: 'ND', 30: 'NE', 31: 'NH', 32: 'NJ', 33: 'NM', 34: 'NV', 35: 'NY', 36: 'OH', 37: 'OK', 38: 'OR', 39: 'PA', 40: 'PR', 41: 'RI', 42: 'SC', 43: 'SD', 44: 'TN', 45: 'TX', 46: 'UT', 47: 'VA', 48: 'VT', 49: 'WA', 50: 'WI', 51: 'WV', 52: 'WY'}
    hipps_options = ['1AA11', '1AA21', '1AA31', '1AB11', '1AB21', '1AB31', '1AC11', '1AC21', '1AC31', '1BA11', '1BA21', '1BA31', '1BB11', '1BB21', '1BB31', '1BC11', '1BC21', '1BC31', '1CA11', '1CA21', '1CA31', '1CB11', '1CB21', '1CB31', '1CC11', '1CC21', '1CC31', '1DA11', '1DA21', '1DA31', '1DB11', '1DB21', '1DB31', '1DC11', '1DC21', '1DC31', '1EA11', '1EA21', '1EA31', '1EB11', '1EB21', '1EB31', '1EC11', '1EC21', '1EC31', '1FA11', '1FA21', '1FA31', '1FB11', '1FB21', '1FB31', '1FC11', '1FC21', '1FC31', '1GA11', '1GA21', '1GA31', '1GB11', '1GB21', '1GB31', '1GC11', '1GC21', '1GC31', '1HA11', '1HA21', '1HA31', '1HB11', '1HB21', '1HB31', '1HC11', '1HC21', '1HC31', '1IA11', '1IA21', '1IA31', '1IB11', '1IB21', '1IB31', '1IC11', '1IC21', '1IC31', '1JA11', '1JA21', '1JA31', '1JB11', '1JB21', '1JB31', '1JC11', '1JC21', '1JC31', '1KA11', '1KA21', '1KA31', '1KB11', '1KB21', '1KB31', '1KC11', '1KC21', '1KC31', '1LA11', '1LA21', '1LA31', '1LB11', '1LB21', '1LB31', '1LC11', '1LC21', '1LC31', '2AA11', '2AA21', '2AA31', '2AB11', '2AB21', '2AB31', '2AC11', '2AC21', '2AC31', '2BA11', '2BA21', '2BA31', '2BB11', '2BB21', '2BB31', '2BC11', '2BC21', '2BC31', '2CA11', '2CA21', '2CA31', '2CB11', '2CB21', '2CB31', '2CC11', '2CC21', '2CC31', '2DA11', '2DA21', '2DA31', '2DB11', '2DB21', '2DB31', '2DC11', '2DC21', '2DC31', '2EA11', '2EA21', '2EA31', '2EB11', '2EB21', '2EB31', '2EC11', '2EC21', '2EC31', '2FA11', '2FA21', '2FA31', '2FB11', '2FB21', '2FB31', '2FC11', '2FC21', '2FC31', '2GA11', '2GA21', '2GA31', '2GB11', '2GB21', '2GB31', '2GC11', '2GC21', '2GC31', '2HA11', '2HA21', '2HA31', '2HB11', '2HB21', '2HB31', '2HC11', '2HC21', '2HC31', '2IA11', '2IA21', '2IA31', '2IB11', '2IB21', '2IB31', '2IC11', '2IC21', '2IC31', '2JA11', '2JA21', '2JA31', '2JB11', '2JB21', '2JB31', '2JC11', '2JC21', '2JC31', '2KA11', '2KA21', '2KA31', '2KB11', '2KB21', '2KB31', '2KC11', '2KC21', '2KC31', '2LA11', '2LA21', '2LA31', '2LB11', '2LB21', '2LB31', '2LC11', '2LC21', '2LC31', '3AA11', '3AA21', '3AA31', '3AB11', '3AB21', '3AB31', '3AC11', '3AC21', '3AC31', '3BA11', '3BA21', '3BA31', '3BB11', '3BB21', '3BB31', '3BC11', '3BC21', '3BC31', '3CA11', '3CA21', '3CA31', '3CB11', '3CB21', '3CB31', '3CC11', '3CC21', '3CC31', '3DA11', '3DA21', '3DA31', '3DB11', '3DB21', '3DB31', '3DC11', '3DC21', '3DC31', '3EA11', '3EA21', '3EA31', '3EB11', '3EB21', '3EB31', '3EC11', '3EC21', '3EC31', '3FA11', '3FA21', '3FA31', '3FB11', '3FB21', '3FB31', '3FC11', '3FC21', '3FC31', '3GA11', '3GA21', '3GA31', '3GB11', '3GB21', '3GB31', '3GC11', '3GC21', '3GC31', '3HA11', '3HA21', '3HA31', '3HB11', '3HB21', '3HB31', '3HC11', '3HC21', '3HC31', '3IA11', '3IA21', '3IA31', '3IB11', '3IB21', '3IB31', '3IC11', '3IC21', '3IC31', '3JA11', '3JA21', '3JA31', '3JB11', '3JB21', '3JB31', '3JC11', '3JC21', '3JC31', '3KA11', '3KA21', '3KA31', '3KB11', '3KB21', '3KB31', '3KC11', '3KC21', '3KC31', '3LA11', '3LA21', '3LA31', '3LB11', '3LB21', '3LB31', '3LC11', '3LC21', '3LC31', '4AA11', '4AA21', '4AA31', '4AB11', '4AB21', '4AB31', '4AC11', '4AC21', '4AC31', '4BA11', '4BA21', '4BA31', '4BB11', '4BB21', '4BB31', '4BC11', '4BC21', '4BC31', '4CA11', '4CA21', '4CA31', '4CB11', '4CB21', '4CB31', '4CC11', '4CC21', '4CC31', '4DA11', '4DA21', '4DA31', '4DB11', '4DB21', '4DB31', '4DC11', '4DC21', '4DC31', '4EA11', '4EA21', '4EA31', '4EB11', '4EB21', '4EB31', '4EC11', '4EC21', '4EC31', '4FA11', '4FA21', '4FA31', '4FB11', '4FB21', '4FB31', '4FC11', '4FC21', '4FC31', '4GA11', '4GA21', '4GA31', '4GB11', '4GB21', '4GB31', '4GC11', '4GC21', '4GC31', '4HA11', '4HA21', '4HA31', '4HB11', '4HB21', '4HB31', '4HC11', '4HC21', '4HC31', '4IA11', '4IA21', '4IA31', '4IB11', '4IB21', '4IB31', '4IC11', '4IC21', '4IC31', '4JA11', '4JA21', '4JA31', '4JB11', '4JB21', '4JB31', '4JC11', '4JC21', '4JC31', '4KA11', '4KA21', '4KA31', '4KB11', '4KB21', '4KB31', '4KC11', '4KC21', '4KC31', '4LA11', '4LA21', '4LA31', '4LB11', '4LB21', '4LB31', '4LC11', '4LC21', '4LC31']
    hipps_dict = {1: '1AA11', 2: '1AA21', 3: '1AA31', 4: '1AB11', 5: '1AB21', 6: '1AB31', 7: '1AC11', 8: '1AC21', 9: '1AC31', 10: '1BA11', 11: '1BA21', 12: '1BA31', 13: '1BB11', 14: '1BB21', 15: '1BB31', 16: '1BC11', 17: '1BC21', 18: '1BC31', 19: '1CA11', 20: '1CA21', 21: '1CA31', 22: '1CB11', 23: '1CB21', 24: '1CB31', 25: '1CC11', 26: '1CC21', 27: '1CC31', 28: '1DA11', 29: '1DA21', 30: '1DA31', 31: '1DB11', 32: '1DB21', 33: '1DB31', 34: '1DC11', 35: '1DC21', 36: '1DC31', 37: '1EA11', 38: '1EA21', 39: '1EA31', 40: '1EB11', 41: '1EB21', 42: '1EB31', 43: '1EC11', 44: '1EC21', 45: '1EC31', 46: '1FA11', 47: '1FA21', 48: '1FA31', 49: '1FB11', 50: '1FB21', 51: '1FB31', 52: '1FC11', 53: '1FC21', 54: '1FC31', 55: '1GA11', 56: '1GA21', 57: '1GA31', 58: '1GB11', 59: '1GB21', 60: '1GB31', 61: '1GC11', 62: '1GC21', 63: '1GC31', 64: '1HA11', 65: '1HA21', 66: '1HA31', 67: '1HB11', 68: '1HB21', 69: '1HB31', 70: '1HC11', 71: '1HC21', 72: '1HC31', 73: '1IA11', 74: '1IA21', 75: '1IA31', 76: '1IB11', 77: '1IB21', 78: '1IB31', 79: '1IC11', 80: '1IC21', 81: '1IC31', 82: '1JA11', 83: '1JA21', 84: '1JA31', 85: '1JB11', 86: '1JB21', 87: '1JB31', 88: '1JC11', 89: '1JC21', 90: '1JC31', 91: '1KA11', 92: '1KA21', 93: '1KA31', 94: '1KB11', 95: '1KB21', 96: '1KB31', 97: '1KC11', 98: '1KC21', 99: '1KC31', 100: '1LA11', 101: '1LA21', 102: '1LA31', 103: '1LB11', 104: '1LB21', 105: '1LB31', 106: '1LC11', 107: '1LC21', 108: '1LC31', 109: '2AA11', 110: '2AA21', 111: '2AA31', 112: '2AB11', 113: '2AB21', 114: '2AB31', 115: '2AC11', 116: '2AC21', 117: '2AC31', 118: '2BA11', 119: '2BA21', 120: '2BA31', 121: '2BB11', 122: '2BB21', 123: '2BB31', 124: '2BC11', 125: '2BC21', 126: '2BC31', 127: '2CA11', 128: '2CA21', 129: '2CA31', 130: '2CB11', 131: '2CB21', 132: '2CB31', 133: '2CC11', 134: '2CC21', 135: '2CC31', 136: '2DA11', 137: '2DA21', 138: '2DA31', 139: '2DB11', 140: '2DB21', 141: '2DB31', 142: '2DC11', 143: '2DC21', 144: '2DC31', 145: '2EA11', 146: '2EA21', 147: '2EA31', 148: '2EB11', 149: '2EB21', 150: '2EB31', 151: '2EC11', 152: '2EC21', 153: '2EC31', 154: '2FA11', 155: '2FA21', 156: '2FA31', 157: '2FB11', 158: '2FB21', 159: '2FB31', 160: '2FC11', 161: '2FC21', 162: '2FC31', 163: '2GA11', 164: '2GA21', 165: '2GA31', 166: '2GB11', 167: '2GB21', 168: '2GB31', 169: '2GC11', 170: '2GC21', 171: '2GC31', 172: '2HA11', 173: '2HA21', 174: '2HA31', 175: '2HB11', 176: '2HB21', 177: '2HB31', 178: '2HC11', 179: '2HC21', 180: '2HC31', 181: '2IA11', 182: '2IA21', 183: '2IA31', 184: '2IB11', 185: '2IB21', 186: '2IB31', 187: '2IC11', 188: '2IC21', 189: '2IC31', 190: '2JA11', 191: '2JA21', 192: '2JA31', 193: '2JB11', 194: '2JB21', 195: '2JB31', 196: '2JC11', 197: '2JC21', 198: '2JC31', 199: '2KA11', 200: '2KA21', 201: '2KA31', 202: '2KB11', 203: '2KB21', 204: '2KB31', 205: '2KC11', 206: '2KC21', 207: '2KC31', 208: '2LA11', 209: '2LA21', 210: '2LA31', 211: '2LB11', 212: '2LB21', 213: '2LB31', 214: '2LC11', 215: '2LC21', 216: '2LC31', 217: '3AA11', 218: '3AA21', 219: '3AA31', 220: '3AB11', 221: '3AB21', 222: '3AB31', 223: '3AC11', 224: '3AC21', 225: '3AC31', 226: '3BA11', 227: '3BA21', 228: '3BA31', 229: '3BB11', 230: '3BB21', 231: '3BB31', 232: '3BC11', 233: '3BC21', 234: '3BC31', 235: '3CA11', 236: '3CA21', 237: '3CA31', 238: '3CB11', 239: '3CB21', 240: '3CB31', 241: '3CC11', 242: '3CC21', 243: '3CC31', 244: '3DA11', 245: '3DA21', 246: '3DA31', 247: '3DB11', 248: '3DB21', 249: '3DB31', 250: '3DC11', 251: '3DC21', 252: '3DC31', 253: '3EA11', 254: '3EA21', 255: '3EA31', 256: '3EB11', 257: '3EB21', 258: '3EB31', 259: '3EC11', 260: '3EC21', 261: '3EC31', 262: '3FA11', 263: '3FA21', 264: '3FA31', 265: '3FB11', 266: '3FB21', 267: '3FB31', 268: '3FC11', 269: '3FC21', 270: '3FC31', 271: '3GA11', 272: '3GA21', 273: '3GA31', 274: '3GB11', 275: '3GB21', 276: '3GB31', 277: '3GC11', 278: '3GC21', 279: '3GC31', 280: '3HA11', 281: '3HA21', 282: '3HA31', 283: '3HB11', 284: '3HB21', 285: '3HB31', 286: '3HC11', 287: '3HC21', 288: '3HC31', 289: '3IA11', 290: '3IA21', 291: '3IA31', 292: '3IB11', 293: '3IB21', 294: '3IB31', 295: '3IC11', 296: '3IC21', 297: '3IC31', 298: '3JA11', 299: '3JA21', 300: '3JA31', 301: '3JB11', 302: '3JB21', 303: '3JB31', 304: '3JC11', 305: '3JC21', 306: '3JC31', 307: '3KA11', 308: '3KA21', 309: '3KA31', 310: '3KB11', 311: '3KB21', 312: '3KB31', 313: '3KC11', 314: '3KC21', 315: '3KC31', 316: '3LA11', 317: '3LA21', 318: '3LA31', 319: '3LB11', 320: '3LB21', 321: '3LB31', 322: '3LC11', 323: '3LC21', 324: '3LC31', 325: '4AA11', 326: '4AA21', 327: '4AA31', 328: '4AB11', 329: '4AB21', 330: '4AB31', 331: '4AC11', 332: '4AC21', 333: '4AC31', 334: '4BA11', 335: '4BA21', 336: '4BA31', 337: '4BB11', 338: '4BB21', 339: '4BB31', 340: '4BC11', 341: '4BC21', 342: '4BC31', 343: '4CA11', 344: '4CA21', 345: '4CA31', 346: '4CB11', 347: '4CB21', 348: '4CB31', 349: '4CC11', 350: '4CC21', 351: '4CC31', 352: '4DA11', 353: '4DA21', 354: '4DA31', 355: '4DB11', 356: '4DB21', 357: '4DB31', 358: '4DC11', 359: '4DC21', 360: '4DC31', 361: '4EA11', 362: '4EA21', 363: '4EA31', 364: '4EB11', 365: '4EB21', 366: '4EB31', 367: '4EC11', 368: '4EC21', 369: '4EC31', 370: '4FA11', 371: '4FA21', 372: '4FA31', 373: '4FB11', 374: '4FB21', 375: '4FB31', 376: '4FC11', 377: '4FC21', 378: '4FC31', 379: '4GA11', 380: '4GA21', 381: '4GA31', 382: '4GB11', 383: '4GB21', 384: '4GB31', 385: '4GC11', 386: '4GC21', 387: '4GC31', 388: '4HA11', 389: '4HA21', 390: '4HA31', 391: '4HB11', 392: '4HB21', 393: '4HB31', 394: '4HC11', 395: '4HC21', 396: '4HC31', 397: '4IA11', 398: '4IA21', 399: '4IA31', 400: '4IB11', 401: '4IB21', 402: '4IB31', 403: '4IC11', 404: '4IC21', 405: '4IC31', 406: '4JA11', 407: '4JA21', 408: '4JA31', 409: '4JB11', 410: '4JB21', 411: '4JB31', 412: '4JC11', 413: '4JC21', 414: '4JC31', 415: '4KA11', 416: '4KA21', 417: '4KA31', 418: '4KB11', 419: '4KB21', 420: '4KB31', 421: '4KC11', 422: '4KC21', 423: '4KC31', 424: '4LA11', 425: '4LA21', 426: '4LA31', 427: '4LB11', 428: '4LB21', 429: '4LB31', 430: '4LC11', 431: '4LC21', 432: '4LC31'}
    state_options = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    with open('state_county.json') as json_file:
        county_dict = json.load(json_file)
    # print(county_dict.keys())
    # print(county_dict['AK'])
    # print(county_dict['AK'][str(1)])
    # '''
    # try:
    calculation_type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "CalculationType"))
    )
    calculation_box = Select(calculation_type)
    calculation_box.select_by_index(0)
    calculation_options = [x.text for x in calculation_box.options]
    # print(calculation_options)

    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button"))
    )
    continue_button.click()

    # for hi in tqdm(range(1,len(hipps_options))):
    if ll == 0:
        ll = 1
    if ul == 0:
        ul = ul+1
    # st.subheader("Hipps Status:")
    for hi in tqdm(range(ll,ul+1), desc="HIPPS Status"):
        # perc = int((hi*100)/ul)
        # if perc % 10 == 0:
        #         # perc = (si*100)/len(state_options)
        #         data_2022.to_csv("Scraped_2022_{}-{}-{}.csv".format(ll,ul,perc),index=False)
        #         # print("Exported")
        #         msg="Successfully {}% completed and mailed".format(perc)
        #         print(msg)
        #         filename = "Scraped_2022_{}-{}-{}.csv".format(ll,ul,perc)
        #         path = "./Scraped_2022_{}-{}-{}.csv".format(ll,ul,perc)
        #         send_mail(filename,path,msg)
            
        start = time.process_time()
        hippscode_selection = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "FormASelection1"))
        )
        hippscode_box = Select(hippscode_selection)
        hippscode_box.select_by_index(hi)
        hipps = hipps_dict[hi]
        print("{} Hipps started at {}".format(hipps,datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
        # len(state_options)
        # st.subheader("State Statuscode")
        # state_options=[1,2,3,4,5,6,7,8,9,0]
        for si in tqdm(range(sstate,len(state_options)), desc="State Status"):
            
            if si%5 == 0:
                # global state
                state = state_dict[si]
                tot_county = len(county_dict[state])
                # tot_county
                # st.subheader("County Statuscode")
                for ci in tqdm(range(1,tot_county), desc="County Status"):
                    state_link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "You must click here to select by state"))
                    )
                    state_link.click()
                    window_after = driver.window_handles[1]
                    driver.switch_to.window(window_after)
                    
                    state_select = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, "StateSelect"))
                    )
                    state_box = Select(state_select)
                    # 1 - 4
                    state_box.select_by_index(si)
                    state = state_dict[si]
                    # print(state)
                    # print(state_box.first_selected_option.text)
                    county_select = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, "CountySelect"))
                    )
                    county_box = Select(county_select)
                    county_box.select_by_index(ci)
                    # county_options = [x.text for x in county_box.options]
                    # county_dict = dict(zip(list(range(1,len(county_options)+1)),county_options))
                    global county
                    county = county_dict[state][str(ci)]
                    # print(county)
                    # print(county_box.first_selected_option.text)
                    apply_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "button"))
                    )
                    apply_button.click()
                    driver.switch_to.window(window_before)

                    raplate_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, "RAPLateDays"))

                    )
                    raplate_box.clear()
                    raplate_box.send_keys("0")

                    flag = True
                    while flag:
                        try:
                            element = driver.find_element_by_xpath('//*[@id="wrappersmapp"]/div[3]/span/center/table/tbody/tr/td/span/a')
                        
                            if element.is_displayed():
                                # print("conitnue not yet clicked")
                                continue1_button = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "button"))
                                )
                                continue1_button.click()
                                flag = True
                                
                        except Exception as e:
                            # print(e)
                            if "no such element" in str(e):
                                flag = False
                            else:
                                # st.error("Exception occured "+str(e))
                                print("Some other error "+str(e))
                    try:
                        row1 = WebDriverWait(driver, 30).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[1]/td[3]')))
                        row2 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[2]/td[3]')))
                        row3 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[3]/td[3]')))
                        row4 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[4]/td[3]')))
                        row5 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[5]/td[3]')))
                        row6 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[6]/td[3]')))
                        row7 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[7]/td[3]')))
                        row8 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[8]/td[3]')))
                            # //*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[9]/td[3]/strong
                        row9 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[9]/td[3]/strong')))
                            # //*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[10]/td[3]
                        row10 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[10]/td[3]')))
                            # //*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[11]/td[3]/strong
                        row11 = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[11]/td[3]/strong')))
                        # row1 = WebDriverWait(driver, 10).until(
                        #     EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[1]/td[3]')))
                        # print(row1.text)
                        template = {"HIPPS code":hipps,"State":state,"County":county,"row1":row1.text,"row2":row2.text,"row3":row3.text,"row4":row4.text
                        ,"row5":row5.text,"row6":row6.text,"row7":row7.text,"row8":row8.text,"row9":row9.text,"row10":row10.text,"row11":row11.text}
                        # print(template)
                        # template = template[["HIPPS code","State","County","row1","row2","row3","row4","row5","row6","row7","row8","row9","row10","row11"]]
                        data_2022 = data_2022.append(template,ignore_index=True)
                        # print(data_2022)
                        driver.back()
                    except:

                        template = {"HIPPS code":hipps,"State":state,"County":county,"row1":"NA","row2":"NA","row3":"NA","row4":"NA"
                        ,"row5":"NA","row6":"NA","row7":"NA","row8":"NA","row9":"NA","row10":"NA","row11":"NA"}
                        # print(template)
                        data_2022 = data_2022.append(template,ignore_index=True)
                        # print(data_2022)
                        driver.back()
                        pass
                driver.quit()
                scrape(hi,ul,si,data_2022)
            else:
                state = state_dict[si]
            tot_county = len(county_dict[state])
            # tot_county
            # st.subheader("County Statuscode")
            for ci in tqdm(range(1,tot_county), desc="County Status"):
                state_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "You must click here to select by state"))
                )
                state_link.click()
                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                
                state_select = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "StateSelect"))
                )
                state_box = Select(state_select)
                # 1 - 4
                state_box.select_by_index(si)
                state = state_dict[si]
                # print(state)
                # print(state_box.first_selected_option.text)
                county_select = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "CountySelect"))
                )
                county_box = Select(county_select)
                county_box.select_by_index(ci)
                # county_options = [x.text for x in county_box.options]
                # county_dict = dict(zip(list(range(1,len(county_options)+1)),county_options))
                #   global county
                county = county_dict[state][str(ci)]
                # print(county)
                # print(county_box.first_selected_option.text)
                apply_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "button"))
                )
                apply_button.click()
                driver.switch_to.window(window_before)

                raplate_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "RAPLateDays"))

                )
                raplate_box.clear()
                raplate_box.send_keys("0")

                flag = True
                while flag:
                    try:
                        element = driver.find_element_by_xpath('//*[@id="wrappersmapp"]/div[3]/span/center/table/tbody/tr/td/span/a')
                    
                        if element.is_displayed():
                            # print("conitnue not yet clicked")
                            continue1_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "button"))
                            )
                            continue1_button.click()
                            flag = True
                            
                    except Exception as e:
                        # print(e)
                        if "no such element" in str(e):
                            flag = False
                        else:
                            # st.error("Exception occured "+str(e))
                            print("Some other error "+str(e))
                try:
                    row1 = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[1]/td[3]')))
                    row2 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[2]/td[3]')))
                    row3 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[3]/td[3]')))
                    row4 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[4]/td[3]')))
                    row5 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[5]/td[3]')))
                    row6 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[6]/td[3]')))
                    row7 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[7]/td[3]')))
                    row8 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[8]/td[3]')))
                        # //*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[9]/td[3]/strong
                    row9 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[9]/td[3]/strong')))
                        # //*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[10]/td[3]
                    row10 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[10]/td[3]')))
                        # //*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[11]/td[3]/strong
                    row11 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[11]/td[3]/strong')))
                    # row1 = WebDriverWait(driver, 10).until(
                    #     EC.presence_of_element_located((By.XPATH, '//*[@id="wrapperapp"]/div[3]/table[2]/tbody/tr[1]/td[3]')))
                    # print(row1.text)
                    template = {"HIPPS code":hipps,"State":state,"County":county,"row1":row1.text,"row2":row2.text,"row3":row3.text,"row4":row4.text
                    ,"row5":row5.text,"row6":row6.text,"row7":row7.text,"row8":row8.text,"row9":row9.text,"row10":row10.text,"row11":row11.text}
                    # print(template)
                    # template = template[["HIPPS code","State","County","row1","row2","row3","row4","row5","row6","row7","row8","row9","row10","row11"]]
                    data_2022 = data_2022.append(template,ignore_index=True)
                    # print(data_2022)
                    driver.back()
                except:

                    template = {"HIPPS code":hipps,"State":state,"County":county,"row1":"NA","row2":"NA","row3":"NA","row4":"NA"
                    ,"row5":"NA","row6":"NA","row7":"NA","row8":"NA","row9":"NA","row10":"NA","row11":"NA"}
                    # print(template)
                    data_2022 = data_2022.append(template,ignore_index=True)
                    # print(data_2022)
                    driver.back()
                    pass
                
        # print("{} Hipps ended at {}".format(hipps,time.process_time() - start))
    # print(data_2022)
    data_2022.to_csv("Scraped_2022_{}-{}.csv".format(ll,ul),index=False)
    print("Exported")
    msg="Successfully completed the whole set by {}".format(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    return 500,msg
    # except Exception as e:
    #     msg = "Ended with the exception {}".format(str(e))
    #     print(e)
    #     # print(data_2022)
    #     # print("Last Hi: {}".format(hipps))
    #     # print("Last Si: {}".format(state))
    #     # print("Last Ci: {}".format(county))
    #     data_2022.to_csv("Scraped_2022_{}-{}_test.csv".format(ll,ul),index=False)
    #     driver.quit()
    #     return 400,msg

    
def send_mail(filename,path,msg):
        with open(path, 'rb') as f:
                data = f.read()
                f.close()
        encoded = base64.b64encode(data).decode()
        message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject='Your File is Ready',
        html_content='<strong>{}</strong>'.format(msg))
        attachment = Attachment()
        attachment.file_content = FileContent(encoded)
        attachment.file_type = FileType('text/csv')
        attachment.file_name = FileName(filename)
        attachment.disposition = Disposition('attachment')
        attachment.content_id = ContentId('Example Content ID')
        message.attachment = attachment
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        # print(response.body)
        # print(response.headers)


# st.header("Scrapper")
# ll = int(st.number_input('Enter the lower limit',step=1))
# ul = int(st.number_input('Enter the upper limit',step=1))
# placeholder = st.empty()
# start = st.empty()
# end = st.empty()
# btn = placeholder.button('Scrape', disabled=False, key='1')
# if btn:
#     now = datetime.now()
#     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#     col1,col2 = st.columns(2)
#     with col1:
#         start.text("The process Started by {}".format(dt_string))
#     with col2:
#         end.text("The process ended by {}".format("-"))
#     placeholder.button('Scrape', disabled=True, key='2')
# placeholder.button('Scrape', disabled=False, key='3')

    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # end.text("The process ended by {}".format(dt_string))

if __name__ == "__main__":
    ll = int(argv[1])
    ul = int(argv[2])
    sstate = 1
    data_2022 = pd.DataFrame()
    print(ll,ul)
    res,msg = scrape(ll,ul,sstate,data_2022)
    # if res == 500:
    #     filename = "Scraped_2022_{}-{}.csv".format(ll,ul)
    #     path = "./Scraped_2022_{}-{}.csv".format(ll,ul)
    #     send_mail(filename,path,msg)
    #     # placeholder.button('Scrape', disabled=False, key='3')
        
    # if res == 400:
    #     filename = "Scraped_2022_{}-{}_test.csv".format(ll,ul)
    #     path = "./Scraped_2022_{}-{}_test.csv".format(ll,ul)
    #     # st.error("Exception occured")
    #     send_mail(filename,path,msg)
        




