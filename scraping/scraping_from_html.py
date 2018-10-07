import json

from bs4 import BeautifulSoup


def get_ad_recipe_list():
    with open("index.html") as fp:  # openには、wgetで習得したhtmlフィアル名を入れてください。
        html_doc = BeautifulSoup(fp, 'html.parser')

    sponsored_ad_section = html_doc.find(
        'div', {'class': 'sponsored_kitchen_ads'}
        )
    ads = sponsored_ad_section.find_all('li')
    ad_recipe_list = []

    for ad in ads:
        recipe = ad.find('a', {'class': 'recipe_title'})
        sponsor = ad.find('div', {'class': 'author_name'})

        recipe_title = recipe.string
        recipe_url = "https://cookpad.com" + recipe.get('href')
        cuisine_img = ad.find('img').get('src')
        sponsor_name = sponsor.a.string
        sponsor_url = "https://cookpad.com" + sponsor.a.get('href')
        sponsored_ad = {"recipe_title": recipe_title,
                        "recipe_url": recipe_url,
                        "cuisine_img": cuisine_img,
                        "sponsor": sponsor_name,
                        "sponsor_url": sponsor_url
                        }
        ad_recipe_list.append(sponsored_ad)
    return ad_recipe_list


if __name__ == '__main__':
    print(json.dumps(
        get_ad_recipe_list(), ensure_ascii=False
    ))
