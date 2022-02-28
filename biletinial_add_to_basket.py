import requests

session = requests.Session()

data = {
    "seanceId": 0,
    "organizerType": 0,
    "a_aid": "",
    "a_bid": "",
    "UserName": "xxxx",
    "Password": "www",
}

url = "https://biletinial.com/Login"
r = session.post(
    url,
    data=data,
    # json=data,
    # headers=headers,
)

print(r)

url = "https://www.biletinial.com/dynamic/addtobasket"

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9,tr;q=0.8,pl;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    # "Cookie": "GA_a_aid=undefined; _gcl_au=1.1.1499094419.1646034263; _ga=GA1.2.1250801251.1646034263; _gid=GA1.2.1522884102.1646034263; _gat_gtag_UA_37466048_1=1; PAPVisitorId=dwWeSYhaLTjrtA7D1vNCHtfKyFcndnHR; NSC_joufscjmfu_iuuqt_ttm=ffffffff09081f7645525d5f4f58455e445a4a42378b; ASP.NET_SessionId=iktuf2dcqu1bkisxfssqde0n; __RequestVerificationToken=lUKtSk4yJU5NTN9UzvB_3ZlramVOHMOmzIayoURAR1KdoLodzXhu0T5I4vdy5gSTUcLTkb3tKHwVZ7R-7ZHKokUQgZE1",
    # "Cookie": "__RequestVerificationToken=Cjl4PVzC5aXAZxV1HwMaXJbkmp1NqK4nZ-8oVmT_82Z6FmGpmsw-2p2-uhYLT8RBOo0ZIBAhlXXtaA3NFUIdRAWj6yk1",
    # "Cookie": "_ga=GA1.2.998594463.1641206690; _gcl_au=1.1.123779180.1641364100; BLTAUTH=oO/7zjjgNuixF199bBybSmpgK1tbwjSG4zhm0N9m28lzN2PTId7cbxCnPQMV1Zqd3AB2DQfnT5i7eMyN7AcSUNaf7VfirdFl2lGuCtKDgTk=; GA_a_aid=undefined; __auc=6cb8940b17f1d35d7aac3ee4d41; _gid=GA1.2.1775419843.1645778271; CookieId=daf7de56-c4bd-4bfd-a473-cb6955512668; cto_bundle=1KXI-l8lMkJQdGpaaHNGSzNGS0NwUTZMbGFjRXAzMTFxMXRPUEhvS3ZFaXVub3JiM09EaFV6a2hGOXNVN2xJMkN4bzdTNDdwS1k3dnE5M2Y2ZU1CY0E2eFZacTdPaGR3dlJOMXlPNDRObG5LMG1tOW81eUlsVVUwSGx6S29mQVlzSWtDNWQzZDlhWTg3dDBzZDFRYWlZaFAlMkZLdWhzZDl5UUxPdDB0Mnp6Nm9UYUxNMSUyQmlBTiUyRndyU01vaHNPSExVZ1pyR1NKS3VQM2JIQmVMSUc3ajlKTlJmVnoxV3clM0QlM0Q; _gaexp=GAX1.2.u8phMWwIQdSuO6wwwMaT5g.19126.0; PAPVisitorId=NVbBmNMOl7OPisGiXFHNnkQN7ihwQzIx; NSC_joufscjmfu_iuuqt_ttm=ffffffff09081f7645525d5f4f58455e445a4a42378b; ASP.NET_SessionId=wbk403ev2ms2ppi4l502ofzq; __RequestVerificationToken=A37TYfUwXvXHGkBGNGGOvHKwIJbo8Sfj4CwP49eOgYoyp_npls97acuLlzlHDx959xO55n1qOEaOFsG2qrHmRrzWRQA1; _gat_gtag_UA_37466048_1=1",
    "Referer": "https://www.biletinial.com/tiyatro/koltuk_secimi",
    "Host": "www.biletinial.com",
    "Connection": "keep-alive",
    "Content-Length": "218",
    # "Acceasdasdnguage": "asdasd",
    # "Acceasdasdnguage": "asdasd",
}
data = {
    "seatId": 2074891,
    "seanceId": 9023012,
    "sessionId": "0237baa9-79ce-481a-bb37-11a2ac2d3697",
    "cinemaBranchId": 4550,
    "__RequestVerificationToken": "Cjl4PVzC5aXAZxV1HwMaXJbkmp1NqK4nZ-8oVmT_82Z6FmGpmsw-2p2-uhYLT8RBOo0ZIBAhlXXtaA3NFUIdRAWj6yk1",
}
cookies = {
    "_ga": "GA1.2.998594463.1641206690",
    "_gcl_au": "1.1.123779180.1641364100",
    "BLTAUTH": "oO/7zjjgNuixF199bBybSmpgK1tbwjSG4zhm0N9m28lzN2PTId7cbxCnPQMV1Zqd3AB2DQfnT5i7eMyN7AcSUNaf7VfirdFl2lGuCtKDgTk",
    "GA_a_aid": "undefined",
    "__auc": "6cb8940b17f1d35d7aac3ee4d41",
    "_gid": "GA1.2.1775419843.1645778271",
    "CookieId": "daf7de56-c4bd-4bfd-a473-cb6955512668",
    "cto_bundle": "1KXI-l8lMkJQdGpaaHNGSzNGS0NwUTZMbGFjRXAzMTFxMXRPUEhvS3ZFaXVub3JiM09EaFV6a2hGOXNVN2xJMkN4bzdTNDdwS1k3dnE5M2Y2ZU1CY0E2eFZacTdPaGR3dlJOMXlPNDRObG5LMG1tOW81eUlsVVUwSGx6S29mQVlzSWtDNWQzZDlhWTg3dDBzZDFRYWlZaFAlMkZLdWhzZDl5UUxPdDB0Mnp6Nm9UYUxNMSUyQmlBTiUyRndyU01vaHNPSExVZ1pyR1NKS3VQM2JIQmVMSUc3ajlKTlJmVnoxV3clM0QlM0Q",
    "_gaexp": "GAX1.2.u8phMWwIQdSuO6wwwMaT5g.19126.0",
    "PAPVisitorId": "NVbBmNMOl7OPisGiXFHNnkQN7ihwQzIx",
    "NSC_joufscjmfu_iuuqt_ttm": "ffffffff09081f7645525d5f4f58455e445a4a42378b",
    "ASP.NET_SessionId": "wbk403ev2ms2ppi4l502ofzq",
    "__RequestVerificationToken": "A37TYfUwXvXHGkBGNGGOvHKwIJbo8Sfj4CwP49eOgYoyp_npls97acuLlzlHDx959xO55n1qOEaOFsG2qrHmRrzWRQA1",
    "_gat_gtag_UA_37466048_1": "1",
}
cookies = "_ga=GA1.2.998594463.1641206690; _gcl_au=1.1.123779180.1641364100; BLTAUTH=oO/7zjjgNuixF199bBybSmpgK1tbwjSG4zhm0N9m28lzN2PTId7cbxCnPQMV1Zqd3AB2DQfnT5i7eMyN7AcSUNaf7VfirdFl2lGuCtKDgTk=; GA_a_aid=undefined; __auc=6cb8940b17f1d35d7aac3ee4d41; _gid=GA1.2.1775419843.1645778271; CookieId=daf7de56-c4bd-4bfd-a473-cb6955512668; cto_bundle=1KXI-l8lMkJQdGpaaHNGSzNGS0NwUTZMbGFjRXAzMTFxMXRPUEhvS3ZFaXVub3JiM09EaFV6a2hGOXNVN2xJMkN4bzdTNDdwS1k3dnE5M2Y2ZU1CY0E2eFZacTdPaGR3dlJOMXlPNDRObG5LMG1tOW81eUlsVVUwSGx6S29mQVlzSWtDNWQzZDlhWTg3dDBzZDFRYWlZaFAlMkZLdWhzZDl5UUxPdDB0Mnp6Nm9UYUxNMSUyQmlBTiUyRndyU01vaHNPSExVZ1pyR1NKS3VQM2JIQmVMSUc3ajlKTlJmVnoxV3clM0QlM0Q; _gaexp=GAX1.2.u8phMWwIQdSuO6wwwMaT5g.19126.0; PAPVisitorId=NVbBmNMOl7OPisGiXFHNnkQN7ihwQzIx; NSC_joufscjmfu_iuuqt_ttm=ffffffff09081f7645525d5f4f58455e445a4a42378b; ASP.NET_SessionId=wbk403ev2ms2ppi4l502ofzq; __RequestVerificationToken=A37TYfUwXvXHGkBGNGGOvHKwIJbo8Sfj4CwP49eOgYoyp_npls97acuLlzlHDx959xO55n1qOEaOFsG2qrHmRrzWRQA1; _gat_gtag_UA_37466048_1=1"

r = session.post(
    url,
    data=data,
    # json=data,
    cookies=cookies,
    headers=headers,
)

print(r.text)
print(r)
print(r.content)
