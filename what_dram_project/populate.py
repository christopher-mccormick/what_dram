from dramapp.models import Region, Distillery, Whisky, Comments

Region(region = 'Islay', views=0).save()

Distillery(name = 'Laphroaig', latitude = '55.62989', longitude = '-6.15202', images = 'test', website = 'http://www.laphroaig.com/', tourevents = 'test',).save()


