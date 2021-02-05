BOT_NAME = 'rigensisbank'

SPIDER_MODULES = ['rigensisbank.spiders']
NEWSPIDER_MODULE = 'rigensisbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'rigensisbank.pipelines.RigensisbankPipeline': 100,

}