<p align="center">
    <img src="https://i.kym-cdn.com/photos/images/original/001/336/797/c9b.gif">
    <br><i>Release!</i>
</p>

<p align="justify">
  <b>Cardcaptor Sakura</b>, abbreviated as CCS, is a Japanese shōjo manga series written and illustrated by the manga group Clamp. The story focuses on Sakura Kinomoto, an elementary school student who discovers magical powers after accidentally freeing a set of magical cards which she must retrieve to prevent catastrophe.
</p>
<p align="justify">
  A sequel by Clamp, <i>Cardcaptor Sakura: Clear Card</i>, focusing on Sakura in junior high school, began serialization in Nakayoshi in 2016.
</p>

## About

<p align="justify">
  Succeeding the release of the <i>Clear Card Arc</i>, a huge fan of the series created this repository after he got as excited about the new season as he was with the first one many years ago. It's too soon to say what you'll find here, but it can become anything.
</p>
<p align="justify">
  Maybe it is just a escape for nostalgic feelings, but I hope that other fans may find it and remember the joy that Kinomoto Sakura brought us while chasing the Clow Cards.
</p>

## Summary

- [Crawlers](#crawlers)

## Crawlers

<p align="justify">
  At this time, we only have spiders to crawl the informations about Clow Cards and Sakura Cards. Follow the steps bellow to use them.
</p>

```sh
# Move into the directory
cd Sakura

# Run the spider named 'clow-cards' and save the data at 'clow-cards.json'.
scrapy crawl clow-cards -o clow-cards.json
scrapy crawl sakura-cards -o sakura-cards.json 
```

### Requirements

- [Python 3.5+](https://www.python.org/)
- [Scrapy](https://scrapy.org/)
