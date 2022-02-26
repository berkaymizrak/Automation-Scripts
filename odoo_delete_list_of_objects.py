import pyautogui
import time
from utils import wait_function, clear_input, wait_in_progess

items = [
    "INV&2022&00863",
    "INV&2022&00864",
    "INV&2022&00865",
    "INV&2022&00866",
    "INV&2022&00867",
    "INV&2022&00868",
    "INV&2022&00869",
    "INV&2022&00870",
    "INV&2022&00871",
    "INV&2022&00872",
    "INV&2022&00873",
    "INV&2022&00874",
    "INV&2022&00875",
    "INV&2022&00876",
    "INV&2022&00877",
    "INV&2022&00878",
    "INV&2022&00879",
    "INV&2022&00880",
    "INV&2022&00881",
    "INV&2022&00882",
    "INV&2022&00886",
    "INV&2022&00887",
    "INV&2022&00888",
    "INV&2022&00889",
    "INV&2022&00890",
    "INV&2022&00891",
    "INV&2022&00892",
    "INV&2022&00893",
    "INV&2022&00894",
    "INV&2022&00896",
    "INV&2022&00897",
    "INV&2022&00898",
    "INV&2022&00899",
    "INV&2022&00900",
    "INV&2022&00901",
    "INV&2022&00902",
    "INV&2022&00903",
    "INV&2022&00904",
    "INV&2022&00905",
    "INV&2022&00906",
    "INV&2022&00907",
    "INV&2022&00908",
    "INV&2022&00909",
    "INV&2022&00910",
    "INV&2022&00911",
    "INV&2022&00917",
    "INV&2022&00918",
    "INV&2022&00919",
    "INV&2022&00920",
    "INV&2022&00921",
    "INV&2022&00922",
    "INV&2022&00923",
    "INV&2022&00924",
    "INV&2022&00925",
    "INV&2022&00926",
    "INV&2022&00927",
    "INV&2022&00928",
    "INV&2022&00929",
    "INV&2022&00930",
    "INV&2022&00931",
    "INV&2022&00932",
    "INV&2022&00933",
    "INV&2022&00934",
    "INV&2022&00935",
    "INV&2022&00943",
    "INV&2022&00944",
    "INV&2022&00945",
    "INV&2022&00946",
    "INV&2022&00947",
    "INV&2022&00948",
    "INV&2022&00949",
    "INV&2022&00950",
    "INV&2022&00951",
    "INV&2022&00952",
    "INV&2022&00953",
    "INV&2022&00954",
    "INV&2022&00955",
    "INV&2022&00956",
    "INV&2022&00957",
    "INV&2022&00958",
    "INV&2022&00959",
    "INV&2022&00960",
    "INV&2022&00961",
    "INV&2022&00962",
    "INV&2022&00963",
    "INV&2022&00964",
    "INV&2022&00965",
    "INV&2022&00966",
    "INV&2022&00967",
    "INV&2022&00968",
    "INV&2022&00969",
    "INV&2022&00970",
    "INV&2022&00971",
    "INV&2022&00972",
    "INV&2022&00974",
    "INV&2022&00975",
    "INV&2022&00976",
    "INV&2022&00977",
    "INV&2022&00978",
    "INV&2022&00979",
    "INV&2022&00980",
    "INV&2022&00983",
    "INV&2022&00984",
    "INV&2022&00985",
    "INV&2022&00986",
    "INV&2022&00987",
    "INV&2022&00988",
    "INV&2022&00989",
    "INV&2022&00990",
    "INV&2022&00991",
    "INV&2022&00992",
    "INV&2022&00993",
    "INV&2022&00994",
    "INV&2022&00997",
    "INV&2022&00998",
    "INV&2022&00999",
    "INV&2022&01000",
    "INV&2022&01001",
    "INV&2022&01002",
    "INV&2022&01003",
    "INV&2022&01004",
    "INV&2022&01005",
    "INV&2022&01006",
    "INV&2022&01007",
    "INV&2022&01008",
    "INV&2022&01009",
    "INV&2022&01010",
    "INV&2022&01011",
    "INV&2022&01013",
    "INV&2022&01014",
    "INV&2022&01015",
    "INV&2022&01016",
    "INV&2022&01017",
    "INV&2022&01018",
    "INV&2022&01019",
    "INV&2022&01020",
    "INV&2022&01021",
    "INV&2022&01022",
    "INV&2022&01023",
    "INV&2022&01024",
    "INV&2022&01025",
    "INV&2022&01026",
    "INV&2022&01027",
    "INV&2022&01029",
    "INV&2022&01030",
    "INV&2022&01031",
    "INV&2022&01032",
    "INV&2022&01033",
    "INV&2022&01034",
    "INV&2022&01035",
    "INV&2022&01037",
    "INV&2022&01038",
    "INV&2022&01039",
    "INV&2022&01040",
    "INV&2022&01041",
    "INV&2022&01042",
    "INV&2022&01043",
    "INV&2022&01044",
    "INV&2022&01045",
    "INV&2022&01047",
    "INV&2022&01048",
    "INV&2022&01049",
    "INV&2022&01050",
    "INV&2022&01051",
    "INV&2022&01052",
    "INV&2022&01053",
    "INV&2022&01054",
    "INV&2022&01055",
    "INV&2022&01056",
    "INV&2022&01057",
    "INV&2022&01058",
    "INV&2022&01059",
    "INV&2022&01060",
    "INV&2022&01061",
    "INV&2022&01062",
    "INV&2022&01063",
    "INV&2022&01064",
    "INV&2022&01067",
    "INV&2022&01068",
    "INV&2022&01069",
    "INV&2022&01070",
    "INV&2022&01071",
    "INV&2022&01072",
    "INV&2022&01073",
    "INV&2022&01074",
    "INV&2022&01075",
    "INV&2022&01079",
    "INV&2022&01080",
    "INV&2022&01081",
    "INV&2022&01082",
    "INV&2022&01083",
    "INV&2022&01084",
    "INV&2022&01085",
    "INV&2022&01086",
    "INV&2022&01087",
    "INV&2022&01088",
    "INV&2022&01089",
    "INV&2022&01091",
    "INV&2022&01092",
    "INV&2022&01093",
    "INV&2022&01094",
    "INV&2022&01095",
    "INV&2022&01096",
    "INV&2022&01097",
    "INV&2022&01098",
    "INV&2022&01099",
    "INV&2022&01100",
    "INV&2022&01101",
    "INV&2022&01102",
    "INV&2022&01103",
    "INV&2022&01104",
    "INV&2022&01105",
    "INV&2022&01106",
    "INV&2022&01107",
    "INV&2022&01108",
    "INV&2022&01109",
    "INV&2022&01110",
    "INV&2022&01112",
    "INV&2022&01113",
    "INV&2022&01114",
    "INV&2022&01115",
    "INV&2022&01116",
    "INV&2022&01117",
    "INV&2022&01118",
    "INV&2022&01119",
    "INV&2022&01122",
    "INV&2022&01123",
    "INV&2022&01124",
    "INV&2022&01125",
    "INV&2022&01126",
    "INV&2022&01127",
    "INV&2022&01128",
    "INV&2022&01129",
    "INV&2022&01130",
    "INV&2022&01132",
    "INV&2022&01133",
    "INV&2022&01134",
    "INV&2022&01135",
    "INV&2022&01136",
    "INV&2022&01137",
    "INV&2022&01138",
    "INV&2022&01139",
    "INV&2022&01140",
    "INV&2022&01141",
    "INV&2022&01142",
    "INV&2022&01143",
    "INV&2022&01144",
    "INV&2022&01145",
    "INV&2022&01146",
    "INV&2022&01147",
    "INV&2022&01148",
    "INV&2022&01149",
    "INV&2022&01150",
    "INV&2022&01151",
    "INV&2022&01152",
    "INV&2022&01155",
    "INV&2022&01156",
    "INV&2022&01157",
    "INV&2022&01158",
    "INV&2022&01159",
    "INV&2022&01160",
    "INV&2022&01161",
    "INV&2022&01162",
    "INV&2022&01163",
    "INV&2022&01164",
    "INV&2022&01166",
    "INV&2022&01167",
    "INV&2022&01168",
    "INV&2022&01170",
    "INV&2022&01171",
    "INV&2022&01172",
    "INV&2022&01174",
    "INV&2022&01175",
    "INV&2022&01176",
    "INV&2022&01177",
    "INV&2022&01178",
    "INV&2022&01179",
    "INV&2022&01180",
    "INV&2022&01181",
    "INV&2022&01182",
    "INV&2022&01183",
    "INV&2022&01186",
    "INV&2022&01187",
    "INV&2022&01188",
    "INV&2022&01189",
    "INV&2022&01190",
    "INV&2022&01192",
    "INV&2022&01193",
    "INV&2022&01194",
    "INV&2022&01195",
    "INV&2022&01196",
    "INV&2022&01198",
    "INV&2022&01199",
    "INV&2022&01200",
    "INV&2022&01201",
    "INV&2022&01202",
    "INV&2022&01203",
    "INV&2022&01204",
    "INV&2022&01205",
    "INV&2022&01206",
    "INV&2022&01207",
    "INV&2022&01208",
    "INV&2022&01209",
    "INV&2022&01210",
    "INV&2022&01212",
    "INV&2022&01213",
    "INV&2022&01214",
    "INV&2022&01215",
    "INV&2022&01216",
    "INV&2022&01217",
    "INV&2022&01218",
    "INV&2022&01219",
    "INV&2022&01220",
    "INV&2022&01221",
    "INV&2022&01223",
    "INV&2022&01224",
    "INV&2022&01225",
    "INV&2022&01226",
    "INV&2022&01227",
    "INV&2022&01228",
    "INV&2022&01229",
    "INV&2022&01230",
    "INV&2022&01231",
    "INV&2022&01236",
    "INV&2022&01237",
    "INV&2022&01238",
    "INV&2022&01239",
    "INV&2022&01240",
    "INV&2022&01241",
    "INV&2022&01242",
    "INV&2022&01243",
    "INV&2022&01244",
    "INV&2022&01245",
    "INV&2022&01249",
    "INV&2022&01250",
    "INV&2022&01251",
    "INV&2022&01252",
    "INV&2022&01253",
    "INV&2022&01254",
    "INV&2022&01255",
    "INV&2022&01256",
    "INV&2022&01257",
    "INV&2022&01258",
    "INV&2022&01259",
    "INV&2022&01260",
    "INV&2022&01264",
    "INV&2022&01265",
    "INV&2022&01266",
    "INV&2022&01267",
    "INV&2022&01268",
    "INV&2022&01269",
    "INV&2022&01270",
    "INV&2022&01271",
    "INV&2022&01272",
    "INV&2022&01273",
    "INV&2022&01274",
    "INV&2022&01275",
    "INV&2022&01276",
    "INV&2022&01277",
    "INV&2022&01278",
    "INV&2022&01279",
    "INV&2022&01280",
    "INV&2022&01281",
    "INV&2022&01282",
    "INV&2022&01283",
    "INV&2022&01284",
    "INV&2022&01354",
    "INV&2022&01355",
    "RINV&2022&00001",
]

pause_time = 20

pyautogui.click(1336, 215)  # Search bar
for enum, item in enumerate(items):
    pyautogui.write(item)
    pyautogui.press('enter')
    if enum % 4 == 0 and enum != 0:
        pass
    else:
        continue
    if wait_function(2, "p"):
        wait_in_progess(pause_time)
    pyautogui.click(288, 308)  # select
    if wait_function(1, "p"):
        wait_in_progess(pause_time)
    pyautogui.click(666, 260)  # Action dropdown
    if wait_function(4, "p"):
        wait_in_progess(pause_time)
    pyautogui.click(679, 449)  # Force delete
    if wait_function(2, "p"):
        wait_in_progess(pause_time)
    pyautogui.click(300, 215)  # Back to invoices
    if wait_function(1, "p"):
        wait_in_progess(pause_time)

    pyautogui.click(1336, 215)  # Search bar
    clear_input(2)