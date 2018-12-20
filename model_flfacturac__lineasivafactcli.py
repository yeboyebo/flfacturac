# @class_declaration interna_lineasivafactcli #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineasivafactcli(modelos.mtd_lineasivafactcli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flfacturac_lineasivafactcli #
class flfacturac_lineasivafactcli(interna_lineasivafactcli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineasivafactcli #
class lineasivafactcli(flfacturac_lineasivafactcli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineasivafactcli_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
