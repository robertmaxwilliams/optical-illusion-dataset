# combines the two JSON files and leaves bank fields where needed
"""
    { moillisions_data.json
        "url": "https://www.moillusions.com/4-dots-illusion/",
        "img_src": "https://www.moillusions.com/wp-content/uploads/2018/01/4-dots-illusion-1-580x342.jpg",
        "alt_text": "dots illusion",
        "categories": [
            "Disappearing Effect"
        ]
    },
        { viperlib_data.json
        "url": "/images/thumbnails/0000/8908/3d_photo_log_illusion_medium.jpg?1238543179",
        "title": "3d photo log illusion",
        "page_url": "/areas/16-lightness-brightness/contributions/1372-3d-photo-log-illusion",
        "category": "16-lightness-brightness",
        "description": "Photo of a 3D version of the Logvinenko Illusion. The illusory effect was weaker althou..."
    },
"""
import json

moillusions = json.load(open('moillusions_data.json'))
viperlib = json.load(open('viperlib_data.json'))

# get categories so I can manually determine which viper 
# categories I should map to which mo categories
viper_categories = set()
mo_categories = set()
for sample in moillusions:
	mo_categories.update(set(sample['categories']))

for sample in viperlib:
	viper_categories.add(sample['category'])

print(viper_categories)
print(mo_categories)

# my choices are somewhat arbitrary, because mo categories are
# much more fine grained than
viper_to_mo = {'12-colour':['Color Adapting', '25-faces', '18-depth', '16-lightness-brightness', '13-motion', '14-spatial-vision', '20-illusions'}


viper_cats = {'12-colour', '25-faces', '18-depth', '16-lightness-brightness', '13-motion', '14-spatial-vision', '20-illusions'}
mo_cats = {'Animals', 'Escher Style', 'Anamorphosis', 'Transportation', 'Google Earth', 'Spot The Object', 'Brain Teaser', 'Games', 'Stereograms', 'Outdoor Illusions', 'Audio Illusions', 'Afterimages', 'Toys', 'Color Adapting', 'Relative Sizes', 'Scary Illusions', 'Skull Illusions', 'Sand Sculptures', 'Billboards', 'World of Weird', 'Animations', 'Art Illusion', 'Science Stuff', 'Photo Illusions', 'Video Illusions', 'Seemingly Bent', 'Art Installation', 'Disappearing Effect', 'Moving Optical Illusions', 'Body Paint', 'Transparent', 'Celebrities', 'Multiple Meanings', '3D Chalk Drawings', 'Perspective Illusions', 'Greatest Hits', 'Murals', 'Holiday Theme', 'News', 'Impossible Objects', 'Motion Illusions', 'David Blaine', 'Funny Illusions', 'Tests'}

`
# actually, I'm just going to use mo illusions for now....
