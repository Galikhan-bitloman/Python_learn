#-------------------------------------------------------------------------------
# Name:        shirt
# Purpose:
#
# Author:      Nag
#
# Created:     12.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def make_shirt(size,text):
    """Размер и текст футболки"""
    print("\nMy shirt " + size + ", My print is '" + text.title() + "!'")
make_shirt(size='XL',text='Hello')