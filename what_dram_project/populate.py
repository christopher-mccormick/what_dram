from dramapp.models import Region, Distillery, Whisky

#Traceback (most recent call last):
#File "<console>", line 1, in <module>
#File "/Users/christophermccormick/Documents/Masters/iTech/what_dram/what_dram_project/populate.py", line 10, in <module>
#Distillery(name = 'Laphroaig', region = Region, latitude = '55.62989', longitude = '6.15202', images = 'test', website = 'http://www.laphroaig.com/', tourevents = 'test',).save()
#File "/Library/Python/2.7/site-packages/django/db/models/base.py", line 355, in __init__
#setattr(self, field.name, rel_obj)
#File "/Library/Python/2.7/site-packages/django/db/models/fields/related.py", line 366, in __set__
#self.field.name, self.field.rel.to._meta.object_name))
#ValueError: Cannot assign "<class 'dramapp.models.Region'>": "Distillery.region" must be a "Region" instance.
#r = Region(name = 'Islay')
#r.save()

Region(region = 'Islay',).save()
Region(region = 'Speyside',).save()
Region(region = 'Highland',).save()
Region(region = 'Lowland',).save()
Region(region = 'Island',).save()
Region(region = 'Campbeltown',).save()

Distillery(name = 'Laphroaig', region = 'Islay', latitude = '55.62989', longitude = '6.15202', images = 'test', website = 'http://www.laphroaig.com/', tourevents = 'test',).save()
Distillery(name = 'Ardbeg', region = 'Islay', latitude = '55.6404', longitude = '6.1087', images = 'test', website = 'http://www.ardbeg.com/', tourevents = 'test',).save()
Distillery(name = 'Old Pulteney', region = 'Highland', latitude = '58.4491', longitude = '3.1701', images = 'test', website = 'http://www.oldpulteney.com/', tourevents = 'test',).save()
Distillery(name = 'Edradour', region = 'Highland', latitude = '56.7017', longitude = '3.7008', images = 'test', website = 'http://www.edradour.com/', tourevents = 'test',).save()
Distillery(name= 'Balblair', region = 'Highland', latitude = '57.8398', longitude = ' 4.1808', images = 'test', website = 'http://www.balblair.com/', tourevents = 'test',).save()
Distillery(name = 'Glenfiddich', region = 'Speyside', latitude = '57.27', longitude = '3.7', images = 'test', website = 'http://www.glenfiddich.com/', tourevents = 'test',).save()
Distillery(name = 'Glenlivet', region = 'Speyside', latitude = '57.341056', longitude = '3.334715', images = 'test', website = 'http://www.theglenlivet.com/', tourevents = 'test',).save()
Distillery(name = 'Auchentoshan', region = 'Lowland', latitude = '55.51', longitude = '2.55', images = 'test', website = 'http://www.auchentoshan.com/', tourevents = 'test',).save()
Distillery(name = 'Glenkinchie', region = 'Lowland', latitude = '55.89021', longitude = '-2.892862', images = 'test', website = 'http://www.discovering-distilleries.com/agecheck.php?redirect=/glenkinchie/index.php', tourevents = 'test',).save()
Distillery(name = 'Highland Park', region = 'Island', latitude = '58.59', longitude = '2.55', images = 'test', website = 'http://www.highlandpark.co.uk/', tourevents = 'test',).save()

Whisky(name = 'Laphroaig', age = '10', whiskytype = 'Single Malt', distillery = 'Laphroaig', region = 'Islay', rating = 'test', tastingnotes = 'Full bodied, Peaty, Smokey', barrelType = 'wood', image = 'test', website = 'http://www.laphroaig.com/whiskies/10yo.aspx', price = '37.50',). save()
Whisky(name = 'Ardbeg', age = '10', whiskytype = 'Single Malt', distillery = 'Ardbeg', region = 'Islay', rating = 'test', tastingnotes = 'Peaty, smokey', barrelType = 'test', image = 'test', website = 'http://www.ardbeg.com/ardbeg/the-ardbeg-range', price = '38.70',). save()
Whisky(name = 'Old Pulteney', age = '12', whiskytype = 'Single Malt', distillery = 'Old Pulteney', region = 'Highland', rating = 'test', tastingnotes = 'Fruity, Spice', barrelType = 'test', image = 'test', website = 'http://www.oldpulteney.com/old-pulteney-whisky/12-year-old-single-malt/', price = '30.99',). save()
Whisky(name = 'Old Pulteney', age = '17', whiskytype = 'Single Malt', distillery = 'Old Pulteney', region = 'Highland', rating = 'test', tastingnotes = 'Complex, wood, fruit, creamy', barrelType = 'test', image = 'test', website = 'http://www.oldpulteney.com/old-pulteney-whisky/17-year-old-single-malt/', price = '52.30',). save()
Whisky(name = 'Old Pulteney', age = '21', whiskytype = 'Single Malt', distillery = 'Old Pulteney', region = 'Highland', rating = 'test', tastingnotes = 'Light, Fruity, Honey, Vanilla', barrelType = 'test', image = 'test', website = 'http://www.oldpulteney.com/old-pulteney-whisky/21-year-old-single-malt/', price = '80.70',). save()
Whisky(name = 'Auchentoshan', age = '12', whiskytype = 'Single Malt', distillery = 'Auchentoshan', region = 'Lowland', rating = 'test', tastingnotes = 'Smooth, nutty, fruity', barrelType = 'test', image = 'test', website = 'http://www.auchentoshan.com/products/our-range.aspx', price = '30.50',). save()
Whisky(name = 'Balblair', age = '10', whiskytype = 'Single Malt', distillery = 'Balblair', region = 'Highland', rating = 'test', tastingnotes = 'Full bodied, fruity', barrelType = 'test', image = 'test', website = 'http://www.balblair.com/exclusive-vintages/', price = '42.00',). save()
Whisky(name = 'Edradour', age = '10', whiskytype = 'Single Malt', distillery = 'Edradour', region = 'Highland', rating = 'test', tastingnotes = 'Fruity', barrelType = 'test', image = 'test', website = 'test', price = '32.50',). save()
Whisky(name = 'Glenfiddich', age = '12', whiskytype = 'Single Malt', distillery = 'Glenfiddich', region = 'Speyside', rating = 'test', tastingnotes = 'Fruity', barrelType = 'test', image = 'test', website = 'http://www.glenfiddich.com/', price = '34.75',). save()
Whisky(name = 'Glenkinchie', age = '12', whiskytype = 'Single Malt', distillery = 'Glenkinchie', region = 'Lowland', rating = 'test', tastingnotes = 'Smooth, sweet', barrelType = 'test', image = 'test', website = 'test', price = '34.00',). save()
Whisky(name = 'Glenlivet', age = '12', whiskytype = 'Single Malt', distillery = 'Glenlivet', region = 'Speyside', rating = 'test', tastingnotes = 'Light, fruity', barrelType = 'test', image = 'test', website = 'test', price = '34.00',). save()
Whisky(name = 'Highland Park', age = '12', whiskytype = 'Single Malt', distillery = 'Highland Park', region = 'Island', rating = 'test', tastingnotes = 'Light smoke, honey, fruit', barrelType = 'wood', image = 'test', website = 'test', price = '30.00',). save()

