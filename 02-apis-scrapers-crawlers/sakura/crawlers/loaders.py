from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

def fix_text_field(self, values):
    text = values[0]
    return text.replace('\n', '')
    
def fix_url_field(self, values):
    url = values[0]
    return url.split('/revision')[0]

class ClowCardLoader(ItemLoader):
    default_output_processor = TakeFirst()
    card_out = fix_text_field
    sign_out = fix_text_field
    magic_type_out = fix_text_field
    img_url_out = fix_url_field

class SakuraCardLoader(ClowCardLoader):
    pass