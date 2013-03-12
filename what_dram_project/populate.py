from dramapp.models import Region, Distillery, Whisky

rIslay = Region(region = 'Islay')
rIslay.save()
rSpey = Region(region = 'Speyside',)
rSpey.save()
rHigh = Region(region = 'Highland',)
rHigh.save()
rLow = Region(region = 'Lowland',)
rLow.save()
rIsland = Region(region = 'Island',)
rIsland.save()
rCamp = Region(region = 'Campbeltown',)
rCamp.save()

d1 = Distillery(name = 'Laphroaig', region = rIslay, latitude = '55.62989', longitude = '-6.15202', images = '/static/imgs/imgs/laphroaig.jpg', website = 'http://www.laphroaig.com/', tourevents = 'Daily tours at 10.30, 11.30, 14.00, 15.30', blurb = 'The Laphroaig distillery was established in 1825 by Donald and Alexander Johnston. The Johnstons who founded Laphroaig were from the Clan Donald and are likely to be from the MacIain of Ardnamurchan branch of the clan. The family anglicized their name to Johnston. They ran the distillery until 1954, when Ian Hunter (who had no children) died and left the distillery to one of his managers, Bessie Williamson. The distillery was sold to Long John International in the 1960s, and subsequently became part of Allied Domecq. The brand was in turn acquired by Fortune Brands in 2005, as one of the brands divested by Pernod Ricard in order to obtain regulatory approval for its takeover of Allied Domecq. Fortune Brands then split up its business product lines in 2011, forming its spirits business into Beam Inc. Laphroaig has been the only whisky to carry the Royal Warrant of the Prince of Wales, which was awarded in person during a visit to the distillery in 1994.',)
d1.save()
d2 = Distillery(name = 'Ardbeg', region = rIslay, latitude = '55.640405', longitude = '-6.108109', images = '/static/imgs/islay-ardbeg-distillery-pano.jpg', website = 'http://www.ardbeg.com/', tourevents = 'Tours every half hour', blurb = 'Ardbeg Distillery (Scottish Gaelic: Taigh-stail Airde Beaga) is a Scotch whisky distillery on the south coast of the isle of Islay, Argyll and Bute, Scotland, in the Inner Hebrides group of islands. The distillery claims to produce the peatiest Islay whisky and uses malted barley sourced from the maltings in Port Ellen. It is one of the fastest growing Islay distilleries.',)
d2.save()
d3 = Distillery(name = 'Old Pulteney', region = rHigh, latitude = '58.434801', longitude = '-3.084658', images = '/static/imgs/old-pulteney-distillery.jpg', website = 'http://www.oldpulteney.com/', tourevents = 'Daily tours', blurb = 'The distillery was established in 1826 AD in the name of Sir William Pulteney (who died in 1805), and for whom Pulteneytown is named. The distillery is the most northerly on the Scottish mainland and was quite inaccessible, except by sea, when established. Barley was brought in by sea, and the whisky was shipped out the same way. Many of the distillery workers were also employed as fishermen. The herring fishing industry is no longer part of daily life in Wick but the distillery continues to operate, producing a Highland single-malt with a reputation as one of the finest available. Characteristics of the whisky are attributed to exposure to sea air during maturation. The distillery is now owned by Inver House Distillers.', )
d3.save()
d4 = Distillery(name = 'Edradour', region = rHigh, latitude = '56.701458', longitude = '-3.70101', images = '/static/imgs/pitlochry-edradour-distillery.jpg', website = 'http://www.edradour.com/', tourevents = 'Daily tours', blurb = 'Edradour distillery (Scottish Gaelic: Eadar Dha Dhobhar, between two rivers) is a Highland single malt whisky distillery based in Pitlochry, Perthshire. Edradour is reputed to be the smallest distillery in Scotland. Established in 1825, the distillery was traditionally run by three men but now there are just two. Only twelve casks are produced each week. They have a tour which costs 7.50 and includes a dram.',)
d4.save()
d5 =Distillery(name= 'Balblair', region = rHigh, latitude = '57.8404', longitude = '-4.180813', images = '/static/imgs/BalblairDistillery.jpg', website = 'http://www.balblair.com/', tourevents = 'Daily tours', blurb = 'Balblair Distillery is a Scotch whisky distillery located in Edderton, Ross-shire,Scotland. Originally founded in 1790, the distillery was rebuilt in 1895 by the designer Charles C Doig to be closer to the Edderton Railway Station on the Inverness and Ross-shire Railway line. However, so good was the original water source that the rebuilt distillery chose to ignore a nearby burn in favour of the original Ault Dearg burn. To this day, the Balblair Distillery continues to use this original water source.', )
d5.save()
d6 = Distillery(name = 'Glenfiddich', region = rSpey, latitude = '57.454018', longitude = '-3.127767', images = '/static/imgs/glenfiddich-distillery.jpg', website = 'http://www.glenfiddich.com/', tourevents = 'Daily tours', blurb = 'The Glenfiddich Distillery is a Speyside single malt Scotch whisky distillery owned by William Grant & Sons in Dufftown, Scotland. Glenfiddich means Valley of the Deer in Gaelic, hence the presence of a stag symbol on Glenfiddich bottles.',)
d6.save()
d7 = Distillery(name = 'Glenlivet', region = rSpey, latitude = '57.343342', longitude = '-3.338715', images = '/static/imgs/The_Glenlivet_distillery.jpg', website = 'http://www.theglenlivet.com/', tourevents = 'Daily tours', blurb = 'The Glenlivet distillery is a distillery near Ballindalloch in Moray, Scotland that produces single malt Scotch whisky. It is the oldest legal distillery in the parish of Glenlivet, and the production place of the Scottish whisky of the same name. It is described in packaging and advertising as "The single malt that started it all". It was founded in 1824 and has operated almost continuously since. The distillery remained open throughout the Great Depression and its only closure came during World War II. The Glenlivet distillery has grown in the post-war period to become one of the biggest single malt distilleries in order to keep up with global demand; The Glenlivet brand is the biggest selling malt whisky in the United States and the second biggest selling single malt brand globally.',)
d7.save()
d8 = Distillery(name = 'Auchentoshan', region = rLow, latitude = '55.922313', longitude = '-4.439655', images = '/static/imgs/auchentoshan_distillery.jpg', website = 'http://www.auchentoshan.com/', tourevents = 'Daily tours', blurb = 'Auchentoshan distillery is a Single Malt whisky distillery in the west of Scotland. The name Auchentoshan is Gaelic and translates as "the corner of the field". The distillery is also known as the Glasgow Malt Whisky due to its close proximity to Glasgow and the breakfast whisky due to its sweet and delicate nature. Auchentoshan is located at the foot of the Kilpatrick hills on the outskirts of Clydebank in West Dunbartonshire near the Erskine Bridge.',)
d8.save()
d9 = Distillery(name = 'Glenkinchie', region = rLow, latitude = '55.889989', longitude = '-2.891258', images = '/static/imgs/glenkinchie_distillery.jpg', website = 'http://www.discovering-distilleries.com/agecheck.php?redirect=/glenkinchie/index.php', tourevents = 'Daily tours', blurb = 'Glenkinchie lies, as the name might suggest, in a glen of the Kinchie Burn near the village of Pencaitland, East Lothian. It is situated about 15 miles from Edinburgh. The distillery is set in farmland. The name Kinchie is a corruption of De Quincy, the original owners of the land. Its origins date back to around 1825 when it was founded by brothers John and George Rate. The original name was Milton Distillery. The brothers probably renamed it in about 1837. In 1969 the distillery stopped malting its own grain and the malting floors were turned into a museum of malt whisky.',)
d9.save()
d10 = Distillery(name = 'Highland Park', region = rIsland, latitude = '58.967911', longitude = '-2.955387', images = '/static/imgs/highland_park.jpg', website = 'http://www.highlandpark.co.uk/', tourevents = 'Daily tours', blurb = 'Highland Park distillery is a Scotch whisky distillery based in Kirkwall, Orkney. It is the most northerly whisky distillery in Scotland, half a mile farther north than that at Scapa distillery. Highland Park has performed well at international spirit ratings competitions. Its 25 year single malt scotch, for example, received double gold medals at the 2007 and 2009 San Francisco World Spirits Competition.',)
d10.save()

w1 = Whisky(name = 'Laphroaig10', title= 'Laphroaig', age = '10', whiskytype = 'Single Malt', distillery = d1, region = rIslay, tastingnotes = 'Full bodied, Peaty, Smokey', barrelType = 'Wood', image = '/static/imgs/laphroaig-10-year-old.jpg', website = 'http://www.laphroaig.com/whiskies/10yo.aspx', price = '37.50',)
w1.save()
w2 = Whisky(name = 'Ardbeg10', title= 'Ardbeg', age = '10', whiskytype = 'Single Malt', distillery = d2, region = rIslay, tastingnotes = 'Peaty, smokey', barrelType = 'Wood', image = '/static/imgs/ArdbegTenYearOld.jpg', website = 'http://www.ardbeg.com/ardbeg/the-ardbeg-range', price = '38.70',)
w2.save()
w3 = Whisky(name = 'Old Pulteney12', title = 'Old Pulteney', age = '12', whiskytype = 'Single Malt', distillery = d3, region = rHigh, tastingnotes = 'Fruity, Spice', barrelType = 'Wood', image = '/static/imgs/OldPulteney12yrold.jpg', website = 'http://www.oldpulteney.com/old-pulteney-whisky/12-year-old-single-malt/', price = '30.99',)
w3.save()
w4 = Whisky(name = 'Old Pulteney17', title = 'Old Pulteney', age = '17', whiskytype = 'Single Malt', distillery = d3, region = rHigh, tastingnotes = 'Complex, wood, fruit, creamy', barrelType = 'Wood', image = '/static/imgs/oldpulteney17.jpg', website = 'http://www.oldpulteney.com/old-pulteney-whisky/17-year-old-single-malt/', price = '52.30',)
w4.save()
w5 = Whisky(name = 'Old Pulteney21', title = 'Old Pulteney', age = '21', whiskytype = 'Single Malt', distillery = d3, region = rHigh, tastingnotes = 'Light, Fruity, Honey, Vanilla', barrelType = 'Wood', image = '/static/imgs/OldPulteney-21-1.jpg', website = 'http://www.oldpulteney.com/old-pulteney-whisky/21-year-old-single-malt/', price = '80.70',)
w5.save()
w6 = Whisky(name = 'Auchentoshan12', title = 'Auchentoshan', age = '12', whiskytype = 'Single Malt', distillery = d8, region = rLow, tastingnotes = 'Smooth, nutty, fruity', barrelType = 'Wood', image = '/static/imgs/auchentoshan.jpg', website = 'http://www.auchentoshan.com/products/our-range.aspx', price = '30.50',)
w6.save()
w7 = Whisky(name = 'Balblair10', title = 'Balblair', age = '10', whiskytype = 'Single Malt', distillery = d5, region = rHigh, tastingnotes = 'Full bodied, fruity', barrelType = 'Wood', image = '/static/imgs/balblair-2002.jpg', website = 'http://www.balblair.com/exclusive-vintages/', price = '42.00',)
w7.save()
w8 = Whisky(name = 'Edradour10', title = 'Edradour', age = '10', whiskytype = 'Single Malt', distillery = d4, region = rHigh, tastingnotes = 'Fruity', barrelType = 'Wood', image = '/static/imgs/edrob_10ov1.jpg', website = 'http://www.edradour.com/index3.html', price = '32.50',)
w8.save()
w9 = Whisky(name = 'Glenfiddich12', title = 'Glenfiddich', age = '12', whiskytype = 'Single Malt', distillery = d6, region = rSpey, tastingnotes = 'Fruity', barrelType = 'Wood', image = '/static/imgs/glenfiddich-15-year-old-tile-02.jpg', website = 'http://www.glenfiddich.com/', price = '34.75',)
w9.save()
w10 = Whisky(name = 'Glenkinchie12', title = 'Glenkinchie', age = '12', whiskytype = 'Single Malt', distillery = d9, region = rLow, tastingnotes = 'Smooth, sweet', barrelType = 'Wood', image = '/static/imgs/glenkinchie.jpg', website = 'http://www.discovering-distilleries.com/agecheck.php?redirect=/glenkinchie/index.php', price = '34.00',)
w10.save()
w11 = Whisky(name = 'Glenlivet12', title = 'Glenlivet', age = '12', whiskytype = 'Single Malt', distillery = d7, region = rSpey, tastingnotes = 'Light, fruity', barrelType = 'Wood', image = '/static/imgs/glenlivet-12-yr.jpg', website = 'http://www.theglenlivet.com/agegateway?url=http%3a%2f%2fwww.theglenlivet.com%2f', price = '34.00',)
w11.save()
w12 = Whisky(name = 'Highland Park12', title = 'Highland Park', age = '12', whiskytype = 'Single Malt', distillery = d10, region = rIslay, tastingnotes = 'Light smoke, honey, fruit', barrelType = 'Wood', image = '/static/imgs/highland-park-12-year-old.jpg', website = 'http://www.highlandpark.co.uk/lda/', price = '30.00',)
w12.save()
