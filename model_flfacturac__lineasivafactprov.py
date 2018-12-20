# @class_declaration interna_lineasivafactprov #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineasivafactprov(modelos.mtd_lineasivafactprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_lineasivafactprov #
class flfacturac_lineasivafactprov(interna_lineasivafactprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineasivafactprov #
class lineasivafactprov(flfacturac_lineasivafactprov, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineasivafactprov_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
