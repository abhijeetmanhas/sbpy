# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
=======================
SBPy Sun Sources Module
=======================

Descriptions of source solar spectra.

"""

E490_2014 = {
    'file': 'e490-00a_2014_hires.csv',
    'wave_unit': 'um',
    'flux_unit': 'W/(m2 um)',
    'description': 'E490-00a (2014) reference solar spectrum (Table 3)',
    'bibcode': 'doi:10.1520/E0490'
}

E490_2014LR = {
    'file': 'e490-00a_2014_hires.csv',
    'wave_unit': 'um',
    'flux_unit': 'W/(m2 um)',
    'description': 'E490-00a (2014) low resolution reference solar spectrum (Table 4)',
    'bibcode': 'doi:10.1520/E0490'
}

Kurucz1993 = {
    'file': 'ftp://ftp.stsci.edu/cdbs/grid/k93models/standards/sun_kurucz93.fits',
    'description': 'Kurucz (1993) model, scaled by Colina et al. (1996).',
    'bibcode': '1993KurCD..13.....K'
}

Castelli1996 = {
    'file': 'ftp://ftp.stsci.edu/cdbs/grid/k93models/standards/sun_castelli.fits',
    'description': 'Castelli model, scaled and presented by Colina et al. (1996).',
    'bibcode': '1996AJ....112..307C'
}
