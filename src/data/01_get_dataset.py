# -*- coding: utf-8 -*-
""" Get the counts from Bing """
from pathlib import Path
import logging
import click
from src.bing_search import BingSearch
from dotenv import find_dotenv, load_dotenv

@click.command()
@click.option('--output_filepath', default='/data/raw', help='path to raw data directory')
def main(output_filepath):
    """ get the data """
    logger = logging.getLogger(__name__)
    logger.info('Getting raw data')

    # TODO: loop through a list of places in Tendring
    places_in_tendring = ['Colchester', 'Clacton-on-Sea', 'Harwich', 
    'Walton-on-the-Naze', 'Dovercourt', 'Brightlingsea', 'Wivenhoe',
    'Frinton-on-Sea', 'Jaywick', 'Manningtree']
    for place in places_in_tendring:
        BingSearch.search(place)

    

if __name__ == '__main__':
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    # not used in this stub but often useful for finding various files
    PROJEC_DIRECTORY = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main() # pylint: disable=E1120
