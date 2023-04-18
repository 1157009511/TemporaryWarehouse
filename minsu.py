import datetime
import threading
import time

import requests

def meituan1():

    headers = {
        'authority': 'cube.meituan.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'uuid=6fa72f13f67e40cd9dc8.1681347658.1.0.0; _lxsdk_cuid=18778214289c8-0b9ce13dbd5789-26031b51-1fa400-18778214289c8; WEBDFPID=v71z5vw951935vu2111x6x604uy56u2x81221785z6897958w1149u5z-1996707659200-1681347658691MKCQQIQfd79fef3d01d5e9aadc18ccd4d0c95073606; ci=30; qruuid=da5166f7-f503-49f5-aa05-72d107321fa8; token2=AgEUH1kALWGFzL_69T55OJ_MJrSKNu-hFvHMsI9Bog-HiEa8pa7hqvbmVnOTaWQMSbNrMx6BxMBi7AAAAAC2FwAA-TbELk0Ly7VnUhHSnAjmnLQLPGAPHHv_nE1VoP4M3z8aiXV8AVUfjKEE-CQ7IhEa; oops=AgEUH1kALWGFzL_69T55OJ_MJrSKNu-hFvHMsI9Bog-HiEa8pa7hqvbmVnOTaWQMSbNrMx6BxMBi7AAAAAC2FwAA-TbELk0Ly7VnUhHSnAjmnLQLPGAPHHv_nE1VoP4M3z8aiXV8AVUfjKEE-CQ7IhEa; lt=AgEUH1kALWGFzL_69T55OJ_MJrSKNu-hFvHMsI9Bog-HiEa8pa7hqvbmVnOTaWQMSbNrMx6BxMBi7AAAAAC2FwAA-TbELk0Ly7VnUhHSnAjmnLQLPGAPHHv_nE1VoP4M3z8aiXV8AVUfjKEE-CQ7IhEa; u=255286286; n=%E7%8C%AB%E7%8C%AB%E5%A4%B43333; firstTime=1681347715829; unc=%E7%8C%AB%E7%8C%AB%E5%A4%B43333; _lxsdk_s=18778c526b7-5c4-ca-c09%7C255286286%7C4; _lx_utm=utm_source%3Dmeizu%26utm_medium%3Dandroid%26utm_term%3D1200080404%26utm_content%3D78d087818efe4b72b83380f8d7509f79a166251995542156436%26utm_campaign%3DAgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024; logan_session_token=l5i528yk88mvvs0aro33',
        'mtgsig': '{"a1":"1.0","a2":1681358410525,"a3":"v71z5vw951935vu2111x6x604uy56u2x81221785z6897958w1149u5z","a4":"ace95ae1d44b8648e15ae9ac48864bd4fc092cd4b48f6700","a5":"SYjtRqdDxxEEpVXoschuBz8ZIuUdN6HWBdubFSVXjHd2LWITHDjDfFTSoO+4QX5UUdDmlrd61+GgPcNAB5YDE2Ly/Ce1PL2bTv8q1qCSQjt0lkuDhPcNT9XFln855cQGvfzL/W8PInGxdj3Q4mErVy0tM23anYAopM2/2ZpoV+JW3a8N","a6":"h1.2PvJ7yhOobsav0aKf7AX5mHmM6BMWi7AlN1ZdYsOdiFpIEdLoNMb+wcCvFrU4rJDe+ZKsFmOCIQBVeV+nP4bQhxRrFDu1ngp1cPnYXOPVtd/6PSgfSrVNzjvS4AFW2a37/WCuRTXPBTdq8NQ79b+XVgGcmATOzWSoPLBWF/QbjbOgCeyK8OW4xSph9KKUWZOqIKZhkAhfWKrtADlT+Vsyu1anEkesWOhRh7ZryWM7rM4lLbz+NvXGC+TajW26rOmuEFg45tFg4EXDehuLW0BOUQUPWiGYk8uJWJRn/tS9TnbBI3Wy8tm2wR3GmijLCWsSh2YQ7qZIu8pRhyLeZpBxUePEX0XVntUSu7FcWMJzKtE4yp9cW5du1A0Cmn+OVLsCyQCYSYZkbpWOK5Gf9cT/6xqSA71ytxfxafHvDl5EPVFRqNMsZ56AiJAMzoCDl2iIMnRsdfs4zu+W89xUXQ41h/VRu/pU/aTcWT6hjKC8nx2ZkA9wVb29s0KApQcCYhii","a7":"dbddc8cf53954046545289051ac7eec55d9473c3c6e3287df45712e2d67fab20","x0":4,"d1":"9704864d5281837ef4cd9d00200b73dc"}',
        'origin': 'https://cube.meituan.com',
        'pragma': 'no-cache',
        'referer': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    params = {
        'k': '228743',
    }

    data = {
        'playWaySecrets': '7702a589b9',
        'userId': '255286286',
        'sourceType': 'MEI_TUAN',
        'voucherSourceType': 'OUTER_APP',
        'weixinCode': '',
        'uuid': '6fa72f13f67e40cd9dc8.1681347658.1.0.0',
        'positionCityId': '402',
        'visitCityId': '30',
        'requestTime': '1681358408634',
        'nonceRandom': '8eebc038-badd-511f-0c2e-085ef5b2aee8',
        'requestSign': 'cGxheVdheVNpZ24sTVRZNE1UTTFPRFF3T0RZek5DdzRaV1ZpWXpBek9DMWlZV1JrTFRVeE1XWXRNR015WlMwd09EVmxaalZpTW1GbFpUZz0=',
        'mini_program_token': 'AgEUH1kALWGFzL_69T55OJ_MJrSKNu-hFvHMsI9Bog-HiEa8pa7hqvbmVnOTaWQMSbNrMx6BxMBi7AAAAAC2FwAA-TbELk0Ly7VnUhHSnAjmnLQLPGAPHHv_nE1VoP4M3z8aiXV8AVUfjKEE-CQ7IhEa',
        'cubeActivityUrl': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1',
        'cubeActivityId': '228743',
        'RiskForm': 'eyJ1c2VyaWQiOiIyNTUyODYyODYiLCJ1dWlkIjoiNmZhNzJmMTNmNjdlNDBjZDlkYzguMTY4MTM0NzY1OC4xLjAuMCIsInRvdWNoUG9pbnQiOiItMTExMiw1NDIiLCJjYW1wYWlnblBsYXRmb3JtIjozLCJwYXJ0bmVyIjoyLCJjdWJlQ2FtcGFpZ25JZCI6MjI4NzQzLCJtYWdpY0N1YmVDYW1wYWlnbmlkIjoiNzcwMmE1ODliOSIsImlzVmlzaXRlZFBhZ2UiOjAsInBsYXRmb3JtIjozLCJoNV9maW5nZXJwcmludCI6Ikg1ZGZwXzEuOC4yX3R0dHRfRE5xalI0M2VLS2lPcmFMY0xSOGRzb004dGpVMTVRMEdIOEhiVFA1L3RtYVlWZk54dW5Zb0RIYk1DZzAxaTVkYk9KYTlRQ0VhMG5VTUUzODQwQkYrV21ENTdSaEhlOW92WitUSW9BZElRWjVreDl1WXMwN1c1ZW5oYlUzd3BHZ1o0RW5oZkRzQzR4dHB1SVl3YlFFTTdOSFRmeU1jbGpScDlGOGdPUEdzLy96MitQQmV1RjJjTE95Mmp1anpZdnFnL0hoTzJpbnZadmRVMzdHR0ZPbjNSdkszVEU4TVZUZllWWnQvZzBxdkk1U2c1TkVRR0dMRitqblB3WVQxTTFmOGhQUmhoNC8zbmpESldnWWVtRmlnVUhCZUk0ak5qVTcyQVFtSS9GZGNWZTJHTk91VDFFZ1dENEVSUVJIZFdJdGZLZmpDMWtBR24wdm9TZCsvOEpFUHVmYjR0Tm5iLzdqUDlRTEgrNnNDNFFLZlZrN1NDekx0YmRnUnYrMVpYUkVVWHdPNi9YQ0xaa2VWc21mZHNuODZxL0N2bFRiRmFZUnhCOVU2TnZOdlJZaUZyMEhaWW02dEhZRjBOekQ5OFV2QVNINHBjU2xLcDJNcWR4Vm1jVFQ1MkYrRGxVWXQrbWpDMnpXU2IvaUhDSWFVSzV6Ykl5a0dNNlpiZ24zeVY1aVFySC9yQmxxbkxpd2lROHZ2UFRLVDJVV3JBR0tGZGhFdEptNkJubUhaMGkzU1VHVkFvd3Z3VUN6bEFkOHZjTjNmVEduZFdtOGZUdU10NTNYQThwSTBJM21pS1pvK2x0TThMeFRzcFRQUEh5RnB0dmFsRFdxTHM4dTdqR0dWMEpGalQwOUNjeVZpcng0V3JrZzNaV2FYajJMQktnVXFERE8wT25SV0pvNUg0ZU4zbzdqUVZ2K2RDVVlOOGZQbHBmM3ptYjV0SlpDRDBxWk94Z2hFNmE5QjFTWXNQbVIwQ2dxMit4Y1c5TzBWOTdDOHhsQk5kR081WTlCR3hac1A1ZXBYOHpoUUlVMDZNZTc0WGRJZTdvN0lBZ2lrcTFZS2lLUlZSWTgzMTVMMHFRdW5VdjhvaVFLUU90cGNOaEI5VGZHdlBTMDNZMU1kSDFqaUJJaERWeFpIUEdHbGRmZzJjRmpNV3FBaVUxYmozUllyNjQ5a0xISEZ2UFdxQ2hvaGVsVEhGM09iT3o0WG53U1U4VHlQOXJXMlplSHhXNWVJenJUbjBaQWFMdEFxN2EvU080L3MvS0dxYmsyb3NjV25lNWNEaTZjNDFXOW9US0FHTTVVWXpWVlhVbUF3OXFDRit5NFh6UElCQlJtN2Q0dlZZQy9zUVR1K3h3QW5GSkh0RVZCNGlzd3o1bFJiOWsrRTgxQ25pTDV2K21wK3RYWHZOaUdRSkdiODQwdFZtSEFubWhpUTNBa2syZ1NSZ3g0TUJNUlYrVHVORFJ1dUdlTXljdVFlTEFCamt2OVB0bE9jSnIwRk9zdHB6dW5tbytWZWlJQ3FocWdWUWozOEEybFRsQnhQT0Yzc1A3bzNSa0FEYzd3QS92SEhGTEVIY3VmaGpRNUJyMWh6L1JBc1g4NnAreW5la2t6UnUwK3g5ZDdQSFYvMG9lYXZvOTUrRzRiMVJkZ0tpUlArRlI5SXNaNTdFdWcrRnlEMXBCMGhrZ015Zkl2YjYvc0RJK2Zid1R2VXN2ZDBRTk03K1FKRjB4T3BLUUVTWmxtNHFGMmZ2d0FoME85QTlBaEZuMkQ4V2p5ZGZFSFBSR2Z2bzdyUUhvRVRNSHVxYkNPWmNNNFRndE9zMEtFRXFvQzM0M2tCTzNRR2gzQk50akF0MWl0Qnd0WStYNkVkTzF0MytwdHJQc1BreHIrc3ZQTzgySjFaVWt2KzArc2piTzJxem1Cb25aUWhNSWk5N2NtQTJEakMrL1RxbEF6U1dqaDdKdHV1V2hDdEJpYkdpaVlXdFMxMnVmbC9qUGVzT3VnY3hjZW9pbkZUMU9DdTE2aGpxUmRERzlZem1IVnpOQU04V1cxN1ZNUlRtdkl3ZnlPTEZKWitDN0p0MEZUOVorN2tYYlFKcTRkbnl3YmJvS0dOVGdhQ2R1dVo0c05UYUNOaWRCVzJJeVZ5OG9nN1ZueFdJL00zdXg0MnlWd0VNUjNWcTRGc1ZoMHlMUWNhcHp1cnc0ZHIzQTNRWGdZbGRaOHVUTTJyOHI1RHpOYytRcnJ5ekptNnllQ1FJRHRRQ0Jma3VQeDVMbFVpYVZhL1h6S0xaejdtMTJrRHVnMkF0a3AzSkNFWEdOM1Z3MTVxdUVzNXdVM2NoUXZ1S1d0SVBIUzJkcytnczZQcUY5SXNncW91ZFN2aFM3cWJ4MTRybTNaczNyaHJEbTZ3QTFtVlhDbHJteVVMMzUzSmtyYzRiN2pMRmFUcGdSM0FvZEpmTStkZ3BHSXR1ZjRLRlZyQjNjQkE3MTNXdnVzWG5aNjcxSk9ROW05V3RjRitrV1B4a28vNnlCRC9ZQmtGSkc5VWU0WTJvK3hsYmFsRzRrM1NFYlpZNmNFL3dwVVhFZmRad1lCSWFXRjRtaHEwUjJPVzF6NVRlNko2RGxmU0czeXhWL3lDM0c1cEU0U0xaUHlVRVkxK091VkNEQnE4T0hRVmZqRFovT2N0bTlrRnMzSEw5dUJoWWhraEJQWm5BYnNqQkM4NUZCSzU0Qzd1RXIvbktyK1BsODJKU0NoVSsvVERYNi9kV1ZPUGkzazhOQWVnUDBRRFlJTW1sVmhGWkVMWFI1UUJ3Y3N6V2F5a1V0RnE3Y2FTYTMxKzNpZ1V0NVMrL2dKM2JnVEx4LzBkRFlXTVBoempBUCs4TGVRZ2cyN3lpdElXUXdYOVYrUks3Vkp2ek5WUXc2K1AvL21ra3VFNFVyRTAxL0lmVVNzbWlDMXAwZ2pTMVVkU1hnQjJ4MUhzdnhFNzUzVlhTb1dneDJ0L3hMS1Vyc05wQmtEUllMTmREdDB4WktDTSs0dHBuL2FQcmI3YTEzYmthVEJzVnVZajRWbmIrNnVoRHNURXp6N3ZZcmE5Ykl3SENncm4wU0h2dVMzRmJKSjlvTkMvcUd1Um0xQVh6SXJzU29yQkRDOHlWNUc4ZTJIak1QVGhza0F3UWhjNG1FZVptbDBRRDFub3VtcjZZNC8xSnl0MUxLSUFaTmxtRnBOS0xKMWdSKy9XbDQvMHFIbXUzTGNIbnVnNXNrTFZsa1plT1lNS0xUOFRQQi9ZVnp2b1VkMzJzOVhjOFp6MGdZSmszeFM3Um9DUjZ1Z3FMZ2hpNHNBK0VCbzZWQk5jWjdmaGtZWHhOa00zaldXSitNSkdta3RUa3pPOFhnOHJRL3lONWxNK0xkR2FxcEZadFMrR2R2cVZ5T2NIV2Z2Mk1IVHNPc2N3TzA3Z3ZORFVmMUdKengzZTcvS3NES1FZYU8wZkhmQzBVR0lvVGl6R2YwTWpwVG1HYkFycXJaYmlpTDNVZng5SUVUWEVtU0U3OXVOcHd2Wi96WUFacm8zWG0yd01qc2FZZmE2eXd6eTZLOG4ydlpCSVEzMjJnSWdGc2k2Um04enkwQWJJQmxoaWZKYXFWTjVOTmtJVVo1ZVZjaWJBeXdqeXpxSW5SUDVsZEJaR2RNZz0ifQ==',
        'extend[lat]': '22.198745',
        'extend[lng]': '113.543873',
        'extend[appType]': '1',
        'extend[osType]': '2',
        'extend[version]': '12.8.404',
        'extend[cubeComponent]': 'redpacket-big',
    }

    response = requests.post(
        'https://cube.meituan.com/topcube/api/toc/playWay/sendCoupon',
        params=params,
        headers=headers,
        data=data,
    )
    print(f'{datetime.datetime.now().strftime("%H:%M:%S.%f")} {response.json()}')


def meituan2():
    headers = {
        'authority': 'cube.meituan.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'logan_session_token=q8s8vq5vyziii46yxuu5; _lx_utm=utm_source%3Dmeizu%26utm_medium%3Dandroid%26utm_term%3D1200080404%26utm_content%3D78d087818efe4b72b83380f8d7509f79a166251995542156436%26utm_campaign%3DAgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024; _lxsdk_s=18778c7c873-b2-a03-c7%7C267073166%7C88; uuid=2a1d76658d0d463c946c.1681350207.1.0.0; WEBDFPID=uu41wv75x0v05vw201898w41wx46wxvx812215169uz97958wu2x019z-1996718417683-1681358417196SSUOEKMfd79fef3d01d5e9aadc18ccd4d0c95077551; qruuid=aa171d64-25cd-401e-bb6a-5094701bdcef; token2=AgHSIJKcvGKc0Ldyn_ljW4Omz0ef_dDNpAU7JcYGJZH5EPiaa-E7dqOsOIOSbemTxAkMeS40lZYUawAAAAC2FwAAr2sIFa1S3e9je_wGObnHJQFgMFjxkHzUNQa9RLlwidWsuxDGOf-A0jRlf2JDoe4g; oops=AgHSIJKcvGKc0Ldyn_ljW4Omz0ef_dDNpAU7JcYGJZH5EPiaa-E7dqOsOIOSbemTxAkMeS40lZYUawAAAAC2FwAAr2sIFa1S3e9je_wGObnHJQFgMFjxkHzUNQa9RLlwidWsuxDGOf-A0jRlf2JDoe4g; lt=AgHSIJKcvGKc0Ldyn_ljW4Omz0ef_dDNpAU7JcYGJZH5EPiaa-E7dqOsOIOSbemTxAkMeS40lZYUawAAAAC2FwAAr2sIFa1S3e9je_wGObnHJQFgMFjxkHzUNQa9RLlwidWsuxDGOf-A0jRlf2JDoe4g; u=267073166; n=rGc364854325; ci=10; rvct=10; firstTime=1681358459372; unc=rGc364854325; _lxsdk_cuid=18778dd11dec8-002921c5fb65d4-5437971-505c8-18778dd11deba',
        'mtgsig': '{"a1":"1.0","a2":1681352487498,"a3":"uu41wv75x0v05vw201898w41wx46wxvx812215169uz97958wu2x019z","a4":"9581db79e2b6bfda79db8195dabfb6e23329ebede9965d0f","a5":"Qb4YKqWnQNIH3UNruZbEHtPn9wIQ4QLbwLtzCkDnPpoWrNrOfmc8JBWVs7LtF3rr3WUyZfHCKEQB7pJ1QJjD+Bfooh40xXTOTZl0mSJaxTnP6KS/fmtFHOhyplg8TUqrkL3GGggy2Uf/46z35RGKjotckzScD1JEBDSENF/XyQhMP0WA","a6":"h1.2LOkAOVARKRUj66TNvRnH0WM8OiUHlkncRt3aqs+Z7c8Ddoo4ACiyyIfSxyKd8Q9CgQVqDJpViGWseO/jHPoXXyN5rs2OFYw5sfepx9x9EtvRHMeILbdTLTX2KgxoOa1gpHiCcl34PMBNLweg/Ag/xHvAGJuYkdxc+z/c1WhFp5zvm9yN20eUqK0r+sm6pH2HQYUFNFny+2u2tCwkpshWywbEjUXa05Sx4btguWk71JogBuBc4J3Gb5s9S+Hk2AKZWNTuW0EtLw2XwkgufFuhZemKlqcf9EtHE0ROA+CS8GeJAyb6QEH/cyOqOmybV797p88xP8Jfigl5U8/W2nmfCsMEU8eceJazek1ZFsIEhzM=","a7":"dbddc8cf53954046545289051ac7eec55d9473c3c6e3287df45712e2d67fab20","x0":4,"d1":"4ba22b9ccaf856c1c44e0727925d5fc4"}',
        'origin': 'https://cube.meituan.com',
        'pragma': 'no-cache',
        'referer': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    }

    params = {
        'k': '228743',
    }

    data = {
        'playWaySecrets': '7702a589b9',
        'userId': '273063744',
        'sourceType': 'MEI_TUAN',
        'voucherSourceType': 'OUTER_APP',
        'weixinCode': '',
        'uuid': '1842c079b83c8-0e731f88b8907-26021e51-1fa400-1842c079b83c8',
        'positionCityId': '402',
        'visitCityId': '10',
        'requestTime': '1681358418557',
        'nonceRandom': '1557c6e5-b165-2def-1080-978be6c772e5',
        'requestSign': 'cGxheVdheVNpZ24sTVRZNE1UTTFPRFF4T0RVMU55d3hOVFUzWXpabE5TMWlNVFkxTFRKa1pXWXRNVEE0TUMwNU56aGlaVFpqTnpjeVpUVT0=',
        'mini_program_token': 'AgHcHpIk6s3v0kaGBudNpn2XJaVybL8wBT1RtiExqx0fYF-FC2wNGUKQNiFYoTjlHREmS9k-8JZ9MgAAAACZFwAA6uIiGqgqLeynKRQ3Unia2MvTBjLByWuPJQffTy2E9SEjzrPWMCy2GSBk2J7wTL98',
        'cubeActivityUrl': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1',
        'cubeActivityId': '228743',
        'RiskForm': 'eyJ1c2VyaWQiOjI3MzA2Mzc0NCwidXVpZCI6IjE4NDJjMDc5YjgzYzgtMGU3MzFmODhiODkwNy0yNjAyMWU1MS0xZmE0MDAtMTg0MmMwNzliODNjOCIsInRvdWNoUG9pbnQiOiI5NjAsMTM2NSIsImNhbXBhaWduUGxhdGZvcm0iOjMsInBhcnRuZXIiOjIsImN1YmVDYW1wYWlnbklkIjoyMjg3NDMsIm1hZ2ljQ3ViZUNhbXBhaWduaWQiOiI3NzAyYTU4OWI5IiwiaXNWaXNpdGVkUGFnZSI6MCwicGxhdGZvcm0iOjMsImg1X2ZpbmdlcnByaW50IjoiSDVkZnBfMS44LjJfdHR0dF9ORlJybzRQc1RHRUFJZ29xamlKWUdzQ251UTdmdVZHVytoTGhMSzhuMmFpTFNmdUxhajgzZytMY2tYcUJIN0I1bTVkV2d1OHZBVHhXWE1VTDRkcUdBYUpGV2VFYmtzRFZidHJrWmZqUWV2WDNmVTdjc0V6ZDI2SGMvTkljZUZia2dqdUlTcFRQeXZSS1VZMXh4VXA3UW5hQkVtekhEVmFFdHVjQW9KZm8vMTdqdjN1UzNIcFlMcDZVMy83MC85OUo0c2JtM2JDckdHVFlnV1BVTkdnKzZ0SVcxL1QrZzhBNkcxSTl0bjc1RTVTTFFiU0gzRlEyc0Y5WkVycEpxUHM5RmM1U0lVb3Mzckpidk43MDMwOTJNODFwbEFRUmgwbXFtT2duZHQ0bkM1M3ZJZ0x4d29RMENuYlV1TnU3Z2tkQ00zMHhaSWF3eTdLMEVSSWsxMXQ2ME1LbDN6YUZuajFqaThtTllkRlk1U1YrdXlxbjRnMXFtYXBiaFNnckRkemw3cFU2R3oxQ3VmM0Vwa1Y1TjdvL2xTY2JVMEw4azZuL3VKUjcxVGxORVRIUnFub3Z1dFNYTE1PeFpsYjZVUkpUZXVXUWowdW5obTQ0eWloa2NkQ2RlZ3VXaUFaNHdzcUtnaDJvZmJiamZTMkxoMGpVS0EzcjBZWDZFcVAwRXQ3ODBGVkVuajdWazAyMjVWM1E5bVVHZkhxaTdQRjlYUDg3b1pIQ1lEaThIZ21BNjBGc0J0UEk1YVNmWTV1azdPZDF4T3JrbFlYeXByYnBsaFNxUHJPQ1V1eEJMankyUXVwOHhPd2thaTZ0aC9CajlBMFpmTkxPRGRWTkd2dTdPT1Fzb3Y4MGFhRjJ3cDB6UmpodzBndHBVcVFzRHJYVldmSlBvb0EyZWFuWW5XZVhId1VpdVV4N2UyTDhqMmJnTm5MeGg5Y2xKQTMrM2FVZ2laejFsMjNRQTVkV2VmWlVWNjFnMThNcVBudkVEZEtMYzZ5aGQwSG1aMXF5R0xuVU4weGRRelFCTGxDdER6Z0RqYzFkL2RxZUZxSmJxRDY3ZllvWU8wVDk2UURTbFBERXNXc1NKZDlWa2ZKTnQ4cmI2TWQzcUd4ZVhKVXNlUWFHaDJKamh2dFpvWitjZHdFeVdoTkdUTExwZWRseDNFSmQ3bUNVSG5EdWZKS1UvYkhpeDNyenBQT3duVytpN0huTENtSTBDdzZJckpESkh0WmNIaE8ydlZZY05lLzg1Q29FeHpnZzRILzliVlRXektiR2dJK2pBOHhYRHlWaDZWWHNPejQ1TmJ5d2M3NnRwYXFSYkhpVUk1VDhNMG9haE9RRTQ4a1crRi93TE0xWDFzSFpBbng4OVJxeXhkdVNEVkh5WE82Z0luQ2lBcjRpWGpVeVpFbXVGSTlwNnAvbGFmeWYwUDNtUHNkWkZBdTZocWhxa004NDFWUHlTNndmb2t5cXB0V1NMN0pFM0d4Qyt4NFozNG5jQ2hGVDN0aG56T01ET3NzeUNUYTJ0bUplVnFTYXBTNHJ2RFhudUxlMURUeW5wVFNPb1RVQ0NYNlMxeHJmNXk3c3lPTWRzRTBnSmg2RWRLcHRwMUhNQzlOL1hMNU5DQTh1dnFqWE9YWkRHelFjRklZZkhaT3ZyckZmdHdxVFVYcWdCS3VEbVRvZGlzaG5pRFJtQU44a1hVNmQ2azVYVGpCdlJtY25BQ1pibkZSNVVvZzNvOENDTHBQNm50SU5MK2xuaEhXZEF0akE4a3RLOFNzZldwZGJLaWMzalA2TUhKWUxkQnJxQi9GbkJzY3oxSkMvTnQ0MWVTdGtPTC82OURydjlBMUpGeDJRVjNMa2tTZ21VRjRwQWhybis4QTduNmRkNnFFTHZtVG9lU2g4em9kaFN0d3AzOUg3VXVrTVFZWmlHeE53dmZMdDhKbXNVYWdZRWswQ1M1ZW56OGFCUGJ2TlByclF6WnY5a1NFeHRrOFFaM0p0OWpUNjVlYXd4SHcwbWRDTVpFWnNSYkMxRHAwTUZDMmdQMnVzY2RERkZDN0NRQmhUc1FLMVpUTHFNeE5VR08vdWt6Y1NxNHJMTkxVdHQ5OFlYWnZJZjRWNWcrbnBLNHpQSEN1a0xRNncxbzR5cjZnUW4zV3VCekUvTC9ZbS9Vc2xraXBBeXc2L2hNb2Y0VmpzUWgyT2sxVlZUdGlaQ282blpDWWlPU1phQjF1NnRBMUlVZDJHcFRQdlpvcW8xYTR1RGFNSURERFlOdkpFbVhzakZKM0RCcVBTR05vL2drcXVvRmlzQWJyb1pKVjR1QVJVdHFDU0Z6WEJxSHFDQ0lWVkU4Mk8rUjJZQW8wMmlEcGZWcng3U2UyVE9aRFlMOFoyOVhOWmxMN3cwYm0wUXlNbFk4aXAyZDlobWkvT2Q3R2x4b0szcFlPNXR2ZnFBS1ZsK2l4Sm5NSCs0SXltME9HN3pLa2JsL2k5cnFMakVWaWVQbUZwc1o4bUJXdEQvQVpEdXhOUWJQTHhhN1dSM0c1b09wN0IyNHdRSlJ3c1JJME00RjdGdlJhdFY2REovaTdNRzRsL1RWSWY0ZmJVRTNCN2NjeDA3RGdWQ1FYRHF1b1BlZDVzOGVNa2NVcGxtNmZJTWs5Z2hEYW96bGo0SzdrNm0wYk1XVDRPMytQSWRHUkNlc0VXVk1aZ3FaWWdVM1FqSGREVXFyTUZtWHNnRWVUcElyelhwdW1DVW9TdFUwbSs2Y2lwRmxaZXQzTldTMDZzOFZBamJsakgyWnNnK1A0by9iL1ExeldLdFBxdWZObXlGZmkvelVLUmxXN1JYaWErSTg0VWI4eXlxU3JkUmtiT3RKdTREN0pxUUc5NlNvMlZtVTBZNFhMK0tUQUFlRG4rZVNlUWpRNnMzQzhOb2lKMDlneHMxb3k1RXcvOTFtSWh0ZDdWWUYwOWdyUVA4L3hJbDVmeWRHTjBab29kSWhmMG9qMmNEcGE1ZDJlb2pwcXhuNzR1bzN1dm5WWjd4QzljTHhoUUR1OE01d05VakJCRnBYdXJzekVvNlpLODdGN1pWdW5RSDl0Ukh6bnNKUlFRL3h2M01jN2phRHZCNS9kQmpvM1NXcVVyUDRDeDJURVkzZ0Fyd0h3OVNEZ09KOWJxSFFwRUZJOE1BYXFwZkVCbFpNckF0RUdocUIvZEFicys3TytHbWRJUUMwcXIyRGVyUU1TV2IrRGdzbE1DOFB1eUxpazNaYVNJWDVTcjhGdURUS0JtZ1QveTV6MW1lbmdjWFR1V1NsY0Z3WnprVUN6Q3lMYi9iSVlPazkzRWdIamlJTno5VEh2YU45SDNudnNkRnV4ZXFFamh0ckNRRXkvTGRUVmhFS3l4ZkJuK0gyREoxNkp6QTB5VzZyWlhaaFhJT2Q2VStvR1hYT2VvQ1dWcHU0bmhKUG5kaVV1a1N6VjZTQT09In0=',
        'extend[lat]': '22.198745',
        'extend[lng]': '113.543873',
        'extend[appType]': '1',
        'extend[osType]': '1',
        'extend[version]': '12.8.404',
        'extend[cubeComponent]': 'redpacket-big',
    }

    response = requests.post(
        'https://cube.meituan.com/topcube/api/toc/playWay/sendCoupon',
        params=params,
        headers=headers,
        data=data,
    )
    print(f'{datetime.datetime.now().strftime("%H:%M:%S.%f")} {response.json()}')


def meituan3():
    headers = {
        'authority': 'cube.meituan.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'uuid=47840f83dbf744bca5a4.1681352593.1.0.0; _lxsdk_cuid=187786c92e2c8-046e0690fcf0e6-26031b51-1fa400-187786c92e29e; WEBDFPID=153827x691865x0vzx695w0uyz228270812213x046w97958v6601832-1996712594768-1681352594426QSAQESCfd79fef3d01d5e9aadc18ccd4d0c95078988; ci=30; qruuid=9bf602e0-0842-4611-9ad4-7de10fa17a7d; token2=AgElJXYmRzobtwmkPAL2-yuKLsPrGxb7pnBr9762w5ODgkp0TBEo4_O1RrVNrGBPKRtkPRwBG-79BAAAAAC2FwAAtH1bW7bcl7EGGluj3nnw7bP7_Oz5qLHN6Yt8ZhKt6SyEGoAJt6bU8mJs-1ioFjye; oops=AgElJXYmRzobtwmkPAL2-yuKLsPrGxb7pnBr9762w5ODgkp0TBEo4_O1RrVNrGBPKRtkPRwBG-79BAAAAAC2FwAAtH1bW7bcl7EGGluj3nnw7bP7_Oz5qLHN6Yt8ZhKt6SyEGoAJt6bU8mJs-1ioFjye; lt=AgElJXYmRzobtwmkPAL2-yuKLsPrGxb7pnBr9762w5ODgkp0TBEo4_O1RrVNrGBPKRtkPRwBG-79BAAAAAC2FwAAtH1bW7bcl7EGGluj3nnw7bP7_Oz5qLHN6Yt8ZhKt6SyEGoAJt6bU8mJs-1ioFjye; u=2218940878; n=qUm810746383; firstTime=1681352614983; unc=qUm810746383; _lx_utm=utm_source%3Dmeizu%26utm_medium%3Dandroid%26utm_term%3D1200080404%26utm_content%3D78d087818efe4b72b83380f8d7509f79a166251995542156436%26utm_campaign%3DAgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024; logan_session_token=1o9tspb6jkzs5xqro4hp; _lxsdk_s=187786c92e3-ad2-be5-195%7C%7C88',
        'mtgsig': '{"a1":"1.0","a2":1681352655749,"a3":"153827x691865x0vzx695w0uyz228270812213x046w97958v6601832","a4":"1eaae21ae239e06f1ae2aa1e6fe039e29f61c766f081fe84","a5":"YqmrZ5H2OwoT34W39VooNFFb6fNqHzxafz3xdk8stMFwxKWclPXFrHG2igPFxk1tTDRHHjpKYODIkekKBde1c8tyIar+AGHNisXboU8uIJrWa0P02yy9xtuxusoKOhWEW+YZAEhtV7pqx5bvOK7qjgC2/Y0DTNQCZe+9sScpOxrk6FlL","a6":"h1.2+t7RCTs9eAeKHIk7SbDtjvJD+uJp8iTzbVMv4wl3ggHSMDKVQK9FLKoCV/IOWgKmxsdwyCgQ9Oc5pm1r4N9bjpJdikWfSXftet3iCLHxU2G0mIUegnttkVeRGuN4bokCrWZtTfQMk8j739Ru1JRZcYTRHbS0+wDTfBfDcXxVnuDFkN+dv5XOWbtWnlUu0kX5SRO9ciFdMFqV+bJsaPMjNJLswDQCceVeIpf4H3p7B/B7JCMpQIv1BNxL76b2fJRhdVDtIsmkfnEfxwr8jh71hex4FxMJwN843wLKVXlkk8XVesUCVFw+4VfRqVKP2V8whO5a973l6UYDPL7R3WCx/Xn+4DRDw4KRf8p8qyNOZOU=","a7":"dbddc8cf53954046545289051ac7eec55d9473c3c6e3287df45712e2d67fab20","x0":4,"d1":"558fb8d5c52314760c1713a341d1cac7"}',
        'origin': 'https://cube.meituan.com',
        'pragma': 'no-cache',
        'referer': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1.',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    }

    params = {
        'k': '228743',
    }

    data = {
        'playWaySecrets': '7702a589b9',
        'userId': '2218940878',
        'sourceType': 'MEI_TUAN',
        'voucherSourceType': 'OUTER_APP',
        'weixinCode': '',
        'uuid': '47840f83dbf744bca5a4.1681352593.1.0.0',
        'positionCityId': '0',
        'visitCityId': '30',
        'requestTime': '1681358401492',
        'nonceRandom': 'ee01cc7e-7f19-6afa-9721-8f7314124643',
        'requestSign': 'cGxheVdheVNpZ24sTVRZNE1UTTFPRFF3TVRRNU1peGxaVEF4WTJNM1pTMDNaakU1TFRaaFptRXRPVGN5TVMwNFpqY3pNVFF4TWpRMk5ETT0=',
        'mini_program_token': 'AgElJXYmRzobtwmkPAL2-yuKLsPrGxb7pnBr9762w5ODgkp0TBEo4_O1RrVNrGBPKRtkPRwBG-79BAAAAAC2FwAAtH1bW7bcl7EGGluj3nnw7bP7_Oz5qLHN6Yt8ZhKt6SyEGoAJt6bU8mJs-1ioFjye',
        'cubeActivityUrl': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1.',
        'cubeActivityId': '228743',
        'RiskForm': 'eyJ1c2VyaWQiOiIyMjE4OTQwODc4IiwidXVpZCI6IjQ3ODQwZjgzZGJmNzQ0YmNhNWE0LjE2ODEzNTI1OTMuMS4wLjAiLCJ0b3VjaFBvaW50IjoiOTQyLDE0MTAiLCJjYW1wYWlnblBsYXRmb3JtIjozLCJwYXJ0bmVyIjoyLCJjdWJlQ2FtcGFpZ25JZCI6MjI4NzQzLCJtYWdpY0N1YmVDYW1wYWlnbmlkIjoiNzcwMmE1ODliOSIsImlzVmlzaXRlZFBhZ2UiOjAsInBsYXRmb3JtIjozLCJoNV9maW5nZXJwcmludCI6Ikg1ZGZwXzEuOC4yX3R0dHRfOUpuejBiZDZ1U1MxbDdBNXNvSnU0TTdycEJUM200WVl6OWR2UWR5TXY4MjFyMmFWYWRKY0dvdzE5a1B4cktMald6OUlDUkM5dURBczlqTUdETUZ6R1NjMzdwYjEvODRiZ0JqdWVmZENsUlFPOENGUGp2Y25hbS9xRHp5dGRZb3BIL1RObVRuTEYwSlZsdXpNVS9DTWpBUVp3MFB6b2dsQjdDZ2UyMkNDYjdlQTcreThZL3lnckRvNjFFK3gwL1FMcjQzdkdraXJLcXU1MkF3czdNVy9UMG1wblZGV01nVzZPb0lGVlAvZXl3YlJIM1I3VjRqUmdiVFlPVDFZSkdVVC9ueCtiYjZNd2twZUtWb3V2L0g0YUhmbXhCNTRMOXkxK3RjbUIrekhUdHkranYzalNBSHRlVGwzMndubDl0ZFJURmhJRVVSS2psdkhvMG0vUysyQ0xDZHRGMWFJeURnbUpKVks4c1hmcXliRktmTndZbStINDBYQ2NOS09CMnRmWUxpbnEvbG5pYXJzUkRFU2NQdXEwcDBzVkxqM2I1cEVrSWJMVGl2bldFblRKQ2JqRE5TaUhUR0FzbVpFOCtQVjhVRTdqbGpTS1kzV1Q3cGppbUhoRFFsdHcvL2ZsMlJVUVBDSkg4emg2dkFsNS9GSUpmdHNLVys3U2pldkNpYnYxYVBkcUkwQVJ6cVBhSGpMRThZUHN4ancrdGNDVFlzOWJBcFlvSU1oRXB5UDBSUXBhK29iTUJiUzdzOEJjcGI1bVp5c3I4dnZsMGtIcEluc21VY016SktCYm54bC9WVzhKc0QyeW1za2dadmFibGpWZVBUejVoQTMxWVR1NmppSVQ5cGdRYXZvTXo3cWtWTFg1dnZweFZYNTdhU0hWTEZnaGxHb0JWSDl2YUpPbmhHR2huOW0xdXNSL2VXRGNNVlJkenZheTFSQ1dKcFE5c3l3SU4vTFIyTDR1UFBxT2xmSDlpZWhacXI3QXBEdGxTWFNnT2VLblNBdVBsTmhJMmt2c3o3UUxPWlFJOFlhWGMxYm96ZGFRQmxETFlaNEZpVUtRN3ZtK21wWnBnRkRVbUd1N21hZFU1bFJxWTIyMkhhUUl1V0VlZDNrRnRwZW9TYWdiZnUxVk5IUitvRmFOSXA5Um02QndETnlNTkw1c3FBSlBYNlF2U3kyNmVjN1VLZkJHMFFBTjhtakxhNk9JYkh6eTBnalpsa1VLd09GNGpQZ2c3ZThxencrU2dBWkdqcHBGSzQ3aDFZeXkrTW00bzIxSmdHc1h5V3VtcVZJaG5CVndJNFJPRGJrY0JyTEw5dkgweUQ4R1BQZHpCd1pGV0ZDQWQ0Z29jTmN0SGF6NmhjVE9yZ1RadXR4TXVOdDVtU1ZaUUlJUWFPVC8ybXNCTDBja1NlYXZjUlJRRDdsOC9GMTFYK3o0cVhVeHA1WmZENjEyRzJBWUk0QmVRSXZSSnYzbUNpSkZhVjFVSk9POThZR09PNVpLUXBOMmZ0S0loWTNqYmF5Z25tZkwrZ2NBWElIRFBYbVBqY3F0NGlrdlZ3RVVsbmhWQ2xDd1ZDN3JzcHRDaHc5MXQzR3JZVSsxSnM5RDkwQWFlUGtPZ1U2TjZzcE5FN1BkVm9OVzhLa2E3QWxPbWh4aTBLMGZBUFo3MTVqODhDRnhrL0g5cUJuODRHMENFNjdLQkxqTFREWHk4dWNyWGxlSFpaQ1NseTNaWmg2SHh0dTRlaDV2Q2hMbkVYUS9uODA5RjNwMU8xSS82cFZHMkNFNGhhdjRtTHpPekpjOFFGNDh1ajJnbUp0YjR5ekwyNTQzc2sxcDJFR210VkdYOUE5UjU1SkhmSlRJanVBd1psd1BOemJKd1JkWUUwai95dExDRUJsMnVWR2xGaGo0NGtCWW0vVnRyQk5xbzFwdGlZZ1VSdjlnODl3Tmk3T1JveFR2ekJUOXZFSlp6LzV4ODkvK2dIUUFveEgyVmdQb2VPaitGSkkvaEpQNzJLWi91NnhmOGQ3T3dzV1lhcUNnQzg1WmdjcFZEMnFTdS9iaDYrWjhPdjNvbDlQNmtqMlZoOXlnY2IxQlpMdHRtY09mR3d3dHJ5NytKcWJabmttb2Y5dXFKUFJ6SlAvandSMGxld3VhaGg2RlN5bnhvbGpWdm9taHRqZVFzK0VVdHNYb3pTNWhJU1p6T0ZYSFJSVmZvSXk5Wk5yZE0veWR4QlM2cW9XWlkwWHExT3FrOExXNTlaYzA0ZFlia1kxb1Q1bW55bmI4TTltcFVHd2owRnVCSUhUN29JRkdFcWdQbXdkRWFkai9YRnJJSjM5QlQ3S3VWYTNJMklrVXdlTFZlS0l2S2pMWXJ3dG1HS2N6UzdTbEFLZlFUWHF0QTc2VlFmWjV3RUVMUWNpVnJhbmlhUEpUcjNlZXFFend6QXFaQWxrdlQrOU83akVVSUhhWGM3eCtLdXE4MWNKbFJBMEJBRnc5S0VuV0pENC9mbTRhMldiUG9IdGcrMCtqSHpCdy81TjVGVWZOSFZSSDIxSnNzL0pQNDB1eVFwZ3FlQTdiRkk1WUJyN0hhMk1yZ1V3by9tR09RaUpwS1ZoZnJ0N0tiS2ZybzVYbjdoZi9ZMlYyclpnNlNqcGIxallxZkUrSlcvOGY5eHpFaXV1aWpJRDMyV1VmV1FWMEdDTjQ4WXpTZzhsRFk3SnBFeitOVW1xUHpJa0RtZGJkNGI0U1p1VTJleldpRkpRTHVLamYxMTN2OFRURUVIdlpTWU0rbkhEVjVkWUFwWXNmejJReWdGcWx3OGJkb0d5M0R1UVJCNEtzSGU1TUIrSkw2VGE0ZWhlUGduaGx5K3FDRmw4c2dNb2I1THIxM3ZFL0EwNmFMRUw1ZWR4TmJoS3RVSlc3RlE2LzUzUTl6aTl3d2xQYStGRlZZdkx3OW1pY0VKVkw3MVNUbzVYV1BTeWJ2S29TN3F5aGU2cVB1V1o3aTJGek9vSU5sWFAzTFBpdzFmZno4Z0paSTJzb1dUSVNUSnkrV3BxWFF0UGV4N1lIbW5XNWVIbE9xQTRPZXAxRmh6VjhBaTFTT2JhMjlQSzIzd2tMZDM1eDVlTEUyU201MjBrakUvczhMcTRUS2llbTRuTUNQejRzN3c5ZksxUDAxZjJRU3dyNjVYK1BaUEE1Nk5BUkY0cEVEZ29jRVNnZzFucUNSMVhXK2hSS3VBZ0g1K2pzQ1lIVHJVUWtac2xBc2xWbmhYY29FcjNYeGJ1NFhZaUt5QitxelFnOVlaVVYrSTgvekRIKzJZdkoxa2Q3aEJwa001cHlLNmF6a1lDR2l5a1owWnhZUS9Cbk5xV2tnSjcxMW9zNFJwWXJJQUtzZVZ5YnJWUytCOUp0UXoyYUpaMDFwbmFGSTBHTHFjNTAvOHdLL1p0azZUb0Y3UDNFSHZvYW16Z0xyZGRLNUdQVHc9PSJ9',
        'extend[lat]': '22.198745',
        'extend[lng]': '113.543873',
        'extend[appType]': '1',
        'extend[osType]': '1',
        'extend[version]': '12.8.404',
        'extend[cubeComponent]': 'redpacket-big',
    }

    response = requests.post(
        'https://cube.meituan.com/topcube/api/toc/playWay/sendCoupon',
        params=params,
        headers=headers,
        data=data,
    )
    print(f'{datetime.datetime.now().strftime("%H:%M:%S.%f")} {response.json()}')


def meituan4():
    headers = {
        'authority': 'cube.meituan.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'uuid=e21906ea81e14bf68f19.1681352761.1.0.0; _lxsdk_cuid=187786f20cdc8-06b65fe05600f7-26031b51-1fa400-187786f20cdc8; WEBDFPID=6zxv815880x75y160839xzzu73x8y0y4812213u76y8979587x33wu64-1996712762306-1681352761976CUAUUYUfd79fef3d01d5e9aadc18ccd4d0c95071361; ci=30; qruuid=b231b0e4-cc9e-400f-9ee4-4a6d0b458c69; token2=AgF6IYijvDkWnlBrJ3x5_O0EBHRy7hGIErSAjIZaBc0pKEtXjk2xRjmUZ5ec5SX8EBgpLjAECPeEdwAAAAC2FwAAKz3RFYvqXpepbjKxpqr8pw-bbGlwpsDyMdLgrlK7AFplTIYCi7UjquVLT-HSQG-Q; oops=AgF6IYijvDkWnlBrJ3x5_O0EBHRy7hGIErSAjIZaBc0pKEtXjk2xRjmUZ5ec5SX8EBgpLjAECPeEdwAAAAC2FwAAKz3RFYvqXpepbjKxpqr8pw-bbGlwpsDyMdLgrlK7AFplTIYCi7UjquVLT-HSQG-Q; lt=AgF6IYijvDkWnlBrJ3x5_O0EBHRy7hGIErSAjIZaBc0pKEtXjk2xRjmUZ5ec5SX8EBgpLjAECPeEdwAAAAC2FwAAKz3RFYvqXpepbjKxpqr8pw-bbGlwpsDyMdLgrlK7AFplTIYCi7UjquVLT-HSQG-Q; u=200125867; n=fqE326478439; firstTime=1681352889030; unc=fqE326478439; _lx_utm=utm_source%3Dmeizu%26utm_medium%3Dandroid%26utm_term%3D1200080404%26utm_content%3D78d087818efe4b72b83380f8d7509f79a166251995542156436%26utm_campaign%3DAgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024; logan_session_token=8z6eksp4l30o7lhqtro7; _lxsdk_s=187786f20ce-06c-573-a0d%7C%7C84',
        'mtgsig': '{"a1":"1.0","a2":1681352923842,"a3":"6zxv815880x75y160839xzzu73x8y0y4812213u76y8979587x33wu64","a4":"e66d6d86213c40ba866d6de6ba403c2144f71c9efeb720bf","a5":"LzmxMvT3R/m0Rh+9WH0SpujbqMD3vioA1xI6fd2fptAW7UftO2JmXpWmaXroX6xckcIhQWTQ2PxWHaNccV+o0/+h2hYUsIhFD7Yx/iclLaE3X91SB98XmB7cxHtILxzfPR+kKV5hQ2WBUyOu5qiRzUCd1z4XBe+M2htNQUoDJDICn9re","a6":"h1.2xKbMBfm1KcWM9ImsErGr3rBItJQfpPxJhbyngcnQfJG2FnZsWn4jNseb0gOGUJi7NknCypXz74qRdc7qlueznW4dFf2wOnAurN75eHe4GF/DbDErldr0RTMgCQih8K8WYifxCAkE51A2Nogn+a2LriZ3LyFajcDQpYCb2tM5iqqAZ7udDDDW5tpf+7ALMyu66vB3Ri1bz/eDEQjh6lD+6UnOkPrQGyc0+RSWSBiVao0sXnZ0LNPY7xYX1+nWohPrybZD4tYhCpXtrwtfa9R9p38IHbyYJZGCnDJKxHTdiqYjLKZDb3kXo1ryLapZshroAi8KiKBTeYeFccAkQaL4QunvFsb+0zACb1LM91upknk=","a7":"dbddc8cf53954046545289051ac7eec55d9473c3c6e3287df45712e2d67fab20","x0":4,"d1":"7dfbbb7040efe915fa75146d99f81682"}',
        'origin': 'https://cube.meituan.com',
        'pragma': 'no-cache',
        'referer': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    }

    params = {
        'k': '228743',
    }

    data = {
        'playWaySecrets': '7702a589b9',
        'userId': '273063744',
        'sourceType': 'MEI_TUAN',
        'voucherSourceType': 'OUTER_APP',
        'weixinCode': '',
        'uuid': '1842c079b83c8-0e731f88b8907-26021e51-1fa400-1842c079b83c8',
        'positionCityId': '402',
        'visitCityId': '30',
        'requestTime': '1681358404540',
        'nonceRandom': '5049f2fd-8a3a-28a0-3199-ff8de1d3cf8e',
        'requestSign': 'cGxheVdheVNpZ24sTVRZNE1UTTFPRFF3TkRVME1DdzFNRFE1WmpKbVpDMDRZVE5oTFRJNFlUQXRNekU1T1MxbVpqaGtaVEZrTTJObU9HVT0=',
        'mini_program_token': 'AgHcHpIk6s3v0kaGBudNpn2XJaVybL8wBT1RtiExqx0fYF-FC2wNGUKQNiFYoTjlHREmS9k-8JZ9MgAAAACZFwAA6uIiGqgqLeynKRQ3Unia2MvTBjLByWuPJQffTy2E9SEjzrPWMCy2GSBk2J7wTL98',
        'cubeActivityUrl': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1',
        'cubeActivityId': '228743',
        'RiskForm': 'eyJ1c2VyaWQiOjI3MzA2Mzc0NCwidXVpZCI6IjE4NDJjMDc5YjgzYzgtMGU3MzFmODhiODkwNy0yNjAyMWU1MS0xZmE0MDAtMTg0MmMwNzliODNjOCIsInRvdWNoUG9pbnQiOiI5NTcsMTM4OSIsImNhbXBhaWduUGxhdGZvcm0iOjMsInBhcnRuZXIiOjIsImN1YmVDYW1wYWlnbklkIjoyMjg3NDMsIm1hZ2ljQ3ViZUNhbXBhaWduaWQiOiI3NzAyYTU4OWI5IiwiaXNWaXNpdGVkUGFnZSI6MCwicGxhdGZvcm0iOjMsImg1X2ZpbmdlcnByaW50IjoiSDVkZnBfMS44LjJfdHR0dF9aQTZudVA2eDhJenNkRjVOZ2F3QUxXdnRWVXZwcXhPRjc3aERaWW5NWlJ1WmdiQStmdFdSRkZxVVpITXRjRVhKTFM5NllKR1RjdEZESk1EYjEyUkF2eC8zajFRdEYyZzdXK2tmeXEwNmNlOWxObnd3Wi92Zmp6MzhZVjhrcVFWSDZzWFoyT2JLNDk0YW4vaFJCd2RNcDVzMlhFeEZubFRMSlQxVnFuNmI0YWlZVXMxdHNyWE8zQmIySkN0RTQ4RUtZWWlOWGgvRWFSa28rV3VZMkYxTDVHRlY2SC9QbGhaaklLTlJRejE2TUdTNWowNUhwNEdnV0ppcFNHd3RpVU9abkZFWklHWCtoU3JzYTQ4OHdjWFhtYS94OG5hTHZmSXJ1bUMvWGlYT011bU5WUDE4c0RtZHhVclZnSzI0U0lZT0lUODRJaDlPTEx4eXdDMVFhVi9MWHIyK1pZR1JtQ1huTjdzVUJzT20xbmgwbUNiRHNFRjRMa3JISXpjcVJjN0lsTUJsbEJObzBiZjVoTTF2QW5CWlpPYXhaQjlsY21OUkpXaWY2SlRJQldGSkMwWFgvYUVUNnY3T1hIdG5zelg1bzhiNlcxWTVxU0xkVzJGT1E3TnlKSFJkRnlJYVd6czJxL1cxZjdnOVh1YThSTitSNDNhN0FFUmh5UzRka0ovaHBiZHdudEFZRGVNNnhhQjFzVXRyWXg3NWRaM2M4WE4wU1BIM0FZVTR2VlVWWTFXOEpPWEJmOFFGK1ZZL0dKRHpidVAvRmg1aTVBVUNwQkFZNnFrQnl6dEJ4aDZWMlNpWlVFRlpHNG9BUnF6SDFiYlp1bk50bWs1Nlp5N3F0UTBqandoZjYvLzJ1YnQ0K0E4enBEY1QvTURHcmd2SW1lZkdkemdxQkdTeHg5N3FyVVVzdXgvdGhjNDVrU1dGMHdXS0poWjE4ZGp2UUttVXdqazdYRGVhcWxIS2hGVlRkeitEV1Y3T1BkYnNTdEtoVGRYZG8vS0ptMVFjcWJhTmo2bGlsaDQ4MHZ3V2JnQWdVYlRXZ2hLSE42aGJLRUZvMWcvRjdFYWlhQ1Ric3R3cXdsS0NPS2J6MUcxRTY1dSsvaFpqME9iQ3VCNzlrQW5iSzZwRTZVeTFCZ2d5U3EvZkl0cmN0R1ZzRE15bVlnQVcvajhobGZ1VDZmU1dRNy9XTEFUbmlhcWZtMjU5NUxnM1BPTVk0MVprdzdhNlNycWswa0ROYWd4NGhrM3JIQkYxNktiNlFSUHpkeFVCbk9RSkdKQmVnQ2FhSTRNWFJkR09sdmlYU0ZWbWF2ZE5TdmtRU3A2dlVwOXZMTDlJS3pyZ01CZmxkUGhnWVNreUxHZTlvNUFSVXpZSXhSd05Ib2R1bllNS1JadXBOY0ZyQ0QwMlZXR1czdHg5L3FweWp3ZTgvNGhGajIvVkJhcVgyTGdUVlYvQmRUZThMbjRJQkxKVXJVZDFMVjVOZldlSC9xVjF6T2VIMjUvS05qN3BxVVpqcFNBWVpuekl2MXBscXZWaXM2b3F5MGxOdTlDbkdnQmNuTFNyejR2aCtDbUh3VWRLSHM2QmxIcDFscm1MRGpWZ1RzMmpCUkFxM01wYU1haXNPNGxKQWF3VVlKRkVJYS8rV1ZXbEpXSENwUUxFZDduOVczREVIMFVhYVZna254Wm1DeHpUSVJvcVB5NDFlSE9JYktJYjJBQTdlejVRRXMra0R6Mnd4emNncUNVVFZnbW1YalBwN29mSkxFSTZvbWZTZDJFMmFIT1lzTGdPeXBvWE1meGRoN25IYmw4MjI3NloySE0wUmhwK1lQeEFzU2YxMVFLWkcwNVhQbEV0MUZXWVBVTjRXUms2eG9rcmlXZzhSZjJ3RWZaUGwyRllVV0dFQ3AzK3kxU1loNVlHUzNHVE1icnZzRVlpY2tic3pCckhTYk1DK2Q2QlhvcDZjSnFsc3paT1JYeUV6RE1LaEpaYWQ0ZVRwdHBqb3VlZ1ZseWJDVno1U1RoejhLdWdNYWlzZUdaNHpxbmxqQXg1YmRBUkpXWWRYVkt3ZVdka1JUMjRRb2dXOWYvNGw3OGJvYjkzdzRiZXYyNHBOdGRIN3NoUURTemhuNEh6Q1N2ZG84T3A0ai9kMWxOTW5iMXlPMS9WaTJ1TGlJY2ZMUVpCakdrcmJrNE4rT0hDQWZleHE0ejRWdUFWUnZ1M1hQQ1VwMDdEZ0NJSUREbHhmRUdtdU96a0Fxd2VjNFYzejJ4dStFT1p6VHFVZ2I0WGFXbjh4SFE2OENLVk9saitzYlI2ZU80enR3ZUUzR0VENmFpSFJidi83bEh5U3pJbEg3bUZzbnA5cUNWWnVzd3hxRVVJaTVvOXIxQi83MXIrUzBCRkE5ZWJKWkJaaGJWby9teE1odkxIc21maVdzMzNSU2lqdWRsVXBuT0QvWFdNVEhUdWdpKzdsZlQ2cGkzc242ckhNbHFiOUZzT0F4YmcrcnMrbXc2dWhWeFQzWldCd2p5bXhHTFhiNEdxaFJPOENoRmpRclUrYVNwNmpIMFFaNllLT0NxekZUMXJPU0hwKzFVVjFDWHU3RVdEbjRNOFZvY1VIanBUZHFrVzUzOC8yMWJBakdSb3ljTTRKYVlVbW9GMmxSZEJTcVY4bVdtcUtBTFZWbmUwTHB1bUg5UUxDMFFSVkRvTDMvYXdhdkNhaFJCdk1rY2tRVmZ4aTNrMGx3OStIMzVwQTZORmd2TSswMWwzMmtpLzF3Nk54WDExZkVGOWZhN1hQR0dTWGVEaXQxOTJTQW5tNytvY0hqY1RLMzRhOFQ4Z1BTQmcvTFFwcHptMWk4Z0JWWjRFQ09iaHNzWGM5RFF2UjVicEd0ai9RTlhVQWpDK2U1R0N1ZjVPb3NpTTFWcmwzS0p1RTErcEVxRnJoL2plVkdDVWZyQ3ZJMmlTaHBqcW4xOGY5L2R2eGlDUXdFckRwWHhEMy9MQUhvTk41d1ZtUWQwWmlrcm5TR1ZlZXFxdXQ2UlhTVEZsTU0xZ3RXYU5hZC9jZmQ0WDM2bzlhZTNCTUt3L2NXTG9Nd3c5UDR6bi9MV1NBMDBZcExjY3FKb2tEcHVKTnh0L05TdTFUTURNUTZsTklsTHo1R25xdkcrYnZoajg4UDgxVEs5dVZ6d1dzTjZGaFVVQjBoUmpjQ3NNSTYvR0V6VmhTbkFHVkFLR1k4Y0RQV3J3RmJFMzhPUTJQNkg5OEpDQmtCYi8zNmZrSFBDdDFKUnkrNE54QTVpNGZGSWJXSUkyS1FKUkR0L0k3U3FjTnlNWXU3WHNZbi9GNGo4NmU2VDV1VzFMMm9sczdTNS80RUpQVU03QnlhOUhxK29QT3BGK21TOXg2SkVCeHFBUW1DK0pFNmJXZGJPcUlDS0ZucWNIVXdkOEtuczZFNmphS1hJbVFDeHBCc3VWcUNUb2dGajBydz09In0=',
        'extend[lat]': '22.198745',
        'extend[lng]': '113.543873',
        'extend[appType]': '1',
        'extend[osType]': '1',
        'extend[version]': '12.8.404',
        'extend[cubeComponent]': 'redpacket-big',
    }

    response = requests.post(
        'https://cube.meituan.com/topcube/api/toc/playWay/sendCoupon',
        params=params,
        headers=headers,
        data=data,
    )
    print(f'{datetime.datetime.now().strftime("%H:%M:%S.%f")} {response.json()}')


def meituan5():
    headers = {
        'authority': 'cube.meituan.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'uuid=74313ba89a004f689378.1681353116.1.0.0; _lxsdk_cuid=18778748effc8-095036e9059f49-26031b51-1fa400-18778748effc8; WEBDFPID=0v6u6vuw221x5z5707v95w763086v4vy812212508vw979582z34777v-1996713118210-1681353117880GIAIISGfd79fef3d01d5e9aadc18ccd4d0c95074237; ci=30; qruuid=68fcd8b0-2711-4623-bc74-cd417660f979; token2=AgF6JOFuOMQCrVkOpYVfUxdSFLc_Jv7m1eXbPMVmEW2p-JMLL6OsnBAIV7Kw04I35ZK5ptaR4SDowgAAAAC2FwAASc0J_aKkQBWUB9fOlQM4U1ySlb6VxeiWZsAK_Hp_lbWoAjlc3Z_rnYzdKi61FzB9; oops=AgF6JOFuOMQCrVkOpYVfUxdSFLc_Jv7m1eXbPMVmEW2p-JMLL6OsnBAIV7Kw04I35ZK5ptaR4SDowgAAAAC2FwAASc0J_aKkQBWUB9fOlQM4U1ySlb6VxeiWZsAK_Hp_lbWoAjlc3Z_rnYzdKi61FzB9; lt=AgF6JOFuOMQCrVkOpYVfUxdSFLc_Jv7m1eXbPMVmEW2p-JMLL6OsnBAIV7Kw04I35ZK5ptaR4SDowgAAAAC2FwAASc0J_aKkQBWUB9fOlQM4U1ySlb6VxeiWZsAK_Hp_lbWoAjlc3Z_rnYzdKi61FzB9; u=35065366; n=%E5%B0%8F%E8%81%AA%E8%8F%9C%E5%A5%88; firstTime=1681353178056; unc=%E5%B0%8F%E8%81%AA%E8%8F%9C%E5%A5%88; _lx_utm=utm_source%3Dmeizu%26utm_medium%3Dandroid%26utm_term%3D1200080404%26utm_content%3D78d087818efe4b72b83380f8d7509f79a166251995542156436%26utm_campaign%3DAgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024; logan_session_token=pg1dxgu1uujp5plcxdv5; _lxsdk_s=18778748f00-a81-4ad-aa1%7C%7C34',
        'mtgsig': '{"a1":"1.0","a2":1681353263312,"a3":"0v6u6vuw221x5z5707v95w763086v4vy812212508vw979582z34777v","a4":"cdc4a8f3f933e79ef3a8c4cd9ee733f92360b2b5bd87814c","a5":"HGN5bbbEJtbWqntiRuuVyWlJVOQSnxADWNydyajznYVBu94jgLVHeil4p3LKzqvBE6n2xfs8ndGejnpemf5Nk3uvqzyepcsVBEnMAwlIHzokUzOTUmJKcb0IXP53Lu/8EFBh8jdnO3r1oGIugXsRKWUlDycgwS7zjnQR/SoqUY5E0u5o","a6":"h1.2CVOtABgwoDEj7I5Eg27Ge4hOzedG2h7wC6mo1oitR1w6NvA4mp+Pz8JWtfRdBqmRCHFG9xqpeAqeF7pzPJZ0/mIqnza9vutsI9yRW2gVS2w/C77CeCbvyt9YWLnjWO9zee6dIeFbfglWvveMDbWuk2Gzlv+hKhuHhEBUCY2W8QKGwnDqroLPJx0h8iNWRAOtd9mhgOPaOgIWwmkCk5wd/ZRwosK3LWbjPxcZtE61/O54AOmUCDENSYiI3Flk//9r6SuwYqY/wkBVa2FRdz1Q5xXr7tqSkesbNNRWpkzc6l2cSAe9OSSceEnsIV8Vh5NvboD8yAE+K6Ka/J4BIW9oM/CwZuvI/kWjWlw4TBTrDtSsWpIfwyjbEw/h4TI7JlBd3qN704BSaCnCxTd0GxsAvLI1fpnZ8jF+m2Afaj0wwtYYdsmeOgbdg5KDlFHFqWzFM/yf0LriL1JI5rs48+HazsVwS6KTrBHReM3RlCYwKWasOM5gct4pNfPrwbt2hUiN","a7":"dbddc8cf53954046545289051ac7eec55d9473c3c6e3287df45712e2d67fab20","x0":4,"d1":"0841da4329a973ba6d8713e007498178"}',
        'origin': 'https://cube.meituan.com',
        'pragma': 'no-cache',
        'referer': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    params = {
        'k': '228743',
    }

    data = {
        'playWaySecrets': '7702a589b9',
        'userId': '273063744',
        'sourceType': 'MEI_TUAN',
        'voucherSourceType': 'OUTER_APP',
        'weixinCode': '',
        'uuid': '1842c079b83c8-0e731f88b8907-26021e51-1fa400-1842c079b83c8',
        'positionCityId': '402',
        'visitCityId': '30',
        'requestTime': '1681358408534',
        'nonceRandom': '2a414240-55f7-b1e0-c01a-0ae02c44fcc9',
        'requestSign': 'cGxheVdheVNpZ24sTVRZNE1UTTFPRFF3T0RVek5Dd3lZVFF4TkRJME1DMDFOV1kzTFdJeFpUQXRZekF4WVMwd1lXVXdNbU0wTkdaall6az0=',
        'mini_program_token': 'AgHcHpIk6s3v0kaGBudNpn2XJaVybL8wBT1RtiExqx0fYF-FC2wNGUKQNiFYoTjlHREmS9k-8JZ9MgAAAACZFwAA6uIiGqgqLeynKRQ3Unia2MvTBjLByWuPJQffTy2E9SEjzrPWMCy2GSBk2J7wTL98',
        'cubeActivityUrl': 'https://cube.meituan.com/cube/block/875151cfe3078f72e4ef/228743/index.html?phx_wake_up_type=mtapp_entry&phx_wake_up_source=hotel_home_page_tab&phx_lat=22768720&phx_lng=113846081&locCityId=440300&cityId=440300&dateBegin=20230402&dateEnd=20230403&phx_ad_delivery_id=static_slot%3A14131%3A236&f=android&utm_source=meizu&utm_medium=android&utm_term=1200080404&version_name=12.8.404&utm_content=78d087818efe4b72b83380f8d7509f79a166251995542156436&utm_campaign=AgroupBgroupC0D100E0Ghomepage_category2_20__a1__c-1024&ci=30&msid=78d087818efe4b72b83380f8d7509f79a1662519955421564361680446130764&p_appid=10&utm_fromapp=wx&lch=appshare_7b5956d2dcd65c2dA1',
        'cubeActivityId': '228743',
        'RiskForm': 'eyJ1c2VyaWQiOjI3MzA2Mzc0NCwidXVpZCI6IjE4NDJjMDc5YjgzYzgtMGU3MzFmODhiODkwNy0yNjAyMWU1MS0xZmE0MDAtMTg0MmMwNzliODNjOCIsInRvdWNoUG9pbnQiOiItMTE0MSw2NDQiLCJjYW1wYWlnblBsYXRmb3JtIjozLCJwYXJ0bmVyIjoyLCJjdWJlQ2FtcGFpZ25JZCI6MjI4NzQzLCJtYWdpY0N1YmVDYW1wYWlnbmlkIjoiNzcwMmE1ODliOSIsImlzVmlzaXRlZFBhZ2UiOjAsInBsYXRmb3JtIjozLCJoNV9maW5nZXJwcmludCI6Ikg1ZGZwXzEuOC4yX3R0dHRfMEVFaXZHRkJsQnVvZEMyaTBCVjBtOHdzWWYzdmY0VE01S3JVRnczOWt6bysvdUhZUjd6b0N2dTZlZnBWZlNrcnRqQnhjSnVuM1JuNWZGWWtEMUxMNmZmNEw3eVhURG5TVHpUaDNrT2Y3c05yUmI3RURJQlJsYmVhT2F1OEVadnpaLzNPLzdGb2UyRHM4MkRIWDd3Q1VNYS9WN2pXbUJQRjZpN2dzUnh6WkVYelBpT09zYTYxNWg1T1RrOWRFZFovcDJPZjRlS3p4Um1HaVlRcWlCZXc4c04vLzM2MGdKYnN1MjMzQ1gwYmZsM25McU9ld09EWHN4RGMzRDV5bnRQVU5ZVGtmMkFCN2ZOR0lBYUZTUHlWbVRNclpDRlRHTFJWV2ZlMkc0a25Pd1hpRHlCVzhUQWgrK1JNditsODViTDh2MTFpM1BTMHJYK29wTGhEVkhXVGNNRnNaZkxDSW9OWWl3WlJIM3dJTnZOL0d3WXhubC9MWEt4SllnMVlvWGc3NEk2REQ0WHhyNEhNMzdQNjVGMDFabG5zaUl5UnRHUmVnai9vMWhhdllaMHVSUEdFOFZRaUFWMysvdDZuVzd3cTFrSjI5cmZ4UFFoZVJqTVZvL29nRlV1MVR5Nkd2b0tKK0xFbjhzQ1VjWFAxRHBKemNadDNZeEZBOUNOSy84UWthZDNPclI3UHZTaHNqZTl6VDloOHZOMEZMRDgxdm5zRmRHWTI1cFMvZ0ZNWGtpQWhEbmNya1R3bGEySzZsVVZ2RC9uQjJqQmVwS2RKNnhsRHhOaGVFNnA2QURsY3htVVQzaE90NGlzQnFyWi9oUlVHWjJNK3JOMGU3NXZBMEVmRUtHdlVOTThNekQvRmlOYnlrU1lhZ21QUlMrdkJRcTZGOHRRK1dLSDA2OWg3VTVBUVdIRm43MS9NRzFNVHBsMlNDQkNLRGJYSzQycWZ1TkF4aUhsNGJWZEMyMk4vRUQwSW9jYUZFOWtMZVVpUWFwbEs2ZW02SlBLNm9PbkZaRTF0UnB0d2tuMllnV2s5N3lNUEtGakdzVGVRZWkyM1htZzMwVGVLdUIwcGZoV1BjSmc4ck9LYUtZYjVrZmNrZUgwNmJJMlBGZmd6aEFIRXJPc21VQWxmUnpaZjJpYUZMZlJ3azNJUCtVdUJZajkweGtDUFBaeG1zNktVY1NTemRteGp6WVlOUTlESE8zNEJzb1hmTDhuVnhTd0dZNGh5TG9zUGdhN1NaNllTQ3RVL0RDOW50cFkvMFhaUjZ2R3lyUTZxdC8vRXdFbWRqN2t4N1g3Y01sMU9Yb2VlbTVGY1RRVkJWWVowMVdCN2VFdGYyTXFoMWZ0SlgvNDRkSm51cXZLam1qajhLSUZWVlBEdHhpSjI3aFJSQy9GN2NaYUNPa3VPTjVRSjVrWTRyb2ZnczIvUnRSQUx6Ylk0NXpWWjAzR05lckkzWHhIMlRMbmJTT3RUMTNuSWU1bDhNakR1aHhKSW13MytLMzFIK3FIZ1JxZ3RGSDRXWDJQS0I1eWg5bmVwVXFsK1R3MjgwOHMzU3A5M0poVytiakxXTHdNblRiMVFGZE5CbVlmV0FxMXhBR2M0OFFxYzdmZlZISHoxSFlXbzQzVlpiaHZlTFMrRll0ZGZvTHFqRVQ4M1ptV1N5Y2hZNUE2a1VMcTNrd0x4SXdOOGw1NVZrcytBQlVWQ2kvZjUwN3M3WVUySXpaL0tQeEtzYlJkU0VYZW1yMXJMRUZLSnkwUVpoQWNFeDkzOEczVjI3SmJ2Y25JeDZEZXVBcWphRklrMjBPcXlXSDBXSHdpRWtsU1pDZUMrVi9idERUMkV2THVveE5lckJ4WEljVW9BUWhJUmhFTjdlQW1qejlwMHRPU2tMdEhabFhJNWlkL3RMUEtwbzBXR1FWWk5pdHd2UjFyV3V1dnZ1b0VyMFpCbzhUMkE5Yk5vYkZuVjVvNUFmNDJ5WW5SZjF5dmhGamJUNG8yejBTcytPbzBIdlVGcWxTbmRwa2ZGalRPdDIzNENzQVJRT0pRRFJ1NlNNcTM3VVl6OGlCWUFjNmlKZElxWHdFKzlEUXBKeGVjSlZLbTVscW1UaUFlb0d0ZCtyaDhCLzhrNnJDc2laUG5ESCs0SWZSYVVXTUVvaW1hWTNHeU9qTm5PdHo5eDZBSnlhYWJYU3lzM1FyZEsvdFN1TEpyUXNSUlNjc0Y5VzRnbEFka2FTN21LbFBQZENpZ2V5L0JSQS9hU25qQkkxTWttVzgzaVlVbjhidnEzWld1M245VkhoT3orc2owLzVUS0FoeHVDN0xjUXRQMEc5Z05lc2FEaElzUmZNRG5ZTDVjY3dpbG02YU9pSEk5T2NOaWpHRmdmWjB4Ry9nbzNWU29PTENBRmFyaXlxZlQ0VnoxZmJSSjlHSVgyczh5bWJ6TTVKRjQxakhON2grRWJENWFwK2Q0Y2RZYk4xR1BaNTU3RmhWZUJsYVNsTDROYjVVKy9qcXhOcGwxZnppUW9mcmYxcjhQR1F1SktZdTJ6MUJ5ajZLdm5CRTdjUFhlVm1hSXhuNEJ4QU1wODFYYmlTSDFXdG5jbHR4anFlbGJUQ1o4V2NNVW1HSjQ1Y2N6bTlJaVhQL1BBY3lVVmpPZUk4Vm5xZHV2TWpVaEt2aEJPQ0QxSDI5bU4vVEE2N1lsNndWMFI5UFdWamRZeDJMOXQ2OW00K0tFVm02ZER5NklleTJyaVdhdXBzQ3JmaXBCcFpQWGF4Q255VGhvZFlGS0VabXBSN1YxWHhjZnMyWlV1V0FON1RGUk9pYWROS0xoZTl0cmdoSzdxQlVzL0l4WDlWQjBKL0VCWml4ZzV2SWxsUlc1S3RpL3N0azVZU0grVENmSUsrWGRDZ2NSdUdoZ3RtcTRiUlBCV1pERm1SemxFRUhiZEJsbU5aZEVJWTc3Q0tGSVg2MnJ5VjdWelhkZHo5aFdsUmQ5L0VScjdreG9sYzhQakFLQjNxVWpvYjBZYzBpd0VuYThkTVVycVRhQTBONkJwa3FidGltTjlYQXNRS1ZxbTJqdTlJWU1tay9HSUZSbDYzMzJNU0VtUUNEUENNZ1F0MFBHZDFqOUg2clQ5N1NPNjhSMkVPblkwMnQxYnlSRzV2Y1NTMFFPR29Ic2ZDZUVpU0drZWhmN2h6NDFzRVM4bnZxUlJKYkpBZDJwdlFhb0hOY1dJQ2c3RjFMU211ZGVtOTZMM2VMcnhIV0lWYmNEZDlFVGtKYmluUGhUNm5HbnB3NWJXaUJqNHdPMTZCNU5BaFl0N0gzMWs4RXZFQno0M2V3cktUU05jYmdkdVp2TVl1ZjUyd1Z6WWRraGo1ZW90K2ZPRzJDMExlM0NkSzBMa3luakYzbElWcXlGNUdvblZxTldVYmlvc2RJaC9zRUFxWkR3aHVVWk9FcVVNYjV2MWFST1BPY2hhSGdTQXlRdFg4Qm53UmlPZ1RLNXFkckdBYnBZWTJYSVR6VXA4K0ZSTmJYcXJPYjdDTUhpQWJ0KzN6ZXBhQmVDYW8yZk1wejBrOXlHR1VUL29pd3kxY2w1QWt1TWRrWklidmFxUjJZT1R6N3JxcDJWVzhodTlWT2VlR0hKSzA5djVUYjFNcFpsUDg4bkUvVWd4eDhNNGhWQT0ifQ==',
        'extend[lat]': '22.198745',
        'extend[lng]': '113.543873',
        'extend[appType]': '1',
        'extend[osType]': '2',
        'extend[version]': '12.8.404',
        'extend[cubeComponent]': 'redpacket-big',
    }

    response = requests.post(
        'https://cube.meituan.com/topcube/api/toc/playWay/sendCoupon',
        params=params,
        headers=headers,
        data=data,
    )
    print(f'{datetime.datetime.now().strftime("%H:%M:%S.%f")} {response.json()}')


if __name__ == '__main__':
    start_time = datetime.datetime.strptime(str(datetime.datetime.now().now())[0:17] + '59.95', '%Y-%m-%d %H:%M:%S.%f')
    print(start_time)
    while datetime.datetime.now() < start_time:
        time.sleep(0.1)
    # 创建线程并启动
    thread1 = threading.Thread(target=meituan1)
    thread2 = threading.Thread(target=meituan2)
    thread3 = threading.Thread(target=meituan3)
    thread4 = threading.Thread(target=meituan4)
    thread5 = threading.Thread(target=meituan5)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

