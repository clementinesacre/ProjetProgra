# -*- coding: utf-8 -*-
import logging
from options import menu
import logging
from classe import variable_globale as vg

if __name__ == '__main__':
    menu.lancement_application()
    logging.basicConfig(filename='history.log', encoding='utf-8', level=logging.DEBUG)

    """vg.logger.info()
    logging.info('So should this')  # tout va bien
    logging.warning('And this, too')  # plus de place bientot dans le .log
    vg.logger.error('And non-ASCII stuff, too, like Øresund and Malmö')"""

