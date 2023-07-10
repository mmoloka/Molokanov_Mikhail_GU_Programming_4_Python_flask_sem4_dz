import requests
import threading
import time

urls = ['https://www.google.ru/', 'https://kwork.ru/','https://www.fl.ru', 'https://toloka.yandex.ru/', 'https://freelance.ru/', 'https://www.upwork.com/', 'https://vc.ru/', 'https://insolvo.com/', 'https://unu.im/', 'https://vsesdal.ru/', 'https://www.etxt.ru/', 'https://advego.com/', 'https://text.ru/', 'https://copylancer.ru/', 'https://workhard.online/', 'https://contentmonster.ru/', 'https://miratext.ru/', 'https://www.turbotext.ru/', 'https://textbroker.ru/', 'https://www.textsale.ru/', 'https://slogoved.ru/', 'https://9writer.ru/', 'http://fll.ru/', 'https://votimenno.ru/', 'https://workhard.pro/', 'https://gengo.com/', 'https://www.getblend.com/', 'https://vakvak.ru/', 'https://di-ci.ru/', 'https://perevodchik.me/', 'https://www2.proz.com/', 'https://translatorsauction.com/', 'https://www.translatorscafe.com/', 'https://perevod01.ru/', 'http://www.trworkshop.net/', 'https://www.behance.net/', 'https://topcreator.org/', 'https://illustrators.ru/', 'http://www.prohq.ru/', 'https://render.ru/', 'https://www.cgtrader.com/', 'https://dribbble.com/', 'https://www.krop.com/', 'https://awayne.biz/', 'https://godesigner.ru/', 'https://www.crowdspring.com/', 'https://www.coroflot.com/', 'https://www.dizkon.ru/', 'https://gamedev.ru/', 'https://diktorov.net/', 'http://radiozvuk.com/', 'https://dictoronline.ru/', 'https://golosmarket.ru/', 'https://www.litres.ru/', 'http://xn--80aaebigofx6aae0c0a9o.xn--p1ai/', 'https://contributor.stock.adobe.com/', 'http://www.wedlife.ru/', 'https://dilavo.ru/', 'https://lori.ru/', 'https://stock.adobe.com/', 'https://ru.dreamstime.com/', 'https://rubrain.com/', 'https://www.freelancejob.ru/', 'https://trastik.com/', 'https://www.rotapost.ru/', 'https://www.miralinks.ru/', 'https://voproso.ru/', 'http://www.e-generator.ru/', 'https://storygo.ru/', 'https://gogetlinks.net/', 'https://www.sape.ru/', 'https://blogun.ru/', 'https://www.telderi.ru/', 'https://ya.ru/', 'https://www.python.org/', 'http://citycelebrity.ru/', 'https://workspace.ru/', 'https://pomogatel.ru/', 'https://sdelau-uroki.ru/', 'https://kursar.su/', 'https://studently.ru/', 'https://gb.ru/', 'https://prepod24.ru/', 'http://www.reshaem.net/', 'https://studwork.ru/', 'http://help-s.ru/', 'https://peshkariki.ru/', 'https://mastergrad.com/',  'http://www.interior-design.club/', 'https://cmet4uk.ru/', 'https://vsesdal.ru/', 'https://studlance.ru/', 'https://www.remontnik.ru/', 'https://kvartirakrasivo.ru/', 'https://archiprofi.ru/', 'https://www.forumhouse.ru/', 'https://www.liveexpert.org/', 'https://hrspace.hh.ru/', 'https://youdo.com/', 'https://www.houzz.ru/', 'http://www.midoma.ru/', 'https://searchengines.guru/', 'https://www.9111.ru/', 'https://hrtime.ru/', 'https://junglejobs.ru/', 'https://consjurist.ru/', 'https://workspace.ru/', 'https://tender.elama.ru/', 'http://seodrom.ru/', 'https://modber.ru/', 'https://proglib.io/', 'https://1clancer.ru/', 'https://www.canstockphoto.ru/', 'https://i-m-i.ru/', 'https://www.etxt.ru/', 'https://www.livemaster.ru/', 'https://www.shutterstock.com/']


def parser_url(url, n):
    response = requests.get(url)
    with open(f"task_8_1/file{n}.html", "w", encoding="utf-8") as f:
        f.write(response.text)


if __name__ == '__main__':
    dt = time.time()
    threads = []
    for n, url in enumerate(urls):
        t = threading.Thread(target=parser_url, args=(url, n))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print(f'Время загрузки: {time.time() - dt: .3f} секунд')

    # Время загрузки:  7.105 секунд
    # Время загрузки:  6.988 секунд
    # Время загрузки:  7.037 секунд