# @class_declaration interna_agruparalbaranescli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_agruparalbaranescli(modelos.mtd_agruparalbaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_agruparalbaranescli #
class flfacturac_agruparalbaranescli(interna_agruparalbaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration agruparalbaranescli #
class agruparalbaranescli(flfacturac_agruparalbaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.agruparalbaranescli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
