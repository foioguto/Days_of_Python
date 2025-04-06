from engine_module import Engine

date = "2000-08-12" # YYYY-MM-DD
url = f"https://www.billboard.com/charts/hot-100/{date}"

engine1 = Engine(date, url)
engine1.scrap()
