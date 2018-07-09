# -*- coding: utf-8 -*-

 #This script initializes the plugin, making it known to QGIS.



# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QuickDigitize class from file QuickDigitize.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .quick_digitize import QuickDigitize
    return QuickDigitize(iface)
